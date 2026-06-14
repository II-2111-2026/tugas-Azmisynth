"""Jawaban w10 — Distribusi Sampling & Teorema Limit Pusat (CLT)"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] CLT: rata-rata sampel mendekati Normal jika n≥30."""
    return True

def q02() -> bool:
    """[T/F] μ_X̄ = μ (rata-rata distribusi sampling = rata-rata populasi)."""
    return True

def q03() -> bool:
    """[T/F] Semakin besar n, Standard Error SEMAKIN KECIL (bukan besar)."""
    return False

def q04() -> str:
    """[MC] SE = σ/√n = 10/√100 = 10/10 = 1"""
    return "B"

def q05() -> str:
    """[MC] Proporsi sampel mendekati Normal jika np≥5 dan n(1-p)≥5."""
    return "B"

def q06() -> str:
    """[MC] SE berkurang dengan √n: perlu 4× sampel untuk setengah error."""
    return "B"

def q07() -> str:
    """[MC] Statistik yang menduga parameter populasi = Estimator."""
    return "A"

def q08() -> float:
    """[Numeric] μ_X̄ = μ = 50 (tidak tergantung n)"""
    return 50.0

def q09() -> float:
    """[Numeric] SE = σ/√n = 12/√36 = 12/6 = 2"""
    return 2.0

def q10() -> float:
    """[Numeric] Z = (X̄-μ)/SE = (104-100)/2 = 2"""
    return 2.0

def q11() -> float:
    """[Numeric] σ_X̄ = σ/√n = 8/√64 = 8/8 = 1"""
    return 1.0

def q12() -> float:
    """[Numeric] X̄ = μ + Z·SE = 80 + 1.5×4 = 80+6 = 86"""
    return 86.0
