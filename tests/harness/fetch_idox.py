# Fetch an Idox Public Access application's documents into a test fixture.
# Implements planning-document-search Recipe C (session + _csrf + keyVal + documents
# tab), with the fixture-specific split: officer report / decision notice / appeal
# material -> truth/ (never shown to a skill run); everything else -> input/documents/.
# Polite: single-threaded, ~2s between downloads, identifying the run in the UA the
# recipe specifies; stops on 403/429 or challenge markers.
#
# Usage: python fetch_idox.py <base_url> <application_ref> <fixture_dir>
#   e.g. python fetch_idox.py https://idox.tendringdc.gov.uk/online-applications \
#            "25/01011/OUT" ../fixtures/tendring-6004354-30-homes
import hashlib, html, json, os, re, sys, time
import requests

BASE, REF, FIXDIR = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3]
BP = re.sub(r"https?://[^/]+", "", BASE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
PACE = 2.0
TRUTH_PAT = re.compile(
    r"officer'?s? report|delegated report|committee report|report to committee|"
    r"decision notice|refusal notice|notice of decision|appeal decision|appeal statement|"
    r"appellant|appeal correspondence|inspector", re.I)

s = requests.Session()
s.headers.update({"User-Agent": UA})

def log(m): print(f"{time.strftime('%H:%M:%S')} {m}", flush=True)

def get(url, **kw):
    r = s.get(url, timeout=120, **kw)
    time.sleep(PACE)
    if r.status_code in (403, 429):
        sys.exit(f"ABORT HTTP {r.status_code} at {url} - stopping per responsible-use rules")
    if r.headers.get("content-type", "").startswith("text/html"):
        low = r.text.lower()
        # a marker only counts as a challenge if the page ALSO lacks the portal's real
        # content (Idox templates carry an empty '#BeginEditable "recaptcha"' block)
        is_portal_page = ("searchcriteria" in low or "applicationdetails" in low
                          or 'name="_csrf"' in low or "/files/" in low)
        for m in ("verify you are human", "cf-chl", "challenge-platform", "awscaptcha"):
            if m in low and not is_portal_page:
                sys.exit(f"ABORT bot-challenge marker '{m}' - stopping, fetch by browser instead")
    return r

def main():
    os.makedirs(os.path.join(FIXDIR, "input", "documents"), exist_ok=True)
    os.makedirs(os.path.join(FIXDIR, "truth"), exist_ok=True)

    # 1. session + csrf
    r = get(f"{BASE}/search.do?action=simple&searchType=Application")
    m = re.search(r'name="_csrf"[^>]*value="([^"]*)"', r.text)
    csrf = m.group(1) if m else ""
    log(f"session ok, csrf={'yes' if csrf else 'NO'}")

    # 2. search
    r = s.post(f"{BASE}/simpleSearchResults.do?action=firstPage",
               data={"_csrf": csrf, "searchType": "Application",
                     "searchCriteria.simpleSearchString": REF,
                     "searchCriteria.simpleSearch": "true"},
               timeout=120, allow_redirects=True)
    time.sleep(PACE)
    cands = list(dict.fromkeys(re.findall(r"keyVal=([A-Z0-9]+)", r.text)))
    if not cands:
        sys.exit("no keyVal found - check ref/base")
    # a ref search can return related records too (e.g. a legal-agreement record citing
    # the ref) - verify each candidate's summary page shows the reference as the
    # application's own reference, not merely in a description
    keyval = None
    for kv in cands:
        rs = get(f"{BASE}/applicationDetails.do?activeTab=summary&keyVal={kv}")
        plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", rs.text))
        m = re.search(r"Reference\s+" + re.escape(REF) + r"\b", plain)
        legal = re.search(r"Legal Agreement", plain[:4000], re.I)
        if m and not legal:
            keyval = kv
            break
        log(f"  candidate {kv} rejected (ref-match={bool(m)} legal-agreement={bool(legal)})")
    if not keyval:
        sys.exit(f"no candidate matched reference exactly (candidates={cands})")
    log(f"keyVal={keyval} (of {len(cands)} candidates)")

    # 3. documents tab; parse rows (link + row text for the description)
    docs_url = f"{BASE}/applicationDetails.do?activeTab=documents&keyVal={keyval}"
    r = get(docs_url)
    rows = []
    for rowm in re.finditer(r"<tr[^>]*>(.*?)</tr>", r.text, re.S):
        row = rowm.group(1)
        lm = re.search(rf'href="({re.escape(BP)}/files/[^"]+)"', row)
        if not lm:
            continue
        text = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", row))).strip()
        rows.append((lm.group(1), text))
    n_table = len(re.findall(rf'href="{re.escape(BP)}/files/', r.text))
    log(f"documents-tab rows with files: {len(rows)} (raw hrefs {n_table})")
    if not rows:
        sys.exit("no document rows found")

    # 4. download, split input/ vs truth/
    host = re.match(r"https://[^/]+", BASE).group(0)
    manifest = {"application_ref": REF, "portal_base": BASE, "keyval": keyval,
                "documents_tab": docs_url, "snapshot_date": time.strftime("%Y-%m-%d"),
                "files": [], "truth_files": []}
    seen_names = {}
    for i, (href, text) in enumerate(rows, 1):
        name = os.path.basename(href.split("?")[0])
        name = re.sub(r"[^A-Za-z0-9._-]", "-", name) or f"doc{i}"
        if name in seen_names:
            seen_names[name] += 1
            stem, dot, ext = name.rpartition(".")
            name = f"{stem or ext}-{seen_names[name]}{dot}{ext if stem else ''}"
        else:
            seen_names[name] = 1
        dest_kind = "truth" if TRUTH_PAT.search(text) else "input"
        sub = "truth" if dest_kind == "truth" else os.path.join("input", "documents")
        rp = get(host + href)
        content = rp.content
        magic_ok = content[:4] in (b"%PDF",) or content[:2] in (b"\xff\xd8", b"PK") or content[:4] == b"\x89PNG"
        path = os.path.join(FIXDIR, sub, name)
        with open(path, "wb") as f:
            f.write(content)
        rec = {"file": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
               "magic_ok": magic_ok, "row_text": text[:200], "source_href": href}
        (manifest["truth_files"] if dest_kind == "truth" else manifest["files"]).append(rec)
        log(f"{i}/{len(rows)} {dest_kind:<5} {name} {len(content)}b magic={magic_ok}")

    with open(os.path.join(FIXDIR, "input", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)
    log(f"DONE input={len(manifest['files'])} truth={len(manifest['truth_files'])}")
    bad = [r["file"] for r in manifest["files"] + manifest["truth_files"] if not r["magic_ok"]]
    if bad:
        log(f"WARNING files failing magic check: {bad}")

if __name__ == "__main__":
    main()
