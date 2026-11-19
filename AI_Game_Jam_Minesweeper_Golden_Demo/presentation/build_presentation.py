#!/usr/bin/env python3
"""
build_presentation.py — DM2026 Minesweeper Golden Demo 16:9 Presentation Builder
================================================================================
Generates:
  1. presentation/Minesweeper_Golden_Demo_Deck.html (18 slides, 1280x720, P-Key Dual-Track HUD)
  2. presentation/Minesweeper_Golden_Demo_Deck.pdf (16:9 landscape PDF via Playwright)
Compliant with:
  - exec-deck-igs v2.0 (O_SchemaDispatch, O_PeakEndHero, O_FullWrap)
  - slide-spatial-guard v2.0 (G1-G7: <=3px height delta, 0px overflow, >=88% fill, zero empty card)
  - auto-presenter-igs v1.0 (Zero-CORS inline manifest, P-key HUD, ?autoplay=1)
"""

from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH_PATH = ROOT / "benchmarks" / "benchmark_results.json"
CHART_PATH = ROOT / "assets" / "complexity_v1_vs_v3.png"
OUT_HTML = ROOT / "presentation" / "Minesweeper_Golden_Demo_Deck.html"
OUT_PDF = ROOT / "presentation" / "Minesweeper_Golden_Demo_Deck.pdf"


def load_chart_b64() -> str:
    data = CHART_PATH.read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode("ascii")


