import time

total_seconds = int()
total_minutes = int()
total_hours = int()

while True:
    if total_seconds >= 59:
        total_seconds = -1
        total_minutes += 1
        
    if total_minutes > 59:
        total_seconds = -1
        total_minutes = 0
        total_hours += 1
        
    time.sleep(1)
    total_seconds += 1 
    print(f"{total_hours}H {total_minutes}M {total_seconds}S")