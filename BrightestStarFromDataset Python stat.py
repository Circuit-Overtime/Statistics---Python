from bs4 import BeautifulSoup
import requests
import pandas as pd

star_name = []
distance = []
mass = []
radius = []
temp_list = []
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"


#main
wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")

for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.strip() for i in td]
    temp_list.append(row)


for i in range(1, len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(star_name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")

#Let's Reach Deneb Star