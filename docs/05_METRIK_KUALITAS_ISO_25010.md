# METRIK & EVALUASI KUALITAS - ISO/IEC 25010:2023

Proses evaluasi mengikuti ISO/IEC 25040:2024 (Quality evaluation framework): menetapkan kebutuhan evaluasi, menentukan metrik, melaksanakan pengukuran, lalu menyimpulkan tingkat kualitas.

| Karakteristik (ISO 25010:2023) | Metrik | Cara Ukur | Hasil Awal (21 Nov 2026) |
|---|---|---|---|
| Functional Suitability | % kasus uji fungsional PASS | Eksekusi kasus BB-01 s.d. BB-16 | Lihat laporan eksekusi manual & otomatis |
| Performance Efficiency | Waktu respons halaman utama; ukuran halaman | Pengukuran HTTP berulang (3x) | Respons 200 dalam ±0,9-1,2 detik; ukuran HTML ±131,8 KB (dari lingkungan uji kelompok) |
| Compatibility | Halaman termuat di viewport desktop & mobile | Playwright viewport 1280x800 dan 375x667; uji browser Chrome | Script tersedia di `tests/`; eksekusi UI penuh dilakukan dari jaringan tanpa proxy |
| Interaction Capability | Kelengkapan label produk (nama, brand, harga, ukuran) | Checklist pada 24 produk halaman pertama | Semua produk halaman pertama menampilkan nama, brand, harga "Rp .../1-3 days", dan ukuran Fit |
| Reliability | Konsistensi status pada pemuatan ulang | GET berulang ke beranda | 200 konsisten pada pengulangan |
| Security (pasif) | Kehadiran header keamanan; redirect HTTPS; penanganan input | Inspeksi header & parameter invalid | HTTPS + redirect 301 baik; HSTS / X-Frame-Options / X-Content-Type-Options belum ada (defect D-01) |
| Maintainability / Flexibility / Safety | - | Tidak diukur: tidak ada akses kode dan tidak relevan untuk portal rental publik | Di luar cakupan (sesuai test plan) |

**Catatan:** Angka performa bersifat indikatif dari satu lingkungan uji pada 21 November 2026 dan dapat berbeda menurut jaringan/lokasi. Pengukuran lanjutan (Lighthouse) dicatat di laporan otomatis bila sudah dijalankan.
