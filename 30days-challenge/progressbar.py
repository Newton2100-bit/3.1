def show_progress(percent):
    filled = int(percent / 5)  # 20 chars total
    bar = "█" * filled + "░" * (20 - filled)
    print(f"[{bar}] {percent}%")

show_progress(75)  # [███████████████░░░░░] 75%
