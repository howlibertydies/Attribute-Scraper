import requests
from bs4 import BeautifulSoup

url = "https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table", class_="standard-table")

attributes_data = []

rows = table.find_all("tr")
for row in rows[1:]:
    columns = row.find_all("td")
    if len(columns) >= 3:
        attribute_name = columns[0].text.strip()
        element_names = columns[1].text.strip()
        description = columns[2].text.strip()
        
        attribute_info = {
            "Attribute": attribute_name,
            "Elements": element_names,
            "Description": description
        }
        
        attributes_data.append(attribute_info)

for attribute in attributes_data:
    print(f"Attribute: {attribute['Attribute']}")
    print(f"Elements: {attribute['Elements']}")
    print(f"Description: {attribute['Description']}")
    print()

import csv

csv_file = "html_attributes.csv"
csv_columns = ["Attribute", "Elements", "Description"]

with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for attribute in attributes_data:
        writer.writerow(attribute)

print(f"Data saved to {csv_file}")
