import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dog_data.csv")

# Total park time by dog
park_summary = df.groupby("dog")["park_minutes"].sum()

# Total expenses
expense_summary = df.groupby("dog")["expense"].sum()

print("Total Park Minutes:")
print(park_summary)

print("\nTotal Expenses:")
print(expense_summary)

# Plot park time
plt.figure()
park_summary.plot(kind="bar")
plt.title("Total Park Time by Dog")
plt.ylabel("Minutes")
plt.xlabel("Dog")
plt.tight_layout()
plt.savefig("park_time_chart.png")
