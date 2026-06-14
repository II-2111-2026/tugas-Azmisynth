"""Jawaban w11 — Interval Kepercayaan (Confidence Interval)"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Tingkat kepercayaan lebih tinggi → interval lebih lebar."""
    return True

def q02() -> bool:
    """[T/F] CI 95% yang sudah dihitung: parameter ada atau tidak ada di dalamnya (bukan probabilitas 95%).
    Pernyataan ini SALAH — interpretasi yang benar: 95% dari interval yang dibangun berulang berisi parameter."""
    return False

def q03() -> bool:
    """[T/F] t-Student → Normal saat df → ∞."""
    return True

def q04() -> str:
    """[MC] Mempersempit CI tanpa ubah tingkat kepercayaan = tingkatkan ukuran sampel."""
    return "B"

def q05() -> str:
    """[MC] z kritis untuk 95% = 1.96"""
    return "B"

def q06() -> str:
    """[MC] df = n-1"""
    return "C"

def q07() -> str:
    """[MC] Estimasi titik terbaik untuk μ = X̄"""
    return "C"

def q08() -> float:
    """[Numeric] Batas bawah = X̄ - ME = 100 - 5 = 95"""
    return 95.0

def q09() -> float:
    """[Numeric] SE = s/√n = 4/√16 = 4/4 = 1"""
    return 1.0

def q10() -> float:
    """[Numeric] df = n-1 = 25-1 = 24"""
    return 24.0

def q11() -> float:
    """[Numeric] Titik tengah interval [a,b] = (a+b)/2; contoh (45,55) → 50"""
    return 50.0

def q12() -> float:
    """[Numeric] ME = z × SE → 2 = 2 × SE → SE = 1"""
    return 1.0
