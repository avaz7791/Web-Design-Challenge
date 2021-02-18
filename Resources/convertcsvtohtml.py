import pandas as pd

#cities_csv = "C:\Users\sonof\UCSDProjects\Web-Design-Challenge\Resources\cities.csv"
cities_csv = "Resources\cities.csv"

csv = pd.read_csv(cities_csv)

cities_df = pd.DataFrame(csv)

#print(cities_df)
cities_df.drop(cities_df.columns[[0]], axis = 1, inplace = True)

#print(cities_df)
cities_df.to_html('citiesdataset.html')