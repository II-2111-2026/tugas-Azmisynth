"""Jawaban w04 — Probabilitas Kondisional & Teorema Bayes"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Jika A dan B independen, P(A|B) = P(A)."""
    return True

def q02() -> bool:
    """[T/F] P(A|B) tidak selalu sama dengan P(B|A)."""
    return False

def q03() -> bool:
    """[T/F] Teorema Bayes memungkinkan membalik kondisi probabilitas."""
    return True

def q04() -> str:
    """[MC] A,B independen: P(A∩B) = 0.5×0.4 = 0.2"""
    return "C"

def q05() -> str:
    """[MC] Rumus Bayes: P(A|B) = P(B|A)P(A)/P(B)"""
    return "A"

def q06() -> str:
    """[MC] Hasil satu eksperimen tidak mempengaruhi lainnya = Independen."""
    return "B"

def q07() -> str:
    """[MC] Sensitivitas tinggi = probabilitas mendeteksi orang sakit sangat tinggi."""
    return "B"

def q08() -> float:
    """[Numeric] P(A|B) = P(A∩B)/P(B) = 0.2/0.5 = 0.4"""
    return 0.4

def q09() -> float:
    """[Numeric] P(Hujan ∩ Macet) = P(Macet|Hujan)×P(Hujan) = 0.8×0.1 = 0.08"""
    return 0.08

def q10() -> float:
    """[Numeric] Bayes: P(Sakit|+) = (0.99×0.01)/((0.99×0.01)+(0.01×0.99)) = 0.5"""
    return 0.5

def q11() -> float:
    """[Numeric] P(B) = P(B|A)P(A) + P(B|Ac)P(Ac) = 0.7×0.3 + 0.4×0.7 = 0.21+0.28 = 0.49"""
    return 0.49

def q12() -> float:
    """[Numeric] P(A|B) = P(B|A)P(A)/P(B) = (0.7×0.3)/0.49 ≈ 0.429"""
    return 0.429
