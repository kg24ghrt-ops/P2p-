import time
import os

print("--- Galaxy Cloud Node Online ---")
print(f"Working Directory: {os.getcwd()}")

for i in range(5):
    print(f"Streaming data packet {i+1}/5...")
    time.sleep(1)

print("✅ Cloud Strategy Complete.")