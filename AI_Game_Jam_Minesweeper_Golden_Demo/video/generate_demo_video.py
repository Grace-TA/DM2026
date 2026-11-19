#!/usr/bin/env python3
"""
generate_demo_video.py — 3–5 Minute 1080p MP4 Golden Demo Video Synthesizer
===========================================================================
Generates a broadcast-grade ~4-minute (220–270s) 1080p MP4 Demo Video modeling how a
2-student AI Game Jam team presents Minesweeper x Discrete Math:
  - Captures LIVE interactive gameplay states from web_demo/index.html via Playwright
  - Renders 1920x1080 spotlight visual slides + real 300-DPI benchmark chart
  - Synthesizes dual-speaker Copilot Neural narration (Andrew & Ava) via Edge-TTS
  - Burns aligned Traditional Chinese SRT subtitles + Phase V broadcast EQ via FFmpeg

Output MP4: ../../DM2026_Golden_Demo_Media/Minesweeper_Golden_Demo_Video_1080p.mp4
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts
from playwright.sync_api import sync_playwright

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = ROOT.parent.parent
BENCH_PATH = ROOT / "benchmarks" / "benchmark_results.json"
CHART_PATH = ROOT / "assets" / "complexity_v1_vs_v3.png"
WEB_DEMO_HTML = ROOT / "web_demo" / "index.html"
SRT_OUT = ROOT / "video" / "subtitles.srt"
MEDIA_DIR = WORKSPACE_ROOT / "DM2026_Golden_Demo_Media"
MP4_OUT = MEDIA_DIR / "Minesweeper_Golden_Demo_Video_1080p.mp4"

VOICE_ANDREW = "en-US-AndrewMultilingualNeural"
VOICE_AVA = "en-US-AvaMultilingualNeural"


def build_scenes(bench: dict) -> list[dict]:
    l100 = bench["lookup_scaling"][-1]
    f100 = bench["flood_fill_survival"][-1]
    f60 = bench["flood_fill_survival"][-2]
    return [
        {
            "id": "S01",
            "speaker": "Andrew",
            "voice": VOICE_ANDREW,
            "kicker": "SCENE 01 · HOOK & CORE PHILOSOPHY",
            "title": "離散數學《踩地雷》AI Game Jam Golden Demo",
            "subtitle": "程式碼可以是 AI 寫的，但離散數學邏輯必須是你的！",
            "mode": "card",
            "code": """# 115-1 VNU 234 · AI Game Jam 評分標準 (總分 110%)
1. 離散數學連結度 (Discrete Math Connection)  : 40% ★ 核心
2. AI 詠唱工程與重構 (Prompt Evolution)      : 30%
3. 遊戲完整度與 UX (FSM & Live Demo)         : 20%
4. NotebookLM 雙來源備戰與創新               : 10%

