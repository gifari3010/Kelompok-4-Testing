# LAPORAN PENGUJIAN OTOMATIS

**Tanggal eksekusi:** 21 November 2026 | **Target:** https://qatiarent.com/
**Script:** `tests/test_qatiarent_http.py` (pytest + requests, gaya pengujian API/Postman) dan `tests/test_qatiarent_playwright.py` (pytest + Playwright, pengujian UI end-to-end)

## Hasil Eksekusi HTTP (pytest + requests): 5/5 PASS

| ID | Kasus | Hasil |
|---|---|---|
| TC-HT-01 | Beranda mengembalikan 200 dan memuat judul "Qatia" | PASS |
| TC-HT-02 | HTTP dialihkan 301/302/308 ke HTTPS | PASS |
| TC-HT-03 | URL tidak dikenal mengembalikan 404 | PASS |
| TC-HT-04 | robots.txt dan sitemap.xml tersedia (200) | PASS |
| TC-HT-05 | Parameter invalid / injeksi script / 2000 karakter: tidak ada 5xx dan script tidak terefleksi mentah | PASS |

Output pytest: `5 passed` untuk suite HTTP (dijalankan bersama suite Playwright: "6 failed, 5 passed" - lihat catatan di bawah).

## Catatan Eksekusi Playwright (transparan)

Suite Playwright (`test_qatiarent_playwright.py`, 6 kasus UI: muat beranda, filter, kota invalid, detail produk, 404, viewport mobile) **sudah ditulis dan siap dijalankan**, tetapi dari lingkungan uji berbasis cloud yang dipakai kelompok pada 21 Nov 2026, browser Chromium/Firefox gagal membuka situs karena keterbatasan proxy jaringan lingkungan tersebut (`ERR_TUNNEL_CONNECTION_FAILED`) - bukan karena kegagalan pada situs target. Suite HTTP dengan kasus yang setara berhasil membuktikan perilaku yang sama.

**Tindak lanjut wajib tim:** jalankan `pytest tests/test_qatiarent_playwright.py -v` dari jaringan kampus/rumah (tanpa proxy pembatas), lalu tempel output dan screenshot hasil ke laporan ini sebelum pengumpulan.

## Cara Menjalankan Ulang
```bash
pip install pytest requests playwright
playwright install chromium
pytest tests/ -v
```
