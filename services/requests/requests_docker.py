import random
import time
import requests

URL = "http://ml_service:8000/api/prediction"

def _generate_random_data():
    return {
        "battery_power": random.randint(500, 2000),
        "blue": random.randint(0, 1),
        "clock_speed": round(random.uniform(0.5, 3.0), 1), 
        "dual_sim": random.randint(0, 1),
        "fc": random.randint(0, 20),
        "four_g": random.randint(0, 1),
        "int_memory": random.randint(8, 64),
        "m_dep": round(random.uniform(0.1, 0.9), 1), 
        "mobile_wt": random.randint(80, 200),
        "n_cores": random.randint(1, 8),
        "pc": random.randint(1, 20),
        "px_height": random.randint(100, 2000),
        "px_width": random.randint(100, 2000),
        "ram": random.randint(512, 8192),
        "sc_h": random.randint(5, 20),
        "sc_w": random.randint(2, 10),
        "talk_time": random.randint(5, 25),
        "three_g": random.randint(0, 1),
        "touch_screen": random.randint(0, 1),
        "wifi": random.randint(0, 1),
        "screen_area": random.randint(10, 200), 
        "pixel_density": random.randint(200, 500), 
        "total_memory": random.randint(1000, 10000),
        "is_high_end": random.randint(0, 1)
    }

def send_request(item_id: int):
    try:
        response = requests.post(f"{URL}?item_id={item_id}", json=_generate_random_data())
        print(f"[{item_id}] Status: {response.status_code}, Response: {response.json()}")
    except Exception as e:
        print(f"[{item_id}] Request failed: {e}")

def run():
    item_id = 1
    while True:
        send_request(item_id)
        item_id += 1
        sleep_time = random.uniform(0, 5)
        print(f"Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    run()
