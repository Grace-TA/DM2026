# 🎤 Golden Demo 上台逐字講稿、數學防禦戰速查與 6 大蘇格拉底 Q&A 實戰手冊

> **對應簡報**：[`Minesweeper_Golden_Demo_Deck.html`](./Minesweeper_Golden_Demo_Deck.html)（共 18 頁 16:9 簡報，按 `P` 鍵開啟雙軌戰略語音 HUD）  
> **發表總時長**：20–25 分鐘（2 人 + AI 團隊標準配當）  
> **核心宗旨**：*「程式碼可以是 AI 寫的，但數學邏輯必須是你的。」*

---

## ⏱️ 一、 20–25 分鐘四環節現場節奏與雙人分工表

| 時間軸 | 發表環節 | 主講分工建議 | 核心展示畫面 | 評審給分焦點 |
|:---:|:---|:---|:---|:---|
| `00:00–05:00` | **1. 產品發表 & Demo Video** | Member A 控場＋播放 4m 影片／實機試玩 | `Minesweeper_Golden_Demo_Video_1080p.mp4` 或 `web_demo/index.html` | 遊戲完整度與 UX (**20%**) |
| `05:00–15:00` | **2. 數學防禦戰 ★（核心 10m）** | Member A 講解網格/集合/關係；Member B 講解 BFS/FSM | `Slide 04–09` + 現場切進 VS Code 開啟 `src/minesweeper_v3_hero.py` | 離散數學連結度 (**40%**) |
| `15:00–20:00` | **3. Prompt 進化與壓測覆盤** | Member B 說明 V1 Bug 抓蟲；Member A 展示圖表與 Pytest | `Slide 10–12` + `assets/complexity_v1_vs_v3.png` + `pytest` 綠燈 | AI Prompting & 工程 (**30%**) |
| `20:00–25:00` | **4. 蘇格拉底 What-if Q&A + STAR** | 雙人互補搶答，一人看代碼行號、一人報數學公式 | `Slide 13–15` + NotebookLM 雙來源展示 | 加分關鍵 & NotebookLM (**10%**) |

---

## 🧭 二、 5 大離散數學概念「行號級」逆向工程備忘表

上台被問「你這 5 個數學觀念寫在程式碼哪裡？」時，直接切出 `src/minesweeper_v3_hero.py` 指向以下精確行號：

1. **Lab 1–2 笛卡兒積網格與獨立矩陣**：[`MinesweeperHeroEngine.__init__`](../src/minesweeper_v3_hero.py) **L65–L66**（`logic_board = [[0 for _ in range(cols)] for _ in range(rows)]`），驗證 `len({id(r) for r in logic_board}) == rows`，消除 V1 `[[0]*cols]*rows`（`minesweeper_v1_buggy.py` L26）淺拷貝連坐污染。
2. **Lab 3 & 5 集合不重複佈雷與組合機率**：`_place_mines()`（**L83–L86**）使用 `set(self.rng.sample(all_cells, self.num_mines))` 嚴格確保 $|M|=10$，並在 `total_board_combinations()`（**L101–L103**）算出 $\binom{81}{10} = 1,878,392,407,320$，以及 `current_unflagged_mine_probability()`（**L105–L111**）即時算出首擊存活率 $87.65\%$。
3. **Lab 4 八方二元關係與負索引守衛**：`is_valid(r, c)`（**L75–L77**，`0 <= r < self.rows and 0 <= c < self.cols`）搭配 `get_neighbors(r, c)`（**L79–L81**）與 `DIRECTIONS_8`（**L45–L49**），徹底阻絕 Python `board[-1][-1]` 負索引靜默偷讀地雷。
4. **Lab 6–8 圖論連通塊與迭代 BFS Mark-on-Enqueue**：`zero_connected_components()`（**L113–L131**）與 `reveal()`（**L145–L185**）採用 `collections.deque` 迭代展開並在入隊當下立即寫入 `seen_local`（**L176–L178**），確保複雜度為線性 $O(|V|+|E|)$，在 `100×100 (10,000 格)` 實測 `45.39 ms` 零爆棧。
5. **Lab 9 有限狀態機 (FSM) 與吸收態鎖定**：`class GameState(Enum)`（**L21–L26**）定義 `{INIT, PLAYING, WON, LOST}`，於 `toggle_flag()`（**L135**）與 `reveal()`（**L150**）入口強制執行 `if self.state != GameState.PLAYING: return`，將 `WON` 與 `LOST` 鎖定為不可逆吸收態。

---

## ⚔️ 三、 蘇格拉底 What-if 六大必考題標準三段式擬答

> **答題鐵律**：**(1) 先講數學定理/複雜度 $\rightarrow$ (2) 再指源碼檔案與函數 $\rightarrow$ (3) 最後報出實測數據！**

1. **Q1：如果把你們的《踩地雷》地圖從 9×9 放大 100 倍（例如 100×100 = 10,000 格），哪段程式會先崩潰？**
   - **擬答**：V1 會先雙重崩潰！第一，查雷用 `if cell in mines_list` 是 $O(N\cdot M)$，一萬格耗時飆升至 `511.05 ms`；第二，遞迴 DFS 在 `60×60`（3,600 格）就會超過 Python 呼叫堆疊上限直接 `RecursionError`。我們的 V3 已升級為 `set` 雜湊（`0.78 ms`，實測快 **`652.4×`**）與 `deque` 迭代 BFS（`100×100` 僅 **`45.39 ms`** 穩過）。
2. **Q2：你們把遞迴改成迭代 BFS，怎麼證明沒有把原本該展開的格子算錯？**
   - **擬答**：在 `tests/test_minesweeper_hero.py` 中，我們以固定種子 `seed=42` 撰寫了 `test_v3_bfs_dfs_equivalence_and_connected_components`，強制對拍 BFS 佇列版與顯式堆疊 DFS 版展開同一顆 `0` 格（`(0, 0)` 展開 6 格），斷言 `bfs_eng.revealed == dfs_eng.revealed`。
3. **Q3：為什麼首擊沒踩到雷的機率是 87.65%，而且每翻開一格就要重算？**
   - **擬答**：因為佈雷屬於**無放回抽樣**，樣本空間分母為尚未揭開且未插旗的未知格數 $HW - |R| - |F|$，分子為剩餘未標記地雷數 $M - |F|$，因此風險隨揭露動態改變。
4. **Q4：如果測試腳本故意傳入負數座標 `(-1, -1)` 或超出邊界 `(9, 0)` 會發生什麼事？**
   - **擬答**：若無邊界守衛，Python 的負索引會環繞讀取最後一列造成隱形作弊或錯判；我們的 `is_valid()` 採用雙閉區間 `0 <= r < rows and 0 <= c < cols` 立即回傳 `False`，並由 `test_v3_negative_index_guard` 通過驗證。
5. **Q5：玩家踩雷進入 `LOST` 後再點安全格，程式會怎麼處理？**
   - **擬答**：`LOST` 與 `WON` 在 FSM 設計中是嚴格吸收態（Absorbing States），所有寫入操作都在入口被 `if self.state != GameState.PLAYING` 擋下，`revealed` 集合與棋盤狀態保持絕對凍結。
6. **Q6：你們覺得 AI 在這次專題幫了什麼忙，又在哪裡差點坑了你們？**
   - **擬答**：AI 在 5 秒內生成了介面與遊戲主體骨架，但它私下用了 `[[0]*W]*H` 淺拷貝、線性 List 掃描與無保護遞迴 DFS——在 9×9 小測試完全看不出來，直到我們用離散數學壓力測試才抓出這四個定時炸彈並通過 V3 重構。
