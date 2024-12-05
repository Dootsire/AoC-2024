import pandas as pd

csv_file = open("data1.csv", "r")

data = pd.read_csv(csv_file)
column_1 = data["Column1"]
column_2 = data["Column2"]

count_1 = column_1.value_counts()
count_2 = column_2.value_counts()

mult = count_1.mul(count_2)
clean_mult = mult.dropna()

reframed = clean_mult.to_frame().reset_index()
reframed_mult = reframed["index"] * reframed["count"]
output = reframed_mult.sum()

print(output)