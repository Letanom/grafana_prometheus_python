from flask import Flask # Flask uygulaması için gerekli kütüphane
from prometheus_client import start_http_server, Summary # Prometheus metrikleri için gerekli kütüphaneler
import random # Rastgele sayılar üretmek için
import time # Zaman işlemleri için 

app = Flask(__name__)

# Prometheus metrikleri
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request') # İstek işleme süresi


# Fake API endpoint
@app.route('/')
def index():
    return "Hello, World! - Ben bir fake API'yim ve Beni KEVIN ÖZŞİMŞEK YAPTII !!\n" 

# API için metrik endpoint
@app.route('/metrics')
def metrics():
    # Bu metrik her zaman rastgele veri dönecek
    fake_data = random.randint(0, 100)
    return f"# HELP fake_data Fake data value\n# TYPE fake_data gauge\nfake_data {fake_data}\n"

if __name__ == '__main__':
    #Metrik sunucusunu başlat ve Flask uygulamasını çalış
    start_http_server(5001)
    app.run(host="0.0.0.0", port=5001)