❓ 核心懸念：AI 5秒寫出的《踩地雷》，如果明天盤面放大 100 倍會發生什麼事？""",
            "narration": (
                "大家好，歡迎來到一百一十五學年度離散數學 AI Game Jam 期末專題的 Golden Demo 示範影片。"
                "我是負責架構與數學防禦戰的 Andrew，等一下由 Ava 帶大家實機演示。"
                "這門課最核心的精神是：程式碼可以是 AI 寫的，但離散數學的邏輯與防呆邊界永遠屬於你。"
                "在接下來的四分鐘裡，我們將從實機操作出發，逆向工程踩地雷背後的五大離散數學支柱，並實測當盤面放大一百倍時，為什麼沒有數學約束的 AI 程式碼會當場崩潰。"
            ),
        },
        {
            "id": "S02",
            "speaker": "Ava",
            "voice": VOICE_AVA,
            "kicker": "SCENE 02 · LIVE GAMEPLAY & MATH HUD",
            "title": "雙棲互動展示：Codespaces Port 8080 實機開局",
            "subtitle": "左欄玩遊戲，右欄即時監控集合基數 |M|、條件機率與 FSM 狀態",
            "mode": "web_init",
            "narration": (
                "大家好，我是 Ava。為了讓評審一目了然遊戲跟數學的關係，我們除了提供 Google Colab 筆記本，"
                "更在 GitHub Codespaces 透過 Port 8080 啟動了這個互動式網頁沙盒。"
                "現在看到的是九乘九、十顆地雷的初始盤面。"
                "右邊的即時數學監控面板馬上算出：地雷集合基數為 10，總共有一點八八兆種合法佈局，第一手盲點的存活安全率精確為百分之八十七點六五。"
            ),
        },
        {
            "id": "S03",
            "speaker": "Ava",
            "voice": VOICE_AVA,
            "kicker": "SCENE 03 · BFS FLOOD FILL & CONDITIONAL PROBABILITY",
            "title": "實機連鎖展開與條件機率動態更新",
            "subtitle": "點開零雷區觸發 BFS 水波紋擴散，右鍵插旗即時重算未知風險",
            "mode": "web_play",
            "narration": (
                "現在我按下自動示範鍵，系統點開了一顆零雷空白格，瞬間透過迭代式 BFS 佇列連鎖展開了整片安全區域，"
                "同時我們開啟旗標模式，在未知格插上一面紅色旗幟。"
                "注意看右上角，剩餘安全格與盲點踩雷率立刻依據無放回條件機率重新計算，"
                "底部的 Trace 紀錄區也會同步印出 Mark-on-Enqueue 展開的精確格子數量與時間複雜度指標。"
            ),
        },
        {
            "id": "S04",
            "speaker": "Andrew",
            "voice": VOICE_ANDREW,
            "kicker": "SCENE 04 · MATH PILLAR 1 (LAB 1–2)",
            "title": "支柱一：笛卡兒積網格與破除淺拷貝污染陷阱",
            "subtitle": "為何 AI 初版寫的 [[0]*cols]*rows 是嚴重記憶體地雷？",
            "mode": "card",
            "code": """# ❌ V1 AI 初版 (淺拷貝連坐污染 Bug)
self.logic_board = [[0] * cols] * rows
v1.logic_board[0][0] = 99
assert v1.logic_board[1][0] == 99   # 改第 0 列，第 1~8 列全部一起變！

