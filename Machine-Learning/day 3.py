import pandas as pd

data = {
    "Name": ["Ravi", "Arun", "John"],
    "Age": [20, 21, 19],
    "Marks": [95, 88, 91]
}

df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)
df = pd.read_csv(r"W:\ML LEARNINGS\ML-Engineer-Journey\Machine-Learning\Day 2\assisment 1\student.csv")

print(df)
print(df.head(1))
print(df.tail(2))
print(df.info())
print(df.describe())