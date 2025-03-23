# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into Pandas DataFrame
df = pd.read_csv("airline_delays.csv")

# Display first few rows
print("Dataset Preview:")
print(df.head())

# 1️⃣ Average Delay Per Airline
average_delay = df.groupby("Airline")["Delay (minutes)"].mean()
print("\nAverage Delay for Each Airline:\n", average_delay)

# 2️⃣ Average Delay Per Destination
avg_delay_dest = df.groupby("Destination")["Delay (minutes)"].mean()
print("\nAverage Delay for Each Destination:\n", avg_delay_dest)

# 3️⃣ Visualizing Delays
plt.figure(figsize=(10,5))
sns.barplot(x="Destination", y="Delay (minutes)", hue="Airline", data=df)
plt.title("Comparison of Arrival Delays by Airline")
plt.xlabel("Destination")
plt.ylabel("Delay (minutes)")
plt.legend(title="Airline")
plt.show()