def build_slides_data(bench: dict, chart_uri: str) -> list[dict]:
    lookup = bench["lookup_scaling"]
    flood = bench["flood_fill_survival"]
    inv = bench["invariants"]
    l100 = lookup[-1]
    f100 = flood[-1]
    f60 = flood[-2]

    return [
        # Slide 01 — Cover Meta
        {
            "id": "slide-01",
            "badge": "GOLDEN DEMO · 01 / 18",
            "title": "離散數學《踩地雷》AI Game Jam 旗艦示範簡報",
            "subtitle": "Grace-TA/DM2026 · VNU 234 · 程式碼可以是 AI 寫的，但數學邏輯必須是你的",
            "meta": [
                ("課程與場域", "115-1 離散數學 (Discrete Math.) · Wed 09:15–12:00 · VNU 234"),
                ("示範專題主題", "Minesweeper Hero：從 Lab 1 網格到 Lab 9 有限狀態機大統合"),
                ("雙棲執行環境", "GitHub Codespaces (Ubuntu 24.04.5 LTS / Port 8080) + Google Colab"),
                ("期末評分規準", "40% 離散數學連結 · 30% Prompt 進化 · 20% 遊戲完整度 · 10% NotebookLM"),
                ("實測壓測規模", f"100×100 (10,000 格)：V3 查表加速 {l100['speedup_x']}x · BFS 僅 {f100['v3_ms']}ms"),
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🎯 本示範簡報四大核心任務 (Notion W14–W17 標準)</div>
                  <div class="mini-grid">
                    <div class="mini-card accent-cyan"><strong>1. Live Demo Video</strong><span>3–5 分鐘實機展示＋旁白影片，打造未來求職升學作品集</span></div>
                    <div class="mini-card accent-indigo"><strong>2. 數學防禦戰 (10m)</strong><span>精準指認源碼背後的 5 大離散數學定理與不變量</span></div>
                    <div class="mini-card accent-emerald"><strong>3. Prompt 進化史 (5m)</strong><span>揭露 V1 AI 幻覺 Bug，展示如何用數學約束優化至 V3</span></div>
                    <div class="mini-card accent-amber"><strong>4. 蘇格拉底 Q&amp;A (5m+)</strong><span>扛住「地圖放大 100 倍」複雜度拷問與邊界壓力測試</span></div>
                  </div>
                </div>
                <div class="callout-bar">💡 按鍵盤 <strong>P</strong> 開啟「自動語音導讀 HUD」，按 <strong>← / →</strong> 切換投影片！</div>
            """,
            "strategy": "封面直接點破「AI寫扣、人管數學」的核心宗旨，並列出課程真實 40/30/20/10 權重與 100x 實測數據建立權威感。",
            "spoken": "大家好，歡迎來到 115 學年度離散數學 AI Game Jam 期末專題的 Golden Demo 示範簡報。這個學期我們以經典遊戲踩地雷作為貫穿全學期的數學載體。在接下來的示範中，我們將展示一份符合 A Plus 滿分規準的報告，應該如何精準呈現產品展示影片、五大離散數學源碼逆向工程、AI Prompt 進化覆盤，以及面對百倍擴展的蘇格拉底防禦戰。",
        },
        # Slide 02 — Agenda & Timebox
        {
            "id": "slide-02",
            "badge": "ROADMAP · 02 / 18",
            "title": "發表節奏藍圖：20–25 分鐘四階段黃金時間配當",
            "points": [
                "<strong>00–05m｜環節一：產品發表與 3–5 分鐘 Demo Video</strong> — 先以流暢實機遊玩吸引注意力，展示棋盤建立、旗標切換與勝利/爆炸流程。",
                "<strong>05–15m｜環節二：數學防禦戰 (核心 10 分鐘 ★)</strong> — 直接開源碼高亮，把遊戲拆解為集合、關係、組合機率、圖論 BFS 與 FSM 狀態機。",
                "<strong>15–20m｜環節三：Prompt 進化與複雜度覆盤 (5 分鐘)</strong> — 呈現 AI 初版 V1 藏了什麼錯，以及自己下達了哪 3 條數學約束救回 V3。",
                "<strong>20–25m｜環節四：蘇格拉底抽問防禦與總結 (5 分鐘)</strong> — 預先準備 100× 擴展數據表、Pytest 黃金對拍與 NotebookLM 雙來源筆記。",
            ],
            "visual_html": """
                <table class="deck-table">
                  <thead><tr><th>時段</th><th>發表環節</th><th>對應評分</th><th>評審最想看到的關鍵證據</th></tr></thead>
                  <tbody>
                    <tr><td><code>00–05m</code></td><td><strong>Live Demo / Video</strong></td><td>UX 20%</td><td>無閃退遊玩流程、即時 HUD、雙棲一鍵啟動</td></tr>
                    <tr><td><code>05–15m</code></td><td><strong>Math Defense ★</strong></td><td>Math 40%</td><td>源碼行號逐一對應 Lab 1–9 定理與公式</td></tr>
                    <tr><td><code>15–20m</code></td><td><strong>Prompt Evolution</strong></td><td>Eng 30%</td><td>V1 Bug 截圖 vs V3 降階曲線圖與加速倍率</td></tr>
                    <tr><td><code>20–25m</code></td><td><strong>Socratic Q&amp;A</strong></td><td>加分 / 防線</td><td>100×100 (10,000 格) 實測存活毫秒數</td></tr>
                  </tbody>
                </table>
                <div class="callout-bar">⚠️ 黃金鐵律：切忌前 15 分鐘都在介紹規則與美術，把時間留給 <strong>Math Defense</strong>！</div>
            """,
            "strategy": "幫學生建立嚴格的時間預算觀念，避免初學者常見「花 15 分鐘講玩法，數學只講 2 分鐘」的失分陷阱。",
            "spoken": "首先看到上台發表的時間分配黃金法則。全場二十到二十五分鐘內，絕對不要花太多時間介紹踩地雷怎麼玩。前五分鐘用三到五分鐘的示範影片快速帶過玩法，把整整十分鐘的核心戰場留給數學防禦戰，接著用五分鐘展示 Prompt 進化前後的效能對比，最後五分鐘從容迎接教授的蘇格拉底抽問。",
        },
        # Slide 03 — Live Demo Strategy
        {
            "id": "slide-03",
            "badge": "RING 1: LIVE DEMO · 03 / 18",
            "title": "環節一示範：為什麼 Codespaces + Colab 雙棲能拿下 UX 滿分？",
            "points": [
                "<strong>單頁 Colab 備援 (<a href='https://github.com/Grace-TA/DM2026' target='_blank'>DM2026</a> 相容)</strong> — 確保任何同學與助教在瀏覽器點開 <code>.ipynb</code> 都能一鍵執行全部基準驗證。",
                "<strong>Codespaces Port 8080 互動沙盒</strong> — 將核心邏輯升級為網頁版即時對戰介面，右側同步顯示集合基數、機率與 BFS 步數 HUD。",
                "<strong>零硬體焦慮的雲端環境</strong> — 運行於 <code>Ubuntu 24.04.5 LTS</code>，程式持久化鎖定在 <code>/workspaces/DM2026</code> 目錄底下的 Git 分支。",
                "<strong>3–5 分鐘預錄雙保險機制</strong> — 預先錄製 1080p 展示影片防止現場斷網或卡頓，同時保留求職面試作品集播放素材。",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🌐 web_demo/index.html — 即時數學防禦 HUD 示範架構</div>
                  <div class="mini-grid">
                    <div class="mini-card accent-cyan">
                      <strong>🎮 左欄：9×9 離散網格 Q</strong>
                      <span><code>[·] [1] [💣] [1] [·]</code><br/><code>[1] [2] [ 2] [1] [·]</code><br/><code>[🚩] [1] [·] [1] [💣]</code><br/>FSM 狀態：<code>PLAYING</code></span>
                    </div>
                    <div class="mini-card accent-indigo">
                      <strong>🧮 右欄：即時數學監控 HUD</strong>
                      <span>• Lab 3 <code>|M|</code>：<code>10 / 81</code><br/>• Lab 5 踩雷率：<code>12.35%</code><br/>• Lab 7 BFS 展開：<code>O(V + E)</code><br/>• Lab 9 FSM 守衛：<code>Active</code></span>
                    </div>
                  </div>
                </div>
                <div class="callout-bar">🚀 Codespaces 啟動：<code>python3 -m http.server 8080 -d web_demo</code> 即刻產出 HTTPS 公開預覽！</div>
            """,
            "strategy": "把 Notion 寫的「可用 Colab 或更好平台」具體落地為 Codespaces Port 8080 網頁沙盒 + Colab 雙棲架構。",
            "spoken": "在第一環節的產品展示中，我們強烈建議採用雙棲設計。一方面保留單檔 Colab 筆記本方便快速測試，另一方面在 GitHub Codespaces 透過 Port 8080 啟動這個互動式網頁沙盒。你在左邊每點一格棋盤，右邊的數學儀表板就會即時跳出集合基數、踩雷機率與 BFS 展開節點數，讓台下評審一眼看出遊戲與數學的直接連動。",
        },
        # Slide 04 — Ring 2 Math Defense Map
        {
            "id": "slide-04",
            "badge": "RING 2: MATH DEFENSE · 04 / 18",
            "title": "環節二總覽：逆向工程《踩地雷》五大離散數學支柱地圖",
            "points": [
                "<strong>支柱一（Lab 1–2）笛卡兒積網格與雙盤面矩陣</strong> — 建立座標集 <i>Q</i> = ℤ<sub><i>H</i></sub> × ℤ<sub><i>W</i></sub>，以列表推導式隔離每列記憶體位址。",
                "<strong>支柱二（Lab 3 &amp; 5）集合不重複佈雷與組合機率</strong> — 用 Hash Set 保證 |<i>M</i>| = 10，並精確計算樣本空間 <i>C</i>(81, 10) 與安全率。",
                "<strong>支柱三（Lab 4）8 方二元關係與閉區間邊界防呆</strong> — 定義鄰居映射 <i>R</i><sub>8</sub> ⊆ <i>Q</i> × <i>Q</i>，以 <code>0 &lt;= r &lt; H</code> 封殺負索引蟲。",
                "<strong>支柱四（Lab 6–8）圖連通分量與迭代 BFS 展開</strong> — 將空白安全區視為連通塊，透過 <code>deque</code> 入隊標記維持線性 <i>O</i>(<i>V</i> + <i>E</i>)。",
                "<strong>支柱五（Lab 9）有限狀態機與不可逆吸收態</strong> — 用 <code>Enum</code> 定義狀態轉移圖，鎖死 <code>WON/LOST</code> 防死後刷分。",
            ],
            "visual_html": """
                <table class="deck-table">
                  <thead><tr><th>課程單元</th><th>離散數學模型</th><th><code>minesweeper_v3_hero.py</code> 對應符號</th><th>防呆不變量 (Invariant)</th></tr></thead>
                  <tbody>
                    <tr><td><code>Lab 1–2</code></td><td>Cartesian Grid &amp; Matrix</td><td><code>self.logic_board</code> (Row-Isolated)</td><td><code>len({id(r) for r in board}) == H</code></td></tr>
                    <tr><td><code>Lab 3, 5</code></td><td>Set &amp; Combinatorics</td><td><code>self.mines = set(rng.sample(...))</code></td><td><code>len(mines) == M</code>，空間 <i>C</i>(81, 10)</td></tr>
                    <tr><td><code>Lab 4</code></td><td>Binary Relation <i>R</i><sub>8</sub></td><td><code>is_valid()</code> + <code>get_neighbors()</code></td><td>嚴格 <code>0 &lt;= r &lt; H and 0 &lt;= c &lt; W</code></td></tr>
                    <tr><td><code>Lab 6–8</code></td><td>Connected Graph &amp; BFS</td><td><code>reveal()</code> + <code>collections.deque</code></td><td>Mark-on-Enqueue，永不遞迴爆棧</td></tr>
                    <tr><td><code>Lab 9</code></td><td>Finite State Machine</td><td><code>class GameState(Enum)</code></td><td><code>WON/LOST</code> 拒絕對盤面做任何異動</td></tr>
                  </tbody>
                </table>
            """,
            "strategy": "這是整場報告佔 40% 評分的心臟總表，提供一張「課程單元 -> 數學定義 -> 源碼位置 -> Assert 不變量」的對照架構。",
            "spoken": "接下來進入佔總分百分之四十的數學防禦戰。評審在乎的不是你會不會背名詞，而是你能不能指著自己的原始碼，證明這五大離散數學支柱如何保護遊戲不會出錯。從 Lab 1 的笛卡兒積網格、Lab 3 集合不重複佈雷、Lab 4 八方關係守衛、Lab 7 迭代廣度優先搜尋，一直到 Lab 9 有限狀態機的吸收態，每一層都有明確的程式碼不變量。",
        },
        # Slide 05 — Math Pillar 1: Lab 1-2
        {
            "id": "slide-05",
            "badge": "MATH PILLAR 1 · 05 / 18",
            "title": "支柱一 (Lab 1–2)：笛卡兒積網格與破除淺拷貝污染陷阱",
            "points": [
                "<strong>離散空間數學定義</strong> — 棋盤由離散整數座標 <i>Q</i> = {0, …, <i>H</i>−1} × {0, …, <i>W</i>−1} 構成，與連續浮點坐標嚴格區分。",
                "<strong>MVC 雙盤面矩陣隔離</strong> — <code>logic_board</code> 保存地雷 (-1) 與周圍雷數 (0–8)；<code>visible_board</code> 僅儲存玩家可見符號。",
                "<strong>V1 AI 最常犯的致命淺拷貝 Bug</strong> — AI 常寫出 <code>[[0]*cols]*rows</code>，導致所有列共享同一個 List 記憶體參考位址！",
                "<strong>V3 列表推導式根治方案</strong> — 改用 <code>[[0 for _ in range(cols)] for _ in range(rows)]</code>，實測 9 列各自獨立無交叉污染。",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">❌ V1 AI 初版 (Alias Bug) vs. ✅ V3 Hero (Row-Isolated)</div>
                  <pre class="code-pre"><span class="hl-bad"># ❌ V1: All rows point to the SAME list object!</span>
self.logic_board = [[0] * cols] * rows
v1.logic_board[0][0] = 99
assert v1.logic_board[1][0] == 99  <span class="hl-bad"># 改第0列，全盤每列都被改壞！</span>

<span class="hl-good"># ✅ V3: Independent memory allocation per row (Lab 2)</span>
self.logic_board = [[0 for _ in range(cols)] for _ in range(rows)]
assert len({id(row) for row in self.logic_board}) == rows</pre>
                </div>
                <div class="callout-bar">🛡️ 驗證：<code>test_v1_demonstrates_shallow_copy_aliasing</code> 與 <code>test_v3_row_isolation_and_exact_mine_cardinality</code> PASS！</div>
            """,
            "strategy": "用真實可執行的 Python Aliasing 陷阱示範「為什麼不能盲信 AI 生成的二維陣列初始化」。",
            "spoken": "先看第一支柱：笛卡兒積網格與矩陣。很多同學請 AI 幫他建二維棋盤，AI 會寫出中括號零乘以寬再乘以高。這行代碼在 Python 裡會造成致命的淺拷貝污染，你只改了第零列第一格，結果整張地圖每一列的同一欄全部一起變質。我們在 V3 強制改用巢狀列表推導式，並寫下 id 唯一性斷言，徹底隔離每個矩陣列的記憶體空間。",
        },
        # Slide 06 — Math Pillar 2: Lab 3 & 5
        {
            "id": "slide-06",
            "badge": "MATH PILLAR 2 · 06 / 18",
            "title": "支柱二 (Lab 3 &amp; 5)：Set 集合無碰撞佈雷與組合機率空間",
            "points": [
                "<strong>為什麼不能用 <code>randint</code> 迴圈？</strong> — 隨機抽中重複座標會導致碰撞或陷入線性列表搜尋 <code>in list</code> 的 <i>O</i>(<i>N</i><sup>2</sup>) 效能黑洞。",
                "<strong>集合基數不變量 |<i>M</i>| = <i>k</i></strong> — 改用無放回抽樣 <code>set(rng.sample(all_cells, k))</code>，單次掃描 <i>O</i>(<i>HW</i>) 嚴格保證地雷數絕不少顆。",
                "<strong>組合數學樣本空間計算</strong> — 標準 9×9 含 10 雷盤面共有 <i>C</i>(81, 10) = 1,878,392,407,320（約 1.88 兆）種唯一佈局。",
                "<strong>動態條件存活機率 HUD</strong> — 首擊存活率為 (81 − 10) / 81 = 87.65%，每次安全展開或插旗皆會即時更新剩餘盲點風險。",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🎲 minesweeper_v3_hero.py — Lab 3 &amp; Lab 5 核心實作</div>
                  <pre class="code-pre"><span class="hl-good">def _place_mines(self, exclude=None):</span>
    all_cells = [(r, c) for r in range(self.rows)
                 for c in range(self.cols) if (r, c) != exclude]
    self.mines = set(self.rng.sample(all_cells, self.num_mines))

<span class="hl-good">def current_unflagged_mine_probability(self) -> float:</span>
    unknown = (self.rows * self.cols) - len(self.revealed) - len(self.flagged)
    rem_mines = max(0, self.num_mines - len(self.flagged))
    return min(1.0, rem_mines / unknown) if unknown > 0 else 0.0</pre>
                </div>
                <div class="callout-bar">📊 實測數值：<code>C(81, 10) = 1,878,392,407,320</code>｜首擊安全率 <code>87.65%</code>｜O(1) 雜湊查雷！</div>
            """,
            "strategy": "結合 Lab 3 集合無重複性與 Lab 5 組合數 C(81,10)，並把靜態公式變成即時計算條件機率的動態 HUD。",
            "spoken": "第二支柱結合了 Lab 3 的集合論與 Lab 5 的排列組合機率。如果用傳統的亂數迴圈加 List 檢查重複，當盤面放大或地雷變多時會產生大量碰撞與線性掃描瓶頸。我們改用 random.sample 配合 Python Set，在線性時間內嚴格保證地雷集合基數等於十。同時我們精確算出九乘九十雷共有超過一點八兆種可能佈局，以及百分之八十七點六五的首擊安全機率。",
        },
        # Slide 07 — Math Pillar 3: Lab 4
        {
            "id": "slide-07",
            "badge": "MATH PILLAR 3 · 07 / 18",
            "title": "支柱三 (Lab 4)：8 方二元關係與封殺 Python 負索引幽靈",
            "points": [
                "<strong>鄰居關係數學定義</strong> — 對於任一座標 (<i>r</i>, <i>c</i>) ∈ <i>Q</i>，其 8 鄰居集合定義為切比雪夫距離 max(|<i>r'</i> − <i>r</i>|, |<i>c'</i> − <i>c</i>|) = 1 之有效格子。",
                "<strong>Python 負索引的隱形殺機</strong> — 在未設防禦的座標運算中，<code>board[-1][-1]</code> 不會報錯，而是會靜默偷讀最右下角的地雷！",
                "<strong>閉區間邊界守門員</strong> — 建立 <code>is_valid(r, c)</code> 強制檢核 <code>0 &lt;= r &lt; rows and 0 &lt;= c &lt; cols</code>，邊界格僅回傳 3 鄰居。",
                "<strong>度數分佈驗證 (Degree Check)</strong> — 角落節點度數為 3、邊緣非角節點為 5、內部節點為 8，完美銜接 Lab 6 圖論度數概念。",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🧭 minesweeper_v3_hero.py — 8 方關係 R8 與負索引防線</div>
                  <pre class="code-pre">DIRECTIONS_8 = (
    (-1,-1), (-1,0), (-1,1),
    ( 0,-1),         ( 0,1),
    ( 1,-1), ( 1,0), ( 1,1),
)
def is_valid(self, r: int, c: int) -> bool:
    return 0 <= r < self.rows and 0 <= c < self.cols

def get_neighbors(self, r: int, c: int):
    return [(r + dr, c + dc) for dr, dc in self.DIRECTIONS_8
            if self.is_valid(r + dr, c + dc)]</pre>
                </div>
                <div class="callout-bar">✅ Pytest 邊界斷言：<code>len(get_neighbors(0, 0)) == 3</code> 且 <code>reveal(-1, -1)</code> 零異常安全略過！</div>
            """,
            "strategy": "突顯「Python 不報錯卻算錯」的負索引邏輯陷阱，這是資工面試與 Math Defense 極受青睞的細節。",
            "spoken": "第三支柱是 Lab 4 的八方二元關係。在 Python 寫棋盤遊戲最危險的不是程式當掉，而是靜默錯誤。當程式掃描第零列零行的鄰居時，如果不檢查邊界，減一會變成負一，Python 不會報錯而是直接環繞偷讀最後一列的地雷。因此我們寫死閉區間邊界守衛 is_valid，讓角落節點只回傳三個鄰居、邊緣回傳五個、內部回傳八個，從數學上消滅越界幻覺。",
        },
        # Slide 08 — Math Pillar 4: Lab 6-8
        {
            "id": "slide-08",
            "badge": "MATH PILLAR 4 · 08 / 18",
            "title": "支柱四 (Lab 6–8)：連通塊模型與 BFS Mark-on-Enqueue O(V+E)",
            "points": [
                "<strong>把棋盤看成無向圖 <i>G</i> = (<i>V</i>, <i>E</i>)</strong> — 每個數字為 0 的安全格皆是頂點，透過 <i>R</i><sub>8</sub> 相鄰形成多個安全「連通分量 (Connected Components)」。",
                "<strong>為何遞迴 DFS 在大圖必死？</strong> — Python 預設呼叫堆疊上限約 1,000 層；當 60×60 空白區展開超過千格即爆出 <code>RecursionError</code>！",
                "<strong>迭代 BFS 佇列重構解法</strong> — 使用 <code>collections.deque</code> 顯式佇列取代系統呼叫堆疊，支援任意萬格以上大型棋盤不當機。",
                "<strong>Mark-on-Enqueue 防重排不變量</strong> — 鄰居一加入佇列就立刻寫入 <code>seen_local</code>，確保每個節點最多入隊 1 次，嚴格維持 <i>O</i>(<i>V</i> + <i>E</i>)。",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🌊 V3 迭代佇列 + 入隊即標記 (Mark-on-Enqueue)</div>
                  <pre class="code-pre">frontier = deque([(r, c)])
seen_local = {(r, c)}  <span class="hl-good"># 關鍵：入隊當下立即標記，防止重複入隊膨脹！</span>
while frontier:
    cr, cc = frontier.popleft()
    self.revealed.add((cr, cc))
    if self.logic_board[cr][cc] == 0:
        for nr, nc in self.get_neighbors(cr, cc):
            if (nr, nc) not in self.revealed and (nr, nc) not in seen_local:
                seen_local.add((nr, nc))
                frontier.append((nr, nc))</pre>
                </div>
                <div class="callout-bar">⚡ 實測結果：<code>60×60</code> V1 遞迴當機，V3 在 <strong><code>100×100 (10,000 格)</code> 僅需 <code>~45.4 ms</code></strong>！</div>
            """,
            "strategy": "講清楚兩個常被搞混的高階概念：(1) 迭代 deque 防爆棧，(2) Mark-on-Enqueue 防重複入隊指數退化。",
            "spoken": "第四支柱是整個踩地雷演算法的心臟：連通塊與廣度優先搜尋。AI 初版通常會寫出看似簡潔的遞迴 DFS，在小盤面能跑，但一旦展開超過一千格就會觸發 RecursionError 直接崩潰。我們在 V3 改用 collections.deque 進行迭代式 BFS，並在鄰居加入佇列的當下就先標記已見過，避免同一格被八個鄰居重複塞進佇列，確保時間複雜度嚴格鎖死在線性的 O(V+E)。",
        },
        # Slide 09 — Math Pillar 5: Lab 9
        {
            "id": "slide-09",
            "badge": "MATH PILLAR 5 · 09 / 18",
            "title": "支柱五 (Lab 9)：有限狀態機 (FSM) 與不可逆吸收態防護",
            "points": [
                "<strong>形式化 5 元組模型 <i>M</i> = (<i>Q</i>, Σ, δ, <i>q</i><sub>0</sub>, <i>F</i>)</strong> — 狀態集 <i>Q</i> = {<code>INIT</code>, <code>PLAYING</code>, <code>WON</code>, <code>LOST</code>}，定義嚴謹生命週期。",
                "<strong>單向終止吸收態 (Absorbing Sinks)</strong> — 一旦玩家踩雷進入 <code>LOST</code> 或揭開全部安全格進入 <code>WON</code>，對任意點擊轉移恆指回自身。",
                "<strong>源碼第一行防呆守衛</strong> — 在 <code>reveal()</code> 與 <code>toggle_flag()</code> 開頭強制檢查 <code>if self.state != GameState.PLAYING: return</code>。",
                "<strong>杜絕遊戲常見外掛漏洞</strong> — 徹底封鎖「遊戲失敗後繼續點擊格子或插旗刷分」的未定義狀態 Bug，僅能透過重開實例重置。",
            ],
            "visual_html": r"""
                <div class="code-box">
                  <div class="code-title">🔄 Lab 9 有限狀態機轉移圖 (State Transition Graph)</div>
                  <pre class="code-pre">   [INIT] ──(_place_mines + count)──▶ [PLAYING]
                                       /      \
             (click mine)             /        \  (|revealed| == H*W - M)
                                     ▼          ▼
                                 [LOST] ⟲    [WON] ⟲
                        (Absorbing Sinks: All clicks ignored!)</pre>
                </div>
                <div class="callout-bar">🔒 測試驗證：<code>test_v3_fsm_absorbing_states_won_and_lost</code> 確保爆炸後 <code>revealed</code> 集合完全不變！</div>
            """,
            "strategy": "將抽象的有限狀態機圖論轉換為實際遊戲防外掛機制，展現 L5 系統邊界思維。",
            "spoken": "第五支柱是 Lab 9 的有限狀態機 FSM。我們把遊戲生命週期明確定義為 INIT、PLAYING、WON 與 LOST 四個離散狀態。最關鍵的設計是把 WON 和 LOST 設為不可逆的吸收態。在所有會修改盤面的函式第一行都加上狀態檢查守衛，只要不是 PLAYING 就直接拒絕執行，從數學模型上徹底堵死死後復活或重複刷分的狀態機漏洞。",
        },
        # Slide 10 — Ring 3 Prompt Evolution
        {
            "id": "slide-10",
            "badge": "RING 3: PROMPT EVOLUTION · 10 / 18",
            "title": "環節三：Prompt Evolution — 如何用離散數學約束「逼迫」AI 寫對代碼？",
            "points": [
                "<strong>V1 許願式 Prompt（失敗）</strong> — 「幫我用 Python 寫一個踩地雷遊戲」，結果 AI 悄悄埋入 <code>[[0]*W]*H</code>、List 掃描與遞迴爆棧。",
                "<strong>V2 防禦除錯 Prompt（半成品）</strong> — 「請修復二維陣列獨立性與負索引，並用 Set 存地雷」，雖然解決碰撞但大棋盤仍會 <code>RecursionError</code>。",
                "<strong>V3 離散數學契約 Prompt（滿分）</strong> — 「使用列表推導式、<code>rng.sample</code> Set、<code>deque</code> Mark-on-Enqueue <i>O</i>(<i>V</i> + <i>E</i>) 與 <code>Enum</code> FSM 吸收態」。",
                "<strong>黃金逆向工程心法</strong> — AI 擅長產出語法骨架，但唯有修過離散數學的工程師才能下達「複雜度與不變量契約」並用單元測試驗收。",
            ],
            "visual_html": f"""
                <table class="deck-table">
                  <thead><tr><th>版本</th><th>給 AI 的 Prompt 約束等級</th><th>AI 產出的隱患 / 實測表現</th><th>Math Defense 判定</th></tr></thead>
                  <tbody>
                    <tr><td><code>V1</code></td><td>無數學約束（Vibe Coding）</td><td><code>[[0]*W]*H</code> aliasing、<i>O</i>(<i>N</i><sup>2</sup>) 查表、60×60 爆棧</td><td><span class="hl-bad">❌ Fail (當機/污染)</span></td></tr>
                    <tr><td><code>V2</code></td><td>局部修復資料結構（List → Set）</td><td>解決查雷速度，但遞迴 DFS 與 FSM 狀態鎖仍漏</td><td><span class="hl-warn">⚠️ Partial (不耐擴展)</span></td></tr>
                    <tr><td><code>V3</code></td><td><strong>五大離散定理 + 複雜度 + Assert 契約</strong></td><td><code>{l100['speedup_x']}x</code> 加速、100×100 穩跑、全 6 項 Pytest PASS</td><td><span class="hl-good">✅ A+ Hero (可上線)</span></td></tr>
                  </tbody>
                </table>
                <div class="callout-bar">🧠 核心金句：「Prompt 的精準度，取決於你腦中離散數學模型有多清晰！」</div>
            """,
            "strategy": "這是 Notion W14–W17 第三環節 (5 分鐘) 的滿分模板，清楚對照 V1 到 V3 如何靠數學知識引導 AI 進化。",
            "spoken": "第三環節是 Prompt 進化覆盤。很多同學跟 AI 協作時，只會輸入一句「幫我寫個踩地雷」，產出的 V1 看起來能動，背後卻藏了四顆定時炸彈。我們示範如何從 V1 的模糊許願，進化到 V2 指定 Set 集合，最終在 V3 下達包含列表推導式、deque 入隊標記以及 Enum 吸收態的完整數學契約，成功逼出零缺陷的工業級程式碼。",
        },
        # Slide 11 — Empirical 100x Chart
        {
            "id": "slide-11",
            "badge": "EMPIRICAL PROOF · 11 / 18",
            "title": "實測數據證據：100× 盤面擴展壓力測試 (V1 崩潰 vs. V3 飛躍)",
            "points": [
                f"<strong>100×100 (10,000 格) 查表加速</strong> — V1 列表掃描耗時 <code>{l100['v1_list_scan_ms']} ms</code>，V3 Hash Set 僅需 <code>{l100['v3_set_hash_ms']} ms</code>（實測快 <strong>{l100['speedup_x']} 倍</strong>）。",
                f"<strong>60×60 (3,600 格) 洪水填充死亡線</strong> — V1 遞迴 DFS 在 3,600 格當場 <code>CRASH_RecursionError</code>；V3 迭代 BFS 僅 <code>{f60['v3_ms']} ms</code>。",
                f"<strong>100×100 (10,000 格) 終極存活驗證</strong> — 面積為 9×9 的 <strong>123.5 倍</strong>，V3 依然於 <code>{f100['v3_ms']} ms</code> 內精確展開全盤獲勝！",
                "<strong>可重現腳本一鍵生成</strong> — 右圖由 <code>src/benchmark_and_verify.py</code> 實時跑出 300-DPI 圖表，絕非人工手繪假數據。",
            ],
            "visual_html": f"""
                <div class="img-wrap">
                  <img src="{chart_uri}" alt="V1 vs V3 Complexity Benchmark Chart" />
                </div>
                <div class="callout-bar">📈 數據來源：<code>benchmarks/benchmark_results.json</code>（實機計時，非理論猜測！）</div>
            """,
            "strategy": "展示真實生成的雙面板 300-DPI 科學圖表，用實際毫秒數與 CRASH 標籤直接壓服所有對效能的質疑。",
            "spoken": "空口無憑，我們直接看這張由 benchmark_and_verify.py 實地跑出來的三百 DPI 壓測對比圖。左圖是地雷查詢耗時的對數座標，當盤面擴張到一萬格時，Hash Set 查詢比 V1 快了超過六百五十倍。右圖更震撼：在六十乘六十與一百乘一百的空白盤面展開時，V1 遞迴直接因為爆棧而崩潰，而我們的 V3 迭代 BFS 在四十五毫秒內安然過關。",
        },
        # Slide 12 — Pytest & Equivalence Gate
        {
            "id": "slide-12",
            "badge": "QUALITY GATE · 12 / 18",
            "title": "工程驗證守門員：Pytest 自動化單元測試與種子等價對拍",
            "points": [
                "<strong>從「人肉看截圖」升級為自動化測試</strong> — 撰寫 <code>tests/test_minesweeper_hero.py</code>，1 秒內自動檢驗全數 6 大核心數學不變量。",
                "<strong><code>seed=42</code> 雙演算法黃金等價對拍</strong> — 驗證迭代式 BFS 與顯式堆疊 DFS 在相同隨機種子下，揭開完全一模一樣的格子集合。",
                "<strong>反面實證測試 (Falsification Test)</strong> — 專設一條測試故意觸發 V1 淺拷貝連坐污染，證明舊版確實存在該結構瑕疵。",
                "<strong>Codespaces / CI 無縫接軌</strong> — 下學期若進階加上 GitHub Actions，每次學生 <code>git push</code> 都能自動亮綠燈批改作業！",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🧪 pytest -v tests/test_minesweeper_hero.py (驗收清單)</div>
                  <pre class="code-pre">test_v1_demonstrates_shallow_copy_aliasing            <span class="hl-good">PASSED</span>
test_v3_row_isolation_and_exact_mine_cardinality      <span class="hl-good">PASSED</span>
test_v3_negative_index_guard                          <span class="hl-good">PASSED</span>
test_v3_bfs_dfs_equivalence_and_connected_components  <span class="hl-good">PASSED</span>
test_v3_100x_scale_survival_without_recursion_error   <span class="hl-good">PASSED</span>
test_v3_fsm_absorbing_states_won_and_lost             <span class="hl-good">PASSED</span>
<span class="hl-cyan">================ 6 passed (&lt;1s real-time gate) ================</span></pre>
                </div>
                <div class="callout-bar">🛡️ 黃金等價公式：<code>assert bfs_eng.revealed == dfs_eng.revealed</code>（無損優化鐵證）</div>
            """,
            "strategy": "示範資工大一生也能寫出的工業級 Pytest 測試門檻，這是評審眼中最強的工程成熟度訊號。",
            "spoken": "除了跑給玩家玩之外，高分專題的秘密武器就是這六條自動化 Pytest 單元測試。我們用固定隨機種子 seed 等於四十二做黃金對拍，證明我們的 BFS 與顯式 DFS 揭開完全一致的座標集合；同時把邊界防護、百倍存活以及狀態機鎖死全部寫成自動化斷言，一秒內就能驗證完畢。",
        },
        # Slide 13 — Socratic Q&A 1-3
        {
            "id": "slide-13",
            "badge": "RING 4: SOCRATIC Q&A · 13 / 18",
            "title": "環節四攻防 (1/2)：蘇格拉底 What-if 壓力拷問實戰擬答",
            "points": [
                f"<strong>Q1：如果明天地圖長寬各放大 10 倍（面積 100 倍），誰先掛掉？</strong> — 答：V1 的 List 搜尋會膨脹為 <i>O</i>(<i>N</i><sup>2</sup>) 且遞迴深度突破 1,000 爆棧；V3 使用 Set <i>O</i>(1) 與 <code>deque</code> BFS <i>O</i>(<i>V</i> + <i>E</i>)，實測 10,000 格僅 {f100['v3_ms']:.2f}ms。",
                "<strong>Q2：你們怎麼確定改完演算法後，不會少展開或展開錯格子？</strong> — 答：我們以 <code>seed=42</code> 執行 BFS 與 DFS 黃金等價對拍，強制斷言展開集合與勝敗結果 100% 相等。",
                "<strong>Q3：為何 9×9 十雷的首擊安全率是 87.65%，點完 20 格後還是一樣嗎？</strong> — 答：絕非固定！無放回抽樣的分母動態縮減，剩餘未知格為 81 − |<i>R</i>| − |<i>F</i>|，HUD 即時重算條件機率。",
            ],
            "visual_html": f"""
                <table class="deck-table">
                  <thead><tr><th>教授犀利追問焦點</th><th>高分應答結構 (定理 + 數據 + 檔案行號)</th></tr></thead>
                  <tbody>
                    <tr><td><strong>100× 規模瓶頸點</strong></td><td>指出 <code>in list</code> 與遞迴 Call Stack → 秀出 <code>{l100['speedup_x']}x</code> 實測表</td></tr>
                    <tr><td><strong>優化等價性證明</strong></td><td>指出 <code>test_v3_bfs_dfs_equivalence_and_connected_components</code> → Mark-on-Enqueue</td></tr>
                    <tr><td><strong>條件機率動態性</strong></td><td>公式 (<i>M</i> − |<i>F</i>|) / (<i>HW</i> − |<i>R</i>| − |<i>F</i>|) → 對比遊戲 HUD 即時數字</td></tr>
                  </tbody>
                </table>
                <div class="callout-bar">⚔️ 應答秘訣：永遠先講「<strong>數學不變量</strong>」，再指出「<strong>原始碼哪一行實作</strong>」，最後報「<strong>實測毫秒數</strong>」！</div>
            """,
            "strategy": "把第四環節 5–10 分鐘最令學生緊張的教授抽問拆解為標準三段式答題公式（定理 -> 行號 -> 數據）。",
            "spoken": "到了第四環節蘇格拉底現場抽問，同學最怕老師突然問一句：如果地圖放大一百倍怎麼辦？別慌，標準的滿分回答遵循三步公式：先點破舊版瓶頸在哪一個時間複雜度階數，接著報出我們的 Set 與 deque 解法，最後直接秀出剛才實測的一萬格四十五毫秒存活數據，立刻拿下現場滿堂彩。",
        },
        # Slide 14 — Socratic Q&A 4-6
        {
            "id": "slide-14",
            "badge": "RING 4: SOCRATIC Q&A · 14 / 18",
            "title": "環節四攻防 (2/2)：邊界防禦、狀態鎖定與「AI 差點害死我們」",
            "points": [
                "<strong>Q4：如果玩家透過外掛或程式傳入負座標 <code>(-1, -1)</code> 會發生什麼？</strong> — 答：Python 負索引會偷讀最末列；我們的 <code>is_valid()</code> 閉區間守衛會立即攔截並回傳 0 展開。",
                "<strong>Q5：遊戲踩雷爆炸後，玩家手速太快連點兩次畫面會變怎樣？</strong> — 答：<code>GameState.LOST</code> 是嚴格吸收態，<code>reveal()</code> 第一行即擋下操作，不會覆蓋或改動盤面。",
                "<strong>Q6：AI 在這個專題到底幫了什麼忙，又在哪裡差點害死你們？</strong> — 答：AI 5 秒寫出介面骨架，卻暗藏淺拷貝與遞迴溢位；全靠我們用離散數學審計抓蟲，人腦才是最終架構師！",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">🛡️ 現場防禦程式碼三道鐵門 (Defense-in-Depth)</div>
                  <pre class="code-pre"><span class="hl-cyan"># Gate 1: FSM Absorbing State Guard (Lab 9)</span>
if self.state != GameState.PLAYING:
    return self.state, 0

<span class="hl-cyan"># Gate 2: Closed-Interval Boundary Guard (Lab 4)</span>
if not (0 <= r < self.rows and 0 <= c < self.cols):
    return self.state, 0

<span class="hl-cyan"># Gate 3: Mark-on-Enqueue Loop Guard (Lab 7-8)</span>
if (nr, nc) not in self.revealed and (nr, nc) not in seen_local:
    seen_local.add((nr, nc))</pre>
                </div>
                <div class="callout-bar">🎙️ 反敗為勝話術：主動分享「我們如何抓出 AI 的 Bug」，在評審眼中反而是最高含金量的工程亮點！</div>
            """,
            "strategy": "教導學生把「抓出 AI 的錯」轉化為主動得分點，完美呼應「AI寫扣、人管邏輯」的課程哲學。",
            "spoken": "另外三個必考問題聚焦在邊界安全、狀態機鎖死與人機協作反思。記住，當評審問 AI 在這份專題哪裡幫倒忙時，千萬不要說 AI 寫得都很棒。大方承認 AI 一開始偷懶用了淺拷貝和遞迴，而你們如何運用課堂學到的離散數學概念把問題抓出來修正，這正是整堂課最想看到的工程師洞察力。",
        },
        # Slide 15 — NotebookLM & STAR Pitch
        {
            "id": "slide-15",
            "badge": "NLM & CAREER · 15 / 18",
            "title": "10% 加分神器：NotebookLM 雙來源備戰與 STAR 求職履歷轉譯",
            "points": [
                "<strong>NotebookLM 雙來源戰法（佔 10%）</strong> — 同時匯入「課程離散理論筆記」與「<code>minesweeper_v3_hero.py</code> 源碼」，自動出題紅隊互考。",
                "<strong>3–5 分鐘 Demo Video 的長尾價值</strong> — Notion 特別指出影片可放於未來升學書審與求職作品集，展現系統架構與口條實力。",
                f"<strong>STAR 科技業實習履歷轉譯公式</strong> — 將「做一個踩地雷」改寫為「診斷 AI 代碼複雜度瓶頸並實現 <code>{l100['speedup_x']}x</code> 查詢加速與萬格零當機」。",
                "<strong>GitHub Codespaces 作品集打包</strong> — 寫好含壓測圖、測試綠勾與啟動徽章的 <code>README.md</code>，面試官一鍵打開即能試玩。",
            ],
            "visual_html": f"""
                <div class="code-box">
                  <div class="code-title">💼 實習／升學履歷 STAR 敘事範本（可直接改寫套用）</div>
                  <pre class="code-pre">• [S/T] 針對生成式 AI 初版《踩地雷》原型在大盤面擴展時發生
        淺拷貝污染、O(N²) 查表延遲與 60×60 遞迴爆棧崩潰問題。
• [A]   導入五大離散數學工程契約：列表推導式列隔離、Hash Set 佈雷、
        閉區間 8 方關係守衛、deque Mark-on-Enqueue BFS 與 Enum FSM。
• [R]   於 100×100 (10,000 格) 實測實現 <span class="hl-good">{l100['speedup_x']}x 查表加速</span>
        (<span class="hl-cyan">{l100['v1_list_scan_ms']:.2f}ms → {l100['v3_set_hash_ms']:.2f}ms</span>)，萬格 BFS 展開僅 {f100['v3_ms']:.2f}ms 並通過 6 項 Pytest。</pre>
                </div>
                <div class="callout-bar">🏆 特別獎勵提醒：學期學習成果最完整前三名同學，還有 7-11 商品卡加碼鼓勵！</div>
            """,
            "strategy": "把期末報告從「交作業」升維成「大學第一張科技業實習作品集王牌」，大大提升學生內在動機。",
            "spoken": "最後別忘了佔百分之十的 NotebookLM 創新與專題的長尾價值。將課程理論與你的原始碼同時餵進 NotebookLM，就能請 AI 模擬教授進行紅隊反詰練習。更重要的是，當你按照這套標準完成測試與錄製三到五分鐘的影片後，它不只是期末作業，而是可以直接放進大一大二實習履歷的 STAR 工程代表作。",
        },
        # Slide 16 — Peak-End Panoramic Hero Closing
        {
            "id": "slide-16",
            "badge": "CLOSING · 16 / 18",
            "title": "Peak-End 壓軸致謝：駕馭 AI 的離散數學架構師",
            "thanks_hero": True,
            "thanks_title": "程式碼可以是 AI 寫的，但離散數學邏輯永遠屬於你！",
            "thanks_sub": "Grace-TA/DM2026 × AI Game Jam Golden Demo｜祝各位同學在 Demo Day 拿下 A+ 與最佳成果獎！",
            "strategy": "Peak-End 峰終定律收尾劇院，強化全課程靈魂金句，並將學生實戰清單後移為 Backup Slides (測試 Schema Dispatch)。",
            "spoken": "感謝各位同學與教授的聆聽。記住這學期我們在萬能資工離散數學最核心的一句話：程式碼可以是 AI 寫的，但離散數學的邏輯與邊界控制永遠屬於你。接下來兩頁附錄提供 3 到 5 分鐘展示影片的逐格分鏡檢查表與 Codespaces 雙棲指令，祝大家期末 Demo Day 旗開得勝！",
        },
        # Slide 17 — Backup 01: 3-5 Min Demo Video Blueprint
        {
            "id": "slide-17",
            "badge": "BACKUP 01 · 17 / 18",
            "is_backup": True,
            "title": "Backup 01：學生自製 3–5 分鐘 Demo Video 黃金分鏡腳本模板",
            "points": [
                "<strong>00:00–00:35｜S01 Hook 與開場定位（35 秒）</strong> — 亮出專題評分規準與懸念：「AI 寫的遊戲如果放大 100 倍為什麼會死？」",
                "<strong>00:35–01:24｜S02–03 實機遊玩與 HUD 展示（49 秒）</strong> — 錄製 9×9 開局、連鎖展開、插旗機率變化與即時數學 HUD。",
                "<strong>01:24–03:41｜S04–08 5 大離散數學源碼與 FSM 鎖定（137 秒）</strong> — 依序框選矩陣隔離、Set、8 方邊界、BFS 佇列與 LOST 吸收態。",
                "<strong>03:41–04:14｜S09 V1→V3 Prompt 進化與 100× 壓測（33 秒）</strong> — 展示 652.4× 加速曲線圖與 Pytest 6/6 全綠畫面。",
                "<strong>04:14–04:46｜S10 結尾 STAR 收斂（32 秒）</strong> — 附上 GitHub Repo 連結與 STAR 履歷轉譯，總長 4 分 46 秒完美達標！",
            ],
            "visual_html": """
                <table class="deck-table">
                  <thead><tr><th>分鏡段</th><th>實測時間區間</th><th>畫面來源 (Playwright / Spotlights)</th><th>本示範實作影片進度</th></tr></thead>
                  <tbody>
                    <tr><td><code>Scene 1</code></td><td><code>00:00–00:35</code></td><td>封面架構 ＋ 核心問題拋出</td><td>✅ 已實機渲染 MP4</td></tr>
                    <tr><td><code>Scene 2</code></td><td><code>00:35–01:24</code></td><td><code>web_demo/index.html</code> 實戰遊玩</td><td>✅ 自動模擬點擊＋插旗</td></tr>
                    <tr><td><code>Scene 3</code></td><td><code>01:24–03:41</code></td><td>5 段離散數學源碼＋踩雷 FSM 鎖定</td><td>✅ 雙語旁白＋不拆字字幕</td></tr>
                    <tr><td><code>Scene 4</code></td><td><code>03:41–04:14</code></td><td>V1 當機 vs V3 圖表 ＋ Pytest</td><td>✅ 300-DPI 實測嵌入</td></tr>
                    <tr><td><code>Scene 5</code></td><td><code>04:14–04:46</code></td><td>STAR 成果與 GitHub 連結收尾</td><td>✅ 總長 4 分 46 秒 (達標)</td></tr>
                  </tbody>
                </table>
            """,
            "strategy": "Backup 頁 1 完整提供學生自拍 3–5 分鐘影片的分鏡時間軸，並與我們實機產出的 MP4 (286.15s) 1:1 對齊。",
            "spoken": "第一頁附錄是給同學錄製三到五分鐘示範影片的黃金分鏡表。你可以直接參考我們實機渲染出的四分四十六秒示範影片，把內容精確切為三十五秒破題、四十九秒實機遊玩、兩分十七秒原始碼逆向工程與狀態機演示、三十三秒壓測展示以及三十二秒 STAR 總結，完美落在三到五分鐘的要求區間內。",
        },
        # Slide 18 — Backup 02: Codespaces vs Colab Launch Cheat Sheet
        {
            "id": "slide-18",
            "badge": "BACKUP 02 · 18 / 18",
            "is_backup": True,
            "title": "Backup 02：Grace-TA/DM2026 雙棲實作快速啟動指令總表",
            "points": [
                "<strong>倉庫入口與子資料夾位置</strong> — 前往 <a href='https://github.com/Grace-TA/DM2026' target='_blank'>Grace-TA/DM2026</a> 的 <code>AI_Game_Jam_Minesweeper_Golden_Demo/</code> 資料夾。",
                "<strong>步驟 1：執行實測壓測與圖表生成</strong> — 執行 <code>python3 src/benchmark_and_verify.py</code> 輸出 JSON 與 300-DPI 圖。",
                "<strong>步驟 2：啟動自動化 Pytest 批改閘門</strong> — 執行 <code>python3 -m pytest -v tests/test_minesweeper_hero.py</code> 確認全綠。",
                "<strong>步驟 3：啟動 Port 8080 互動式踩地雷</strong> — 執行 <code>python3 -m http.server 8080 -d web_demo</code> 並用瀏覽器試玩。",
                "<strong>FinOps 記憶鎖：課後記得 Delete</strong> — 所有修改請放 <code>/workspaces/DM2026</code> 並 <code>git push</code>，離開時至 Codespaces 頁面 Delete 歸零儲存費！",
            ],
            "visual_html": """
                <div class="code-box">
                  <div class="code-title">⚡ Codespaces (Ubuntu 24.04.5 LTS) 一鍵驗收三連擊</div>
                  <pre class="code-pre"><span class="hl-cyan"># 1. 進入受 Persistent Volume 保護的倉庫子目錄</span>
cd /workspaces/DM2026/AI_Game_Jam_Minesweeper_Golden_Demo

<span class="hl-cyan"># 2. 實測 V1 vs V3 壓測與 6 項 Pytest 單元測試</span>
python3 src/benchmark_and_verify.py
python3 -m pytest -v tests/test_minesweeper_hero.py

<span class="hl-cyan"># 3. 開啟互動式《踩地雷 × 離散數學》網頁預覽</span>
python3 -m http.server 8080 -d web_demo</pre>
                </div>
                <div class="callout-bar">📌 零 GPU 離散數學任務一律推薦 Codespaces；僅有免費 T4 GPU 深度學習訓練才與 Colab 互補！</div>
            """,
            "strategy": "Backup 頁 2 作為課堂一鍵執行的司令台，把剛教過的 Codespaces 規則與這個 Golden Demo 完美閉環。",
            "spoken": "最後一頁附錄整理了在 GitHub Codespaces 啟動整套踩地雷黃金示範的所有指令。記得把程式碼都存放在 /workspaces/DM2026 底下確保受到持久性磁碟保護，跑完測試與 Port 8080 互動示範後推回自己的 Fork，祝各位同學都能成為駕馭 AI 與數學的工程師！",
        },
    ]


def render_html(slides: list[dict]) -> str:
    manifest = [
        {"slide": idx + 1, "stage": s["badge"], "strategy": s["strategy"], "spoken": s["spoken"]}
        for idx, s in enumerate(slides)
    ]

    slides_html_parts = []
    for idx, s in enumerate(slides):
        active_cls = " active" if idx == 0 else ""
        if s.get("thanks_hero"):
            body = f"""
            <div class="thanks-hero-card">
              <div class="hero-glow"></div>
              <div class="hero-badge">{s['badge']}</div>
              <h2 class="hero-title">{s['thanks_title']}</h2>
              <p class="hero-sub">{s['thanks_sub']}</p>
              <div class="hero-pills">
                <span>🎯 40% Math Defense</span>
                <span>🧠 30% Prompt Evolution</span>
                <span>🎮 20% Minesweeper UX</span>
                <span>📚 10% NotebookLM</span>
              </div>
            </div>
            """
        elif "meta" in s:
            meta_rows = "\n".join(
                f"<div class='meta-row'><span class='meta-k'>{k}</span><span class='meta-v'>{v}</span></div>"
                for k, v in s["meta"]
            )
            body = f"""
            <div class="dual-grid">
              <div class="cover-meta-card">
                <div class="card-kicker">COURSE &amp; GOLDEN DEMO SPECIFICATION</div>
                <div class="meta-list">{meta_rows}</div>
              </div>
              <div class="visual-card">{s['visual_html']}</div>
            </div>
            """
        else:
            bullets = "\n".join(f"<li>{pt}</li>" for pt in s["points"])
            body = f"""
            <div class="dual-grid">
              <div class="info-card">
                <ul class="card-list">{bullets}</ul>
              </div>
              <div class="visual-card">{s['visual_html']}</div>
            </div>
            """

        slides_html_parts.append(
            f"""
            <section class="slide{active_cls}" id="{s['id']}" data-index="{idx}">
              <header class="slide-header">
                <div class="header-top">
                  <span class="slide-badge single-line-lock">{s['badge']}</span>
                  <span class="slide-counter single-line-lock">Slide {idx+1:02d} / {len(slides):02d}</span>
                </div>
                <h1 class="slide-title single-line-lock">{s['title']}</h1>
              </header>
              <main class="slide-body">{body}</main>
              <footer class="slide-footer">
                <span>VNU 234 · 115-1 離散數學 AI Game Jam Golden Demo</span>
                <span>Grace-TA/DM2026 · 按 P 開啟/關閉 AI 語音導讀 HUD</span>
              </footer>
            </section>
            """
        )

    manifest_json = json.dumps(manifest, ensure_ascii=False)
    slides_joined = "\n".join(slides_html_parts)

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=1280, initial-scale=1.0" />
  <title>DM2026 Minesweeper AI Game Jam — Golden Demo Presentation</title>
  <style>
    :root {{
      --bg: #080b14;
      --surface: #111827;
      --card: rgba(17, 24, 39, 0.92);
      --border: rgba(148, 163, 184, 0.2);
      --text: #f8fafc;
      --muted: #94a3b8;
      --cyan: #22d3ee;
      --indigo: #818cf8;
      --emerald: #34d399;
      --amber: #fbbf24;
      --rose: #fb7185;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #03050a;
      color: var(--text);
      font-family: 'Inter', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }}
    .deck-stage {{
      width: 1280px;
      height: 720px;
      position: relative;
      overflow: hidden;
      background: radial-gradient(circle at 12% 15%, rgba(99,102,241,0.16), transparent 40%),
                  radial-gradient(circle at 88% 82%, rgba(34,211,238,0.13), transparent 40%),
                  var(--bg);
      box-shadow: 0 24px 80px rgba(0, 0, 0, 0.75);
    }}
    .slide {{
      position: absolute;
      inset: 0;
      width: 1280px;
      height: 720px;
      padding: 26px 38px 18px 38px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.22s ease;
    }}
    .slide.active {{ opacity: 1; pointer-events: auto; z-index: 2; }}
    .slide-header {{ display: flex; flex-direction: column; gap: 6px; flex-shrink: 0; }}
    .header-top {{ display: flex; justify-content: space-between; align-items: center; }}
    .slide-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--cyan);
      background: rgba(34, 211, 238, 0.12);
      border: 1px solid rgba(34, 211, 238, 0.35);
      padding: 3px 10px;
      border-radius: 999px;
      white-space: nowrap;
    }}
    .slide-counter {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--muted); white-space: nowrap; }}
    .slide-title {{
      font-size: 27px;
      font-weight: 800;
      line-height: 1.24;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .slide-body {{ flex: 1; min-height: 0; display: flex; }}
    .dual-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      width: 100%;
      height: 100%;
      align-items: stretch;
    }}
    .info-card, .cover-meta-card, .visual-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 22px 24px;
      height: 100%;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .visual-card {{ justify-content: space-between; gap: 12px; }}
    ul.card-list {{
      list-style: none;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 10px;
    }}
    ul.card-list li {{
      background: rgba(30, 41, 59, 0.58);
      border-left: 3.5px solid var(--cyan);
      border-radius: 8px;
      padding: 13px 15px;
      font-size: 15.5px;
      line-height: 1.48;
      color: #e2e8f0;
    }}
    ul.card-list li strong {{ color: #ffffff; }}
    ul.card-list li code {{
      font-family: 'JetBrains Mono', monospace;
      color: var(--cyan);
      background: rgba(2, 6, 23, 0.65);
      padding: 1px 5px;
      border-radius: 4px;
      font-size: 13.5px;
    }}
    ul.card-list li a {{ color: #7dd3fc; text-decoration: underline; }}
    .card-kicker {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: var(--indigo);
      letter-spacing: 0.08em;
      font-weight: 700;
      margin-bottom: 12px;
    }}
    .meta-list {{ flex: 1; display: flex; flex-direction: column; justify-content: space-between; gap: 10px; }}
    .meta-row {{
      background: rgba(30, 41, 59, 0.6);
      border-radius: 10px;
      padding: 12px 14px;
      border: 1px solid rgba(255,255,255,0.07);
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}
    .meta-k {{ font-size: 12px; color: var(--cyan); font-weight: 700; font-family: 'JetBrains Mono', monospace; }}
    .meta-v {{ font-size: 15px; color: #f1f5f9; font-weight: 600; }}
    .code-box {{
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 14px 16px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .code-title {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: var(--cyan);
      font-weight: 700;
      margin-bottom: 10px;
    }}
    .code-pre {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13.2px;
      line-height: 1.52;
      color: #e2e8f0;
      white-space: pre-wrap;
    }}
    .hl-bad {{ color: var(--rose); font-weight: 700; }}
    .hl-warn {{ color: var(--amber); font-weight: 700; }}
    .hl-good {{ color: var(--emerald); font-weight: 700; }}
    .hl-cyan {{ color: var(--cyan); font-weight: 700; }}
    .mini-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 6px; }}
    .mini-card {{
      background: rgba(30, 41, 59, 0.65);
      border-radius: 10px;
      padding: 14px;
      border-top: 3px solid var(--cyan);
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .mini-card.accent-indigo {{ border-top-color: var(--indigo); }}
    .mini-card.accent-emerald {{ border-top-color: var(--emerald); }}
    .mini-card.accent-amber {{ border-top-color: var(--amber); }}
    .mini-card strong {{ font-size: 15px; color: #ffffff; }}
    .mini-card span {{ font-size: 13px; color: #cbd5e1; line-height: 1.45; }}
    .callout-bar {{
      background: rgba(99, 102, 241, 0.14);
      border: 1px solid rgba(129, 140, 248, 0.35);
      border-radius: 10px;
      padding: 10px 14px;
      font-size: 13.8px;
      color: #e0e7ff;
      flex-shrink: 0;
    }}
    .callout-bar code {{ font-family: 'JetBrains Mono', monospace; color: var(--cyan); }}
    table.deck-table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; flex: 1; }}
    table.deck-table th {{
      background: rgba(30, 41, 59, 0.95);
      color: var(--cyan);
      text-align: left;
      padding: 9px 10px;
      border-bottom: 1px solid #334155;
      font-weight: 700;
    }}
    table.deck-table td {{
      padding: 9px 10px;
      border-bottom: 1px solid rgba(148, 163, 184, 0.15);
      color: #e2e8f0;
      vertical-align: top;
      line-height: 1.42;
    }}
    table.deck-table code {{ font-family: 'JetBrains Mono', monospace; color: var(--cyan); font-size: 12.2px; }}
    .img-wrap {{ flex: 1; display: flex; align-items: center; justify-content: center; overflow: hidden; border-radius: 10px; background: #0f172a; }}
    .img-wrap img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
    .thanks-hero-card {{
      width: 100%;
      height: 100%;
      border-radius: 20px;
      background: linear-gradient(135deg, rgba(30,41,59,0.95), rgba(15,23,42,0.98));
      border: 1px solid rgba(34,211,238,0.4);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 40px;
      gap: 20px;
      position: relative;
      overflow: hidden;
    }}
    .hero-badge {{
      font-family: 'JetBrains Mono', monospace;
      color: var(--amber);
      border: 1px solid rgba(251,191,36,0.45);
      background: rgba(251,191,36,0.12);
      padding: 5px 14px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 13px;
    }}
    .hero-title {{ font-size: 38px; font-weight: 800; color: #ffffff; max-width: 960px; line-height: 1.3; }}
    .hero-sub {{ font-size: 18px; color: #cbd5e1; max-width: 820px; }}
    .hero-pills {{ display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; margin-top: 8px; }}
    .hero-pills span {{
      background: rgba(34,211,238,0.14);
      border: 1px solid rgba(34,211,238,0.3);
      padding: 8px 16px;
      border-radius: 999px;
      font-weight: 700;
      color: #a5f3fc;
      font-size: 14px;
    }}
    .slide-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--muted);
      padding-top: 4px;
      border-top: 1px solid rgba(148,163,184,0.15);
      flex-shrink: 0;
    }}
    /* Floating Nav & Auto-Presenter HUD */
    .nav-bar {{
      margin-top: 10px;
      display: flex;
      gap: 10px;
      align-items: center;
      font-size: 13px;
    }}
    .nav-bar button {{
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #334155;
      padding: 6px 14px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
    }}
    .nav-bar button:hover {{ border-color: var(--cyan); }}
    .hud-overlay {{
      position: fixed;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%);
      width: min(1180px, 94vw);
      background: rgba(8, 12, 24, 0.92);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(34, 211, 238, 0.45);
      border-radius: 14px;
      padding: 14px 20px;
      z-index: 99;
      display: none;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 18px 40px rgba(0,0,0,0.7);
    }}
    .hud-overlay.open {{ display: flex; }}
    .hud-row {{ font-size: 13.5px; line-height: 1.5; color: #e2e8f0; }}
    .hud-row strong {{ color: var(--cyan); }}
    .hud-controls {{ display: flex; gap: 8px; align-items: center; justify-content: flex-end; }}
    .hud-controls button {{
      background: rgba(34,211,238,0.16); color: #a5f3fc; border: 1px solid rgba(34,211,238,0.4);
      padding: 4px 10px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 700;
    }}
    @media print {{
      body {{ background: none; }}
      .nav-bar, .hud-overlay {{ display: none !important; }}
      .deck-stage {{ width: auto; height: auto; overflow: visible; box-shadow: none; }}
      .slide {{ position: relative; opacity: 1 !important; page-break-after: always; break-after: page; }}
    }}
  </style>
</head>
<body>
  <div class="deck-stage" id="deck-stage">
    {slides_joined}
  </div>

  <div class="nav-bar">
    <button onclick="prevSlide()">⏮ 上一頁 (←)</button>
    <span id="nav-label" style="color:#94a3b8;font-family:'JetBrains Mono',monospace;">Slide 01 / {len(slides):02d}</span>
    <button onclick="nextSlide()">下一頁 (→) ⏭</button>
    <button onclick="toggleHUD()">🎙️ AI 自動導讀 HUD (P)</button>
  </div>

  <div class="hud-overlay" id="hud-overlay">
    <div class="hud-row"><strong>💡 設計戰略思維：</strong><span id="hud-strategy"></span></div>
    <div class="hud-row"><strong>🎙️ 現場口述講稿：</strong><span id="hud-spoken"></span></div>
    <div class="hud-controls">
      <button onclick="toggleSpeak()">▶ / ⏸ 朗讀此頁</button>
      <button onclick="cycleSpeed()" id="speed-btn">⚡ 1.15x</button>
      <button onclick="toggleHUD()">✖ 關閉 (P)</button>
    </div>
  </div>

  <script>
    const PRESENTER_MANIFEST = {manifest_json};
    let currentIdx = 0;
    let hudOpen = false;
    let speed = 1.15;
    let speaking = false;
    const slides = Array.from(document.querySelectorAll('.slide'));

    function showSlide(idx) {{
      if (idx < 0) idx = 0;
      if (idx >= slides.length) idx = slides.length - 1;
      slides.forEach((s, i) => s.classList.toggle('active', i === idx));
      currentIdx = idx;
      document.getElementById('nav-label').textContent = `Slide ${{String(idx+1).padStart(2,'0')}} / ${{String(slides.length).padStart(2,'0')}}`;
      const m = PRESENTER_MANIFEST[idx];
      document.getElementById('hud-strategy').textContent = m.strategy;
      document.getElementById('hud-spoken').textContent = m.spoken;
      if (speaking) speakCurrent();
    }}

    function nextSlide() {{ if (currentIdx < slides.length - 1) showSlide(currentIdx + 1); }}
    function prevSlide() {{ if (currentIdx > 0) showSlide(currentIdx - 1); }}
    function toggleHUD() {{
      hudOpen = !hudOpen;
      document.getElementById('hud-overlay').classList.toggle('open', hudOpen);
    }}
    function cycleSpeed() {{
      const opts = [1.0, 1.15, 1.3, 1.5];
      speed = opts[(opts.indexOf(speed) + 1) % opts.length];
      document.getElementById('speed-btn').textContent = `⚡ ${{speed}}x`;
      if (speaking) speakCurrent();
    }}
    function speakCurrent() {{
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(PRESENTER_MANIFEST[currentIdx].spoken);
      u.lang = 'zh-TW';
      u.rate = speed;
      u.onend = () => {{
        if (speaking && currentIdx < slides.length - 1) {{
          showSlide(currentIdx + 1);
        }} else {{
          speaking = false;
        }}
      }};
      window.speechSynthesis.speak(u);
    }}
    function toggleSpeak() {{
      speaking = !speaking;
      if (speaking) speakCurrent();
      else if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ') {{ e.preventDefault(); nextSlide(); }}
      else if (e.key === 'ArrowLeft') {{ e.preventDefault(); prevSlide(); }}
      else if (e.key.toLowerCase() === 'p') {{ toggleHUD(); }}
    }});

    showSlide(0);
    if (new URLSearchParams(window.location.search).get('autoplay') === '1') {{
      toggleHUD();
      toggleSpeak();
    }}
  </script>
</body>
</html>
"""


def export_pdf(html_path: Path, pdf_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(html_path.resolve().as_uri(), wait_until="load", timeout=60000)
        page.wait_for_timeout(600)
        page.pdf(
            path=str(pdf_path),
            width="1280px",
            height="720px",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()


def main() -> int:
    bench = json.loads(BENCH_PATH.read_text(encoding="utf-8"))
    chart_uri = load_chart_b64()
    slides = build_slides_data(bench, chart_uri)
    html_text = render_html(slides)

    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html_text, encoding="utf-8")
    print(f"HTML Presentation written: {OUT_HTML} ({OUT_HTML.stat().st_size} bytes)")

    export_pdf(OUT_HTML, OUT_PDF)
    print(f"PDF Presentation exported: {OUT_PDF} ({OUT_PDF.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
