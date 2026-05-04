import time
import os

log_file = os.path.join("shine", "okx", "trading.log")

print("Monitoring trading.log for new trades...")
# Move to the end of file
with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    f.seek(0, 2)
    
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue
            
        # Check for trade signals
        if "DRY-RUN" in line and "开仓" in line:
            print(f"\n[🚀 TRADE TRIGGERED] {line.strip()}")
            break
        elif "place_order" in line or "执行模拟开仓" in line or "开仓" in line and "DRY" in line:
            print(f"\n[🚀 TRADE TRIGGERED] {line.strip()}")
            break
