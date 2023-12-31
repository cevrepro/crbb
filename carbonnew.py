import matplotlib.pyplot as plt

def soru_sor_float(soru):
    return float(input(f"{soru} (örneğin: 0.5): "))

def soru_sor_bool(soru):
    return input(f"{soru} (evet/hayır): ").lower() == 'evet'

def karbon_ayak_izi_hesapla():
    toplam_karbon_ayak_izi = 0

    toplam_karbon_ayak_izi += soru_sor_float("Haftalık elektrik tüketimi (kWh): ") * 0.057
    toplam_karbon_ayak_izi += soru_sor_float("Günlük doğal gaz tüketimi (m³): ") * 0.2
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık araç benzin tüketimi (litre): ") * 0.3286
    toplam_karbon_ayak_izi += soru_sor_bool("Toplu taşıma kullanıyor musunuz? ") * 0.15
    toplam_karbon_ayak_izi += soru_sor_float("Günlük uçak seyahati mesafesi (km): ") * 0.25
    toplam_karbon_ayak_izi += soru_sor_float("Günlük su tüketimi (m³): ") * 0.0714
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık ürün ambalaj atıkları ağırlığı (kg): ") * 0.00714
    toplam_karbon_ayak_izi += soru_sor_float("Günlük bilgisayar ve cihaz enerji tüketimi (kWh): ") * 0.05
    toplam_karbon_ayak_izi += soru_sor_bool("Evde kullanılan doğal gaz yenilenebilir kaynaklı mı? ") * 0.1
    toplam_karbon_ayak_izi += soru_sor_float("Günlük kişi başına su tüketimi (m³): ") * 0.3
    toplam_karbon_ayak_izi += soru_sor_bool("Evde kullanılan ısıtma sistemini yenilenebilir kaynaklardan mı alıyorsunuz? ") * 0.2
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık etkinliklerden kaynaklanan karbon salınımı (kg): ") * 1.4286
    toplam_karbon_ayak_izi += soru_sor_float("Günlük beyaz eşya enerji tüketimi (kWh): ") * 0.2
    toplam_karbon_ayak_izi += soru_sor_float("Günlük uçak seyahati karbon salınımı (kg): ") * 50
    toplam_karbon_ayak_izi += soru_sor_float("Günlük kısa mesafe seyahatleri karbon salınımı (kg): ") * 1
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık alışveriş karbon salınımı (kg): ") * 1.4286
    toplam_karbon_ayak_izi += soru_sor_bool("Kullanılmayan elektronik cihazların fişini çekiyor musunuz? ") * 0.02
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık işe gitme araç karbon salınımı (kg): ") * 0.5714
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık tatil karbon salınımı (kg): ") * 2.8571
    toplam_karbon_ayak_izi += soru_sor_float("Haftalık etkinlik karbon salınımı (kg): ") * 0.7143
    toplam_karbon_ayak_izi += soru_sor_float("Günlük beyaz eşya enerji tüketimi (kWh): ") * 0.2

    # Diğer hesaplama adımları...

    return toplam_karbon_ayak_izi

def grafik_ciz(toplam_karbon_ayak_izi):
    plt.bar(["Toplam Karbon Ayak İzi"], [toplam_karbon_ayak_izi], color='green')
    plt.ylabel("CO2 Eşdeğeri (kg)")
    plt.title("Toplam Karbon Ayak İzi")
    plt.show()

def main():
    print("Karbon Ayak İzi Hesaplama Programına Hoş Geldiniz")
    toplam_karbon_ayak_izi = karbon_ayak_izi_hesapla()
    print(f"Toplam Karbon Ayak İzi: {toplam_karbon_ayak_izi:.2f} kgCO2")
    grafik_ciz(toplam_karbon_ayak_izi)

if __name__ == "__main__":
    main()
