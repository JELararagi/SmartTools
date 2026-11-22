# SmartTools 製品ガイド / Product guides

23製品の紹介文と図を日本語・英語で管理しています。各紹介は、無料公開した1.0.0の解説書にある一つの作例に対応します。宣伝用に撮り直した画像や架空の操作結果は使用していません。

[日本語の解説書](../docs/manuals/) · [English manuals](../docs/en/manuals/) · [製品別の原稿と作例 / Product catalog](products.json) · [無料公開版 / Free release](https://github.com/JELararagi/SmartTools/releases/tag/v1.0.0)

## 原稿の更新

`products.json` に、商品名、版、実例ID、日英の見出しと説明、試す時の条件、画像のパス・説明・Gitハッシュを収録しています。変更後に `python catalog/guide.py --update-manuals` を実行すると、解説書の先頭にある紹介欄を更新できます。`--check` は原稿と46ページの一致を照合します。

## 別のサイトへ移す / Export

リポジトリ全体を取得し、次を実行してください。Python 3.9以降で動作します。

```text
python catalog/guide.py --export ../smarttools-product-pages
```

指定した新規または空のフォルダーに、製品ごとの日本語・英語のMarkdownと対応する画像が出ます。画像のハッシュを確かめ、照合した原稿と画像を一緒に移せます。販売経路が決まったら、そのサービスで権利確認済みの商品に価格・決済・購入済みファイルの受け取り先を設定します。このリポジトリは解説書の配布に使用します。

Each entry has a stable product name, edition, example ID, bilingual copy, two source figures and a note about reproducing the result. Run the export command from a full checkout for self-contained product copy and images. The command uses only the Python standard library. The exported pages have no payment-provider dependency.
