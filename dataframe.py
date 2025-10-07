import pandas as pd

data = {
    "Name": ["William", "Sri", "Trisha", "Rakesh", "Michael"],
    "Age": [20, 20, 21, 25, 17],
    "Marks": [96, 100, 95, 82, 57]
    }

df = pd.DataFrame(data)

print("The data frame: ", df)

print("Accessing column of data frame: ", df['Name'])

df["Grade"] = ["A","A+", "A", "B", "D"]

print("After adding new column: ", df)

print("First two rows: ", df.head(2))

print("Statistics")

print(df.describe())
