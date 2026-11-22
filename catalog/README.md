# SmartTools 製品ガイド / Illustrated product guides

23製品それぞれの解説書は、Blenderで最初に開く画面から始まります。日本語版・英語版で実際の画面を使い、開く場所、モード、タブ、見出しを案内しています。代表作例には操作前後の写真と手順があり、同じ製品の作例をさらに2件たどれます。

[日本語の入口](../docs/index.html) · [English guides](../docs/en/index.html) · [製品原稿・画像の出所](products.json) · [無料公開版](https://github.com/JELararagi/SmartTools/releases/tag/v1.0.0)

## 原稿と画像

`products.json` には、各言語の案内文、入口画像の元見出しとキャプション、作例の画像パスとGit blobハッシュを収録しています。`sources` は、関連ツールの公式資料を参照するためのリンク集です。各解説書の本文・PDF・無料版ZIPは従来の場所から開けます。

## 更新と移植

リポジトリ全体を取得し、Python 3.9以降で実行します。PNGを作り直すときはPillowと日本語フォントも必要です。フォントは `--font` と `--bold-font` で指定できます。

```text
python catalog/render_diagrams.py
python catalog/guide.py --update-manuals
python catalog/guide.py --check
python catalog/guide.py --export ../smarttools-product-pages
```

`--export` は新規または空のフォルダーに、各言語・各製品のMarkdownと画像をまとめます。PNGは、その製品の入口と操作前後の写真を1枚に配置したものです。

Each manual opens with a screenshot of the actual Blender controls, the steps to open them, and a landmark to look for. The featured example follows with screenshots of the operation and its result. Two further worked examples link to their instructions in the manual. The commands above regenerate the guides and export self-contained product pages for another storefront.

[日本語ヘルプ](https://jelararagi.github.io/SmartTools/#help) · [English Help](https://jelararagi.github.io/SmartTools/en/#help)
