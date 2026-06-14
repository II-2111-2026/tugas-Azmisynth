"""Jawaban w12 — Uji Hipotesis (Hypothesis Testing)"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] p-value < α → TOLAK H0 (bukan gagal menolak)."""
    return False

def q02() -> bool:
    """[T/F] Galat Tipe I = menolak H0 padahal H0 BENAR."""
    return True

def q03() -> bool:
    """[T/F] Sampel lebih besar → power uji meningkat."""
    return True

def q04() -> str:
    """[MC] Probabilitas kekuatan bukti melawan H0 = p-value."""
    return "B"

def q05() -> str:
    """[MC] H0: μ=50 vs H1: μ≠50 → uji dua arah."""
    return "C"

def q06() -> str:
    """[MC] Menolak H0 padahal H0 SALAH = keputusan benar (Power), bukan galat.
    Kondisi menolak H0 padahal benar = Galat Tipe I."""
    return "A"

def q07() -> str:
    """[MC] Tingkat signifikansi umum = 0.05"""
    return "B"

def q08() -> float:
    """[Numeric] |z|=2.58 > z_kritis=1.96 → tolak H0 → 1"""
    return 1.0

def q09() -> float:
    """[Numeric] CI 99% → α = 1-0.99 = 0.01"""
    return 0.01

def q10() -> float:
    """[Numeric] df = n-1 = 10-1 = 9"""
    return 9.0

def q11() -> float:
    """[Numeric] p-value=0.02 < α=0.05 → tolak H0 → 1"""
    return 1.0

def q12() -> float:
    """[Numeric] z=0 → simetris sempurna → p-value dua arah = 1 (100%)"""
    return 1.0
