# DEFECT LOG - QATIARENT

| ID | Judul | Severity | Priority | Bukti | Rekomendasi |
|---|---|---|---|---|---|
| D-01 | Header keamanan penting belum diterapkan (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy tidak ada; CSP hanya `upgrade-insecure-requests`) | Medium | Medium | Inspeksi header respons beranda, 21 Nov 2026 | Tambahkan header tersebut di level server (LiteSpeed) / aplikasi, lalu uji ulang dengan securityheaders.com |
| D-02 | Konten produk tidak ada pada HTML awal (bergantung penuh pada rendering JavaScript) | Low | Low | HTML awal: 0 form, 0 input, 0 img produk; konten muncul setelah JS jalan | Pertimbangkan server-side rendering / pre-render untuk SEO dan ketahanan bila JS gagal |
| D-03 | Nilai parameter filter yang invalid diam-diam diganti ke default tanpa pemberitahuan ke pengguna | Low | Low | `city=KOTA_TIDAK_ADA_123` -> URL ternormalisasi `city=1` tanpa pesan apa pun | Tampilkan pesan "kota tidak ditemukan, menampilkan area default" agar pengguna tidak bingung |

Defect dicatat mengikuti proses pada ISO/IEC/IEEE 29119: ditemukan saat eksekusi uji, dibuktikan, diberi severity/priority, dan disertai rekomendasi. Perbaikan berada di tangan pemilik aplikasi (pihak ketiga); kelompok hanya melaporkan.
