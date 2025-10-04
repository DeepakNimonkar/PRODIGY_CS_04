import time

log_file = "key_log.txt"

print("Simple Key Logger By : Deepak")
print("Type something and press Enter. It will auto-save after 3 entries.\n")

entry_count = 0
max_entries = 3
logs = []

while True:
    user_input = input("Type something: ")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    logs.append(f"{timestamp} - {user_input}")
    entry_count += 1

    print(f"Entry logged ✅ ({entry_count}/{max_entries})\n")

    if entry_count >= max_entries:
        with open(log_file, "a") as f:
            for log in logs:
                f.write(log + "\n")
        print(f"✅ {entry_count} entries saved to {log_file}")
        break
