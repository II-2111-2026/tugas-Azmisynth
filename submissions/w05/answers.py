"""Jawaban w05 — Variabel Acak: Nilai Harapan & Variansi"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] E[X] tidak harus merupakan nilai yang mungkin (bisa di antara nilai)."""
    return False

def q02() -> bool:
    """[T/F] Variansi tidak pernah negatif (definisi non-negatif)."""
    return True

def q03() -> bool:
    """[T/F] Jika X = c (konstanta), E[X]=c dan Var(X)=0."""
    return True

def q04() -> str:
    """[MC] E[2X+3] = 2E[X]+3 = 2×5+3 = 13"""
    return "B"

def q05() -> str:
    """[MC] Var(X) = E[X²] - (E[X])²"""
    return "A"

def q06() -> str:
    """[MC] Fungsi P(X=x) = PMF (Probability Mass Function)."""
    return "C"

def q07() -> str:
    """[MC] Simpangan baku = akar kuadrat dari variansi."""
    return "A"

def q08() -> float:
    """[Numeric] E[X] = 0×0.4 + 1×0.6 = 0.6"""
    return 0.6

def q09() -> float:
    """[Numeric] Var(X) = E[X²]-(E[X])² = (0²×0.4+1²×0.6)-0.6² = 0.6-0.36 = 0.24"""
    return 0.24

def q10() -> float:
    """[Numeric] Var(X) = E[X²]-(E[X])² = 116-100 = 16"""
    return 16.0

def q11() -> float:
    """[Numeric] E[X] = (1+2+3)/3 = 2"""
    return 2.0

def q12() -> float:
    """[Numeric] Var(3X+5) = 9×Var(X) = 9×4 = 36"""
    return 36.0
