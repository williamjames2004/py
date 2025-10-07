import pandas as pd

data = [10,20,30]

series = pd.Series(data)

print("1st Series: ", series)

series2 = pd.Series([100,200,300], index=["A", "B", "C"])

print("2nd Series: ", series2)

print("1st Element: ", series[0])
print("1st Element of series 2: ", series2['A'])

print("Addition: ", series+5)

print("\nStatistics")
print("Min value: ", series.min())
print("Max value: ", series.max())
print("Mean value: ", series.mean())
