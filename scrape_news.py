import requests
from bs4 import BeautifulSoup
import csv

# 取得したいページ（練習用サイト）
url = "https://quotes.toscrape.com/"

# HTMLを取得
response = requests.get(url)
response.raise_for_status()  # エラー時に例外を出す
soup = BeautifulSoup(response.text, "html.parser")

# 名言と著者を取得
quotes = soup.select("div.quote")

rows = []

for q in quotes:
    text = q.select_one("span.text").get_text(strip=True)
    author = q.select_one("small.author").get_text(strip=True)
    rows.append([text, author])

# CSVに保存
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["quote", "author"])
    writer.writerows(rows)

print("スクレイピング完了！output.csv に保存しました。")
