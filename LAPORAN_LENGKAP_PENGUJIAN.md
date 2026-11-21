# LAPORAN LENGKAP PENGUJIAN SISTEM WEBSITE QATIARENT

**Kelompok 4 - Mata Kuliah Testing & Quality Assurance**
Teknik Informatika, Universitas Pamulang - Tahun Akademik 2026/2027
Anggota: Gifari Arliansyah (231011401190), Kaka Aditya (231011400167), Haikal Ammanu (231011402378), Rafi Hibban Hafizh (231011402071)
**Target:** https://qatiarent.com/ | **Batas pengumpulan:** 19 Desember 2026
**Versi laporan:** 1.1 - 21 November 2026 (perapihan repo & pelengkapan dokumen)

## Ringkasan Eksekutif
Kelompok menguji portal rental pakaian Qatiarent berdasarkan standar ISO/IEC/IEEE 29119-1:2022, ISO/IEC 25010:2023, ISO/IEC 25040:2024, dan ISO/IEC/IEEE 29119-5:2024. Pengujian manual (black box, white box sisi klien, grey box) dan otomatis (pytest + requests; Playwright) dilaksanakan pada 21 November 2026. Hasil: 13 kasus manual PASS, 1 FAIL, 3 defect tercatat, suite otomatis HTTP 5/5 PASS. Wawancara QA profesional **belum dilaksanakan** dan dijadwalkan sesuai timeline (dokumen hasil disiapkan sebagai template jujur, bukan karangan).

## 1. Pemilihan Aplikasi (Ketentuan Poin 1)
Qatiarent adalah portal rental pakaian yang sudah berjalan, dioperasikan sebagai bisnis lokal (area Bandung) berskala menengah ke bawah, dibuat/dikelola perusahaan - memenuhi kriteria tugas. Bukti lengkap: `reports/BUKTI_PEMILIHAN_APLIKASI.md`. Fitur yang diuji: filter kota/durasi/pengiriman/tanggal pemakaian, daftar produk (230 hasil), detail produk, Cek Jadwal.

## 2. Standar & Dokumentasi (Poin 2)
Standar terverifikasi rentang 2022-2026: ISO/IEC/IEEE 29119-1:2022 (General concepts), ISO/IEC 25010:2023 (Product quality model), ISO/IEC 25040:2024 (Quality evaluation framework), ISO/IEC/IEEE 29119-5:2024 (Keyword-driven testing), ISO/IEC 25019:2023 (Quality-in-use model, pendamping). Detail & koreksi judul resmi: `docs/06_LANDASAN_METODE.md`. Rencana pengujian: `docs/01_TEST_PLAN_ISO_29119.md`; jadwal: `docs/02_TIMELINE.md`.

## 3. Pengujian yang Dilakukan (Poin 3)
- **Manual Black Box** (EP, BVA, decision table): kasus `docs/03_TEST_CASES_BLACK_BOX.md`, eksekusi `reports/MANUAL_TEST_EXECUTION_REPORT.md`.
- **Manual White Box & Grey Box**: terbatas sisi klien karena tidak ada akses kode sumber pemilik (dinyatakan terbuka sebagai batasan) - kasus `docs/04_TEST_CASES_WHITE_GREY_BOX.md`.
- **Otomatis**: script Playwright (UI) dan requests (HTTP) di `tests/`; hasil `reports/AUTOMATED_TEST_REPORT.md` (HTTP 5/5 PASS; suite Playwright siap jalan dan perlu dieksekusi ulang dari jaringan tanpa proxy pembatas).
- **Temuan**: 3 defect (header keamanan belum lengkap - medium; konten bergantung penuh pada JS - low; normalisasi parameter tanpa pemberitahuan - low) di `reports/DEFECT_LOG.md`.
- **Metrik kualitas** ISO 25010: `docs/05_METRIK_KUALITAS_ISO_25010.md`.

## 4. Wawancara QA Profesional (Poin 4)
Status: **belum dilaksanakan** per 21 November 2026. Pedoman, syarat narasumber (>= 3 tahun), dan 14 pertanyaan siap di `docs/07_PEDOMAN_WAWANCARA.md`; template hasil di `reports/WAWANCARA_QA_PROFESIONAL.md`. Target pelaksanaan paling lambat 11 Desember 2026 sesuai timeline. Hasil tidak dikarang sebelum wawancara terjadi.

## 5. Laporan di GitHub (Poin 5)
Seluruh laporan tersusun dalam satu repositori ini dengan struktur `docs/` (perencanaan & kasus uji), `reports/` (hasil & bukti), `tests/` (script otomasi). Pada 21 November 2026 repo dirapikan: dua file duplikat di root (`01_TEST_PLAN_ISO_29119.md` versi lama dan `02_TIMELINE.md` yang identik) dihapus karena versi resminya ada di `docs/`.

## 6. Alasan Metode & Jurnal (Poin 6)
Pemilihan kombinasi black/white/grey box, teknik EP/BVA/decision table, otomasi Playwright, dan evaluasi ISO 25010 didukung jurnal internasional (Empirical Software Engineering 2026; IJSEKE 2023; AJRCOS 2025; CEOG 2024) dan jurnal SINTA 1-3 (JSINBIS - SINTA 2; JUTI - SINTA 2; JuTISI - SINTA 3). Uraian lengkap: `docs/06_LANDASAN_METODE.md`.

## 7. Kesimpulan & Saran
Fungsionalitas inti Qatiarent (katalog, filter, penanganan parameter) bekerja baik pada pengujian 21 November 2026. Kelemahan utama ada pada pengerasan keamanan sisi header dan ketergantungan rendering JavaScript. Untuk pemilik aplikasi: lengkapi header keamanan dan pertimbangkan SSR. Untuk kelompok: lengkapi eksekusi visual + screenshot, jalankan suite Playwright dari jaringan kampus, dan laksanakan wawancara sebelum 11 Desember 2026.

## 8. Checklist Ketentuan Tugas
| Poin | Status |
|---|---|
| 1. Aplikasi web skala menengah ke bawah, perusahaan/komunitas | SELESAI - Qatiarent, bukti di reports/ |
| 2. Dokumentasi standar IEEE/ISO 2022-2026 | SELESAI - docs/06 (terverifikasi, dengan koreksi judul resmi) |
| 3. Testing manual (black/white/grey) + otomatis dari awal sampai akhir | SEBAGIAN BESAR SELESAI - eksekusi tercatat; sisa: screenshot visual & eksekusi Playwright dari jaringan tanpa proxy |
| 4. Wawancara QA profesional >= 3 tahun | BELUM - pedoman siap, pelaksanaan terjadwal (paling lambat 11 Des 2026) |
| 5. Laporan di GitHub, satu repositori terstruktur | SELESAI - repo ini, duplikat dibersihkan |
| 6. Alasan metode + jurnal internasional & SINTA 1-3 | SELESAI - docs/06 (dengan catatan verifikasi ulang peringkat SINTA saat pengumpulan) |
