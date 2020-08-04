import pandas as pd
data = pd.read_csv("D:/py10/air.csv")
df = pd.DataFrame(data)
#print(data)

print("平均值")
print(df.mean())
print()

print("最大值")
print(df.max())
print()

mx = df["AQI"].max()
mn = df["AQI"].min()
print(f"aqi最高 : {mx} 最低 : {mn}")
print()

print("中位數")
print(df.median())
print()

print("眾數")
print(df.mode())
print()

print("標準差")
print(df.std())
print()