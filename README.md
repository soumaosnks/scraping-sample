# 🕸️ Webスクレイピング サンプルツール

Python を使って Web サイトから **名言（quote）と著者名（author）** を取得し、  
CSV に保存するサンプルプロジェクトです。

スクレイピングの基本である  
**「HTML取得 → パース → 必要な情報を抽出 → CSVに保存」**  
という一連の流れを学べます。

---

## 📂 プロジェクト構成
'''
scraping-sample/
├─ scrape_news.py        # スクレイピング本体
├─ output.csv            # 実行後に自動生成される出力ファイル
├─ requirements.txt      # 必要ライブラリ
└─ README.md             # この説明書
'''

---

## 🚀 使い方

### ① 必要なライブラリをインストール

このプロジェクトでは以下のライブラリを使用します：

- requests  
- beautifulsoup4  

以下のコマンドで一括インストールできます

- ```bash
- pip install -r requirements.txt

### ② スクリプトを実行

以下のコマンドを実行すると、Webサイトから名言データを取得し、
`output.csv` に保存されます。

- python scrape_news.py

実行後、ターミナルに以下のようなメッセージが表示されます：
スクレイピング完了！output.csv に保存しました。

### ③ 出力ファイルを確認

スクリプト実行後、プロジェクトフォルダに `output.csv` が生成されます。

中身には、取得した名言（quote）と著者名（author）が一覧で保存されています。

例：
quote,author
"The world as we have created it is a process of our thinking.",Albert Einstein
"It is our choices, Harry, that show what we truly are.",J.K. Rowling
