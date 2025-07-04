import requests
from bs4 import BeautifulSoup

url = "https://realpython.com/"

keywords = ['KI', 'Python', 'Technologie']

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

h2_titles = soup.find_all("h2")
# a_titles = soup.find_all("a")

titles = set()

for tag in h2_titles:
    text = tag.get_text(strip=True)
    if text:
        titles.add(text)

with open("titel.txt", "w", encoding="utf-8") as file:
    for title in sorted(titles):
        file.write(title + "\n")

print("Gefundeene Schlagwörter in Titeln:")
for keyword in keywords:
    matches = [title for title in titles if keyword.lower() in title.lower()]
    if matches:
        print(f"\n'{keyword}' gefunden in:")
        for match in matches:
            print(f"- {match}")