"""Jawaban w14 — Aplikasi Statistik: A/B Testing, Anomali, Evaluasi Model"""
from __future__ import annotations

def q01() -> bool:
    """[T/F] Pengujian A/B adalah aplikasi nyata uji hipotesis dua sampel."""
    return True

def q02() -> bool:
    """[T/F] Presisi = TP/(TP+FP) → proporsi prediksi positif yang benar."""
    return True

def q03() -> bool:
    """[T/F] Outlier dalam monitoring sistem TIDAK diabaikan — itu anomali penting."""
    return False

def q04() -> str:
    """[MC] Dataset imbalanced → F1-Score lebih tepat dari akurasi."""
    return "B"

def q05() -> str:
    """[MC] Data di luar 3σ = outlier/anomali."""
    return "B"

def q06() -> str:
    """[MC] Pengujian A/B untuk menentukan versi produk mana yang lebih baik."""
    return "B"

def q07() -> str:
    """[MC] Presisi=1.0 → TP/(TP+FP)=1 → FP=0 → tidak ada false positive."""
    return "A"

def q08() -> float:
    """[Numeric] Presisi = TP/(TP+FP) = 80/(80+20) = 0.8"""
    return 0.8

def q09() -> float:
    """[Numeric] Prediksi benar = akurasi × total = 0.95 × 1000 = 950"""
    return 950.0

def q10() -> float:
    """[Numeric] F1 = 2×(P×R)/(P+R) = 2×(0.8×0.8)/(0.8+0.8) = 0.8"""
    return 0.8

def q11() -> float:
    """[Numeric] Z = (110-100)/5 = 2"""
    return 2.0

def q12() -> float:
    """[Numeric] p-value=0.001 < α=0.05 → ada perbedaan signifikan → 1"""
    return 1.0
