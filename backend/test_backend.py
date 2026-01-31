import requests
import time
import sys

BASE_URL = "http://127.0.0.1:8000"

def wait_for_server():
    for _ in range(10):
        try:
            requests.get(f"{BASE_URL}/health")
            return True
        except:
            time.sleep(1)
    return False

def test_endpoints():
    print("Testing /health...")
    resp = requests.get(f"{BASE_URL}/health")
    print(f"Health: {resp.status_code} {resp.json()}")
    if resp.status_code != 200: exit(1)

    print("\nTesting /api/ai/explain (Mock)...")
    # This might fail 401 if API key is invalid, but 200/401/500 proves endpoint exists
    try:
        resp = requests.post(f"{BASE_URL}/api/ai/explain", json={"query": "test"})
        print(f"Explain: {resp.status_code}")
        # We expect 401 or 200, not 404
        if resp.status_code == 404:
            print("Endpoint not found!")
            exit(1)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if not wait_for_server():
        print("Server failed to start")
        sys.exit(1)
    test_endpoints()
