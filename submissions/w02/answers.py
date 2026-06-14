"""Jawaban w02 — Hukum Probabilitas & Operasi Himpunan"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Jika dua kejadian A dan B saling lepas, maka P(A∩B) = 0."""
    return True

def q02() -> bool:
    """[T/F] Probabilitas dari gabungan dua kejadian selalu lebih besar daripada probabilitas masing-masing kejadian."""
    return False

def q03() -> bool:
    """[T/F] Hukum komplemen menyatakan bahwa P(A)+P(Ac) = 1."""
    return True

def q04() -> str:
    """[MC] P(A∪B) jika P(A)=0.4, P(B)=0.3, saling lepas → 0.4+0.3 = 0.7"""
    return "A"

def q05() -> str:
    """[MC] Simbol irisan antara kejadian A dan B."""
    return "B"

def q06() -> str:
    """[MC] Jika A ⊂ B, maka P(A∩B) = P(A)."""
    return "B"

def q07() -> str:
    """[MC] Area di luar lingkaran A di diagram Venn = komplemen A (Ac)."""
    return "B"

def q08() -> float:
    """[Numeric] P(A∪B) = P(A)+P(B)-P(A∩B) = 0.6+0.5-0.2 = 0.9"""
    return 0.9

def q09() -> float:
    """[Numeric] P(berhasil) = 1 - P(gagal) = 1 - 0.05 = 0.95"""
    return 0.95

def q10() -> float:
    """[Numeric] Saling lepas → P(A∩B) = 0"""
    return 0.0

def q11() -> float:
    """[Numeric] P(genap) pada dadu = 3/6 = 0.5"""
    return 0.5

def q12() -> float:
    """[Numeric] Saling lepas: P(A∪B) = P(A)+P(B) → 0.8 = 0.5+P(B) → P(B) = 0.3"""
    return 0.3
