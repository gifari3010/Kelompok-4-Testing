# LAPORAN EKSEKUSI PENGUJIAN MANUAL

**Target:** https://qatiarent.com/ | **Tanggal eksekusi:** 21 November 2026
**Penguji:** Kelompok 4 (dibantu eksekusi teknis terverifikasi dari lingkungan uji kelompok)
**Metode:** Black box (EP, BVA, decision table), white box sisi klien, grey box - lihat `docs/03` dan `docs/04`.

> Kejujuran hasil: tabel ini hanya memuat kasus yang benar-benar dieksekusi dan teramati hasilnya pada tanggal di atas. Kasus yang memerlukan interaksi visual lanjutan di UI ditandai sebagai "Sebagian" dan wajib dilengkapi tangkapan layar oleh penguji saat sesi manual di browser.

| ID | Kasus | Hasil Aktual Teramati | Status |
|---|---|---|---|
| BB-01 | Buka beranda tanpa parameter | Dialihkan ke URL berparameter default: `?useByDate=23-11-2026&duration=1&city=1&shippingType=Next%20day`; daftar produk tampil ("Showing 1 to 24 of 230 results") | PASS |
| BB-02 | Kota tersedia (city=1 / area Bandung) | Halaman menampilkan produk dengan keterangan pengiriman dari area Bandung | PASS |
| BB-03 | Kota tidak valid | Status 200, parameter dinormalisasi kembali ke `city=1` (default) | PASS |
| BB-05 | Durasi ekstrem / di luar pilihan | Parameter dinormalisasi oleh situs ke nilai default; tidak ada error 5xx | PASS |
| BB-11 | Daftar produk & kelengkapan label | 24 produk halaman pertama tampil lengkap: nama, brand, harga "Rp .../1-3 days", kategori, ukuran Fit | PASS |
| BB-13 | URL tidak ada | HTTP 404 | PASS |
| BB-14 | Akses HTTP | HTTP 301 ke HTTPS | PASS |
| BB-15 | Injeksi script via parameter | Status 200; string `<script>alert(1)</script>` tidak terefleksi mentah pada respons | PASS |
| BB-16 | Parameter 2000 karakter | Status 200; dinormalisasi ke default; tanpa 5xx | PASS |
| BB-04, BB-06 s.d. BB-10, BB-12 | BVA tanggal/durasi lewat UI, decision table kombinasi filter, pagination UI | Belum dieksekusi penuh secara visual pada sesi ini | SEBAGIAN - lengkapi saat sesi manual kelompok + screenshot |
| WB-01 | Header keamanan | CSP hanya `upgrade-insecure-requests`; HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy **tidak ada** | FAIL -> Defect D-01 |
| WB-02 | Struktur HTML awal | HTML awal tidak memuat form/input/img produk (0 ditemukan); konten dirender sisi klien (JavaScript) | CATATAN -> Defect D-02 (dampak SEO/aksesibilitas) |
| WB-03 | robots.txt | 200, ukuran 67 byte | PASS |
| WB-04 | sitemap.xml | 200, ukuran 545 byte | PASS |
| WB-05 | Pola redirect beranda | Konsisten: tanggal pemakaian terisi H+2 dari tanggal akses | PASS |
| GB-01 s.d. GB-04 | Manipulasi parameter (grey box) | Semua dinormalisasi ke default tanpa error 5xx; tidak ada refleksi script | PASS |
| GB-05 | Konsistensi harga daftar vs detail | Memerlukan klik detail produk secara visual | SEBAGIAN |

**Ringkasan:** 13 PASS, 1 FAIL, 1 catatan, 3 kelompok kasus SEBAGIAN (perlu sesi visual + screenshot).
**Lingkungan:** Server terdeteksi LiteSpeed; waktu respons beranda ±0,9-1,2 detik dan ukuran HTML ±131,8 KB dari lingkungan uji pada 21 Nov 2026.
