import csv
import requests
from bs4 import BeautifulSoup


# Version 1
# def fetch_data(url):
#     response = requests.get(url)
#     keywords = ['KI', 'Python', 'Technologie']
#     soup = BeautifulSoup(response.text, "html.parser")
#     titles = soup.find_all("h2")
#
#     a_titles = soup.select("article a")
#     with open("titles.csv", "w", newline="", encoding="utf-8") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Title"])
#         for title in titles:
#             writer.writerow([title.get_text(strip=True)])
#         for link in soup.find_all("a", href=True):
#             href = link.get("href")
#             text = link.get_text(strip=True)
#             if text and ('/tutorial' in href or '/article' in href):
#                 writer.writerow([text])
#             if keywords and any(keyword.lower() in text.lower() in titles.lower() and a_titles.lower() for keyword in keywords):
#                 print(f"Gefundenes Schlagwort: {text}")
#     return titles + a_titles
#
# def main():
#     url = "https://realpython.com/"
#     titles = fetch_data(url)
#
#     with open("titles.csv", "r", encoding="utf-8") as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)
#         for i, row in enumerate(reader):
#             if i < 3:
#                 print(row[0])
#             else:
#                 break
# if __name__ == "__main__":
#     main()


# Version 2

#
# url = "https://realpython.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# keywords = ['KI', 'AI', 'Python', 'Technologie', 'Technology']
#
# h2_titles = []
# a_titles = []
#
# for tag in soup.find_all('h2'):
#     text = tag.get_text(strip=True)
#     if text:
#         h2_titles.append(text)
#         for keyword in keywords:
#             if keyword.lower() in text.lower():
#                 print(f"Found da '{keyword}' in article title: {text}")
# for tag in soup.find_all('a'):
#     text = tag.get_text(strip=True)
#     if text:
#         a_titles.append(text)
#         for keyword in keywords:
#             if keyword.lower() in text.lower():
#                 print(f"Found da '{keyword}' in link title: {text}")
#
# with open("title.txt", "w", encoding="utf-8") as file:
#     file.write("=== Articles (h2) ===\n \n")
#     for title in h2_titles:
#         file.write(title + "\n")
#     file.write("\n=== Links (a) ===\n \n")
#     for title in a_titles:
#         file.write(title + "\n")
#

#Version 3

url = "https://realpython.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

keywords = ['KI', 'AI', 'Python', 'Technologie', 'Technology'] # I mean... KI and Technologie make little sense in on an English site.... buuuuut I added it anyway.

h2_titles = []
article_links = []

for tag in soup.find_all('h2'):
    text = tag.get_text().replace("\n", " ").strip()

    if text:
        h2_titles.append(text)
        for keyword in keywords:
            if keyword.lower() in text.lower():
                print(f"Found '{keyword}' in article title: {text}")

for tag in soup.find_all('a', href=True):
    href = tag['href']
    text = tag.get_text().replace("\n", " ").strip()
    if (("/article" in href) or ("/tutorial" in href) or (href.startswith("/") and len(href) > 1)) \
        and not href.startswith("#") and text:
        url_full = href if href.startswith("http") else "https://realpython.com" + href
        article_links.append((text, url_full))
        for keyword in keywords:
            if keyword.lower() in text.lower():
                print(f"Found '{keyword}' in article link: {text}")

with open("titles_and_links.txt", "w", encoding="utf-8") as file:
    file.write("=== Article Headlines (h2) ===\n\n")
    for title in h2_titles:
        file.write(title + "\n")
    file.write("\n=== Article Links (a) ===\n\n")
    for text, link in article_links:
        file.write(f"{text} : {link}\n")
    file.write("\n=== Keywords Found ===\n\n")
    for keyword in keywords:
        file.write(f"Keyword: {keyword}\n")



