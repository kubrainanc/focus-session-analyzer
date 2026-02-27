import os
import pandas as pd
from datetime import datetime, date
from analysis import analyze_sessions

DATA_FILE = "data/sessions.csv"

def ensure_file():
    # Create data folder and csv if missing
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["date", "start", "end", "minutes", "label", "productivity"])
        df.to_csv(DATA_FILE, index=False)
def minutes_between(start_str, end_str):
    # HH:MM -> minutes difference (handles midnight)
    fmt = "%H:%M"
    s = datetime.strptime(start_str, fmt)
    e = datetime.strptime(end_str, fmt)
    diff = (e - s).total_seconds() / 60
    if diff <= 0:
        diff += 24 * 60
    return int(diff)

def add_session():
    d = input("Date (YYYY-MM-DD) [today]: ").strip()
    if d == "":
        d = date.today().isoformat()

    start = input("Start (HH:MM): ").strip()
    end = input("End (HH:MM): ").strip()
    label = input("Label [general]: ").strip() or "general"
    prod_str = input("Productivity (1-5): ").strip()

    try:
        prod = int(prod_str)
        if prod < 1 or prod > 5:
            print("Productivity must be 1-5.")
            return
        mins = minutes_between(start, end)
    except Exception:
        print("Wrong input format. Try again.")
        return

    df = pd.read_csv(DATA_FILE)
    new_row = {
        "date": d,
        "start": start,
        "end": end,
        "minutes": mins,
        "label": label,
        "productivity": prod
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    print("Session saved:", mins, "minutes")

def show_last():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("No sessions yet.")
        return
    print(df.tail(10).to_string(index=False))

def main():
    ensure_file()
    os.makedirs("reports", exist_ok=True)

    while True:
        print("\nFocus Session Analyzer")
        print("1) Add session")
        print("2) Show last 10")
        print("3) Analyze + charts")
        print("4) Exit")

        c = input("Choose: ").strip()

        if c == "1":
            add_session()
        elif c == "2":
            show_last()
        elif c == "3":
            analyze_sessions(DATA_FILE, "reports")
        elif c == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()