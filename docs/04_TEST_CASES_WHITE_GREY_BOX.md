# KASUS UJI WHITE BOX & GREY BOX - QATIARENT

**Batasan penting (dicatat apa adanya):** Kelompok tidak memiliki akses ke kode sumber (source code) Qatiarent, karena aplikasi milik perusahaan pihak ketiga. White box penuh (membaca logika internal, path coverage atas kode server) **tidak dapat dilakukan**. Sebagai gantinya dilakukan:

1. **White box sisi klien** - menganalisis artefak yang memang terbuka untuk publik: struktur HTML, header respons HTTP, file `robots.txt` dan `sitemap.xml`, serta perilaku redirect dan parameter URL.
2. **Grey box** - menggabungkan pengetahuan sebagian struktur (nama parameter `city`, `duration`, `shippingType`, `useByDate`, pola URL, teknologi server LiteSpeed) dengan pengujian black box.

Apabila pemilik aplikasi memberi akses repositori/kode, white box penuh (unit test, path coverage) akan ditambahkan sebagai pengujian lanjutan.

## White Box Sisi Klien

| ID | Objek Analisis | Cara | Hasil yang Diharapkan |
|---|---|---|---|
| WB-01 | Header respons halaman utama | Inspeksi header HTTP | Ada header keamanan dasar (HSTS, X-Frame-Options, X-Content-Type-Options, CSP) |
| WB-02 | Struktur HTML awal | Lihat sumber halaman | Konten utama dapat diindeks mesin pencari (tidak sepenuhnya bergantung pada JavaScript) |
| WB-03 | `robots.txt` | Buka `/robots.txt` | File ada (200) dan tidak membuka path sensitif |
| WB-04 | `sitemap.xml` | Buka `/sitemap.xml` | File ada (200) dan berisi URL yang valid |
| WB-05 | Pola redirect beranda | Amati URL akhir setelah membuka `/` | Parameter default terisi konsisten (city, duration, shippingType, useByDate) |

## Grey Box

| ID | Skenario | Pengetahuan Internal yang Dipakai | Hasil yang Diharapkan |
|---|---|---|---|
| GB-01 | Manipulasi nilai `city` di luar daftar kota | Nama & format parameter dari URL | Nilai invalid dinormalisasi ke default, bukan error |
| GB-02 | Manipulasi `duration` ekstrem (0 / 999) | Nama parameter durasi | Dinormalisasi / ditolak tanpa 5xx |
| GB-03 | Tanggal `useByDate` format terbalik / tidak valid | Format tanggal DD-MM-YYYY dari URL default | Ditangani tanpa 5xx |
| GB-04 | Injeksi script lewat parameter | Parameter dirender kembali ke halaman (refleksi) | Tidak ada script yang terefleksi mentah / dieksekusi |
| GB-05 | Konsistensi harga | Harga tampil per paket "1-3 days" | Harga pada daftar dan detail produk sama untuk produk yang sama |

Hasil eksekusi: `reports/MANUAL_TEST_EXECUTION_REPORT.md` dan temuan: `reports/DEFECT_LOG.md`.
