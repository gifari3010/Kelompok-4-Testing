# DOKUMEN RENCANA PENGUJIAN SISTEM (TEST PLAN)

## Berdasarkan Standar ISO/IEC/IEEE 29119-1:2022 & ISO/IEC 25010:2023

---

## 1. Informasi Dokumen

| Parameter                 | Deskripsi                                                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Judul Proyek              | Analisis Pengujian Kualitas dan Fungsionalitas Website Qatiarent Menggunakan Pengujian Manual (Black Box, Grey Box) dan Otomatis Berdasarkan Standar ISO/IEC 25010:2023 |
| Nama Aplikasi / Target    | Website Resmi Qatiarent                                                                                                                                                 |
| URL Target                | https://qatiarent.com/                                                                                                                                                  |
| Tim Penyusun (Kelompok)   | 1. Gifari Arliansyah (NIM: 231011401190)<br>2. Kaka Aditya (NIM: 231011400167)<br>3. Haikal Ammanu (NIM: 231011402378)<br>4. Rafi Hibban Hafizh (NIM: 231011402071)     |
| Mata Kuliah               | Testing & Quality Assurance (QA)                                                                                                                                        |
| Program Studi / Institusi | Teknik Informatika, Universitas Pamulang                                                                                                                                |
| Tahun Akademik            | 2026/2027                                                                                                                                                               |
| Versi Dokumen             | 1.1 (revisi 27 November 2026: white box dicabut dari metode — lihat catatan revisi di bawah)                                                                            |
| Tanggal                   | 18 November 2026                                                                                                                                                        |
| Batas Pengumpulan         | 19 Desember 2026                                                                                                                                                        |

> **Catatan revisi 1.1 (27 November 2026):** Metode dievaluasi ulang. Versi 1.0 mencantumkan white box (termasuk label "white box sisi klien"), padahal kelompok tidak memiliki akses kode sumber Qatiarent dan kondisi itu sudah dikonfirmasi ulang. White box **dicabut** dari rencana: metode resmi proyek ini adalah black box + grey box + otomasi. Pemeriksaan artefak teknis publik yang semula dilabeli white box direklasifikasi menjadi grey box — lihat `docs/04_TEST_CASES_GREY_BOX.md`.

## 2. Latar Belakang dan Tujuan

Qatiarent adalah aplikasi web berbasis RPL/portal yang dikembangkan oleh perusahaan. Skalanya dipilih pada kategori menengah ke bawah dari sisi bisnis dan jumlah pengunjung.

> **Isi dari tim:** lampirkan bukti kriteria pemilihan (profil perusahaan, perkiraan trafik, tanggal akses) di `reports/BUKTI_PEMILIHAN_APLIKASI.md`.

Tujuan pengujian:

1. Menilai fungsionalitas utama website (pencarian, filter, pemesanan).
2. Menilai karakteristik kualitas non-fungsional terpilih menurut ISO/IEC 25010:2023.
3. Menghasilkan temuan cacat (defect) beserta rekomendasi perbaikan.

## 3. Standar dan Referensi (rentang 2022-2026)

| No  | Standar / Referensi                          | Tahun     | Peran dalam pengujian                            |
| --- | -------------------------------------------- | --------- | ------------------------------------------------ |
| 1   | ISO/IEC 25010:2023 (Product quality model)   | 2023      | Model karakteristik kualitas yang diuji          |
| 2   | ISO/IEC/IEEE 29119-1:2022 (General concepts) | 2022      | Konsep dan terminologi pengujian perangkat lunak |
| 3   | ISO/IEC 25040:2024 (Evaluation process)      | 2024      | Proses evaluasi kualitas                         |
| 4   | Jurnal SINTA 1-3 (alasan metode)             | 2022-2026 | Lihat `docs/06_LANDASAN_METODE.md`               |

> **Catatan:** pastikan nomor dan tahun standar sudah diverifikasi di iso.org atau ieee.org sebelum dikumpulkan, dan konfirmasi ke dosen apakah struktur dokumen 29119-3 (terbit 2021) boleh dipakai sebagai template saja.

## 4. Ruang Lingkup

### 4.1 Dalam cakupan (in scope)

Fitur yang teridentifikasi dari parameter URL situs (`city`, `duration`, `shippingType`, `useByDate`):

- Pencarian dan pemilihan kota
- Pemilihan durasi sewa
- Pemilihan jenis pengiriman (mis. _Next day_)
- Pemilihan tanggal pemakaian
- Daftar dan detail produk, keranjang/pemesanan, form kontak (**sesuaikan setelah eksplorasi situs**)
- Tampilan responsif (desktop dan mobile)

### 4.2 Di luar cakupan (out of scope)

