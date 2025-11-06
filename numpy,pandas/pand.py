import pandas as pd #used for data manipulation and analysis
import numpy as np
data = {'Name': ['Prathamesh', 'Sahil', 'Aditya', 'Snehal'],'Marks': [85, 20, 78, 50],
        'Age': [20, 21, 19, 22]}


df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nMarks Column:\n", df['Marks'])

#to add extra column
df['Grade'] = ['A', 'A+', 'B', 'A']
print("\nAfter Adding Grade Column:\n", df)

print("\nStudents with marks > 80:\n", df[df['Marks'] > 60])
print("\n")

#to read data of external files
a=pd.read_csv(r"C:\Users\psjad\OneDrive\Desktop\Advertising.csv")
print(a)


