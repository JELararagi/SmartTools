# ライセンス / License

## 日本語

このリポジトリには、SmartTools（Blender 用アドオン 23 個）の ZIP と、解説書（ウェブ版・PDF・画像）が入っています。ライセンスはアドオンごとに異なります。**正本は、各 ZIP の中のライセンス文書と `blender_manifest.toml` です。** 下の表は、その記載を ZIP から読み出して並べたものです。

### アドオンごとのライセンス

| アドオン | manifest の license | ZIP の中の文書 | 文書の SPDX の行 |
|---|---|---|---|
| Smart Geometry | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |
| Smart Modeling | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Modifier | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Sculpt | `SPDX:LicenseRef-JELararagi-Proprietary, SPDX:GPL-3.0-or-later` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Transform | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Node | `SPDX:GPL-2.0-or-later` | license.txt | GPL-2.0-or-later |
| Smart Paint | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Shader | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart UV | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |
| Smart Animation | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Cloth | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Rig | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | （SPDX の行なし。先頭の行：Smart Rig Suite） |
| Smart Selector | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Shapekey | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart CamLight | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |
| Smart Composite | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Render | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| キーマップマネージャー | `SPDX:GPL-3.0-or-later` | LICENSE.txt | GPL-3.0-or-later |
| Smart File | `SPDX:GPL-3.0-or-later` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart ID | `SPDX:GPL-3.0-or-later` | LICENSE.txt | GPL-3.0-or-later |
| Smart Overlay | `SPDX:LicenseRef-JELararagi-Proprietary` | license.txt | LicenseRef-JELararagi-Proprietary |
| Smart Tools Manager | `SPDX:LicenseRef-JELararagi-Proprietary` | （なし） | — |
| Smart Workspace | `SPDX:GPL-3.0-or-later` | license.txt | GPL-3.0-or-later |

### 12 本に共通の文

次の 12 本の ZIP の中の `license.txt` は、同じ文です：Smart Modeling・Smart Modifier・Smart Transform・Smart Shader・Smart Animation・Smart Cloth・Smart Selector・Smart Shapekey・Smart Composite・Smart Render・Smart File・Smart Overlay。
次は Smart Cloth の `license.txt` からの原文のままの引用です。

```text
SPDX-License-Identifier: LicenseRef-JELararagi-Proprietary
Copyright (C) 2026 JELararagi. All Rights Reserved.

Unified JELararagi license notice for Blender Extension / user_default compatible add-ons.
This package is provided for JELararagi. Redistribution, relicensing, or removal of this notice is not permitted without explicit permission. Bundled third-party components, if any, retain their original notices where included.
```

### GPL の付いたアドオン

- GPL-3.0-or-later：Smart Geometry・Smart UV・Smart CamLight・キーマップマネージャー・Smart File・Smart ID・Smart Workspace（全文は [LICENSES/GPL-3.0-or-later.txt](LICENSES/GPL-3.0-or-later.txt)）
- GPL-2.0-or-later：Smart Node（全文は [LICENSES/GPL-2.0-or-later.txt](LICENSES/GPL-2.0-or-later.txt)）
- Smart Sculpt：独自のライセンスと GPL-3.0 の部分があります（edit_mode_sculpt は Strict Edit Mode Sculpt v1.4.8 に由来します）。

GPL の付いたアドオンの ZIP には、ソースコード（.py）がそのまま入っています。

### 第三者の部品

次のアドオンは、第三者が作った部品を含みます。著作権の表示とライセンスは、ZIP の中のその部品のフォルダーにあります。

- Smart Animation：camera_shakify・sakura_poselib
- Smart Geometry：debris*
- Smart Modeling：edgeflow
- Smart Node：node_arrange
- Smart Workspace：screencast_keys

### 解説書

解説書（`docs/manuals/` のウェブ版・PDF・画像）と、このサイトのページは © 2026 JELararagi. All rights reserved.

## English

This repository contains the ZIPs of SmartTools (23 Blender extensions) and their manuals (web pages, PDFs and images). Licenses differ per add-on. **The authoritative texts are the license documents and `blender_manifest.toml` inside each ZIP.** The table above lists them as read from the ZIPs.

- These 12 add-ons share the same license text, quoted above from Smart Cloth: Smart Modeling, Smart Modifier, Smart Transform, Smart Shader, Smart Animation, Smart Cloth, Smart Selector, Smart Shapekey, Smart Composite, Smart Render, Smart File, Smart Overlay.
- GPL-3.0-or-later: Smart Geometry, Smart UV, Smart CamLight, キーマップマネージャー, Smart File, Smart ID, Smart Workspace. GPL-2.0-or-later: Smart Node. Full texts: [LICENSES/](LICENSES/).
- Smart Sculpt: its own license, with a GPL-3.0 part (edit_mode_sculpt, derived from Strict Edit Mode Sculpt v1.4.8).
- Third-party components (Smart Animation: camera_shakify, sakura_poselib; Smart Geometry: debris*; Smart Modeling: edgeflow; Smart Node: node_arrange; Smart Workspace: screencast_keys). Their copyright notices and licenses are in the component folders inside the ZIPs.
- The ZIPs of the GPL-licensed add-ons contain their Python source code (.py) as is.
- Manuals (`docs/manuals/`, web pages, PDFs and images) and the pages of this site: © 2026 JELararagi. All rights reserved.
