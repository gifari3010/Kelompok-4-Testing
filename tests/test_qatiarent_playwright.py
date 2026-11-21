"""
Pengujian otomatis website Qatiarent (https://qatiarent.com)
Kelompok 4 - Testing & QA, Universitas Pamulang

Cara menjalankan:
    pip install playwright pytest
    playwright install chromium
    pytest tests/test_qatiarent_playwright.py -v

Catatan etika pengujian: tes ini hanya membaca halaman publik dengan
frekuensi rendah. Tidak ada transaksi/pembayaran nyata yang dilakukan.
"""
import re
import pytest
from playwright.sync_api import sync_playwright

BASE = "https://qatiarent.com"


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()
        yield pg
        browser.close()


def test_homepage_loads_and_shows_products(page):
    """TC-OT-01: Halaman utama termuat (HTTP 200) dan menampilkan produk."""
    resp = page.goto(BASE + "/", wait_until="domcontentloaded", timeout=60000)
    assert resp is not None and resp.status == 200
    assert "Qatia" in page.title()
    body = page.inner_text("body")
    assert "results" in body  # indikator jumlah hasil, mis. "Showing 1 to 24 of 230 results"
    assert "Rp" in body       # harga produk tampil


def test_filter_parameters_are_accepted(page):
    """TC-OT-02: Kombinasi parameter filter (city, duration, shippingType, useByDate) diterima."""
    url = BASE + "/?city=1&duration=1&shippingType=Next%20day&useByDate=23-11-2026"
    resp = page.goto(url, wait_until="domcontentloaded", timeout=60000)
    assert resp is not None and resp.status == 200
    body = page.inner_text("body")
    assert "Rp" in body


def test_invalid_city_falls_back_without_error(page):
    """TC-OT-03: Nilai kota tidak valid tidak menimbulkan error 5xx; situs kembali ke pilihan default."""
    resp = page.goto(BASE + "/?city=KOTA_TIDAK_ADA_123", wait_until="domcontentloaded", timeout=60000)
    assert resp is not None and resp.status < 500


def test_product_detail_opens(page):
    """TC-OT-04: Klik produk pertama membuka halaman detail yang memuat harga."""
    page.goto(BASE + "/", wait_until="domcontentloaded", timeout=60000)
    link = page.locator("a[href*='/product'], a[href*='product']").first
    if link.count() == 0:
        pytest.skip("Tautan detail produk tidak ditemukan pada struktur halaman saat ini")
    href = link.get_attribute("href")
    resp = page.goto(href if href.startswith("http") else BASE + href,
                     wait_until="domcontentloaded", timeout=60000)
    assert resp is not None and resp.status == 200
    assert "Rp" in page.inner_text("body")


def test_unknown_page_returns_404(page):
    """TC-OT-05: URL yang tidak ada mengembalikan HTTP 404."""
    resp = page.goto(BASE + "/halaman-tidak-ada-xyz123", wait_until="domcontentloaded", timeout=60000)
    assert resp is not None and resp.status == 404


def test_mobile_viewport_loads(page):
    """TC-OT-06: Halaman utama termuat pada viewport mobile (375x667)."""
    page.set_viewport_size({"width": 375, "height": 667})
    resp = page.goto(BASE + "/", wait_until="domcontentloaded", timeout=60000)
    assert resp is not None and resp.status == 200
    assert "Rp" in page.inner_text("body")
    page.set_viewport_size({"width": 1280, "height": 800})
