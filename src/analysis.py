import os
import pandas as pd
import matplotlib.pyplot as plt


def analyze_sessions(csv_path: str, out_dir: str = "reports"):
    # basic checks
    if not os.path.exists(csv_path):
        print("No data file found. Add a session first.")
        return

    df = pd.read_csv(csv_path)
    if df.empty:
        print("No sessions to analyze.")
        return

    os.makedirs(out_dir, exist_ok=True)

    # small helpers from existing columns
    # start is like "22:40" -> start_hour = 22
    df["start_hour"] = df["start"].astype(str).str.slice(0, 2).astype(int)
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

    total_min = int(df["minutes"].sum())
    avg_min = float(df["minutes"].mean())

    best_hour = df.groupby("start_hour")["productivity"].mean().sort_values(ascending=False).index[0]
    best_label = df.groupby("label")["productivity"].mean().sort_values(ascending=False).index[0]

    print("\n--- Summary ---")
    print("Total focus time:", total_min, "min")
    print("Average session:", round(avg_min, 1), "min")
    print("Best start hour:", f"{best_hour:02d}:00")
    print("Best label (avg productivity):", best_label)

    # Chart 1: Avg productivity by start hour
    hour_score = df.groupby("start_hour")["productivity"].mean().reindex(range(24), fill_value=0)

    plt.figure()
    hour_score.plot(kind="bar")
    plt.title("Average Productivity by Start Hour")
    plt.xlabel("Hour")
    plt.ylabel("Avg Productivity (1-5)")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "avg_productivity_by_hour.png"), dpi=200)
    plt.close()

    # Chart 2: Total minutes by weekday
    day_minutes = df.groupby("weekday")["minutes"].sum()
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_minutes = day_minutes.reindex(order).dropna()

    plt.figure()
    day_minutes.plot(kind="bar")
    plt.title("Total Focus Minutes by Weekday")
    plt.xlabel("Weekday")
    plt.ylabel("Minutes")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "minutes_by_weekday.png"), dpi=200)
    plt.close()

    # Chart 3: Avg productivity by label
    label_score = df.groupby("label")["productivity"].mean().sort_values(ascending=False)

    plt.figure()
    label_score.plot(kind="bar")
    plt.title("Average Productivity by Label")
    plt.xlabel("Label")
    plt.ylabel("Avg Productivity (1-5)")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "avg_productivity_by_label.png"), dpi=200)
    plt.close()

    print("\nCharts saved in:", out_dir)