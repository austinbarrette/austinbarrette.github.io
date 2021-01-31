import pandas as pd

file = "11-Web\Homework\Instructions\Resources\cities.csv"
df = pd.read_csv(file)

#to html file
df.to_html(output.html)

#Assign it to a variable (string)
html_file = df.to_html()
