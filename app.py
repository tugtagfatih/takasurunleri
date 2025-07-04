from flask import Flask, render_template, request

app = Flask(__name__)

# Kullanıcının verdiği şube listesi
subeler = [
    "Adana", "Adana / Çukurova", "Afyon", "Artvin", "Antalya / Manavgat", "Aksaray", "Amasya",
    "Ankara", "Ankara / Çankaya", "Ankara / Ümitköy Çayyolu", "Ankara / Yenişehir", "Antalya",
    "Antalya / Alanya", "Aydın", "Aydın / Kuşadası", "Aydın / Söke", "Balıkesir", "Balıkesir / Ayvalık",
    "Balıkesir / Bandırma", "Balıkesir / Burhaniye", "Balıkesir / Edremit", "Bolu", "Burdur",
    "Bursa", "Çanakkale", "Çanakkale / Gelibolu", "Denizli", "Düzce", "Edirne", "Eskişehir",
    "Gaziantep", "Gaziemir", "Giresun", "Gençlik Birimi", "Isparta", "İstanbul / Ataşehir",
    "İstanbul / Avcılar", "İstanbul / Bahçelievler", "İstanbul / Bahçeşehir", "İstanbul / Bakırköy",
    "İstanbul / Beşiktaş", "İstanbul / Beylikdüzü", "İstanbul / Beyoğlu", "İstanbul / Büyükçekmece",
    "İstanbul / Erenköy", "İstanbul / Fatih", "İstanbul / Gaziosmanpaşa", "İstanbul / Göktürk",
    "İstanbul / Kadıköy", "İstanbul / Kağıthane", "İstanbul / Kartal", "İstanbul / Küçükçekmece",
    "İstanbul / Maltepe", "İstanbul / Merter", "İstanbul / Pendik", "İstanbul / Sarıyer",
    "İstanbul / Silivri", "İstanbul / Şile", "İstanbul / Şişli", "İstanbul / Ümraniye",
    "İstanbul / Üsküdar", "İstanbul / Zekeriyaköy", "İstanbul / Zeytinburnu", "İzmir",
    "İzmir / Çeşme", "İzmir / Güzelbahçe", "İzmir / Karşıyaka", "İzmir / Ödemiş",
    "İzmir / Seferihisar", "İzmir / Selçuk", "İzmir / Torbalı", "İzmir / Urla",
    "Karadeniz Ereğli", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırklareli",
    "Kırklareli / Lüleburgaz", "Kocaeli / İzmit", "Kocaeli / Değirmendere", "Kocaeli / Gebze",
    "Kocaeli / Kandıra", "Kocaeli / Körfez / Yarımca", "Konya", "Konya / Akşehir",
    "Konya / Ereğli", "Kütahya", "Kütahya / Tavşanlı", "Manisa", "Manisa / Akhisar",
    "Manisa / Alaşehir", "Manisa / Salihli", "Manisa / Soma", "Mersin", "Mersin / Mezitli",
    "Mersin / Silifke", "Mersin / Tarsus", "Muğla", "Muğla / Bodrum", "Muğla / Fethiye",
    "Muğla / Marmaris", "Nevşehir / Ürgüp", "Niğde", "Sakarya", "Samsun",
    "Samsun / 19 Mayıs Atakum", "Sinop", "Sivas", "Tekirdağ", "Tekirdağ / Çerkezköy",
    "Tekirdağ /Çorlu", "Trabzon", "Uşak", "Yalova", "Yalova / Altınova", "Zonguldak"
]

# Örnek ürün veritabanı (normalde bu bir veritabanında olur)
urunler = [
    {
        "id": 1,
        "ad": "Vintage Kot Ceket",
        "beden": "M",
        "renk": "Mavi",
        "sehir": "İstanbul",
        "sube": "İstanbul / Kadıköy",
        "fiyat": 250
    },
    {
        "id": 2,
        "ad": "Yazlık Keten Gömlek",
        "beden": "L",
        "renk": "Beyaz",
        "sehir": "İzmir",
        "sube": "İzmir / Çeşme",
        "fiyat": 180
    },
    {
        "id": 3,
        "ad": "Desenli T-Shirt",
        "beden": "S",
        "renk": "Siyah",
        "sehir": "Ankara",
        "sube": "Ankara / Çankaya",
        "fiyat": 90
    },
    {
        "id": 4,
        "ad": "Kışlık Yün Kazak",
        "beden": "XL",
        "renk": "Bordo",
        "sehir": "Bursa",
        "sube": "Bursa",
        "fiyat": 220
    },
    {
        "id": 5,
        "ad": "Kargo Pantolon",
        "beden": "M",
        "renk": "Haki",
        "sehir": "Antalya",
        "sube": "Antalya / Alanya",
        "fiyat": 150
    }
]


@app.route('/')
def index():
    # Filtreleme için URL'den parametreleri al
    secili_sehir = request.args.get('sehir')
    secili_sube = request.args.get('sube')
    secili_beden = request.args.get('beden')
    secili_renk = request.args.get('renk')

    # Filtrelenecek ürün listesini kopyala
    filtrelenmis_urunler = urunler[:]

    # Şehir filtresini uygula
    if secili_sehir:
        filtrelenmis_urunler = [u for u in filtrelenmis_urunler if u['sehir'] == secili_sehir]

    # Şube filtresini uygula
    if secili_sube:
        filtrelenmis_urunler = [u for u in filtrelenmis_urunler if u['sube'] == secili_sube]

    # Beden filtresini uygula
    if secili_beden:
        filtrelenmis_urunler = [u for u in filtrelenmis_urunler if u['beden'] == secili_beden]

    # Renk filtresini uygula
    if secili_renk:
        filtrelenmis_urunler = [u for u in filtrelenmis_urunler if u['renk'] == secili_renk]

    # Filtre seçeneklerini doldurmak için benzersiz değerleri al
    sehirler = sorted(list(set(u['sehir'] for u in urunler)))
    renkler = sorted(list(set(u['renk'] for u in urunler)))
    bedenler = ["S", "M", "L", "XL"]

    return render_template(
        'index.html',
        urunler=filtrelenmis_urunler,
        sehirler=sehirler,
        subeler=sorted(subeler),
        bedenler=bedenler,
        renkler=renkler,
        secili_sehir=secili_sehir,
        secili_sube=secili_sube,
        secili_beden=secili_beden,
        secili_renk=secili_renk
    )

if __name__ == '__main__':
    app.run(debug=True)