# ✅ V3 Hero (Lab 1–2 列表推導式：每列獨立配置記憶體)
self.logic_board = [[0 for _ in range(cols)] for _ in range(rows)]
assert len({id(row) for row in self.logic_board}) == rows  # PASS""",
            "narration": (
                "進入核心的數學防禦戰，我們逆向工程指出五大離散數學支柱。"
                "第一支柱來自 Lab 1 與 Lab 2 的笛卡兒積網格與矩陣。"
                "不加約束直接請 AI 寫二維陣列時，它常偷懶寫出中括號零乘以寬再乘以高。"
                "這會讓所有列指向同一個記憶體位址，改第零列就等於污染整張地圖。"
                "我們在 V3 改用雙層列表推導式建立獨立列物件，並寫上 id 唯一性斷言徹底根除這個 Bug。"
            ),
        },
        {
            "id": "S05",
            "speaker": "Ava",
            "voice": VOICE_AVA,
            "kicker": "SCENE 05 · MATH PILLAR 2 (LAB 3 & LAB 5)",
            "title": "支柱二：Set 集合無碰撞佈雷與組合樣本空間",
            "subtitle": "以 rng.sample() 取代亂數迴圈，O(1) 雜湊查表消滅 O(N²) 延遲",
            "mode": "card",
            "code": """# ❌ V1: randint 重複碰撞 + List 線性掃描 O(N*M)
while len(self.mines_list) < self.num_mines:
    if (r, c) not in self.mines_list: ...

# ✅ V3: Lab 3 & 5 無放回抽樣 + Hash Set (O(1) 查雷)
all_cells = [(r, c) for r in range(rows) for c in range(cols)]
self.mines = set(self.rng.sample(all_cells, self.num_mines))
# 9x9 共 C(81, 10) = 1,878,392,407,320 種合法盤面，嚴格保證 |M| == 10""",
            "narration": (
                "第二支柱結合了 Lab 3 的集合論與 Lab 5 的組合機率。"
                "如果用傳統亂數搭配 List 檢查重複，當盤面放大到一萬格、地雷數來到兩千五百顆時，每次查詢都要從頭線性掃描，"
                "時間複雜度會惡化成平方級數。"
                "我們在 V3 改用 random.sample 搭配 Python Set 雜湊集合，單次線性時間就能嚴格保證集合基數等於地雷總數，查詢速度也保持在常數級。"
            ),
        },
        {
            "id": "S06",
            "speaker": "Andrew",
            "voice": VOICE_ANDREW,
            "kicker": "SCENE 06 · MATH PILLAR 3 (LAB 4)",
            "title": "支柱三：八方二元關係 R8 與負索引幽靈防禦",
            "subtitle": "封殺 Python board[-1][-1] 不報錯卻偷讀右下角的隱形 Bug",
            "mode": "card",
            "code": """# Lab 4: 8-Neighbor Binary Relation R_8 ⊆ Q × Q
DIRECTIONS_8 = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def is_valid(self, r: int, c: int) -> bool:
    # 閉區間雙邊界守衛：拒絕 Python 負索引靜默環繞讀取！
    return 0 <= r < self.rows and 0 <= c < self.cols

def get_neighbors(self, r: int, c: int):
    return [(r+dr, c+dc) for dr, dc in self.DIRECTIONS_8 if self.is_valid(r+dr, c+dc)]""",
            "narration": (
                "第三支柱對應 Lab 4 的八方二元關係。"
                "在 Python 裡寫二維網格最容易踩到一個恐怖陷阱：當座標計算出負一的時候，程式不會報錯，"
                "反而會利用負索引機制去偷讀最底列與最右欄的資料，導致計算周圍地雷數完全算錯。"
                "因此我們在 get_neighbors 強制掛上雙閉區間邊界守衛，確保角落點度數嚴格等於三、邊緣點等於五、內部點等於八。"
            ),
        },
        {
            "id": "S07",
            "speaker": "Ava",
            "voice": VOICE_AVA,
            "kicker": "SCENE 07 · MATH PILLAR 4 (LAB 6–8)",
            "title": "支柱四：圖連通分量與迭代 BFS Mark-on-Enqueue",
            "subtitle": "消滅遞迴 RecursionError，將連鎖展開複雜度鎖死在 O(V + E)",
            "mode": "card",
            "code": """# Lab 6–8: collections.deque 迭代展開 + 入隊立即標記 (Mark-on-Enqueue)
frontier = deque([(r, c)])
seen_local = {(r, c)}  # 不等 pop 出來才標記，徹底防止同一節點重複入隊！

while frontier:
    cr, cc = frontier.popleft()
    self.revealed.add((cr, cc))
    if self.logic_board[cr][cc] == 0:
        for nr, nc in self.get_neighbors(cr, cc):
            if (nr, nc) not in self.revealed and (nr, nc) not in seen_local:
                seen_local.add((nr, nc))
                frontier.append((nr, nc))""",
            "narration": (
                "第四支柱是整個演算法的核心：Lab 6 到 Lab 8 的圖論連通塊與廣度優先搜尋。"
                "AI 初版寫的遞迴 DFS 只要遇到超過一千格的空白安全區，就會撞上 Python 呼叫堆疊上限而當機。"
                "我們將它重構為 collections.deque 的迭代式佇列，"
                "並且堅持在鄰居進佇列的瞬間就寫入 seen_local 集合，避免重複入隊造成指數級膨脹，讓時間複雜度嚴格維持在線性的 O(V+E)。"
            ),
        },
        {
            "id": "S08",
            "speaker": "Andrew",
            "voice": VOICE_ANDREW,
            "kicker": "SCENE 08 · MATH PILLAR 5 (LAB 9)",
            "title": "支柱五：有限狀態機 (FSM) 與不可逆吸收態鎖定",
            "subtitle": "踩雷進入 LOST 吸收態後，任何非法點擊全部在函式入口遭攔截",
            "mode": "web_lost",
            "narration": (
                "第五支柱來自 Lab 9 的有限狀態機。"
                "請看實機畫面：當玩家不幸點到地雷時，系統狀態從 PLAYING 不可逆地轉移到 LOST。"
                "此時如果我再嘗試點擊棋盤上任何其他安全格，底部的追蹤列馬上跳出紅字攔截警告。"
                "因為我們把 WON 與 LOST 設計成數學上的吸收態，所有異動函式第一行都會檢查狀態，徹底杜絕死後繼續點擊刷分的外掛漏洞。"
            ),
        },
        {
            "id": "S09",
            "speaker": "Ava",
            "voice": VOICE_AVA,
            "kicker": "SCENE 09 · PROMPT EVOLUTION & 100X BENCHMARK PROOF",
            "title": f"Prompt 進化實測：V1 崩潰 vs V3 實現 {l100['speedup_x']} 倍查詢加速",
            "subtitle": (
                f"100×100 (10,000 格) V1 {f100['v1_status']}，"
                f"V3 僅 {f100['v3_ms']:.2f}ms 完成且 Pytest 6/6 全綠"
            ),
            "mode": "chart",
            "pytest_strip": (
                "✅ pytest -v tests/test_minesweeper_hero.py  ──▶  "
                f"6 passed (<1s)  |  seed=42 Equivalence Gate: PASS  |  100×100 BFS: {f100['v3_ms']:.2f}ms"
            ),
            "narration": (
                "最後來看看 Prompt 進化前後的真實壓測證據。"
                "我們把 AI 初版 V1 跟以五大數學契約約束重構的 V3，從九乘九一路放大到一百乘一百，也就是一萬格的大盤面進行對決。"
                f"從實測圖表可以看到，右邊的 V1 遞迴在六十乘六十就已經徹底當機，而 V3 僅花 {f100['v3_ms']:.2f} 毫秒就安全展開一萬格"
                f"（在六十乘六十也僅需 {f60['v3_ms']:.2f} 毫秒）。"
                f"左邊的對數曲線更證明，Hash Set 查詢比 List 掃描快了整整 {l100['speedup_x']} 倍，而且六項 Pytest 自動化單元測試在一秒內全部綠燈通過。"
            ),
        },
        {
            "id": "S10",
            "speaker": "Andrew",
            "voice": VOICE_ANDREW,
            "kicker": "SCENE 10 · SOCRATIC DEFENSE & STAR TAKEAWAY",
            "title": "從期末報告到科技業實習履歷：你的 STAR 代表作",
            "subtitle": "完整代碼、簡報與一鍵重現腳本已收錄於 Grace-TA/DM2026",
            "mode": "card",
            "code": f"""# 🌟 帶得走的 STAR 工程敘事 & Grace-TA/DM2026 快速入口
• [S/T] 診斷生成式 AI 棋盤原型於百倍擴展時的淺拷貝、O(N²) 與爆棧危機
• [A]   導入 5 大離散數學契約 + seed=42 等價對拍 + 6 項 Pytest 自動化閘門
• [R]   100×100 查表加速 {l100['speedup_x']}x ({l100['v1_list_scan_ms']:.2f}ms → {l100['v3_set_hash_ms']:.2f}ms)，BFS {f100['v3_ms']:.2f}ms 零爆棧

🚀 GitHub Repo: https://github.com/Grace-TA/DM2026
📂 Subfolder  : AI_Game_Jam_Minesweeper_Golden_Demo/""",
            "narration": (
                "這就是我們為大家準備的離散數學踩地雷 Golden Demo。"
                "只要按照這個結構準備：先錄製三到五分鐘的實機與代碼講解影片，接著用十分鐘守住五大數學支柱，"
                "再用五分鐘秀出 V1 到 V3 的壓測加速對比，最後把這份量化成果寫成求職用的 STAR 履歷故事。"
                "所有原始碼、網頁沙盒與十八頁簡報都已經上傳到 Grace-TA 的 DM2026 倉庫。祝大家期末 Demo Day 順利拿下高分，謝謝大家！"
            ),
        },
    ]


