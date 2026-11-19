# 💣 AI Game Jam Golden Demo — 離散數學《踩地雷》旗艦示範專題

> **所屬課程**：萬能科技大學 115 學年第 1 學期《離散數學 (Discrete Math.)》`W14–W17 AI Game Jam`  
> **課程宗旨**：*「程式碼可以是 AI 寫的，但數學邏輯必須是你的。」*  
> **雙棲平台**：**GitHub Codespaces (`Ubuntu 24.04.5 LTS` / Port 8080 / `pytest`)** ＋ **Google Colab 單檔筆記本**  
> **成果驗證狀態**：`pytest` 6/6 全綠通過（`< 1s`）｜`slide-spatial-guard v2.0` 18/18 投影片 `0` 違規（水平零溢位、平均填充率 `99.6%`）｜`100×100` 查表加速 `652.4×`（`511.05ms → 0.78ms`）

---

## 📊 Infographic 1：Golden Demo 交付資產全景總覽表 (Deliverable Manifest)

| # | 資產檔案 / 資料夾 | 類型 | 對應 W14–W17 發表與評量角色 | 立即開啟／執行方式 |
|:-:|:---|:---:|:---|:---|
| **1** | [`presentation/Minesweeper_Golden_Demo_Deck.html`](./presentation/Minesweeper_Golden_Demo_Deck.html) | `16:9` 互動簡報 | **上台發表簡報（18 頁，含 `P` 鍵 AI 語音 HUD）** | 瀏覽器雙擊開啟，或轉匯 [`PDF`](./presentation/Minesweeper_Golden_Demo_Deck.pdf) |
| **2** | [`presentation/Presenter_Script_and_QA_Handbook.md`](./presentation/Presenter_Script_and_QA_Handbook.md) | 講稿與攻防手冊 | **20–25m 雙人分工講稿 + 6 大蘇格拉底 Q&A** | 上台前 10 分鐘背誦源碼行號與三段式擬答 |
| **3** | [`video/generate_demo_video.py`](./video/generate_demo_video.py) & [`storyboard_and_script.md`](./video/storyboard_and_script.md) | `3–5 min` 示範影片套件 | **3–5 分鐘 1080p MP4 合成器 + 分鏡 + 字幕** | 執行 `python3 video/generate_demo_video.py`（本機已輸出 1080p MP4） |
| **4** | [`web_demo/index.html`](./web_demo/index.html) | 互動網頁沙盒 | **環節一 Live Demo（20% UX＋即時離散 HUD）** | `python3 -m http.server 8080 -d web_demo` |
| **5** | [`src/minesweeper_v3_hero.py`](./src/minesweeper_v3_hero.py) vs. [`v1_buggy.py`](./src/minesweeper_v1_buggy.py) | Python 核心引擎 | **環節二・三 源碼逆向工程 & V1→V3 Prompt 進化** | 搭配 [`benchmark_and_verify.py`](./src/benchmark_and_verify.py) 實測壓測 |
| **6** | [`tests/test_minesweeper_hero.py`](./tests/test_minesweeper_hero.py) | `pytest` 自動化測試 | **工程驗證守門員（`seed=42` BFS≡DFS 與 100× 壓測）** | `python3 -m pytest -v tests/test_minesweeper_hero.py` |
| **7** | [`notebooks/DM2026_Minesweeper_Golden_Demo_Colab.ipynb`](./notebooks/DM2026_Minesweeper_Golden_Demo_Colab.ipynb) | Colab / Jupyter | **Google Colab 單檔相容版** | 直接上傳 Colab 或於 Codespaces 開啟執行 |

---

## 📊 Infographic 2：五大離散數學支柱與源碼逆向工程對照表 (Math Defense 40%)

| 支柱 | 課程對應單元 | 數學模型與核心不變量 (Invariant) | `minesweeper_v3_hero.py` 實作核心 | 解決的 AI V1 致命缺陷 |
|:---:|:---|:---|:---|:---|
| **1** | `Lab 1–2` 網格與矩陣 | 笛卡兒積 $Q=\mathbb{Z}_H\times\mathbb{Z}_W$；獨立列記憶體 | `[[0 for _ in range(cols)] for _ in range(rows)]` | 消滅 `[[0]*cols]*rows` 淺拷貝連坐污染 |
| **2** | `Lab 3 & 5` 集合與機率 | Hash Set $\|M\|=k$；樣本空間 $\binom{81}{10}=1.88\times 10^{12}$ | `set(self.rng.sample(all_cells, k))` | 消除 `randint` 碰撞與 $O(N^2)$ 列表查雷 |
| **3** | `Lab 4` 八方二元關係 | $R_8\subseteq Q\times Q$；閉區間雙邊界防呆 | `0 <= r < self.rows and 0 <= c < self.cols` | 封殺 `board[-1][-1]` 負索引靜默偷讀 |
| **4** | `Lab 6–8` 連通塊與 BFS | 無向圖 $G=(V,E)$；Mark-on-Enqueue $O(V+E)$ | `collections.deque` + 入隊即加入 `seen_local` | 根除 60×60+ 大圖遞迴 `RecursionError` 爆棧 |
| **5** | `Lab 9` 有限狀態機 | FSM $M=(Q,\Sigma,\delta,q_0,F)$ 吸收態鎖定 | `if self.state != GameState.PLAYING: return` | 杜絕爆炸/勝利後繼續點擊修改盤面外掛 |

