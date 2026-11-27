# KASUS UJI GREY BOX - QATIARENT

## Evaluasi Ulang Metode (Revisi 27 November 2026)

Pada versi awal dokumen ini, sebagian pemeriksaan artefak teknis sempat dilabeli "white box sisi klien". Setelah dievaluasi ulang, label tersebut **dicabut** karena tidak tepat:

- White box testing menurut definisinya mensyaratkan akses ke struktur internal aplikasi: kode sumber, logika program, dan jalur eksekusi (untuk misalnya path/branch coverage dan unit test).
- Kelompok **tidak memiliki akses ke kode sumber Qatiarent** — aplikasi milik perusahaan pihak ketiga dan tidak ada izin/akses repositori yang diberikan. Kondisi ini sudah dikonfirmasi ulang oleh kelompok pada 27 November 2026.
- Pemeriksaan artefak yang memang terbuka untuk publik (header HTTP, struktur HTML awal, `robots.txt`, `sitemap.xml`, pola redirect dan parameter URL) **bukan** white box. Pemeriksaan itu memakai pengetahuan teknis sebagian tentang cara aplikasi bekerja dari luar, sehingga klasifikasinya yang benar adalah **grey box**.

Kesimpulan evaluasi: metode pengujian kelompok adalah **black box + grey box + otomasi**. White box **tidak dilakukan** pada proyek ini. Apabila di kemudian hari pemilik aplikasi memberi akses repositori/kode, white box penuh (unit test, path coverage) dapat ditambahkan sebagai pengujian lanjutan.

## Kasus Uji Grey Box

Grey box di sini menggabungkan pengetahuan sebagian struktur (nama parameter `city`, `duration`, `shippingType`, `useByDate`, pola URL, teknologi server LiteSpeed, serta artefak teknis publik) dengan pengujian dari sisi pengguna.

### A. Manipulasi parameter berdasarkan pengetahuan struktur

| ID | Skenario | Pengetahuan Internal yang Dipakai | Hasil yang Diharapkan |
|---|---|---|---|
| GB-01 | Manipulasi nilai `city` di luar daftar kota | Nama & format parameter dari URL | Nilai invalid dinormalisasi ke default, bukan error |
| GB-02 | Manipulasi `duration` ekstrem (0 / 999) | Nama parameter durasi | Dinormalisasi / ditolak tanpa 5xx |
| GB-03 | Tanggal `useByDate` format terbalik / tidak valid | Format tanggal DD-MM-YYYY dari URL default | Ditangani tanpa 5xx |
| GB-04 | Injeksi script lewat parameter | Parameter dirender kembali ke halaman (refleksi) | Tidak ada script yang terefleksi mentah / dieksekusi |
| GB-05 | Konsistensi harga | Harga tampil per paket "1-3 days" | Harga pada daftar dan detail produk sama untuk produk yang sama |

### B. Inspeksi artefak teknis publik (semula WB-01 s.d. WB-05, direklasifikasi 27 Nov 2026)

| ID | Objek Analisis | Cara | Hasil yang Diharapkan |
|---|---|---|---|
| GB-06 | Header respons halaman utama | Inspeksi header HTTP | Ada header keamanan dasar (HSTS, X-Frame-Options, X-Content-Type-Options, CSP) |
| GB-07 | Struktur HTML awal | Lihat sumber halaman | Konten utama dapat diindeks mesin pencari (tidak sepenuhnya bergantung pada JavaScript) |
| GB-08 | `robots.txt` | Buka `/robots.txt` | File ada (200) dan tidak membuka path sensitif |
| GB-09 | `sitemap.xml` | Buka `/sitemap.xml` | File ada (200) dan berisi URL yang valid |
| GB-10 | Pola redirect beranda | Amati URL akhir setelah membuka `/` | Parameter default terisi konsisten (city, duration, shippingType, useByDate) |

Hasil eksekusi: `reports/MANUAL_TEST_EXECUTION_REPORT.md` dan temuan: `reports/DEFECT_LOG.md`.
