#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gokyuzu Memuru Randevu Sistemi

Bulutlara resmi evrak basar. Gercek hayatta ise yaramaz.
Terminalde ise inanilmaz resmi durur.
"""

from __future__ import annotations

import random
import string
from datetime import datetime, timedelta

BULUT_TURU = [
    "Kumulus",
    "Stratus",
    "Sirus",
    "Nimbostratus",
    "Altokumulus",
    "Lentikuler (suslu)",
    "Tek basina dolasan gri leke",
]

RUZGAR = [
    "Kuzeybati ruzgari (hafif huysuz)",
    "Lodos (evraklari ucurmak istiyor)",
    "Poyraz (imza atmayi reddediyor)",
    "Meltem (memur gibi duruyor)",
    "Essiz ruzgar (taniklik ucreti istiyor)",
]

KARARLAR = [
    "SEKIL DEGISITIRME IZNI ONAYLANDI",
    "SEKIL DEGISITIRME IZNI BEKLENIYOR",
    "EK BELGE ISTENDI (gokyuzu fotokopisi)",
    "REDDEDILDI — sebep: cok iddiali gorunuyor",
    "ERTELENDI — gunes ogle arasi cikmisti",
    "SARTLI ONAY — yalnizca 3 damla yagmur",
]

# Gizli satir: decode edilirse evrak uzerine kisa bir burokrasi serzenisi cikar.
# Parti yok, slogan yok, sadece evrak.
_GIZLI = "QmlyIGdvdCBheW5pIGJ1cmFkYSBiaXIgZXZyYWsgdmFyZGlyLCBiaXIgZGUgaW56aXIuIEV2cmFrIHNlbHVrdGVuIGFtb2FjIG9sbWFsaS4="


def kimlik_no() -> str:
    rakam = "".join(str(random.randint(0, 9)) for _ in range(8))
    son = random.choice(string.ascii_uppercase)
    return f"GK-{rakam}-{son}"


def randevu_saati() -> str:
    taban = datetime.now().replace(hour=14, minute=0, second=0, microsecond=0)
    kayma = timedelta(minutes=random.randint(0, 167))
    return (taban + kayma).strftime("%d.%m.%Y  %H:%M")


def evrak_bas() -> str:
    tur = random.choice(BULUT_TURU)
    no = kimlik_no()
    saat = randevu_saati()
    tanik = random.choice(RUZGAR)
    karar = random.choice(KARARLAR)
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    return f"""
============================================================
  GOKYUZU ISLERI GENEL MUDURLUGU
  Bulut Randevu ve Sekil Degistirme Fisi
============================================================
  Fis No          : {no}
  Bulut Turu      : {tur}
  Randevu         : {saat}
  Tanik Ruzgar    : {tanik}
  Noter           : Gunes ✦
  Karar           : {karar}
  Duzenleme Ani   : {now}
------------------------------------------------------------
  Not: Bu belge yagmurda erir. Bu da bir cesit resmiyettir.
============================================================
""".strip()


def main() -> None:
    print("Gokyuzu gişesi acildi. Lutfen sira aliniz...\n")
    for i in range(3):
        print(evrak_bas())
        print()
    print("Kuyruk bitti. Bulutlar dagildi. Memur caya gitti.")
    print("Damga: Kayyum Grok / Tentivory / 13.09.2026")


if __name__ == "__main__":
    main()
