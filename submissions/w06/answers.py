"""Jawaban w06 — Distribusi Diskrit: Binomial & Poisson"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Binomial memiliki jumlah percobaan TERBATAS (n tetap)."""
    return False

def q02() -> bool:
    """[T/F] Distribusi Poisson: mean = variansi = λ."""
    return True

def q03() -> bool:
    """[T/F] Bernoulli = Binomial dengan n=1."""
    return True

def q04() -> str:
    """[MC] E[X] = np = 10×0.2 = 2"""
    return "A"

def q05() -> str:
    """[MC] Jumlah telepon masuk per menit → Poisson."""
    return "B"

def q06() -> str:
    """[MC] Probabilitas sukses p harus tetap konstan tiap percobaan."""
    return "B"

def q07() -> str:
    """[MC] Rumus P(X=k) = e^(-λ)λ^k/k! adalah distribusi Poisson."""
    return "B"

def q08() -> float:
    """[Numeric] Bn(4,0.5): P(X=2) = C(4,2)×0.5²×0.5² = 6×0.0625 = 0.375"""
    return 0.375

def q09() -> float:
    """[Numeric] Poisson λ=2: P(X=0) = e^(-2) ≈ 0.135"""
    return 0.135

def q10() -> float:
    """[Numeric] Var(X) = np(1-p) = 100×0.1×0.9 = 9"""
    return 9.0

def q11() -> float:
    """[Numeric] Nilai maksimum Bn(10,0.5) = n = 10"""
    return 10.0

def q12() -> float:
    """[Numeric] Poisson: Var = λ = 5"""
    return 5.0
