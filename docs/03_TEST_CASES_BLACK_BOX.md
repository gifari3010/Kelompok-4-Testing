# KASUS UJI BLACK BOX - QATIARENT

**Metode:** Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Decision Table
**Dasar:** ISO/IEC/IEEE 29119-1:2022 (konsep pengujian), karakteristik Functional Suitability ISO/IEC 25010:2023
**Target:** https://qatiarent.com/ - pengujian hanya dari sisi pengguna, tanpa melihat kode sumber.
**Tanggal penyusunan:** 21 November 2026

Fitur yang diuji (hasil eksplorasi situs): katalog produk rental pakaian, filter kota (`city`), durasi sewa (`duration`), jenis pengiriman (`shippingType`), tanggal pemakaian (`useByDate`), daftar produk (230 hasil, 24 per halaman), detail produk, dan halaman "Cek Jadwal".

| ID | Skenario | Data Uji | Hasil yang Diharapkan | Teknik |
|---|---|---|---|---|
| BB-01 | Buka halaman utama tanpa parameter | URL `/` | Situs mengarahkan ke filter default (kota default, durasi 1, Next day, tanggal pemakaian H+2) dan daftar produk tampil | EP |
| BB-02 | Pilih kota yang tersedia (mis. Bandung / city=1) | `city=1` | Produk yang tampil sesuai area kota tersebut | EP (kelas valid) |
| BB-03 | Isi kota yang tidak ada | `city=KOTA_TIDAK_ADA_123` | Tidak error; situs kembali ke kota default / hasil kosong yang wajar | EP (kelas invalid) |
| BB-04 | Durasi sewa minimum | `duration=1` (1-3 hari) | Harga tampil per paket 1-3 hari | BVA (batas bawah) |
| BB-05 | Durasi di luar pilihan | `duration=0` atau `duration=999` | Ditolak / dinormalisasi ke pilihan terdekat, tanpa error 5xx | BVA + EP invalid |
| BB-06 | Tanggal pemakaian = hari ini | `useByDate` = hari ini | Sistem memberi tahu ketersediaan sesuai aturan pengiriman | BVA |
| BB-07 | Tanggal pemakaian = kemarin (lampau) | `useByDate` = H-1 | Ditolak atau dinormalisasi; tidak bisa memesan untuk tanggal lampau | BVA (di bawah batas) |
| BB-08 | Tanggal pemakaian jauh di masa depan | `useByDate` = H+365 | Diterima atau dibatasi sesuai kebijakan; tanpa error | BVA (di atas batas) |
| BB-09 | Kombinasi filter lengkap | city + duration + shippingType=Next day + useByDate valid | Hasil konsisten dengan semua filter (decision table: semua kondisi benar) | Decision Table |
| BB-10 | Kombinasi filter tidak lengkap | Hanya `city`, parameter lain kosong | Situs melengkapi parameter lain dengan nilai default | Decision Table |
| BB-11 | Buka detail produk dari daftar | Klik produk pertama (mis. Sylvie Dress) | Halaman detail tampil: nama, brand, harga, ukuran (Fit), kategori | EP |
| BB-12 | Navigasi halaman daftar produk | Pindah ke halaman 2 daftar | Produk berganti, indikator "Showing ... of 230 results" konsisten | EP |
| BB-13 | URL halaman yang tidak ada | `/halaman-tidak-ada-xyz123` | HTTP 404 dengan halaman tidak ditemukan | EP invalid |
| BB-14 | Akses lewat HTTP | `http://qatiarent.com/` | Dialihkan (301) ke HTTPS | EP |
| BB-15 | Input script pada parameter | `city=<script>alert(1)</script>` | Script tidak dieksekusi / tidak terefleksi mentah di halaman | EP invalid (keamanan dasar) |
| BB-16 | Parameter sangat panjang | `city=` + 2000 karakter | Tidak error 5xx; ditangani dengan aman | BVA |

Hasil eksekusi kasus-kasus ini dicatat di `reports/MANUAL_TEST_EXECUTION_REPORT.md`.
Kasus yang membutuhkan interaksi visual penuh (klik filter di UI) dieksekusi manual oleh penguji di browser; kasus berbasis parameter/HTTP juga diverifikasi lewat pengujian otomatis di `tests/`.
