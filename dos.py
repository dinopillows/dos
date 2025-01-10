import requests
import time

def simulate_layer7_attack(url, num_requests, delay):
    for _ in range(num_requests):
        try:
            # Mencoba mengirim permintaan GET ke URL
            response = requests.get(url)
            print(f"Permintaan ke-{_+1} dikirim. Status kode: {response.status_code}")
        except requests.RequestException as e:
            print(f"Terjadi kesalahan saat mengirim permintaan: {e}")
        
        # Menambah delay untuk tidak mengoverload server dalam simulasi ini
        time.sleep(delay)

if __name__ == "__main__":
    target_url = "http://example.com"  # Ganti dengan URL yang Anda izinkan untuk diuji dalam lingkungan kontrol
    number_of_requests = 5  # Jumlah permintaan yang akan dikirim
    delay_between_requests = 1  # Delay dalam detik antara setiap permintaan

    simulate_layer7_attack(target_url, number_of_requests, delay_between_requests)