- Load/stress/DoS testing (tanpa izin tertulis pemilik)
- Transaksi pembayaran nyata
- Pengujian server, jaringan, dan infrastruktur milik pihak lain

## 5. Karakteristik Kualitas yang Diuji (ISO/IEC 25010:2023)

| Karakteristik                        | Dipilih          | Pendekatan                                |
| ------------------------------------ | ---------------- | ----------------------------------------- |
| Functional Suitability               | Ya               | Black box manual + otomatis               |
| Performance Efficiency               | Ya (ringan)      | Lighthouse / waktu muat halaman           |
| Compatibility                        | Ya               | Uji lintas browser                        |
| Interaction Capability (Usability)   | Ya               | Heuristik + checklist, kuesioner opsional |
| Reliability                          | Sebagian         | Konsistensi hasil pada pengulangan tes    |
| Security                             | Sebagian (pasif) | Cek HTTPS, header, validasi input dasar   |
| Maintainability, Flexibility, Safety | Tidak            | Tidak ada akses kode / tidak relevan      |

## 6. Strategi dan Pendekatan Pengujian

| Jenis              | Teknik                                                                                                                                                  | Alat                                        | Keterangan                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------- |
| Manual - Black box | Equivalence partitioning, boundary value, decision table                                                                                                | Browser, spreadsheet kasus uji              | Dokumen `03_TEST_CASES_BLACK_BOX.md`  |
| Otomatis           | Script end-to-end                                                                                                                                       | Playwright (atau Selenium) + GitHub Actions | Folder `tests/`                       |
| Non-fungsional     | Audit performa/aksesibilitas                                                                                                                            | Lighthouse, WAVE                            | Hasil di `reports/`                   |
| Wawancara          | Wawancara QA profesional (≥3 tahun)                                                                                                                     | Daring / luring                             | `reports/WAWANCARA_QA_PROFESIONAL.md` |

## 7. Lingkungan Pengujian

| Komponen         | Spesifikasi (isi)                                    |
| ---------------- | ---------------------------------------------------- |
| Perangkat        | [Laptop/OS]                                          |
| Browser          | Chrome [versi], Firefox [versi], Safari/Edge [versi] |
| Perangkat mobile | [Tipe HP / emulator]                                 |
| Jaringan         | [Wi-Fi/4G, kecepatan]                                |
| Alat otomatis    | Node.js [versi], Playwright [versi]                  |

## 8. Kriteria Masuk, Lulus, dan Keluar

- **Masuk:** izin pengujian tersedia, test plan disetujui dosen, lingkungan siap.
- **Lulus kasus uji:** hasil aktual sama dengan hasil diharapkan.
- **Keluar:** seluruh kasus uji dieksekusi, defect tercatat dengan tingkat keparahan, laporan selesai.
- **Penangguhan:** situs tidak dapat diakses atau pemilik meminta pengujian dihentikan.

## 9. Manajemen Risiko

| Risiko                          | Dampak                          | Mitigasi                                                                                                                                                          |
| ------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tidak ada akses source code     | White box tidak dapat dilakukan | White box dinyatakan terbuka sebagai metode yang TIDAK dilakukan; cakupan pengujian dialihkan ke grey box (pengetahuan struktur sebagian + artefak teknis publik) |
| Situs berubah saat pengujian    | Hasil tak konsisten             | Catat tanggal/versi, simpan screenshot                                                                                                                            |
| Narasumber QA sulit dijadwalkan | Belum Melakukan Wawancara       | Seharusnya dihubungi minggu ini                                                                                                                                   |
| Tes otomatis memicu pemblokiran | Tes gagal                       | Atur jeda wajar antar aksi, jangan paralel berlebihan                                                                                                             |

## 10. Peran dan Tanggung Jawab

| Anggota            | Peran                                 |
| ------------------ | ------------------------------------- |
| Gifari Arliansyah  | Test lead, penulis test plan, laporan |
| Kaka Aditya        | Penguji manual (black box)            |
| Haikal Ammanu      | Otomasi (Playwright, CI)              |
| Rafi Hibban Hafizh | Wawancara QA, kajian jurnal           |

## 11. Deliverable

`docs/` (test plan, metrik, kasus uji, pedoman wawancara), `reports/` (eksekusi manual, otomatis, wawancara), `tests/`, `LAPORAN_LENGKAP_PENGUJIAN.md`, dan presentasi.

## 12. Jadwal

Lihat [`02_TIMELINE.md`](02_TIMELINE.md).

## 13. Persetujuan

| Pihak                       | Nama                             | Tanda tangan / Tanggal |
| --------------------------- | -------------------------------- | ---------------------- |
| Dosen pengampu              | ASEP ERLAN MAULANA S.KOM., M.KOM |                        |
| Pemilik aplikasi (izin uji) | Rizal                            |                        |
