# simulate_error.py

import argparse
import sys
import threading
import time
import requests

def simulate_http_500():
    print("[*] Simulating HTTP 500 Error...")
    response = requests.Response()
    response.status_code = 500
    raise requests.HTTPError("Internal Server Error", response=response)

def simulate_cpu_spike():
    print("[*] Simulating high CPU usage...")
    def burn_cpu():
        while True:
            pass
    for _ in range(10):  # 10 threads to burn CPU
        t = threading.Thread(target=burn_cpu)
        t.start()
    time.sleep(30)
    print("[*] CPU spike simulation complete.")

def simulate_crash():
    print("[*] Simulating application crash...")
    raise Exception("Application crashed due to unhandled exception")

def simulate_memory_leak():
    print("[*] Simulating memory exhaustion...")
    big_list = []
    try:
        while True:
            big_list.append("X" * 10**6)  # Add 1MB per iteration
    except MemoryError:
        print("[!] Memory exhausted.")

def main():
    parser = argparse.ArgumentParser(description="Incident Simulation Script")
    parser.add_argument("error_type", choices=["http500", "cpu", "crash", "memory"], 
                        help="Type of error to simulate")

    args = parser.parse_args()

    try:
        if args.error_type == "http500":
            simulate_http_500()
        elif args.error_type == "cpu":
            simulate_cpu_spike()
        elif args.error_type == "crash":
            simulate_crash()
        elif args.error_type == "memory":
            simulate_memory_leak()
    except Exception as e:
        print(f"[!] Exception caught: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
