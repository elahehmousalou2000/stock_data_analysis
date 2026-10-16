import pandas as pd

df = pd.read_csv("stock.csv")
df["change"] = df["close"].pct_change()

print(df[["date", "close", "change"]].tail())
print("Average close:", df["close"].mean())