---

## 📊 Infographic 3：V1 AI 初版 vs. V3 Hero 實測壓測成績表 (Prompt Evolution 30%)

> 以下數據全數由 [`src/benchmark_and_verify.py`](./src/benchmark_and_verify.py) 實機跑出並儲存於 [`benchmarks/benchmark_results.json`](./benchmarks/benchmark_results.json)：

| 測試項目 / 規模 | 格數 (`H×W`) | ❌ V1 AI 原始版（無數學約束） | ✅ V3 Hero 工程版（五大數學契約） | 實測工程效能提升 |
|:---|---:|:---|:---|:---:|
| **查雷運算 `9×9`** | `81` | `0.0466 ms` (`List` 掃描) | `0.0052 ms` (`Set` 雜湊) | **`8.94×` 加速** |
| **查雷運算 `30×30`** | `900` | `3.4027 ms` (`List` 掃描) | `0.0570 ms` (`Set` 雜湊) | **`59.69×` 加速** |
| **查雷運算 `60×60`** | `3,600` | `59.8532 ms` (`List` 掃描) | `0.2889 ms` (`Set` 雜湊) | **`207.15×` 加速** |
| **查雷運算 `100×100` (123.5×)** | `10,000` | `511.0542 ms` (`List` 掃描) | `0.7833 ms` (`Set` 雜湊) | **`652.40×` 加速** |
| **空白展開 `60×60`** | `3,600` | 💥 **`CRASH_RecursionError`** | ✅ **`14.60 ms`** (`deque` 展開全盤) | **從崩潰變秒殺** |
| **空白展開 `100×100`** | `10,000` | 💥 **`CRASH_RecursionError`** | ✅ **`45.39 ms`** (`deque` 展開全盤) | **抗住 100× 審查** |

---

## 📊 Infographic 4：W14–W17 評分標準（總分 110%）與學生自檢護照

| 評分面向 | 權重 | Golden Demo 對應示範頁與證據 | 學生上台前必檢 Checkpoints |
|:---|:---:|:---|:---|
| **1. 離散數學連結度** | **40%** | `Slide 04–09` + `minesweeper_v3_hero.py` | 能說出至少 5 個離散概念與程式碼行號，扛住 100× 擴展 |
| **2. Prompt Evolution & 工程** | **30%** | `Slide 10–12` + `complexity_v1_vs_v3.png` | 保留 V1 Bug 證據、V3 重構後實測倍率與 `pytest` 全綠截圖 |
| **3. 遊戲完整度與 Demo Video** | **20%** | `web_demo/index.html` + `3–5m Video` | 遊戲操作流暢無閃退、錄製完整 3–5 分鐘含語音與字幕影片 |
| **4. NotebookLM & 創新加分** | **10% (+10%)** | `Slide 15` + STAR 求職履歷模板 | 雙來源（理論+源碼）問答備戰、Port 8080 互動 HUD 展示 |

---

## 🚀 快速在 GitHub Codespaces / 本機重現 (30 秒驗收)

```bash
cd /workspaces/DM2026/AI_Game_Jam_Minesweeper_Golden_Demo

# 1. 執行 100× 壓力測試並產生 300-DPI 對比圖
python3 src/benchmark_and_verify.py

# 2. 執行 6 項自動化 Pytest 單元測試
python3 -m pytest -v tests/test_minesweeper_hero.py

# 3. 開啟可玩互動版《踩地雷 × 離散數學沙盒》（搭配 Ports 8080 預覽）
python3 -m http.server 8080 -d web_demo
```

> **提示**：完整簡報亦提供 16:9 [`Minesweeper_Golden_Demo_Deck.pdf`](./presentation/Minesweeper_Golden_Demo_Deck.pdf) 與 [`Minesweeper_Golden_Demo_Deck.html`](./presentation/Minesweeper_Golden_Demo_Deck.html)（開啟後按鍵盤 `P` 即可召喚雙軌 AI 語音導讀 HUD）。1080p 實機渲染示範影片預設輸出至本機 `DM2026_Golden_Demo_Media/Minesweeper_Golden_Demo_Video_1080p.mp4`，可使用 [`video/generate_demo_video.py`](./video/generate_demo_video.py) 一鍵重製。

---

<p align="center">
  © 2026 iGS / Dr. Horace Chen — Muse Academy × Grace-TA/DM2026
</p>
