import pandas as pd

csv_file = open("data1.csv", "r")

data = pd.read_csv(csv_file)
column_1 = data["Column1"]
column_2 = data["Column2"]

column_1 = column_1.sort_values(ascending=True).reset_index(drop=True)
column_2 = column_2.sort_values(ascending=True).reset_index(drop=True)

output = column_1.sub(column_2)
output = output.abs()
out = output.sum()

print(out)