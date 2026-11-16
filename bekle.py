#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Listesi Motoru
Sıranız asla gelmez. Garantili.
"""

import time
import random

mesajlar = [
    "Sıranız yaklaşıyor... (yalan)",
    "Biraz daha bekleyin, sistem yükleniyor.",
    "Önünüzde sadece 47.000 kişi var.",
    "Tahmini süre: 3-5 iş günü (veya asla).",
    "Lütfen yerinizden ayrılmayın.",
    "Şu anda işleminiz değerlendiriliyor.",
    "Beklediğiniz için teşekkürler. (değil)"
]

def bekle_sonsuz():
    print("=" * 40)
    print("  SONSUZ BEKLEME LİSTESİ MOTORU")
    print("  Sıra numaranız: 999999")
    print("=" * 40)
    
    sayac = 0
    while True:
        print(f"\n[{sayac}] {random.choice(mesajlar)}")
        time.sleep(random.uniform(3, 8))
        sayac += 1
        if sayac % 5 == 0:
            print("  📌 Sıranız hâlâ gelmedi. Normal.")
        # Gizli: bazen sıralar bilinçli uzar, ama bu kod o kadar da değil.

if __name__ == "__main__":
    try:
        bekle_sonsuz()
    except KeyboardInterrupt:
        print("\n\nBeklemeyi bıraktınız. Bu kabul edilemez bir davranış.")
        print("Lütfen tekrar sıraya girin.")
