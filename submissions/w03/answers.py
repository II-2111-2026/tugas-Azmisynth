"""Jawaban w03 — Reliabilitas Sistem (Seri & Paralel)"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Konfigurasi paralel gagal hanya jika SEMUA komponen gagal."""
    return True

def q02() -> bool:
    """[T/F] Komponen seri MENURUNKAN reliabilitas, bukan meningkatkan."""
    return False

def q03() -> bool:
    """[T/F] Reliabilitas sistem seri ≤ reliabilitas komponen terlemah."""
    return True

def q04() -> str:
    """[MC] Paralel 2 komponen R=0.9: 1-(1-0.9)^2 = 1-0.01 = 0.99"""
    return "B"

def q05() -> str:
    """[MC] Seri 3 komponen R=0.8: 0.8^3 = 0.512"""
    return "A"

def q06() -> str:
    """[MC] Paralel paling tahan kegagalan komponen tunggal."""
    return "B"

def q07() -> str:
    """[MC] Probabilitas sistem berfungsi pada waktu t = Reliabilitas."""
    return "B"

def q08() -> float:
    """[Numeric] Seri: R = 0.95 × 0.8 = 0.76"""
    return 0.76

def q09() -> float:
    """[Numeric] P(dua server gagal bersamaan) = (1-0.9)^2 = 0.01"""
    return 0.01

def q10() -> float:
    """[Numeric] P(gagal) = 1 - 0.99 = 0.01"""
    return 0.01

def q11() -> float:
    """[Numeric] Paralel 3 lampu R=0.5: 1-(1-0.5)^3 = 1-0.125 = 0.875"""
    return 0.875

def q12() -> float:
    """[Numeric] Seri 10 komponen R=0.99: 0.99^10 ≈ 0.904"""
    return 0.904
