from django.contrib.auth.models import User
from todos.models import Todo
import random

# Önceden tanımlanmış görev kelimeleri
tasks = [
    "Yeni proje için gereksinimleri topla",
    "Müşteri uygulaması için veritabanı şemasını tasarla",
    "Kullanıcı kimlik doğrulama modülünü uygula",
    "RESTful API uç noktalarını geliştir",
    "Temel işlevler için birim testleri yaz",
    "Takım üyeleri için kod incelemesi yap",
    "QA ekibi tarafından rapor edilen hataları düzelt",
    "Performans için veritabanı sorgularını optimize et",
    "Harici geliştiriciler için API uç noktalarını belgele",
    "Stajyer ortamı için dağıtım betikleri hazırla",
    "Üretim sunucularında yük testi yap",
    "Mobil uygulama için UI tel çizimlerini tasarla",
    "React kullanarak ön uç bileşenlerini uygula",
    "Üçüncü taraf ödeme ağ geçidini entegre et",
    "Confluence'da proje belgelerini güncelle",
    "Sprint retrospektif toplantısı yap",
    "Web uygulaması için güvenlik denetimi yap",
    "Uygulama performans profilleme yap",
    "Teknik özellik belgesi hazırla",
    "API yanıtları için önbellekleme stratejisi uygula",
    "AI/ML algoritmaları üzerine araştırma yap ve uygula",
    "Otomatik dağıtım boru hattı oluştur",
    "Kullanıcı grubuyla kullanılabilirlik testi yap",
    "Gerçek zamanlı güncellemeler için web soketleri uygula",
    "Üretim sunucuları için izleme uyarıları ayarla",
    "İçerik yönetimi için yönetici paneli geliştir",
    "UX/UI tasarımı için kullanıcı kişaları oluştur",
    "Jenkins kullanarak CI/CD boru hattı yapılandır",
    "Son teknolojiler hakkında teknik blog yazısı yaz",
    "Yeni işe alımlar için eğitim materyalleri hazırla",
    "Şirket kodlama standartlarını gözden geçir ve güncelle",
    "Geliştiriciler için takım oluşturma etkinliği düzenle",
    "iOS platformu için mobil uygulama geliştir",
    "E-posta bildirim servisini uygula",
    "Mobil uygulamalar için sürekli entegrasyon kurulumu yap",
    "Web uygulaması için erişilebilirlik denetimi yap",
    "Ölçeklenebilirlik için mikro hizmet mimarisini geliştir",
    "OAuth2 kimlik doğrulama akışını uygula",
    "Selenium kullanarak otomatik test betikleri oluştur",
    "Veri görselleştirme panosu tasarla ve uygula",
    "Konteyner yönetimi için Kubernetes kümesi kur",
    "API uç noktaları için performans ölçütleri yaz",
    "Django çerçevesi kullanarak backend hizmetleri geliştir",
    "Uygulama için çok dil desteği uygula",
    "Özellik karşılaştırması için A/B testi yap",
    "Ön uç varlıklarını daha hızlı yüklemek için optimize et",
    "Takım güncellemeleri için Slack bildirimlerini entegre et",
    "Uygulama için video konferans özelliği geliştir",
    "GDPR uyumluluk özelliklerini uygula",
    "İş süreçleri için iş akışları otomasyonu oluştur",
    "Yazılım güncellemeleri için otomatik güncelleme mekanizması oluştur",
    "Kod tabanını sık sık güncellemek ve bakım yapmak",
    "Güvenlik açıkları için düzenli tarama yap",
    "Müşteri geri bildirimlerini analiz et ve iyileştirme önerileri sun",
    "DevOps süreçlerini iyileştirmek için öneriler geliştir",
    "Yazılım eğitimleri düzenlemek ve sunmak",
    "Performansı izlemek ve iyileştirme fırsatlarını belirlemek",
    "Kodlama standartlarını takip etmek ve geliştirmek",
    "Günlük stand-up toplantıları düzenlemek",
    "Ürün yönetimi ile işbirliği yaparak ürün gereksinimlerini anlamak",
    "Kullanıcı geri bildirimleri ile ürün özelliklerini iyileştirmek",
    "Yeni teknolojiler üzerine araştırmalar yapmak ve raporlamak",
    "Yazılım geliştirme süreçlerini belgelemek ve güncellemek",
    "Proje yönetimi yazılımı kullanarak projeleri izlemek",
    "Uygulama için yük testleri yapmak ve iyileştirme önerileri sunmak",
    "Müşteri taleplerine hızlı yanıt vermek",
    "Proje sürümlerini yönetmek ve güncellemeleri sağlamak",
    "Yazılım mühendisliği standartlarını ve yönergelerini takip etmek",
    "Güvenlik politikalarını ve prosedürlerini uygulamak",
    "Mevcut ürünlerin sürdürülebilirliğini sağlamak",
    "Çeşitli ekiplerle işbirliği yaparak proje başarıları sağlamak",
    "Yazılım süreçlerini sürekli iyileştirmek için öneriler geliştirmek",
    "Kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım hatalarını hızlı bir şekilde tanımlamak ve düzeltmek",
    "Yazılım sürüm kontrol sistemini kullanmak ve yönetmek",
    "Teknik dökümantasyon oluşturmak ve güncellemek",
    "Yazılım testlerini ve doğrulamalarını yönetmek",
    "Geliştirme süreçlerini ve takımları yönetmek",
    "Ekip üyelerinin gelişimini teşvik etmek ve desteklemek",
    "Takım içi işbirliği ve iletişimi güçlendirmek",
    "Yeni eğilimler ve teknolojiler hakkında eğitimler düzenlemek",
    "Yazılım geliştirme süreçlerinde ekip çalışmasını teşvik etmek",
    "Yazılım sistemleri için güvenlik testleri yapmak",
    "Yazılım geliştirme süreçlerini sürekli olarak iyileştirmek",
    "Müşteri beklentilerini karşılamak için yazılım çözümleri sunmak",
    "Yazılım geliştirme projelerini planlamak ve yönetmek",
    "Yazılım performansını değerlendirmek ve optimize etmek",
    "Mevcut yazılım çözümlerini sürdürmek ve desteklemek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerini otomatikleştirmek için çözümler geliştirmek",
    "Yazılım mühendisliği konularında eğitimler vermek ve gelişmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak için çözümler geliştirmek",
    "Yazılım güvenliği ve veri gizliliği konularında politikaları ve yönergeleri uygulamak",
    "Yazılım test stratejileri oluşturmak ve uygulamak",
    "Yazılım süreçlerinde risk yönetimi stratejileri uygulamak",
    "Yazılım geliştirme süreçlerinde dökümantasyon standartlarını oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde işbirliği ve iletişimi güçlendirmek",
    "Yazılım süreçlerinde kalite güvence yöntemleri uygulamak",
    "Yazılım geliştirme süreçlerinde veri yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım sistemlerinin güvenliği için proaktif çözümler geliştirmek",
    "Yazılım geliştirme süreçlerinde yenilikçi çözümler geliştirmek",
    "Yazılım test süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım süreçlerinde sürdürülebilirlik stratejileri geliştirmek",
    "Yazılım geliştirme projelerinde zaman ve bütçe yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde eğitim ve öğretim faaliyetleri düzenlemek",
    "Yazılım geliştirme süreçlerinde iş sürekliliği planları oluşturmak ve uygulamak",
    "Yazılım güvenlik açıklarını tespit etmek ve düzeltmek",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde teknik destek sağlamak",
    "Yazılım süreçlerinde yönetim ve liderlik görevlerini üstlenmek",
    "Yazılım geliştirme süreçlerinde güncel eğilimleri takip etmek",
    "Yazılım süreçlerinde sürdürülebilir çözümler geliştirmek",
    "Yazılım geliştirme süreçlerinde veri analizi yapmak ve raporlamak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ekip üyelerini yönlendirmek ve geliştirmek",
    "Yazılım geliştirme süreçlerinde sıkı takım çalışması yapmak",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi yapmak ve geliştirmek",
    "Yazılım geliştirme süreçlerinde stratejik ortaklıklar ve işbirlikleri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek",
    "Yazılım geliştirme süreçlerinde müşteri memnuniyetini artırmak",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini uygulamak",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde yenilikçi çözümler ve teknolojiler sunmak",
    "Yazılım geliştirme süreçlerinde müşteri beklentilerini anlamak ve karşılamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliği ve iletişimi güçlendirmek",
    "Yazılım geliştirme süreçlerinde süreç performansını izlemek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde teknik becerileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ürün ve hizmet portföyünü yönetmek",
    "Yazılım geliştirme süreçlerinde proje paydaşlarıyla işbirliği yapmak",
    "Yazılım geliştirme süreçlerinde iş stratejilerini ve hedeflerini belirlemek",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde ekip performansını yönetmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi yapmak ve geliştirmek",
    "Yazılım geliştirme süreçlerinde stratejik ortaklıklar ve işbirlikleri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek",
    "Yazılım geliştirme süreçlerinde müşteri memnuniyetini artırmak",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini uygulamak",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde yenilikçi çözümler ve teknolojiler sunmak",
    "Yazılım geliştirme süreçlerinde müşteri beklentilerini anlamak ve karşılamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliği ve iletişimi güçlendirmek",
    "Yazılım geliştirme süreçlerinde süreç performansını izlemek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde teknik becerileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ürün ve hizmet portföyünü yönetmek",
    "Yazılım geliştirme süreçlerinde proje paydaşlarıyla işbirliği yapmak",
    "Yazılım geliştirme süreçlerinde iş stratejilerini ve hedeflerini belirlemek",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde ekip performansını yönetmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi yapmak ve geliştirmek",
    "Yazılım geliştirme süreçlerinde stratejik ortaklıklar ve işbirlikleri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek",
    "Yazılım geliştirme süreçlerinde müşteri memnuniyetini artırmak",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini uygulamak",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde yenilikçi çözümler ve teknolojiler sunmak",
    "Yazılım geliştirme süreçlerinde müşteri beklentilerini anlamak ve karşılamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliği ve iletişimi güçlendirmek",
    "Yazılım geliştirme süreçlerinde süreç performansını izlemek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde teknik becerileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ürün ve hizmet portföyünü yönetmek",
    "Yazılım geliştirme süreçlerinde proje paydaşlarıyla işbirliği yapmak",
    "Yazılım geliştirme süreçlerinde iş stratejilerini ve hedeflerini belirlemek",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde ekip performansını yönetmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi yapmak ve geliştirmek",
    "Yazılım geliştirme süreçlerinde stratejik ortaklıklar ve işbirlikleri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek",
    "Yazılım geliştirme süreçlerinde müşteri memnuniyetini artırmak",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini uygulamak",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde teknik becerileri geliştirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ürün ve hizmet portföyünü yönetmek",
    "Yazılım geliştirme süreçlerinde proje paydaşlarıyla işbirliği yapmak",
    "Yazılım geliştirme süreçlerinde iş stratejilerini ve hedeflerini belirlemek",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde ekip performansını yönetmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi yapmak ve geliştirmek",
    "Yazılım geliştirme süreçlerinde stratejik ortaklıklar ve işbirlikleri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek",
    "Yazılım geliştirme süreçlerinde müşteri memnuniyetini artırmak",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini uygulamak",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde yenilikçi çözümler ve teknolojiler sunmak",
    "Yazılım geliştirme süreçlerinde müşteri beklentilerini anlamak ve karşılamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliği ve iletişimi güçlendirmek",
    "Yazılım geliştirme süreçlerinde süreç performansını izlemek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde teknik becerileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ürün ve hizmet portföyünü yönetmek",
    "Yazılım geliştirme süreçlerinde proje paydaşlarıyla işbirliği yapmak",
    "Yazılım geliştirme süreçlerinde iş stratejilerini ve hedeflerini belirlemek",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde ekip performansını yönetmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi yapmak ve geliştirmek",
    "Yazılım geliştirme süreçlerinde stratejik ortaklıklar ve işbirlikleri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip performansını değerlendirmek",
    "Yazılım geliştirme süreçlerinde müşteri memnuniyetini artırmak",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini uygulamak",
    "Yazılım geliştirme süreçlerinde süreç iyileştirme çalışmaları yapmak",
    "Yazılım geliştirme süreçlerinde yenilikçi çözümler ve teknolojiler sunmak",
    "Yazılım geliştirme süreçlerinde müşteri beklentilerini anlamak ve karşılamak",
    "Yazılım geliştirme süreçlerinde ekip yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliği ve iletişimi güçlendirmek",
    "Yazılım geliştirme süreçlerinde süreç performansını izlemek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde teknik becerileri geliştirmek ve uygulamak",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini kullanmak",
    "Yazılım geliştirme süreçlerinde ürün ve hizmet portföyünü yönetmek",
    "Yazılım geliştirme süreçlerinde proje paydaşlarıyla işbirliği yapmak",
    "Yazılım geliştirme süreçlerinde iş stratejilerini ve hedeflerini belirlemek",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde ekip performansını yönetmek",
    "Yazılım geliştirme süreçlerinde verimliliği artırmak",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde müşteri odaklı çözümler sunmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme stratejileri geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı geri bildirimlerini değerlendirmek",
    "Yazılım geliştirme süreçlerinde ekip üyelerinin motivasyonunu sağlamak",
    "Yazılım geliştirme süreçlerinde teknoloji ve yöntemler konusunda eğitimler vermek",
    "Yazılım geliştirme süreçlerinde öğrenme ve gelişimi teşvik etmek",
    "Yazılım geliştirme süreçlerinde ekip performansını iyileştirmek",
    "Yazılım geliştirme süreçlerinde ürün güncellemelerini yönetmek",
    "Yazılım geliştirme süreçlerinde stratejik planlama yapmak",
    "Yazılım geliştirme süreçlerinde ekip motivasyonunu artırmak",
    "Yazılım geliştirme süreçlerinde süreç analizi yapmak ve iyileştirme önerileri sunmak",
    "Yazılım geliştirme süreçlerinde müşteri ilişkileri yönetimi yapmak",
    "Yazılım geliştirme süreçlerinde proje planlama ve takip etme",
    "Yazılım geliştirme süreçlerinde risk yönetimi stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde teknik ve operasyonel stratejiler geliştirmek",
    "Yazılım geliştirme süreçlerinde ekip işbirliğini teşvik etmek",
    "Yazılım geliştirme süreçlerinde süreç dökümantasyonunu oluşturmak ve güncellemek",
    "Yazılım geliştirme süreçlerinde hizmet yönetimi süreçlerini geliştirmek",
    "Yazılım geliştirme süreçlerinde kullanıcı arayüzü ve kullanıcı deneyimini geliştirmek",
    "Yazılım geliştirme süreçlerinde otomasyon çözümleri geliştirmek",
    "Yazılım geliştirme süreçlerinde veri güvenliği stratejileri oluşturmak ve uygulamak",
    "Yazılım geliştirme süreçlerinde sistem performansını değerlendirmek ve iyileştirmek",
    "Yazılım geliştirme süreçlerinde stratejik hedeflere ulaşmak için planlama yapmak",
    "Yazılım geliştirme süreçlerinde sürekli iyileştirme fırsatlarını değerlendirmek",
    "Yazılım geliştirme süreçlerinde proje yönetimi becerilerini geliştirmek",
    "Yazılım geliştirme süreçlerinde yeni teknolojileri ve trendleri takip etmek",
    "Yazılım geliştirme süreçlerinde ürün stratejileri geliştirmek ve uygulamak",
]

# Tüm kullanıcıları al
users = User.objects.all()

# Her kullanıcı için 3000 görev oluştur
for user in users:
    for _ in range(30):
        # Rastgele bir görev kelimesi seç
        task = random.choice(tasks)
        
        # Görev başlığını oluştur
        todo_title = f"{random.randint(1, 427)}.Görev {task}"
        
        # Görevi tamamlanmış olarak işaretleme
        is_completed = random.choice([True, False])
        
        # Todo nesnesini oluştur ve kaydet
        Todo.objects.create(
            title=todo_title,
            is_completed=is_completed,
            user_id=user.pk
        )

print("Görevler oluşturuldu.")
