# ライセンス / License

## 日本語

このリポジトリには、SmartTools（Blender 用アドオン 23 個）の ZIP と、解説書（ウェブ版・PDF・画像）が入っています。ライセンスはアドオンごとに異なります。**正本は、各 ZIP の中のライセンス文書と `blender_manifest.toml` です。** 下の表は、その記載を ZIP から読み出して並べたものです。

### アドオンごとのライセンス

| アドオン | manifest の license | ZIP の中の文書 | 文書の SPDX の行 |
|---|---|---|---|
| SmartGeometry Suite | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |
| SmartModeling Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartModifier Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartSculpt Suite | `SPDX:LicenseRef-JELararagi-Proprietary, SPDX:GPL-3.0-or-later` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartTransform Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartNode Suite | `SPDX:GPL-2.0-or-later` | license.txt | GPL-2.0-or-later |
| SmartPaint Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartShader Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartUV Suite | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |
| SmartAnimation Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartCloth Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartRig Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | （SPDX の行なし。先頭の行：Smart Rig Suite） |
| SmartSelector Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartShapekey Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartCamLight Suite | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |
| SmartComposite Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartRender Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| キーマップマネージャー | `SPDX:GPL-3.0-or-later` | LICENSE.txt | GPL-3.0-or-later |
| SmartFile Suite | `SPDX:GPL-3.0-or-later` | license.txt | LicenseRef-JELararagi-Proprietary |
| SmartID Suite | `SPDX:GPL-3.0-or-later` | LICENSE.txt | GPL-3.0-or-later |
| SmartOverlay Suite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Tools Manager | `SPDX:LicenseRef-JELararagi-Proprietary` | （なし） | — |
| SmartWorkspace Suite | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |

### 12 本に共通の文

次の 12 本の ZIP の中の `license.txt` は、同じ文です：SmartModeling Suite・SmartModifier Suite・SmartTransform Suite・SmartShader Suite・SmartAnimation Suite・SmartCloth Suite・SmartSelector Suite・SmartShapekey Suite・SmartComposite Suite・SmartRender Suite・SmartFile Suite・SmartOverlay Suite。
次は SmartCloth Suite の `license.txt` からの原文のままの引用です。

```text
SPDX-License-Identifier: LicenseRef-JELararagi-Proprietary
Copyright (C) 2026 JELararagi. All Rights Reserved.

Unified JELararagi license notice for Blender Extension / user_default compatible add-ons.
This package is provided for JELararagi. Redistribution, relicensing, or removal of this notice is not permitted without explicit permission. Bundled third-party components, if any, retain their original notices where included.
```

### GPL の付いたアドオン

- GPL-3.0-or-later：SmartGeometry Suite・SmartUV Suite・SmartCamLight Suite・キーマップマネージャー・SmartFile Suite・SmartID Suite・SmartWorkspace Suite（全文は [LICENSES/GPL-3.0-or-later.txt](LICENSES/GPL-3.0-or-later.txt)）
- GPL-2.0-or-later：SmartNode Suite（全文は [LICENSES/GPL-2.0-or-later.txt](LICENSES/GPL-2.0-or-later.txt)）
- SmartSculpt Suite：独自のライセンスと GPL-3.0 の部分があります（edit_mode_sculpt は Strict Edit Mode Sculpt v1.4.8 に由来します）。

GPL の付いたアドオンの ZIP には、ソースコード（.py）がそのまま入っています。

### 第三者の部品

次のアドオンは、第三者が作った部品を含みます。著作権の表示とライセンスは、ZIP の中のその部品のフォルダーにあります。

- SmartAnimation Suite：camera_shakify・sakura_poselib
- SmartGeometry Suite：debris*
- SmartModeling Suite：edgeflow
- SmartNode Suite：node_arrange
- SmartWorkspace Suite：screencast_keys

### 解説書

解説書（`docs/manuals/` のウェブ版・PDF・画像）と、このサイトのページは © 2026 JELararagi. All rights reserved.

## English

This repository contains the ZIPs of SmartTools (23 Blender extensions) and their manuals (web pages, PDFs and images). Licenses differ per add-on. **The authoritative texts are the license documents and `blender_manifest.toml` inside each ZIP.** The table above lists them as read from the ZIPs.

- These 12 add-ons share the same license text, quoted above from SmartCloth Suite: SmartModeling Suite, SmartModifier Suite, SmartTransform Suite, SmartShader Suite, SmartAnimation Suite, SmartCloth Suite, SmartSelector Suite, SmartShapekey Suite, SmartComposite Suite, SmartRender Suite, SmartFile Suite, SmartOverlay Suite.
- GPL-3.0-or-later: SmartGeometry Suite, SmartUV Suite, SmartCamLight Suite, キーマップマネージャー, SmartFile Suite, SmartID Suite, SmartWorkspace Suite. GPL-2.0-or-later: SmartNode Suite. Full texts: [LICENSES/](LICENSES/).
- SmartSculpt Suite: its own license, with a GPL-3.0 part (edit_mode_sculpt, derived from Strict Edit Mode Sculpt v1.4.8).
- Third-party components (SmartAnimation Suite: camera_shakify, sakura_poselib; SmartGeometry Suite: debris*; SmartModeling Suite: edgeflow; SmartNode Suite: node_arrange; SmartWorkspace Suite: screencast_keys). Their copyright notices and licenses are in the component folders inside the ZIPs.
- The ZIPs of the GPL-licensed add-ons contain their Python source code (.py) as is.
- Manuals (`docs/manuals/`, web pages, PDFs and images) and the pages of this site: © 2026 JELararagi. All rights reserved.
