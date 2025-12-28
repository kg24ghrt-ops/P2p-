import time
import os

print("--- Galaxy Cloud Node Online ---")
print(f"Working Directory: {os.getcwd()}")

# Create a dummy output file for the artifact test
with open("output.txt", "w") as f:
    f.write("This file was generated in the cloud!\n")
    f.write(f"Timestamp: {time.ctime()}\n")

for i in range(5):
    print(f"Streaming data packet {i+1}/5...")
    time.sleep(1)

print("✅ Cloud Strategy Complete.")