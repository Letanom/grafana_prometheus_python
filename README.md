# grafana_prometheus_python

📊 Grafana & Prometheus & Python 

Python kullanarak basit bir fake API çalıştırdım ve bu API'nin metriklerini Prometheus'a yolladım.

Bu proje, Prometheus ile veri toplayıp Grafana ile görselleştirmek için hazırlanmıştır. 

🚀 Nasıl Çalıştırılır?

Gerekli araçları yükleyin:

Docker
Docker Compose

Projeyi klonlayın:

bash

git clone https://github.com/Letanom/grafana_prometheus_python.git
cd grafana_prometheus_python
Docker ile başlatın:

bash
docker-compose up -d
Kontroller:

Fake API: http://localhost:5001/metrics

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (Kullanıcı: admin, Şifre: admin)

📌 Ne İşe Yarar?

Python ile basit bir API oluşturur.

API'nin metriklerini Prometheus toplar.

Grafana ile verileri görselleştirirsiniz.

🤝 Katkıda Bulunmak

Kodları geliştirmek isteyenler pull request açabilir. Sorularınızı issue olarak yazabilirsiniz.
