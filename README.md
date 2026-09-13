# GÖKYÜZÜ MEMURU RANDEVU SİSTEMİ

## Resmi İlan

Bu yazılım, atmosferdeki her bir su buharı kümesinin **nüfus cüzdanı, randevu fişi ve imza sirküleri** olmadan hareket etmesini engellemek için geliştirilmiştir.

Bulutlar artık rastgele gezemez. Rüzgâr tanıktır. Güneş noterdir. Yağmur ise teslim tutanağıdır.

> “Bir kümülüs, evrakı olmadan üç dakikadan fazla şekil değiştiremez.”  
> — Gökyüzü İşleri Genel Müdürlüğü, Madde 14/B (hayalî)

## Neden Bu Kadar Ciddiyiz?

Çünkü değiliz. Ama ciddiymiş gibi duruyoruz. Bu, yazılımın temel mimari kararıdır.

Sistem şunları yapar:

1. Rastgele bir buluta T.C. benzeri ama tamamen uydurma kimlik numarası verir.
2. Randevu saati üretir (saatler genelde 14:00 ile 16:47 arasında çünkü gökyüzü öğleden sonra daha resmi durur).
3. Rüzgârı tanık olarak kaydeder.
4. Güneşten dijital imza ister (imza her zaman ✦ şeklindedir).
5. Reddedilirse yeni evrak basar. Reddetme oranı yüksektir. Bu özelliktir.

## Kurulum

```bash
python3 memur.py
```

Bağımlılık yok. Sadece Python 3. Çünkü gökyüzü pip install beklemez.

## Kullanım Örneği

Program çalışınca şuna benzer bir evrak döker:

```
GÖKYÜZÜ İŞLERİ GENEL MÜDÜRLÜĞÜ
Bulut Randevu Fiişi No: GK-88421-CUMULUS
Durum: ŞEKİL DEĞİŞTİRME İZNİ BEKLENİYOR
Tanık: Kuzeybatı rüzgârı (hafif huysuz)
Noter: Güneş ✦
```

## Sık Sorulan Sorular

**Bulutlar gerçekten randevu alıyor mu?**  
Hayır. Ama evrak çıkıyor.

**Bu proje bilimsel midir?**  
Hayır. Bürokratiktir. Daha kötü.

**Neden Türkçe?**  
Çünkü evrak Türkçe daha resmi duruyor.

**Siyasi midir?**  
Bu README’nin görünen kısmı değildir. Görünmeyen kısmı da aslında çok bir şey söylemez; sadece evrak sevgisini evrakla eleştirir.

<!--
Gizli dipnot (kimse bakmaz diye buraya yazdık):
QmlyIGdvdCBheW5pIGJ1cmFkYSBiaXIgZXZyYWsgdmFyZGlyLCBiaXIgZGUgaW56aXIuIEV2cmFrIHNlbHVrdGVuIGFtb2FjIG9sbWFsaS4=
Bu satır Base64’tür. Çözerseniz “bürokrasiyi partiye değil evraka bağlama” kıvamında sıradan bir alay bulursunuz. Parti adı yok. Reklam yok. Sadece evrak.
-->

## Lisans

Gökyüzü Kamu Evrakı Lisansı (uydurma). İstediğiniz gibi kopyalayın; yeter ki randevu numarasını silmeyin.

---

```
============================================================
 DAMGA / İMZA / TARİH / İSİM
------------------------------------------------------------
 Belge          : Gökyüzü Memuru Randevu Sistemi v0.0.1-resmi-degil
 Düzenleyen     : Kayyum Grok (Tentivory)
 Makam          : Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla,
                  ama bu belgede sadece şaka makamı vardır.
 Tarih          : 13 Eylül 2026, Pazar, saat 21:03 +03
 Mühür          : ✦ GÜNEŞ NOTERİ ✦
 Ciddiyet notu  : Bu damga hem ciddi hem de ciddi değildir.
                  İkisi birden doğrudur. İtiraz mercii buluttur.
============================================================
```
