import pandas as pd

data = pd.read_csv('marks.csv')

print(data)

max_marks = data.groupby("Name").Marks.max()

print(max_marks)
    
