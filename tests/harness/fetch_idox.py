# Fetch an Idox Public Access application's documents into a test fixture.
# Implements planning-document-search Recipe C (session + _csrf + keyVal + documents
# tab), with the fixture-specific split: officer report / decision notice / appeal
# material -> truth/ (never shown to a skill run); everything else -> input/documents/.
# Polite: single-threaded, ~6s between requests, identifying the run in the UA the
# recipe specifies; stops on 403/429 or challenge markers.
#
# Usage: python fetch_idox.py <base_url> <application_ref> <fixture_dir>
#   e.g. python fetch_idox.py https://idox.tendringdc.gov.uk/online-applications \
#            "25/01011/OUT" ../fixtures/tendring-6004354-30-homes
import hashlib, html, json, os, re, sys, time
import requests

BASE, REF, FIXDIR = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3]
DECISION_DATE = sys.argv[4] if len(sys.argv) > 4 else ""  # YYYY-MM-DD; docs received after -> truth/
BP = re.sub(r"https?://[^/]+", "", BASE)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
PACE = 6.0
TRUTH_PAT = re.compile(
    r"officer'?s? report|delegated report|committee report|report to committee|"
    r"decision notice|refusal notice|notice of decision|notice of refusal|"
    r"confirmation of refusal|appeal decision|appeal statement|written justification|"
    r"appellant|appeal correspondence|inspector|\bappeal\b|dismissed|allowed|"
    r"legal agreement|section 106|unilateral undertaking", re.I)

DATE_PAT = re.compile(r"(\d{1,2})[./](\d{1,2})[./](\d{2,4})")
MONTHS = {m: i+1 for i, m in enumerate(
    ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])}
DATE_TEXT_PAT = re.compile(r"(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{4})", re.I)

def received_after_decision(text):
    """True if the row text carries a received date later than DECISION_DATE."""
    if not DECISION_DATE:
        return False
    dates = []
    for d, m, y in DATE_PAT.findall(text):
        y = int(y); y += 2000 if y < 100 else 0
        try:
            dates.append(f"{y:04d}-{int(m):02d}-{int(d):02d}")
        except ValueError:
            continue
    for d, mon, y in DATE_TEXT_PAT.findall(text):
        dates.append(f"{int(y):04d}-{MONTHS[mon.lower()[:3]]:02d}-{int(d):02d}")
    return bool(dates) and min(dates) >= DECISION_DATE

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
    downloads_this_window = 0
    CHUNK, CHUNK_PAUSE = 10, 600   # Idox portals cap bursts at ~12 file GETs (observed
                                   # Tendring + Cornwall, Aug 2026): pause between chunks
    for i, (href, text) in enumerate(rows, 1):
        name = os.path.basename(href.split("?")[0])
        name = re.sub(r"[^A-Za-z0-9._-]", "-", name) or f"doc{i}"
        if name in seen_names:
            seen_names[name] += 1
            stem, dot, ext = name.rpartition(".")
            name = f"{stem or ext}-{seen_names[name]}{dot}{ext if stem else ''}"
        else:
            seen_names[name] = 1
        dest_kind = "truth" if (TRUTH_PAT.search(text) or received_after_decision(text)) else "input"
        sub = "truth" if dest_kind == "truth" else os.path.join("input", "documents")
        path0 = os.path.join(FIXDIR, sub, name)
        alt = os.path.join(FIXDIR, "truth" if sub != "truth" else os.path.join("input", "documents"), name)
        if os.path.exists(path0) or os.path.exists(alt):
            existing = path0 if os.path.exists(path0) else alt
            content = open(existing, "rb").read()
            if content[:4] == b"%PDF" or content[:2] == b"\xff\xd8" or content[:2] == b"PK" or content[:4] == bytes([0xD0,0xCF,0x11,0xE0]):
                if existing != path0:
                    os.replace(existing, path0)   # re-route per current rules
                sha = hashlib.sha256(content).hexdigest()
                rec = {"file": name, "bytes": len(content), "sha256": sha, "magic_ok": True,
                       "row_text": text[:200], "source_href": href, "resumed": True}
                (manifest["truth_files"] if dest_kind == "truth" else manifest["files"]).append(rec)
                log(f"{i}/{len(rows)} SKIP(resume->{dest_kind}) {name}")
                continue
        if downloads_this_window >= CHUNK:
            log(f"chunk pause {CHUNK_PAUSE}s (burst-limit avoidance)")
            time.sleep(CHUNK_PAUSE)
            downloads_this_window = 0
        rp = get(host + href)
        downloads_this_window += 1
        content = rp.content
        magic_ok = content[:4] in (b"%PDF",) or content[:2] in (b"\xff\xd8", b"PK") or content[:4] == b"\x89PNG" or content[:4] == bytes([0xD0,0xCF,0x11,0xE0])
        path = path0
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