def render_spotlight_html(scene: dict, chart_b64: str) -> str:
    body_block = ""
    if scene["mode"] == "chart":
        strip = scene.get(
            "pytest_strip",
            "✅ pytest -v tests/test_minesweeper_hero.py  ──▶  6 passed (<1s)  |  seed=42 Equivalence Gate: PASS",
        )
        body_block = f"""
        <div class="chart-wrap">
          <img src="{chart_b64}" alt="Benchmark Chart" />
          <div class="pytest-strip">{strip}</div>
        </div>
        """
    else:
        escaped = (
            scene["code"]
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )
        body_block = f"""
        <div class="code-card">
          <div class="code-dots"><span></span><span></span><span></span><code>DM2026 / AI_Game_Jam_Minesweeper_Golden_Demo</code></div>
          <pre>{escaped}</pre>
        </div>
        """

    speaker_badge = "🎙️ Speaker A · Andrew (Math & Arch)" if scene["speaker"] == "Andrew" else "🎙️ Speaker B · Ava (Live & Benchmark)"
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: 1920px; height: 1080px; overflow: hidden;
      background: radial-gradient(circle at 12% 18%, rgba(99,102,241,0.22), transparent 38%),
                  radial-gradient(circle at 86% 80%, rgba(34,211,238,0.16), transparent 40%),
                  #070a12;
      color: #f8fafc;
      font-family: 'Inter', 'Microsoft JhengHei', 'Noto Sans TC', sans-serif;
      padding: 46px 86px 132px 86px;
      display: flex; flex-direction: column; justify-content: space-between;
    }}
    .top-bar {{ display: flex; justify-content: space-between; align-items: center; }}
    .kicker {{
      font-family: 'JetBrains Mono', monospace; font-size: 22px; font-weight: 700;
      color: #22d3ee; background: rgba(34,211,238,0.12);
      border: 1px solid rgba(34,211,238,0.4); padding: 8px 20px; border-radius: 999px;
    }}
    .speaker {{
      font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700;
      color: #fde68a; background: rgba(245,158,11,0.14);
      border: 1px solid rgba(245,158,11,0.4); padding: 8px 20px; border-radius: 999px;
    }}
    .title-block {{ margin-top: 16px; margin-bottom: 16px; }}
    h1 {{ font-size: 50px; font-weight: 800; line-height: 1.2; color: #ffffff; }}
    .sub {{ font-size: 26px; color: #94a3b8; margin-top: 8px; font-weight: 600; }}
    .code-card {{
      flex: 1; background: #020617; border: 1.5px solid #334155; border-radius: 22px;
      padding: 26px 36px; display: flex; flex-direction: column; justify-content: center;
      box-shadow: 0 24px 64px rgba(0,0,0,0.65);
    }}
    .code-dots {{
      display: flex; align-items: center; gap: 10px; margin-bottom: 20px;
      padding-bottom: 12px; border-bottom: 1px solid #1e293b;
    }}
    .code-dots span {{ width: 14px; height: 14px; border-radius: 50%; background: #475569; }}
    .code-dots span:nth-child(1) {{ background: #f43f5e; }}
    .code-dots span:nth-child(2) {{ background: #fbbf24; }}
    .code-dots span:nth-child(3) {{ background: #10b981; }}
    .code-dots code {{ margin-left: 12px; font-family: 'JetBrains Mono', monospace; font-size: 20px; color: #94a3b8; }}
    pre {{
      font-family: 'JetBrains Mono', 'Consolas', monospace;
      font-size: 26px; line-height: 1.54; color: #e2e8f0; white-space: pre-wrap;
    }}
    .chart-wrap {{
      flex: 1; min-height: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px;
      background: #0f172a; border: 1.5px solid #334155; border-radius: 22px; padding: 14px 20px;
    }}
    .chart-wrap img {{ max-width: 100%; max-height: 540px; object-fit: contain; }}
    .pytest-strip {{
      font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700;
      color: #6ee7b7; background: rgba(16,185,129,0.14); border: 1px solid rgba(16,185,129,0.4);
      padding: 8px 22px; border-radius: 12px;
    }}
  </style>
</head>
<body>
  <div>
    <div class="top-bar">
      <span class="kicker">{scene['kicker']}</span>
      <span class="speaker">{speaker_badge}</span>
    </div>
    <div class="title-block">
      <h1>{scene['title']}</h1>
      <div class="sub">{scene['subtitle']}</div>
    </div>
  </div>
  {body_block}
</body>
</html>"""


def capture_visual_frames(scenes: list[dict], work_dir: Path, chart_b64: str) -> dict[str, Path]:
    """Capture 1920x1080 PNG frames for all 10 scenes (including live web_demo captures)."""
    frames: dict[str, Path] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        # 1. Capture live interactive Minesweeper web_demo states
        page.goto(WEB_DEMO_HTML.resolve().as_uri(), wait_until="load", timeout=30000)
        page.wait_for_timeout(800)
        page.evaluate("document.body.style.zoom = '0.86'; document.body.style.paddingBottom = '90px';")

        # S02: Initial 9x9 state
        p_s02 = work_dir / "S02.png"
        page.screenshot(path=str(p_s02))
        frames["S02"] = p_s02

        # S03: Trigger autoDemoStep (BFS flood fill) + toggle flag + flag a cell
        page.click("text=⚡ 自動示範 BFS")
        page.wait_for_timeout(450)
        page.click("#btn-flag")
        page.wait_for_timeout(200)
        # Click first unrevealed cell to plant a flag cleanly
        unrevealed = page.locator(".cell:not(.revealed)").first
        if unrevealed.count() > 0:
            unrevealed.click()
        page.wait_for_timeout(350)
        p_s03 = work_dir / "S03.png"
        page.screenshot(path=str(p_s03))
        frames["S03"] = p_s03

        # S08: Trigger LOST absorbing state directly via page.evaluate for deterministic BOOM frame
        page.evaluate("""() => {
            if (flagMode) toggleFlagMode();
            const firstMine = Array.from(mines)[0].split(',').map(Number);
            revealCell(firstMine[0], firstMine[1]);
            // Attempt another click to trigger FSM absorbing state guard message
            for (let r = 0; r < H; r++) {
                for (let c = 0; c < W; c++) {
                    if (!mines.has(key(r,c)) && !revealed.has(key(r,c))) {
                        revealCell(r, c);
                        return;
                    }
                }
            }
        }""")
        page.wait_for_timeout(450)
        p_s08 = work_dir / "S08.png"
        page.screenshot(path=str(p_s08))
        frames["S08"] = p_s08

        # 2. Capture all Spotlight Card / Chart frames
        for sc in scenes:
            if sc["id"] in frames:
                continue
            html_str = render_spotlight_html(sc, chart_b64)
            tmp_html = work_dir / f"{sc['id']}.html"
            tmp_html.write_text(html_str, encoding="utf-8")
            page.goto(tmp_html.resolve().as_uri(), wait_until="load", timeout=30000)
            page.wait_for_timeout(300)
            out_png = work_dir / f"{sc['id']}.png"
            page.screenshot(path=str(out_png))
            frames[sc["id"]] = out_png

        browser.close()
    return frames


async def synthesize_all_audio(scenes: list[dict], work_dir: Path) -> dict[str, Path]:
    """Synthesize MP3 narration per scene using Edge-TTS with Semaphore(3)."""
    sem = asyncio.Semaphore(3)
    audio_paths: dict[str, Path] = {}

    async def synth_one(sc: dict) -> None:
        out_mp3 = work_dir / f"{sc['id']}.mp3"
        async with sem:
            for attempt in range(3):
                try:
                    comm = edge_tts.Communicate(sc["narration"], sc["voice"], rate="+26%")
                    await comm.save(str(out_mp3))
                    audio_paths[sc["id"]] = out_mp3
                    return
                except Exception as exc:
                    if attempt == 2:
                        raise RuntimeError(f"Edge-TTS failed for {sc['id']}: {exc}") from exc
                    await asyncio.sleep(1.5 * (attempt + 1))

    await asyncio.gather(*(synth_one(sc) for sc in scenes))
    return audio_paths


def probe_duration(path: Path) -> float:
    import re
    res = subprocess.run(
        ["ffmpeg", "-i", str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
        check=False,
    )
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", res.stderr or "")
    if not m:
        raise RuntimeError(f"Could not parse duration from ffmpeg output for {path}")
    hh, mm, ss = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return hh * 3600.0 + mm * 60.0 + ss


def fmt_srt_time(sec: float) -> str:
    ms = int(round((sec - int(sec)) * 1000))
    total = int(sec)
    if ms >= 1000:
        ms -= 1000
        total += 1
    hh = total // 3600
    mm = (total % 3600) // 60
    ss = total % 60
    return f"{hh:02d}:{mm:02d}:{ss:02d},{ms:03d}"


def split_caption_chunks(text: str, max_chars: int = 34) -> list[str]:
    """Split Chinese/English narration cleanly without breaking ASCII words mid-token."""
    import re
    raw_clauses = [c.strip() for c in re.split(r"(?<=[。！？，；：])", text) if c.strip()]
    chunks: list[str] = []
    cur = ""
    for cl in raw_clauses:
        if len(cur) + len(cl) <= max_chars:
            cur += cl
        else:
            if cur:
                chunks.append(cur)
            if len(cl) > max_chars:
                tokens = re.findall(r"[A-Za-z0-9_.\-+/%]+|\s+|.", cl)
                sub = ""
                for tok in tokens:
                    if sub and len(sub) + len(tok) > max_chars:
                        if sub.strip():
                            chunks.append(sub.strip())
                        sub = tok.lstrip()
                    else:
                        sub += tok
                if sub.strip():
                    chunks.append(sub.strip())
                cur = ""
            else:
                cur = cl
    if cur:
        chunks.append(cur)
    return chunks


def build_srt(scenes: list[dict], durations: dict[str, float], srt_path: Path) -> None:
    lines: list[str] = []
    idx = 1
    cursor = 0.0
    for sc in scenes:
        dur = durations[sc["id"]]
        chunks = split_caption_chunks(sc["narration"], max_chars=34)
        total_chars = max(1, sum(len(c) for c in chunks))
        speak_dur = max(0.5, dur - 0.35)
        t_ptr = cursor
        for c in chunks:
            seg = speak_dur * (len(c) / total_chars)
            t_end = min(cursor + dur - 0.05, t_ptr + seg)
            lines.append(f"{idx}")
            lines.append(f"{fmt_srt_time(t_ptr)} --> {fmt_srt_time(t_end)}")
            lines.append(c)
            lines.append("")
            idx += 1
            t_ptr = t_end
        cursor += dur
    srt_path.write_text("\n".join(lines), encoding="utf-8")


def assemble_video(
    scenes: list[dict],
    frames: dict[str, Path],
    audios: dict[str, Path],
    durations: dict[str, float],
    srt_path: Path,
    work_dir: Path,
    mp4_out: Path,
) -> None:
    mp4_out.parent.mkdir(parents=True, exist_ok=True)
    seg_list_file = work_dir / "segments.txt"
    seg_entries: list[str] = []

    for sc in scenes:
        sid = sc["id"]
        png = frames[sid]
        mp3 = audios[sid]
        dur = durations[sid]
        seg_mp4 = work_dir / f"{sid}_seg.mp4"

        # Encode still 1080p frame + broadcast EQ audio padded to exact dur
        cmd = [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-framerate",
            "30",
            "-i",
            str(png),
            "-i",
            str(mp3),
            "-t",
            f"{dur:.3f}",
            "-af",
            "highpass=f=75,equalizer=f=180:width_type=o:width=1:g=2,equalizer=f=3500:width_type=o:width=1:g=1.5,acompressor=threshold=-18dB:ratio=2.2,apad",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-pix_fmt",
            "yuv420p",
            "-r",
            "30",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-ar",
            "48000",
            "-shortest",
            str(seg_mp4),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        seg_entries.append(f"file '{seg_mp4.as_posix()}'")

    seg_list_file.write_text("\n".join(seg_entries), encoding="utf-8")
    raw_concat = work_dir / "concat_raw.mp4"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(seg_list_file),
            "-c",
            "copy",
            str(raw_concat),
        ],
        check=True,
        capture_output=True,
    )

    # Burn crisp subtitles from work_dir copy (avoid Windows colon escaping issues)
    local_srt = work_dir / "subs.srt"
    shutil.copy2(srt_path, local_srt)
    vf_sub = "subtitles=subs.srt:force_style='FontName=Microsoft JhengHei,FontSize=17,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H80000000,BorderStyle=1,Outline=2,Shadow=1,MarginV=20'"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(raw_concat),
            "-vf",
            vf_sub,
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "copy",
            "-movflags",
            "+faststart",
            str(mp4_out),
        ],
        cwd=str(work_dir),
        check=True,
        capture_output=True,
    )


def main() -> int:
    bench = json.loads(BENCH_PATH.read_text(encoding="utf-8"))
    chart_b64 = "data:image/png;base64," + base64.b64encode(CHART_PATH.read_bytes()).decode("ascii")
    scenes = build_scenes(bench)

    with tempfile.TemporaryDirectory(prefix="dm2026_vid_") as tmp:
        work_dir = Path(tmp)
        print("1/4 Capturing 1080p live gameplay & spotlight frames...")
        frames = capture_visual_frames(scenes, work_dir, chart_b64)

        print("2/4 Synthesizing Edge-TTS dual-copilot narration (Andrew & Ava)...")
        audios = asyncio.run(synthesize_all_audio(scenes, work_dir))

        durations: dict[str, float] = {}
        total_sec = 0.0
        for sc in scenes:
            d = probe_duration(audios[sc["id"]]) + 0.25
            durations[sc["id"]] = d
            total_sec += d
            print(f"   - {sc['id']} ({sc['speaker']}): {d:.2f}s")

        print(f"3/4 Building aligned subtitles.srt (Total target duration: {total_sec:.2f}s = {total_sec/60:.2f} min)...")
        build_srt(scenes, durations, SRT_OUT)

        print("4/4 Rendering 1080p H.264 MP4 with Phase V broadcast EQ & burned-in subtitles...")
        assemble_video(scenes, frames, audios, durations, SRT_OUT, work_dir, MP4_OUT)

    final_dur = probe_duration(MP4_OUT)
    size_mb = MP4_OUT.stat().st_size / (1024 * 1024)
    print(f"DONE! Video: {MP4_OUT} | Duration: {final_dur:.2f}s ({final_dur/60:.2f} min) | Size: {size_mb:.2f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
