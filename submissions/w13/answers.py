"""Jawaban w13 — Regresi Linear"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Regresi meminimalkan KUADRAT selisih (OLS), bukan absolut."""
    return False

def q02() -> bool:
    """[T/F] R²=0.85 berarti 85% variasi Y dijelaskan oleh X."""
    return True

def q03() -> bool:
    """[T/F] Regresi berganda menggunakan >1 variabel independen."""
    return True

def q04() -> str:
    """[MC] Dalam Y = β0 + β1·X: β1 = kemiringan (slope)."""
    return "B"

def q05() -> str:
    """[MC] r=-0.9 → hubungan sangat kuat dan negatif."""
    return "B"

def q06() -> str:
    """[MC] R²=0.00 → model paling buruk (tidak ada variasi yang dijelaskan)."""
    return "C"

def q07() -> str:
    """[MC] Garis regresi memotong sumbu Y = Intersep."""
    return "B"

def q08() -> float:
    """[Numeric] Ŷ = 5 + 2×10 = 25"""
    return 25.0

def q09() -> float:
    """[Numeric] r = √R² = √0.64 = 0.8"""
    return 0.8

def q10() -> float:
    """[Numeric] Rata-rata residual pada OLS klasik = 0"""
    return 0.0

def q11() -> float:
    """[Numeric] slope β1 = ΔY/ΔX = 10/2 = 5"""
    return 5.0

def q12() -> float:
    """[Numeric] β1 = Sxy/Sxx = 40/10 = 4"""
    return 4.0
