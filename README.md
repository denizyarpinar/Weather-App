# 🌤️ Weather App (Hava Durumu Uygulaması)

Bu proje, Python'ın popüler GUI (Grafiksel Kullanıcı Arayüzü) kütüphanesi **Tkinter** ve **OpenWeatherMap API** kullanılarak geliştirilmiş masaüstü tabanlı bir hava durumu uygulamasıdır. Kullanıcıların arattığı şehre ait anlık sıcaklık, basınç, nem ve hava durumu açıklaması verilerini dinamik olarak çeker ve listeler.

---

## 🚀 Özellikler

- **Kullanıcı Dostu Arayüz:** Tkinter kütüphanesi ile sade, anlaşılır ve kullanımı kolay modern bir GUI tasarımı.
- **Canlı Veri Takibi:** OpenWeatherMap API entegrasyonu sayesinde dünya genelindeki şehirlerin anlık hava durumu bilgileri.
- **Dinamik Listeleme:** Şehir araması başarılı olduğunda arama alanı gizlenir ve verileri seçebileceğiniz etkileşimli bir `Listbox` yapısı devreye girer.
- **Hata Yönetimi:** Geçersiz şehir isimleri (404 hatası) veya internet bağlantı sorunları için terminal tabanlı bilgilendirme mekanizması.

---

## 🛠️ Kullanılan Teknolojiler

- **Programlama Dili:** Python 3.x
- **Arayüz Kütüphanesi:** Tkinter (Python ile dahili gelir)
- **Ağ/Protokol Yönetimi:** `requests` kütüphanesi (API istekleri için)
- **Veri Sağlayıcı (API):** OpenWeatherMap API

---

## 📦 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Gereksinimlerin Yüklenmesi

Projenin internet üzerinden veri çekebilmesi için `requests` kütüphanesine ihtiyacı vardır. Eğer bilgisayarınızda yüklü değilse, terminal veya komut satırını açarak aşağıdaki komutla yükleyebilirsiniz:

```bash
pip install requests
