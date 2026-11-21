"""
Pengujian otomatis level HTTP untuk Qatiarent (gaya Postman/API testing).
Menjalankan:  pip install requests pytest
              pytest tests/test_qatiarent_http.py -v
Hanya membaca halaman publik, tanpa transaksi nyata.
"""
import requests

BASE = "https://qatiarent.com"
S = requests.Session()
S.headers.update({"User-Agent": "Mozilla/5.0 (QA student testing, low frequency)"})


def test_homepage_200():
    r = S.get(BASE + "/", timeout=30)
    assert r.status_code == 200
    assert "Qatia" in r.text


def test_http_redirects_to_https():
    r = S.get("http://qatiarent.com/", timeout=30, allow_redirects=False)
    assert r.status_code in (301, 302, 308)
    assert r.headers.get("Location", "").startswith("https://")


def test_unknown_page_404():
    r = S.get(BASE + "/halaman-tidak-ada-xyz123", timeout=30)
    assert r.status_code == 404


def test_robots_and_sitemap_exist():
    assert S.get(BASE + "/robots.txt", timeout=30).status_code == 200
    assert S.get(BASE + "/sitemap.xml", timeout=30).status_code == 200


def test_invalid_parameters_do_not_5xx():
    for url in ["/?city=KOTA_TIDAK_ADA_123",
                "/?city=%3Cscript%3Ealert(1)%3C/script%3E",
                "/?city=" + "A" * 2000]:
        r = S.get(BASE + url, timeout=30)
        assert r.status_code < 500, url
        assert "<script>alert(1)</script>" not in r.text  # tidak terefleksi mentah
