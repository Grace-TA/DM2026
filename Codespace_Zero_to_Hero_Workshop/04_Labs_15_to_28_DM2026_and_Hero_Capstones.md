# Book 4：DM2026 離散數學雲端實戰與英雄專題（Labs 15–28）

> **Course Context**: 115學年第1學期 離散數學（Discrete Mathematics）— `https://github.com/Grace-TA/DM2026`  
> **Workshop Topology**: 學生端採用 **個人 Fork + `2-core` Codespace**（每月免費額度 120 core-hours ≈ 60 小時雙核運行）；講師端使用 **Southeast Asia `4-core • 16GB RAM • 32GB` Codespace**（[`fantastic-dollop`](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)）進行 Live Demo。  
> **Pedagogical Framework**: L.A.W. Engine（量化目標與 IF-THEN 通過門檻）× Bloom's Taxonomy（L3 Apply → L6 Create）× DIKW Metallurgy（從 Colab 單檔礦石鍛造為模組化雲端遺產）。

---

## 🗺️ Book 4 總覽與課程對齊矩陣（Curriculum Alignment Matrix）

| Cycle | Lab | 主題與核心技能 | 對應 `DM2026` 原始單元 | 難度 | Bloom's | 權重 |
|:-----:|:---:|:---------------|:-----------------------|:----:|:-------:|:----:|
| 4/5 | Lab 15 | Colab 遷移至 Codespaces `.ipynb` 與 `calendar` 模組 | `WEEK01.md` & `WEEK02 #1` | ★☆☆ | L3 Apply | 5% |
| 4/5 | Lab 16 | 修復縮排錯誤（實作 1135）與命題邏輯真值表 CLI（實作 1140） | `WEEK02 #2, #3, #4` | ★★☆ | L4 Analyze | 7% |
| 4/5 | Lab 17 | 字串清洗管線（實作 1160）與 `enumerate()` 離散索引（實作 1171） | `WEEK02 #5, #6, #7` | ★★☆ | L3 Apply | 6% |
| 4/5 | Lab 18 | VS Code 斷點除錯器透視切片步進（實作 1175）與 9×9 巢狀迴圈 | `WEEK02 #8, #9, #10` | ★★☆ | L4 Analyze | 7% |
| 5/6 | Lab 19 | 集合論與 Set Comprehension：交/聯/差集與冪集生成器 | `WEEK03 #01, #03, #06` | ★★☆ | L4 Analyze | 8% |
| 5/6 | Lab 20 | 函式、字典與 `try-except`：離散關係（自反/對稱/遞移）檢測器 | `WEEK03 #04, #05, #07, #08` | ★★☆ | L5 Evaluate | 8% |
| 5/6 | Lab 21 | 物件導向（OOP）重構：多檔案 `discrete_toolkit/` 套件架構 | `WEEK03 #09` | ★★★ | L6 Create | 9% |
| 5/6 | Lab 22 | Matplotlib & NumPy 無頭繪圖：4 相位三角波與等比例單位圓 PNG | `WEEK03 #10, #11, #12` | ★★☆ | L3 Apply | 7% |
| 6 | Lab 23 | 離散數學互動展示站：Python 生成 HTML/SVG 溫氏圖與 Port 8080 轉發 | 集合論視覺化延伸 | ★★★ | L6 Create | 8% |
| 6 | Lab 24 | 神經符號自動化批改閘門：用 `pytest` 取代人工截圖對帳 | 全課程單元驗證 | ★★★ | L5 Evaluate | 9% |
| 6 | Lab 25 | 客製化 `DM2026` Dockerfile 與 Prebuild 預先編譯加速策略 | Codespaces 容器工程 | ★★★ | L5 Evaluate | 6% |
| 6 | Lab 26 | Codespaces 內建 Copilot / AI Agent 輔助除錯與時間複雜度重構 | `WEEK03` 演算法優化 | ★★☆ | L4 Analyze | 6% |
| 6 | Lab 27 | 多人協作與 PR 閉環：個人 Fork 發起 Pull Request 至 `Grace-TA/DM2026` | GitHub 團隊協作 | ★★★ | L5 Evaluate | 7% |
| 6 | Lab 28 | 終極 Hero Capstone：DM2026 雲端離散數學實驗室＋配額清零歸位儀式 | `WEEK01–03` 總整合 | ★★★ | L6 Create | 7% |

---

# Cycle 4/5：Colab 至 Codespaces 遷移（`DM2026` `WEEK01`–`WEEK02`）

## Lab 15：從 `WEEK01.md` Colab 遷移至 Codespaces Jupyter Notebook（`.ipynb` 核心選擇與執行 `calendar` 模組）

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★☆☆（入門級遷移）
- **Bloom's Level**: **L3 Apply（應用）** — 能在 GitHub Codespaces 雲端容器中建立與執行 `.ipynb` 筆記本，取代單機無狀態的 Google Colab。
- **Course Weight**: 5%（環境遷移基礎閘門）
- **Prerequisites（前置依賴數：2）**:
  1. 已完成個人 GitHub Fork（`<your-username>/DM2026`）並啟動 `2-core` Codespace。
  2. 已閱讀 `Grace-TA/DM2026` 根目錄之 `WEEK01.md`（`# My first Google Colab`）與 `WEEK02.md` 第 1 節（`Calendar` 模組）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 學生能在 `notebooks/week01_lab15.ipynb` 選擇正確的 Python 3 Kernel 並執行 `calendar.month()` 與 `datetime` UTC+8 時間戳記，且單元執行狀態皆為綠勾（Exit 0） `THEN` 通過 Lab 15；`ELSE` 檢核 `.venv` 或 `ipykernel` 套件安裝狀態並重選 Kernel。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
> **選型黃金準則**：在「一般程式開發、演算法教學（如離散數學 `DM2026` 常用之 `NetworkX`、`SymPy`、`Z3` 僅需 CPU）、多檔案專案與軟體工程」上，Codespaces **完全取代** Google Colab 且更強大；僅在「需要免費 T4 GPU 訓練深度學習模型」時，兩者屬於**互補關係**。

1. **確認作業環境與拓撲**：登入個人 GitHub 帳號，開啟你 Fork 自 `https://github.com/Grace-TA/DM2026` 的專屬倉庫，點選 `Code` -> `Codespaces` -> 在 `2-core` 規格下啟動或恢復你的 Codespace（講師將於 `fantastic-dollop` 4-core / 16GB RAM `Ubuntu 24.04.5 LTS` 環境同步演示）。
2. **檢視原始教材基線與持久目錄**：確認工作目錄位於受 Persistent Volume 保護的 `/workspaces/DM2026`，於 VS Code 側邊欄開啟 `WEEK01.md` 與 `WEEK02.md`，比較 Google Colab（閒置約 90 分鐘斷線清空磁碟）與 Codespaces（`/workspaces/DM2026` 永久保留磁碟狀態 + 原生 `git push`）的差異。
3. **安裝/驗證 Jupyter 延伸模組與核心**：確認已安裝 `ms-toolsai.jupyter` 擴充套件，開啟 Codespaces 終端機（`` Ctrl + ` ``），執行以下指令確認 Python 與 `ipykernel` 就緒：
   ```bash
   python3 --version
   python3 -m pip install --quiet ipykernel jupyter
   ```
4. **建立遷移筆記本**：在專案根目錄建立 `notebooks/` 資料夾，並於其中新增 `week01_lab15.ipynb`（可使用指令 `mkdir -p notebooks && touch notebooks/week01_lab15.ipynb` 或透過 VS Code UI 新增）。
5. **選擇 Notebook Kernel**：開啟 `notebooks/week01_lab15.ipynb`，點擊右上角的 **Select Kernel** -> **Python Environments...** -> 選擇容器預設的 Python 3 解譯器（例如 `/usr/local/bin/python` 或 `.venv/bin/python`）。
6. **撰寫 Cell 1（Markdown 宣告）**：新增 Markdown Cell，記錄學號、Fork 倉庫網址與遷移來源 `WEEK01.md`。
7. **撰寫 Cell 2（`calendar` 模組實戰）**：新增 Code Cell，匯入 Python 內建 `calendar` 與 `math` 模組，印出 **115 學年第 1 學期開學月份（2026 年 9 月）** 的月曆，並判斷 2026 年是否為閏年（`calendar.isleap(2026)`）。
8. **撰寫 Cell 3（UTC+8 時間戳記驗證）**：承襲 `DM2026` 課程慣例，利用 `datetime` 與 `timezone(timedelta(hours=8))` 印出台北標準時間戳記作為完成憑證，按下 `Run All` 並存檔（`Ctrl+S`）。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是 Muse Academy（繆思學院）的資深 Python 與離散數學雲端實習助教，精通 Google Colab 與 GitHub Codespaces Jupyter Notebook 核心架構。
</epistemic_role>

<dm2026_context>
- 目標倉庫：Grace-TA/DM2026（115學年第1學期 離散數學 Discrete Math，工作目錄 /workspaces/DM2026 受 Persistent Volume 保護）
- 學生環境：個人 Fork + 2-core GitHub Codespace（Ubuntu 24.04.5 LTS 容器 + ms-toolsai.jupyter）
- 原始教材：WEEK01.md（# My first Google Colab）與 WEEK02.md 第 1 節（Calendar）& 第 2 節（math module & % formatting）
</dm2026_context>

<embedded_code_or_spec>
請協助我將以下原本在 Google Colab 執行的 DM2026 WEEK01/02 示範程式碼，改寫並封裝為適合 Codespaces `.ipynb` 執行的結構化 Cell 內容：

~~~python
import calendar
import math
from datetime import datetime, timezone, timedelta

# 1. 顯示 2026 年 9 月（115學年第1學期開學月）月曆
year, month = 2026, 9
print(calendar.month(year, month))
print("Is 2026 leap year?:", calendar.isleap(year))

# 2. 結合 WEEK02 #2: math 模組與 % 格式化輸出離散數學常用常數
print("ceil(log2(100)) = %d, pi = %.4f" % (math.ceil(math.log2(100)), math.pi))

# 3. 台北時間 (UTC+8) 執行時間戳記
tw_tz = timezone(timedelta(hours=8))
print("Verified at (UTC+8):", datetime.now(tw_tz).strftime("%Y-%m-%d %H:%M:%S"))
~~~
</embedded_code_or_spec>

<task>
1. 檢查上述程式碼在 Codespaces Jupyter Kernel 執行時是否需要額外第三方套件。
2. 為每個區塊加上繁體中文教學註解與英文專有名詞（如 Binary Logarithm, Ceiling Function），解釋為何 `ceil(log2(N))` 在離散數學中代表編碼 N 個狀態所需的最小位元數（bits）。
3. 提供當 VS Code 顯示「No Kernel Found」時的終端機修復指令。
</task>

<output_contract>
- 輸出語言：繁體中文說明＋英文技術名詞與程式碼註解。
- 必須包含：3 個對應 `.ipynb` Cell 的完整程式碼、離散數學位元數解釋、以及 2 條常見 Kernel 錯誤排解指令。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
     September 2026
  Mo Tu We Th Fr Sa Su
      1  2  3  4  5  6
   7  8  9 10 11 12 13
  14 15 16 17 18 19 20
  21 22 23 24 25 26 27
  28 29 30

  Is 2026 leap year?: False
  ceil(log2(100)) = 7, pi = 3.1416
  Verified at (UTC+8): 2026-09-14 10:15:32
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀 A**：右上角 Kernel 一直轉圈或顯示 `Running cells with 'Python' requires the ipykernel package`。
    - **解法**：於終端機執行 `python3 -m pip install -U ipykernel`，再按 `Ctrl+Shift+P` -> 輸入 `Developer: Reload Window` 重新載入視窗。
  - **症狀 B**：Codespace 顯示 UTC 時間而非台北時間。
    - **解法**：雲端 Linux 容器預設為 UTC，`WEEK02 #10` 與 `WEEK03 #12` 之時間戳記務必使用 `timezone(timedelta(hours=8))` 強制對齊 UTC+8，切勿直接呼叫無時區之 `datetime.now()`。

---

## Lab 16：`WEEK02` 實作 1135 & 1140 升級：在 Codespaces 修復縮排錯誤並以 Python 實作命題邏輯真值表（Truth Table CLI）

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆（進階語法與邏輯計算）
- **Bloom's Level**: **L4 Analyze（分析）** — 能診斷 Python `IndentationError`，並將離散數學命題邏輯連接詞（$\neg, \land, \lor, \rightarrow, \leftrightarrow$）映射為確定性布林運算函式。
- **Course Weight**: 7%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 15（確認 Codespaces Python 執行環境正常）。
  2. 理解 `WEEK02.md` 第 3 節（Fix indentation & two-way if-else `[實作 1135]`）與第 4 節（Boolean operations `[實作 1140]`）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 學生撰寫的 `src/lab16_truth_table.py` 通過 Python `py_compile` 語法檢查（0 `IndentationError`）且正確輸出包含 $p, q, \neg p, p \land q, p \lor q, p \rightarrow q, p \leftrightarrow q$ 共 4 列（$2^2 = 4$）完全正確之真值表 `THEN` 通過 Lab 16；`ELSE` 檢核條件蘊含式（Implication）`not p or q` 之邏輯等價寫法。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立模組目錄**：在 Codespaces 終端機執行 `mkdir -p src`，將從本 Lab 開始的作業程式統一收斂於 `src/` 目錄，擺脫 Colab 零散檔名。
2. **重現並修復 `[實作 1135]` 縮排陷阱**：在 `src/lab16_truth_table.py` 先練習辨識雙向條件判斷（Two-way `if-else`）常見的混用 Tab 與 Space 錯誤；在 VS Code 右下角狀態列確認縮排設定為 `Spaces: 4`。
3. **定義離散數學邏輯運算元**：在 Python 中，`not`、`and`、`or` 僅原生覆蓋 $\neg, \land, \lor$；請依據邏輯等價律定義函式：
   - 蘊含（Implication, $p \rightarrow q$）：`def implies(p: bool, q: bool) -> bool: return (not p) or q`
   - 雙條件（Biconditional, $p \leftrightarrow q$）：`def iff(p: bool, q: bool) -> bool: return p == q`
   - 互斥或（XOR, $p \oplus q$）：`def xor(p: bool, q: bool) -> bool: return p != q`
4. **使用 `itertools.product` 生成布林空間**：利用 `itertools.product([True, False], repeat=2)` 自動生成所有 $2^2 = 4$ 種真值指派（Truth Assignment），避免手寫四組硬編碼變數。
5. **實作進階 3 變數重言式（Tautology）驗證器**：擴充函式驗證迪摩根定律（De Morgan's Law）：$\neg(p \land q) \leftrightarrow (\neg p \lor \neg q)$ 在所有真值組合下恆為 `True`。
6. **加入 CLI 格式化表格輸出**：使用 f-string 對齊欄位（例如 `f"{str(p):<6}"`），輸出乾淨的 ASCII 真值表，並附上 `[實作 1135]` 成績等級分類示範函式（修復縮排後的乾淨版本）。
7. **執行語法與邏輯檢查**：在終端機執行 `python3 -m py_compile src/lab16_truth_table.py && python3 src/lab16_truth_table.py` 確認零錯誤並截存輸出結果。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是專精離散數學（Propositional Logic）與 Python 靜態語法分析的 Codespaces 導師。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK02.md
  - 第 3 節：Fix indentation & two-way if-else [實作 1135]
  - 第 4 節：Boolean operations [實作 1140]
- 開發環境：GitHub Codespaces VS Code（4-space indentation 標準）
</dm2026_context>

<embedded_code_or_spec>
以下是一段模擬 WEEK02 學生常犯「縮排錯亂＋布林邏輯未封裝」的待修復程式碼，請據此升級為 Truth Table CLI：

~~~python
# Broken legacy Colab snippet (DO NOT RUN DIRECTLY)
def check_score_1135(score):
if score >= 60:
    print("Pass")
  else:
        print("Fail")

# WEEK02 [實作 1140] 基礎布林操作升級需求：
# 需輸出 p, q 之 NOT, AND, OR, IMPLIES (p -> q), IFF (p <-> q), XOR，
# 並驗證 De Morgan's Law: not(p and q) == ((not p) or (not q))
~~~
</embedded_code_or_spec>

<task>
1. 逐行指出 `check_score_1135` 的 3 處縮排錯誤原因（Missing indent after colon, `else` misaligned with `if`, inconsistent 2 vs 4 vs 8 spaces）。
2. 撰寫完整可執行的 `src/lab16_truth_table.py`，包含：
   - 修復後的 `classify_score_1135(score: int) -> str`（Two-way if-else + 型別驗證）。
   - `implies(p, q)`、`iff(p, q)`、`xor(p, q)` 函式與英文 docstring。
   - `print_truth_table()` 使用 `itertools.product([True, False], repeat=2)` 印出整齊對齊的真值表，並統計 De Morgan's Law 是否為 Tautology（4/4 為 True）。
</task>

<output_contract>
- 產出單一完整 Python 程式碼（無任何省略或 placeholder）。
- 繁體中文解釋縮排原理與 Implication 在 `p=False, q=False` 時為何為 `True`（Vacuous Truth 空真）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  [實作 1135 修復驗證] Score 75 -> Pass | Score 42 -> Fail

  === Propositional Logic Truth Table (WEEK02 [實作 1140] Upgrade) ===
  p      q      ~p     p^q    pvq    p->q   p<->q  p(+)q  DeMorgan_OK
  --------------------------------------------------------------------
  True   True   False  True   True   True   True   False  True
  True   False  False  False  True   False  False  True   True
  False  True   True   False  True   True   False  True   True
  False  False  True   False  False  True   True   False  True
  --------------------------------------------------------------------
  Tautology Check (De Morgan's Law): 4/4 PASSED (Valid Tautology!)
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **常見陷阱 1**：學生常把 `p -> q` 誤寫為 `p <= q` 雖然在 Python 布林中（`False=0, True=1`）結果碰巧相同，但在工程可讀性極差！務必使用明確的邏輯等價式 `(not p) or q`。
  - **常見陷阱 2**：VS Code 中若出現 `TabError: inconsistent use of tabs and spaces in indentation`，按下 `Ctrl+Shift+P` 執行 `Convert Indentation to Spaces` 即可一鍵統一為 4 個空白字元。

---

## Lab 17：`WEEK02` 實作 1160 & 1171 升級：字串清洗管線與 `enumerate()` 離散索引模組化

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆
- **Bloom's Level**: **L3 Apply（應用）** — 將字元處理與異質串列遍歷（Heterogeneous List + `enumerate()`）重構為可重用的離散資料預處理管線（Preprocessing Pipeline）。
- **Course Weight**: 6%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 16（熟悉 `src/` 目錄與 Python 函式定義）。
  2. 熟悉 `WEEK02.md` 第 5–7 節（Strings, String cleaning & replace `[實作 1160]`, Heterogeneous list & `enumerate()` `[實作 1171]`）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 程式能將含有多餘空白、大小寫混雜與特殊符號的原始字串（如離散數學集合表達式 `"  { A , b , C , 101 , A }  "`）清洗為標準化元素，並使用 `enumerate(items, start=1)` 正確印出每個異質元素的「索引—型別—數值」三元組 `THEN` 通過 Lab 17；`ELSE` 檢核 `.strip()`、`.replace()` 與 `isinstance()` 的呼叫順序。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立檔案**：在 Codespaces 建立 `src/lab17_string_enum.py`。
2. **實作字串清洗管線（`[實作 1160]` 升級）**：針對常見髒資料（如 `"  DM2026:  Discrete_Math!!  #Week02  "` 或不規則集合字串），鏈式呼叫 `.strip()`、`.replace()`、`.lower()` 與 `.split()`，移除雜訊符號並提取乾淨 Token。
3. **處理異質串列（Heterogeneous List, `[實作 1171]` 升級）**：建立一個同時包含 `int`、`float`、`str`、`bool`、`tuple` 的離散數學特徵串列，例如：`discrete_items = [42, 3.14159, "Proposition_P", True, (1, 0), "Set_A"]`。
4. **運用 `enumerate()` 建立離散序列映射**：在離散數學中，有限序列（Sequence）本質上是從指標集 $\mathbb{Z}^+$ 或 $\mathbb{N}$ 到目標集合 $S$ 的函數 $a: \{0, 1, \dots, n-1\} \to S$。使用 `for idx, val in enumerate(discrete_items, start=1):` 同時取得 1-based 索引與元素值，避免使用低可讀性的 `range(len(...))`。
5. **型別指紋統計**：結合字典或計數邏輯，記錄每個元素對應的 `type(val).__name__`，並特別示範清洗字串轉成有序不重複元素索引表。
6. **加入模組保護區段**：在檔案底部加上 `if __name__ == "__main__":` 執行區塊，使該檔案未來可被 Lab 24 的 `pytest` 直接匯入測試而不觸發多餘列印。
7. **執行驗證**：於終端機執行 `python3 src/lab17_string_enum.py` 檢視清洗前後對比與索引報表。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是專精 Python 資料工程與離散數學序列表示法（Discrete Sequences & Indexing）的軟體工程導師。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK02.md
  - 第 5 節：Strings
  - 第 6 節：String cleaning & replace [實作 1160]
  - 第 7 節：Heterogeneous list & enumerate() [實作 1171]
</dm2026_context>

<embedded_code_or_spec>
以下為需整合並模組化的資料清洗與異質串列索引規格：

~~~python
raw_records = [
    "  {  Alpha ,  BETA , gamma ,  alpha  }  ",
    "  Set_S = [  10 , 20 , 30 , 20 ]  ",
]

heterogeneous_sample = [115, "Discrete_Math", 2.71828, True, ("p", "q"), None]
~~~
</embedded_code_or_spec>

<task>
請撰寫完整檔案 `src/lab17_string_enum.py`：
1. 實作 `clean_symbol_string(raw: str) -> list[str]`：移除 `{`, `}`, `[`, `]`, `Set_S =` 等分隔符號與前後空白，統一轉小寫，依逗號切割並去除空字串。
2. 實作 `inspect_heterogeneous_list(items: list) -> list[tuple[int, str, str]]`：使用 `enumerate(items, start=1)` 回傳 `(index, type_name, repr_value)` 串列。
3. 在 `if __name__ == "__main__":` 中示範清洗結果與異質串列格式化表格，並在註解中連結離散數學「序列即函數 $f: I \to S$」的概念。
</task>

<output_contract>
- 僅輸出可執行的完整 Python 程式碼與簡潔繁體中文解析。
- 禁止使用任何外部套件（僅限 Python 標準函式庫）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  === [實作 1160] String Cleaning Pipeline ===
  Raw     : '  {  Alpha ,  BETA , gamma ,  alpha  }  '
  Cleaned : ['alpha', 'beta', 'gamma', 'alpha']

  === [實作 1171] Heterogeneous List & enumerate() Mapping ===
  Idx | Type      | Value
  ----+-----------+-------------------
    1 | int       | 115
    2 | str       | 'Discrete_Math'
    3 | float     | 2.71828
    4 | bool      | True
    5 | tuple     | ('p', 'q')
    6 | NoneType  | None
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **常見陷阱**：對字串執行 `s.replace(",", " ")` 卻忘記賦值回去（如只寫 `s.replace(...)` 沒寫 `s = s.replace(...)`）。Python 的 `str` 是不可變物件（Immutable），所有字串方法皆回傳新字串，必須重新綁定變數！

---

## Lab 18：`WEEK02` 實作 1175 & 9X9 乘法表升級：VS Code 斷點除錯器（Debugger Step-Over & Watch）透視巢狀迴圈

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆
- **Bloom's Level**: **L4 Analyze（分析）** — 放棄低效的「到處插 `print()`」除錯法，改用 Codespaces VS Code 內建 Debugger（Breakpoint, Step Over `F10`, Step Into `F11`, Watch Expression）即時追蹤迴圈變數與步進切片狀態。
- **Course Weight**: 7%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 17（熟悉 `src/` 檔案建立與 Python 執行）。
  2. 熟悉 `WEEK02.md` 第 8 節（Slicing & `range()` step loop `[實作 1175 & 1175a]`）與第 9–10 節（Table 9X9 & Timestamped final result）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 學生能正確實作等差數列切片（`[實作 1175 / 1175a]`）與模運算乘積表（9×9 Multiplication Table & $\mathbb{Z}_9$ Cayley Table 延伸），並設定條件斷點（Conditional Breakpoint: `i == 7 and j == 8`）於 Watch 視窗觀測變數值 `THEN` 通過 Lab 18；`ELSE` 檢核 `.vscode/launch.json` 與 Python Debugger 延伸套件狀態。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立除錯目標程式**：建立 `src/lab18_loop_debugger.py`，整合三項任務：(a) 串列切片步進 `seq[start:stop:step]` 與負索引反轉（`[實作 1175]`）；(b) `range(start, stop, step)` 生成偶數/奇數等差數列（`[實作 1175a]`）；(c) 雙層巢狀迴圈生成 9×9 乘法表與 $\mathbb{Z}_9$ 模乘法表（Modular Multiplication Table）。
2. **設定條件斷點（Conditional Breakpoint）**：在編輯器左邊界行號旁點擊右鍵 -> **Add Conditional Breakpoint...**，在內層迴圈 `product = i * j` 那一行輸入條件 `i == 7 and j == 8`。
3. **啟動 VS Code Debugger**：按 `F5`（或點擊左側蟲子圖示 **Run and Debug** -> 選擇 **Python Debugger: Python File**）。程式將高速略過前面 50 多個迭代，精準暫停在 `(i=7, j=8)` 的瞬間！
4. **運用 Watch 視窗透視狀態**：在左側 **WATCH** 面板點擊 `+`，依序加入監看表達式：`i`、`j`、`i * j`、`(i * j) % 9`。
5. **執行 Step Over (`F10`) 單步追蹤**：連續按 3 次 `F10`，親眼觀察 `j` 從 `8` 推進到 `9`，接著外層迴圈 `i` 從 `7` 遞增至 `8`，徹底理解巢狀迴圈執行序（Execution Trace）。
6. **驗證 `[實作 1175 & 1175a]` 切片對照**：繼續執行（`F5` Continue）至程式結束，確認切片運算與 `range()` 步進迴圈產生完全等價的數列，並加上 `WEEK02 #10` UTC+8 驗證時間戳記。
7. **記錄除錯觀測日誌**：在程式註解或終端機確認條件斷點命中時的輸出正確無誤。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是精通軟體除錯工程（Interactive Debugging）與離散數學代數結構（Modular Arithmetic Cayley Tables）的技術教練。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK02.md
  - 第 8 節：Slicing & range() step loop [實作 1175 & 1175a]
  - 第 9 節：Table 9X9
  - 第 10 節：Timestamped final result
- 工具環境：Codespaces VS Code Python Debugger
</dm2026_context>

<embedded_code_or_spec>
請協助我撰寫 `src/lab18_loop_debugger.py`，需涵蓋以下離散序列與表格規格：
1. `[實作 1175]` 給定 `nums = list(range(1, 21))`，使用 slicing 取出：偶數索引元素、步進為 3 的元素、以及完全反轉序列 `nums[::-1]`。
2. `[實作 1175a]` 使用 `range(start, stop, step)` 計算 $1 + 3 + 5 + \dots + 19$ 的總和，並驗證是否等於 $n^2$（此處 $n=10 \implies 100$）。
3. `Table 9X9`：利用巢狀 `for i in range(1, 10)` 與 `for j in range(1, 10)`，同時計算標準 9×9 乘法表與 $\mathbb{Z}_9$ 模乘法表（`(i * j) % 9`），方便學生設定條件斷點 `i == 7 and j == 8` 進行 Step-Over 觀測。
4. 附上 UTC+8 台灣時間完成戳記。
</embedded_code_or_spec>

<task>
1. 產生完整可執行的 `src/lab18_loop_debugger.py`（含清楚分段函式與型別註記）。
2. 提供一份簡易的「VS Code Conditional Breakpoint 3 分鐘操作卡」，告訴學生在哪一行下斷點、Watch 要填什麼算式、按 `F10` 後變數如何變化。
</task>

<output_contract>
- 輸出完整 Python 程式碼（Zero placeholders）。
- 繁體中文搭配英文 Debugger 專有名詞（Breakpoint, Call Stack, Watch Expression, Step Over）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  === [實作 1175] Slicing Verification ===
  Every 3rd element (nums[::3]): [1, 4, 7, 10, 13, 16, 19]
  Reversed last 5 (nums[-1:-6:-1]): [20, 19, 18, 17, 16]

  === [實作 1175a] Odd Sum Theorem (1+3+...+19 = n^2) ===
  Computed sum: 100 | Formula 10^2: 100 | Match: True

  === [WEEK02 #9] 9x9 Multiplication Table (Excerpt i=7..9) ===
  7x1= 7 7x2=14 7x3=21 7x4=28 7x5=35 7x6=42 7x7=49 7x8=56 7x9=63
  ...
  === [WEEK02 #10] Verified at (UTC+8): 2026-09-21 14:20:05 ===
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀**：按 `F5` 時 VS Code 提示找不到 Python 延伸套件或 Debugger 沒反應。
  - **解法**：檢查左側 Extensions 面板是否已啟用 `ms-python.python` 與 `ms-python.debugpy`；若 Codespaces 剛建立尚未安裝完成，等待右下角進度條完成或點擊 `Install in Codespaces`。

---

# Cycle 5/6：離散數學容器、OOP 與視覺化（`DM2026` `WEEK03`）

## Lab 19：`WEEK03` 集合論（Sets & Set Comprehension）：在 Codespaces 實作交集、聯集、差集與冪集（Power Set）生成器

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆
- **Bloom's Level**: **L4 Analyze（分析）** — 掌握 Python `set` 雜湊唯一性（Hash Uniqueness）與 Set Comprehension，並能實作卡氏積（Cartesian Product）及基數為 $2^{|S|}$ 的冪集（Power Set, $\mathcal{P}(S)$）演算法。
- **Course Weight**: 8%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 18（具備迴圈與函式撰寫能力）。
  2. 閱讀 `WEEK03.md` 第 01、03、06 節（字元重複與反轉、List comprehension、Sets & set comprehension）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 程式正確計算兩集合 $A, B$ 之聯集 $|A \cup B|$、交集 $|A \cap B|$、差集 $A \setminus B$、對稱差集 $A \oplus B$，驗證排容原理 $|A \cup B| = |A| + |B| - |A \cap B|$，且 `power_set(S)` 針對 4 元素集合產出精確 $2^4 = 16$ 個 `frozenset` 子集 `THEN` 通過 Lab 19；`ELSE` 檢核集合元素不可變性（為何子集需使用 `frozenset` 而非 `set` 放入大集合）。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立集合論實戰模組**：在 Codespaces 建立 `src/lab19_set_theory.py`。
2. **練習 `WEEK03 #01 & #03` 字串與 Comprehension 暖身**：利用 List/Set Comprehension 快速抽出給定單字（如 `"discrete mathematics"`）的不重複母音集合與子音集合。
3. **實作基礎集合代數運算**：定義宇集 $U = \{1, 2, \dots, 12\}$，與兩個透過 Set Comprehension 生成的子集：
   - $A = \{x \in U \mid x \bmod 2 = 0\}$（偶數集）
   - $B = \{x \in U \mid x \bmod 3 = 0\}$（3 的倍數集）
   使用 Python 運算子 `|`（Union）、`&`（Intersection）、`-`（Difference）、`^`（Symmetric Difference）計算並自動驗證 **排容原理（Inclusion-Exclusion Principle）** 與 **補集律（Complement Law）**。
4. **實作卡氏積（Cartesian Product）**：使用巢狀 Set Comprehension `{(a, b) for a in X for b in Y}` 計算 $X \times Y$，並驗證基數 $|X \times Y| = |X| \cdot |Y|$。
5. **挑戰冪集（Power Set, $\mathcal{P}(S)$）生成器**：撰寫兩種做法並比較：
   - 做法 A：使用標準函式庫 `itertools.combinations(S, r)` 從 $r=0$ 迭代到 $|S|$。
   - 做法 B：使用 **位元遮罩（Bitmasking, `0` 到 `2**n - 1`）** 展示離散數學中「$n$ 元素集合的冪集與 $n$-bit 二進位字串存在 1-to-1 Bijection」之核心定理！
6. **處理集合的集合（Set of Sets）型別陷阱**：因 Python `set` 物件本身不可雜湊（Unhashable），若要將所有子集收進一個大 `set`，必須將每個子集封裝為 `frozenset`。
7. **執行驗證**：執行 `python3 src/lab19_set_theory.py` 確認基數驗證與 16 個冪集元素全數正確印出。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是精通組合數學（Combinatorics）、集合論（Set Theory）與 Python 容器底層雜湊機制的大學講師。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK03.md
  - 01. char repeat & reverse step
  - 03. List comprehension
  - 06. Sets & set comprehension
- 教學目標：將離散數學集合恆等式與冪集同構定理轉化為可執行的 Python 程式碼。
</dm2026_context>

<embedded_code_or_spec>
請實作一個離散數學集合論實驗模組 `src/lab19_set_theory.py`，包含：
1. Set Comprehension 建構宇集 $U = \{1..12\}$、偶數集 $A$、3 的倍數集 $B$。
2. 驗證 Inclusion-Exclusion Principle：$|A \cup B| == |A| + |B| - |A \cap B|$。
3. 驗證 De Morgan's Law for Sets：$(U \setminus (A \cup B)) == (U \setminus A) \cap (U \setminus B)$。
4. Cartesian Product $X \times Y$ where $X = \{1, 2\}, Y = \{'a', 'b', 'c'\}$。
5. `power_set_bitmask(elements: set) -> set[frozenset]`：利用 bitmask `mask in range(1 << n)` 生成 $\mathcal{P}(S)$，並驗證 $|\mathcal{P}(S)| == 2^{|S|}$。
</embedded_code_or_spec>

<task>
1. 撰寫完整可執行的 `src/lab19_set_theory.py`。
2. 在程式碼註解中說明為何 Python 會拋出 `TypeError: unhashable type: 'set'`，以及為何 `frozenset` 是表示數學「集合的集合」的標準解法。
3. 以 `S = {'p', 'q', 'r', 's'}` 執行測試，依子集大小排序印出所有 16 個元素。
</task>

<output_contract>
- 輸出完整 Python 檔案內容（無任何省略）。
- 包含數學符號對照表（Math Notation vs Python Set Operator）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  === Inclusion-Exclusion & De Morgan's Verification ===
  |A u B| = 8 == |A|(6) + |B|(4) - |A n B|(2) -> PASS
  De Morgan's Law (U - (A|B)) == (U-A)&(U-B) -> PASS: {1, 5, 7, 11}

  === Cartesian Product X x Y (|X|=2, |Y|=3) ===
  Size: 6 -> {(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')}

  === Power Set P({'p', 'q', 'r', 's'}) via Bitmask ===
  Cardinality: 16 == 2^4 -> PASS
  Subsets: [], ['p'], ['q'], ['r'], ['s'], ..., ['p', 'q', 'r', 's']
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **常見陷阱**：寫 `{}` 想建立空集合！在 Python 中 `{}` 建立的是空字典 `dict`，建立空集合**必須**寫 `set()`（或 `frozenset()`）。這也是離散數學寫空集合 $\emptyset$ 時最容易出現的語法 bug。

---

## Lab 20：`WEEK03` 函式、字典與 `try-except`：打造耐錯的離散關係（Relation: 自反/對稱/遞移）檢測器

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆
- **Bloom's Level**: **L5 Evaluate（評鑑）** — 結合 `dict`（鄰接表表示法）、函式抽象化、`while` 迴圈控制（`break`/`continue`, `WEEK03 #04 P1133B/C`）與 `try-except` 防禦性程式設計，對任意有限二元關係 $R \subseteq A \times A$ 自動判定等價關係（Equivalence Relation）或偏序關係（Partial Order）。
- **Course Weight**: 8%
- **Prerequisites（前置依賴數：3）**:
  1. 完成 Lab 19（理解集合與序對 Tuple $(a, b) \in A \times A$）。
  2. 熟悉 `WEEK03.md` 第 04 節（While loop `break`/`continue` `P1133B/C`）與第 05, 07, 08 節（Dictionary, Functions, `try-except` error handling）。
  3. 理解離散數學二元關係三大性質：Reflexive（自反）、Symmetric（對稱）、Antisymmetric（反對稱）、Transitive（遞移）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 學生實作的關係檢測器能對合法序對準確回傳四大性質布林值（並正確判定 Equivalence Relation），且在輸入非法格式（如缺少逗號、元素不在集合 $A$ 內）時透過 `try-except ValueError` 優雅攔截並要求重試而不崩潰 `THEN` 通過 Lab 20；`ELSE` 檢核 `is_transitive` 是否正確處理 $(a, b) \in R \land (b, c) \in R \implies (a, c) \in R$ 且不誤判反對稱性（Antisymmetric）。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立關係檢測檔案**：在 Codespaces 建立 `src/lab20_relation_checker.py`。
2. **用字典建構關係鄰接表（Adjacency Dictionary）**：除了儲存序對集合 `R: set[tuple]`，亦實作轉換函式 `build_adjacency_dict(domain: set, R: set[tuple]) -> dict[str, set]`，對應 `WEEK03 #05 Dictionary` 教學內容。
3. **撰寫四大性質純函式（Pure Functions, `WEEK03 #07`）**：
   - `is_reflexive(A, R)`: $\forall a \in A, (a, a) \in R$
   - `is_symmetric(R)`: $\forall (a, b) \in R, (b, a) \in R$
   - `is_antisymmetric(R)`: $\forall (a, b) \in R, (b, a) \in R \implies a = b$
   - `is_transitive(R)`: $\forall (a, b) \in R, \forall (b, c) \in R \implies (a, c) \in R$
4. **合成高階關係分類器**：實作 `classify_relation(A, R) -> dict`，自動判斷是否為 **Equivalence Relation（等價關係：Reflexive + Symmetric + Transitive）** 或 **Partial Order（偏序關係：Reflexive + Antisymmetric + Transitive）**。
5. **打造耐錯的互動式 CLI 輸入迴圈（`WEEK03 #04 & #08`）**：利用 `while True:` 搭配 `continue`（格式錯誤重新輸入）與 `break`（輸入 `done` 結束），並在解析序對 `a,b` 時使用 `try-except ValueError` 捕捉非法輸入與不在定義域 $A$ 內的越界元素（Domain Boundary Check）。
6. **執行內建標準測試案例**：預置三組離散數學經典關係測試：(1) 整除關係 `divides` on $\{1,2,3,6\}$（應為 Partial Order）；(2) 模 3 同餘關係 `mod 3` on $\{0,1,2,3,4,5\}$（應為 Equivalence Relation）；(3) 一般無規律關係。
7. **測試異常輸入防呆**：故意輸入 `"abc"` 或 `"99,1"` 驗證程式能印出友善警告並繼續運行，不因 `Exception` 中斷。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是專精離散數學「關係與圖論（Relations & Directed Graphs）」及防禦性 Python 程式設計（Defensive Programming）的架構導師。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK03.md
  - 04. While loop break/continue (P1133B/C 互動輸入迴圈模式)
  - 05. Dictionary
  - 07. Functions
  - 08. try-except error handling
</dm2026_context>

<embedded_code_or_spec>
請實作 `src/lab20_relation_checker.py`，同時支援「程式自動驗證模式」與「互動式 `try-except` + `while/break/continue` 輸入模式」：
- 定義域集合 $A$ 可為整數或字串。
- 必須檢測以下 4 種性質：
  1. `is_reflexive(domain, rel)`
  2. `is_symmetric(rel)`
  3. `is_antisymmetric(rel)`
  4. `is_transitive(rel)`
- 特別注意：離散數學中 Symmetric 與 Antisymmetric 並非互補（Not mutually exclusive）！例如恆等關係 $I = \{(1,1), (2,2)\}$ 同時滿足 Symmetric 與 Antisymmetric。
</embedded_code_or_spec>

<task>
1. 撰寫完整可執行的 `src/lab20_relation_checker.py`。
2. 實作 `parse_pair(raw: str, domain: set[int]) -> tuple[int, int]`，使用 `try-except ValueError` 攔截非整數或長度不等於 2 的輸入，並檢查兩元素是否皆屬於 `domain`（否則主動 `raise ValueError`）。
3. 提供 `interactive_session()` 使用 `while True:`、`continue`（空行跳過）、`break`（輸入 `done` 結束）。
4. 在 `main()` 中先跑完 2 組預設經典定理測試（整除偏序 + 同餘等價關係），再詢問使用者是否進入互動測試（預設支援 `--batch` 旗標直接跳過互動以便自動化執行）。
</task>

<output_contract>
- 輸出完整 Python 程式碼，不得包含任何 `TODO` 或省略區塊。
- 清楚區分「對稱」與「反對稱」的邏輯反例搜尋方式。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  === Case 1: Divisibility on {1, 2, 3, 6} ===
  Reflexive: True | Symmetric: False | Antisymmetric: True | Transitive: True
  Classification -> Partial Order (Poset)

  === Case 2: Congruence mod 3 on {0, 1, 2, 3, 4, 5} ===
  Reflexive: True | Symmetric: True | Antisymmetric: False | Transitive: True
  Classification -> Equivalence Relation

  [Interactive Input Guard Test]
  Input '1,abc' -> Caught ValueError: Invalid integer in pair. Please retry.
  Input '1,99'  -> Caught ValueError: Element 99 not in domain {1, 2, 3}.
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **常見陷阱**：很多初學者把 `is_antisymmetric` 誤寫成 `not is_symmetric(rel)`，這是嚴重的離散數學觀念錯誤！以 $R = \{(1,1), (2,2)\}$ 為例，它既對稱又反對稱；而 $R = \{(1,2), (2,1), (1,3)\}$ 既不對稱也不反對稱。程式碼必須嚴格依定義檢查 `if a != b and (b, a) in rel: return False`。

---

## Lab 21：`WEEK03` 物件導向（OOP & Classes）：從單檔 Colab 升級為多檔案 `discrete_toolkit/` 套件架構

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★★（進階工程架構）
- **Bloom's Level**: **L6 Create（創造）** — 徹底突破 Google Colab「單一長頁面 Notebook」的工程天花板，依照 Python 套件規範設計並實作多檔案物件導向套件 `discrete_toolkit/`（包含類別封裝、Magic Methods `__repr__`/`__and__`/`__or__` 與跨模組匯入）。
- **Course Weight**: 9%
- **Prerequisites（前置依賴數：3）**:
  1. 完成 Lab 19 與 Lab 20（掌握集合論與二元關係之運算邏輯）。
  2. 閱讀 `WEEK03.md` 第 09 節（OOP & Classes）。
  3. 理解 Python `__init__.py` 套件識別機制與 `PYTHONPATH` 相對/絕對匯入規則。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 專案具備完整 `discrete_toolkit/__init__.py`、`logic.py`、`sets.py`、`relations.py` 四個檔案，支援 `from discrete_toolkit import TruthEvaluator, FiniteSet, BinaryRelation`，且運算子重載（Operator Overloading，如 `A & B`、`A | B`、`R.compose(S)`）與 `__repr__` 輸出皆通過驗證腳本 `THEN` 通過 Lab 21；`ELSE` 檢核 `ModuleNotFoundError` 是否因從錯誤工作目錄啟動或遺漏 `pyproject.toml` / `PYTHONPATH=.` 所致。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **規劃多檔案套件樹狀結構**：在 Codespaces 專案根目錄建立以下資料夾與檔案：
   ```text
   discrete_toolkit/
   ├── __init__.py
   ├── logic.py       # 命題邏輯類別 PropositionEvaluator
   ├── sets.py        # 有限集合封裝 FiniteSet (支援 &, |, -, power_set)
   └── relations.py   # 二元關係類別 BinaryRelation (繼承或組合 FiniteSet)
   ```
2. **實作 `discrete_toolkit/sets.py`**：定義 `FiniteSet` 類別，內部以 `frozenset` 儲存不可變元素，並實作 Python 魔術方法（Dunder Methods）：`__len__`、`__contains__`、`__and__`（交集 `&`）、`__or__`（聯集 `|`）、`__sub__`（差集 `-`）、`power_set()` 與 `__repr__`。
3. **實作 `discrete_toolkit/relations.py`**：定義 `BinaryRelation` 類別，建構子接收 `domain: FiniteSet` 與 `pairs: set[tuple]`，並於 `__init__` 執行自動邊界驗證（不合法序對立即拋出 `ValueError`）；提供 `.is_equivalence()`、`.is_partial_order()` 與關係合成 `.compose(other)`（$S \circ R$）。
4. **實作 `discrete_toolkit/logic.py`**：定義 `PropositionEvaluator` 類別，封裝真值表計算與重言式（Tautology）檢查方法。
5. **配置套件出口 `discrete_toolkit/__init__.py`**：匯出核心類別並定義 `__all__ = ["FiniteSet", "BinaryRelation", "PropositionEvaluator"]`。
6. **撰寫跨模組入口腳本 `src/lab21_oop_demo.py`**：匯入上述自製套件，實例化兩個 `FiniteSet` 與一個 `BinaryRelation` 物件，展示如數學教科書般優雅的物件導向語法（例如 `(A & B).power_set()`）。
7. **使用 `PYTHONPATH=. python3 src/lab21_oop_demo.py` 執行測試**：確保無 `ModuleNotFoundError` 並驗證所有類別方法運作正常。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是 Python 套件架構師（Package Architect）與物件導向設計（OOP Design Patterns）專家。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK03.md 第 09 節（OOP & Classes）
- 工程目標：克服 Colab 無法優雅管理多檔案模組的痛點，在 Codespaces 建立標準 Python Package `discrete_toolkit/`。
</dm2026_context>

<embedded_code_or_spec>
請設計 `discrete_toolkit/` 多檔案架構規格：
1. `discrete_toolkit/sets.py`：`FiniteSet` 類別，不可變設計（Immutable wrapper around `frozenset`），實作 `__or__`, `__and__`, `__sub__`, `__eq__`, `__len__`, `__iter__`, `__repr__` 與 `power_set()`。
2. `discrete_toolkit/relations.py`：`BinaryRelation` 類別，具備建構時驗證（Domain closure check）、`is_reflexive()`, `is_symmetric()`, `is_antisymmetric()`, `is_transitive()`, `is_equivalence()`, `is_partial_order()` 與 `compose(other: "BinaryRelation") -> "BinaryRelation"`。
3. `discrete_toolkit/logic.py`：`PropositionEvaluator` 類別，支援自訂雙變數邏輯函數並判定 Tautology / Contradiction / Contingency。
4. `discrete_toolkit/__init__.py`：統一匯出三大類別。
5. `src/lab21_oop_demo.py`：完整展示腳本。
</embedded_code_or_spec>

<task>
請依序輸出上述 5 個檔案的完整程式碼（不可省略任何方法），並在最後附上 `mkdir -p` 與執行測試指令，說明為何 OOP 封裝能避免全域變數污染並提升單元測試可測性（Testability）。
</task>

<output_contract>
- 每個檔案以獨立 `### File: <path>` 標題區隔，程式碼完全可直接複製存檔執行。
- 繁體中文架構解析＋英文類別/方法 Docstrings（Google Style）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ PYTHONPATH=. python3 src/lab21_oop_demo.py
  FiniteSet A: FiniteSet({1, 2, 3})
  FiniteSet B: FiniteSet({2, 3, 4})
  A & B = FiniteSet({2, 3}) -> Power Set size = 4
  Relation R on {1, 2, 3}: BinaryRelation(pairs=5, equivalence=False, partial_order=False)
  R o R (Composition) pairs count: 7
  Proposition (p -> q) <-> (~p v q): Classification = Tautology
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀**：執行 `python3 src/lab21_oop_demo.py` 時出現 `ModuleNotFoundError: No module named 'discrete_toolkit'`。
  - **解法**：因為執行腳本位於 `src/` 子目錄下，Python 預設 `sys.path[0]` 是 `src/` 而非專案根目錄！請改用 `PYTHONPATH=. python3 src/lab21_oop_demo.py`，或在終端機安裝可編輯套件（`pip install -e .` 搭配極簡 `pyproject.toml`）。

---

## Lab 22：`WEEK03` Matplotlib & NumPy 視覺化突破：在無螢幕雲端容器輸出 4 相位三角波與等比例單位圓 PNG（`plt.savefig` 與 VS Code 內嵌預覽）

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆
- **Bloom's Level**: **L3 Apply（應用）** — 解決純 Linux 無頭容器（Headless Container，無 X11/GUI 視窗）執行 `plt.show()` 無法彈窗或報錯的痛點，掌握 `Agg` 非互動式後端、`plt.savefig(..., dpi=300)` 高解析度輸出與 VS Code 內嵌圖片預覽工作流。
- **Course Weight**: 7%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 15（已確認 Codespaces Python 與 pip 環境正常）。
  2. 閱讀 `WEEK03.md` 第 10–12 節（Matplotlib & NumPy 4-phase triangle waves with `pi` phase shift, Unit circle parametric plot `x=cos(theta), y=sin(theta)` with equal aspect ratio, Timestamped learning verification）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 腳本在無任何 GUI 視窗下成功於 `outputs/` 生成 `lab22_4phase_triangle_waves.png` 與 `lab22_unit_circle.png` 兩張 PNG 檔案（每張檔案大小 > 20 KB 且為 300 DPI），其中單位圓 `ax.set_aspect('equal')` 確保視覺正圓不變形，且圖表標題含 UTC+8 驗證時間戳記 `THEN` 通過 Lab 22；`ELSE` 檢核 `matplotlib.use("Agg")` 是否於 `import matplotlib.pyplot as plt` 之前宣告。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **安裝科學計算與繪圖套件**：在 Codespaces 終端機執行：
   ```bash
   python3 -m pip install --quiet numpy matplotlib
   mkdir -p outputs
   ```
2. **設定 Headless 繪圖後端（關鍵步驟）**：在撰寫 `src/lab22_visualizations.py` 最頂端，**必須**先執行 `import matplotlib; matplotlib.use("Agg")` 再匯入 `pyplot`，避免容器嘗試尋找不存在的 `TkAgg` / X11 Display 造成警告或掛死。
3. **實作 4 相位三角波（`WEEK03 #10` 升級版）**：
   - 使用 `np.linspace(0, 4 * np.pi, 1000)` 生成時間/角度軸 $t$。
   - 利用標準三角波數學公式（或 SciPy-free 之 `2 / np.pi * np.arcsin(np.sin(t - phase))`），針對四個相位偏移量 $\phi \in \{0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}\}$ 建立 $2 \times 2$ Subplots 子圖，標記網格線與 $\pi$ 倍數刻度（`xticks`）。
4. **實作參數式單位圓（`WEEK03 #11` 升級版）**：
   - 生成 $\theta \in [0, 2\pi]$：`theta = np.linspace(0, 2 * np.pi, 600)`。
   - 計算 $x = \cos(\theta), y = \sin(\theta)$。
   - **強制呼叫 `ax.set_aspect('equal', adjustable='box')`**，確保 $1:1$ 等比例呈現真正的圓形而非橢圓，並標註 $0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}$ 四個軸交點與單位半徑向量。
5. **嵌入 UTC+8 時間戳記浮水印（`WEEK03 #12`）**：透過 `fig.suptitle()` 與右下角註記寫入執行者學號與 `Asia/Taipei` 時間戳記。
6. **輸出與資源釋放**：使用 `plt.savefig("outputs/...", dpi=300, bbox_inches="tight")` 存檔，並務必呼叫 `plt.close(fig)` 釋放記憶體（保護 2-core 容器記憶體配額）。
7. **VS Code 內嵌預覽驗收**：執行 `python3 src/lab22_visualizations.py` 後，在 VS Code 檔案總管直接雙擊 `outputs/lab22_4phase_triangle_waves.png` 與 `outputs/lab22_unit_circle.png`，Codespaces 會直接在分頁渲染高畫質圖片！

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是精通科學計算視覺化（NumPy & Matplotlib Headless Rendering）與三角函數訊號分析的教育工程師。
</epistemic_role>

<dm2026_context>
- 對應教材：Grace-TA/DM2026 WEEK03.md
  - 10. Matplotlib & NumPy 4-phase triangle waves with pi phase shift
  - 11. Unit circle parametric plot x=cos(theta), y=sin(theta) with equal aspect ratio
  - 12. Timestamped learning verification
- 環境限制：GitHub Codespaces 2-core Linux 無 GUI 螢幕容器（必須使用 Agg backend + savefig）。
</dm2026_context>

<embedded_code_or_spec>
請實作無須 `scipy`、純靠 `numpy` 與 `matplotlib` 的 `src/lab22_visualizations.py`：
1. 第一圖 `outputs/lab22_4phase_triangle_waves.png`：
   - 公式：$y(t, \phi) = \frac{2}{\pi} \arcsin(\sin(t - \phi))$
   - 4 個子圖（2x2 grid）分別對應 $\phi = 0, \pi/2, \pi, 3\pi/2$。
   - X 軸範圍 $[0, 4\pi]$，Y 軸範圍 $[-1.25, 1.25]$，加上清晰 Legend 與 Grid。
2. 第二圖 `outputs/lab22_unit_circle.png`：
   - 參數式：$x = \cos(\theta), y = \sin(\theta)$，$\theta \in [0, 2\pi]$。
   - 必須設定 `ax.set_aspect("equal", adjustable="box")`，並畫出原點 $(0,0)$ 到 $( \cos(\pi/4), \sin(\pi/4) )$ 的半徑箭頭與角度標註。
3. 兩張圖皆須包含 UTC+8 完成驗證時間戳記，並於終端機印出檔案路徑與 bytes 大小。
</embedded_code_or_spec>

<task>
撰寫完整、可直接在 Codespaces 無頭環境執行的 `src/lab22_visualizations.py`，並提醒學生在無中文字型的 Linux 容器中如何避免 Matplotlib 標籤出現「豆腐方塊（Tofu Boxes）」亂碼。
</task>

<output_contract>
- 圖表標籤（Title, Axis Labels, Legend）建議使用英文與 LaTeX 數學語法（如 `r"$\phi = \pi/2$"`），確保 Linux 容器 100% 無字型缺字問題。
- 輸出完整 Python 程式碼＋終端機預檢指令。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ python3 src/lab22_visualizations.py
  [OK] Saved: outputs/lab22_4phase_triangle_waves.png (184,520 bytes)
  [OK] Saved: outputs/lab22_unit_circle.png (112,340 bytes)
  [Verified UTC+8]: 2026-09-28 16:40:12
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀 A**：執行時跳出 `UserWarning: Glyph 22294 missing from font(s) DejaVu Sans`，圖片中文變成方框 `□□`。
    - **解法**：Codespaces 基礎 Debian/Ubuntu 映像檔預設未安裝 Noto Sans CJK 中文字型！圖表內之軸標籤與標題請遵守雙語原則使用英文與 Matplotlib 內建 MathText（如 `r"Phase $\phi = \pi/2$"`），保證 100% 跨平台渲染零方框。
  - **症狀 B**：圓形看起來像扁平橢圓。
    - **解法**：檢查是否遺漏 `ax.set_aspect("equal", adjustable="box")`，這是 `WEEK03 #11` 的核心考點。

---

# Cycle 6：Hero Capstones — 互動網頁、自動測試、容器優化、AI 與協作閉環

## Lab 23：離散數學互動展示站：用 Python 產生 HTML/SVG 互動式集合溫氏圖並透過 Codespaces Port Forwarding (Port 8080) 公開分享

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★★
- **Bloom's Level**: **L6 Create（創造）** — 用 Python 生成完全自足（Self-Contained）的暗黑玻璃擬態風格 HTML5 + SVG 互動式集合溫氏圖（Venn Diagram）網頁，並運用 Codespaces **Port Forwarding（連接埠轉發）** 能力，一鍵生成 HTTPS 公開預覽連結給教授或同學體驗！
- **Course Weight**: 8%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 19（精通集合聯集、交集、差集與對稱差集區域定義）。
  2. 了解基礎 HTTP 靜態伺服器啟動指令（`python3 -m http.server 8080`）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 執行 `src/lab23_venn_site_gen.py` 成功產出 `web/index.html`（內含可點擊切換 $A \cap B$、$A \cup B$、$A \setminus B$、$B \setminus A$、$A \oplus B$ 高亮之 SVG 溫氏圖與集合元素計算機），且透過 Codespaces Ports 面板轉發 `Port 8080` 後能在瀏覽器開啟並回傳 HTTP 200 OK `THEN` 通過 Lab 23；`ELSE` 檢核網頁伺服器是否綁定 `--directory web` 及 Port Visibility 設定（Private vs Public）。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立網頁生成腳本**：在 Codespaces 建立 `web/` 目錄與 `src/lab23_venn_site_gen.py`。
2. **設計 Python HTML/SVG 生成器**：讓 Python 腳本接收預設集合資料（亦可動態編輯輸入框），將精確的 SVG `<clipPath>` 與 Venn 兩圓路徑計算寫入單一自包含的 `web/index.html`（Dark Theme `#0a0a0f` 搭配毛玻璃卡片與互動 JavaScript）。
3. **加入離散數學區域高亮引擎**：在生成的網頁內建 6 顆互動按鈕：`A ∩ B`（交集）、`A ∪ B`（聯集）、`A \ B`（差集）、`B \ A`、`A ⊕ B`（對稱差集）、`Reset`，點擊時即時切換 SVG `<path>` 填色與邏輯表達式顯示（如 `(x ∈ A) ∧ (x ∉ B)`），並實作即時元素輸入計算機。
4. **執行腳本產出靜態網站**：於終端機執行 `python3 src/lab23_venn_site_gen.py`，確認產出 `web/index.html`。
5. **啟動 Python HTTP 伺服器**：在終端機執行：
   ```bash
   python3 -m http.server 8080 --directory web
   ```
6. **啟用 Codespaces Port Forwarding**：觀察 VS Code 底部 **PORTS** 面板（若未自動彈出，切換至 Terminal 旁的 `PORTS` 分頁並點擊 `Add Port` 輸入 `8080`）。
7. **分享與預覽網址**：點擊 `8080` 列的地球圖示 **Open in Browser**；若要讓老師或同學在同一網路外預覽，在 `Visibility` 欄位點擊右鍵將 `Private` 切換為 `Public`（驗收完畢建議切回 Private 或停止 Server）。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是兼通前端互動設計（SVG Geometry & Glassmorphism UI）與離散數學教學視覺化的全端開發者。
</epistemic_role>

<dm2026_context>
- 課程背景：DM2026 離散數學集合論（Venn Diagram & Set Operations）
- 運行方式：在 Codespaces 執行 Python 生成 `web/index.html`，並透過 `python3 -m http.server 8080 --directory web` 搭配 Port Forwarding 進行全班 Live Demo。
</dm2026_context>

<embedded_code_or_spec>
請撰寫 `src/lab23_venn_site_gen.py`，此 Python 腳本執行後會寫出一個完全自足（Zero external JS/CSS dependencies）的 `web/index.html`，具備以下規格：
1. 視覺風格：暗黑科技感（背景 `#0a0a0f`、卡片 `#12121a` 搭配微光邊框），標題為「DM2026 Interactive Set Theory & Venn Explorer」。
2. SVG 幾何精準切割：使用 SVG `<defs>` + `<clipPath>` 與複合區域，精確獨立控制四個互斥區域：(1) Only A (`A \ B`)、(2) Intersection (`A ∩ B`)、(3) Only B (`B \ A`)、(4) Universe Outside (`(A ∪ B)'`)。
3. 互動控制面板：提供按鈕切換 `A ∩ B`, `A ∪ B`, `A \ B`, `B \ A`, `A ⊕ B`, `(A ∪ B)'`，並同時讓使用者在網頁輸入逗號分隔的 Set A 與 Set B（預設 `A = 1,2,3,4`、`B = 3,4,5,6`），即時計算並顯示結果集合與基數（Cardinality）。
</embedded_code_or_spec>

<task>
1. 產出完整的 `src/lab23_venn_site_gen.py`（使用 Python triple-quoted f-string 或 raw string 生成 `web/index.html`）。
2. 提供啟動 Port 8080 與測試連線 `curl -I http://localhost:8080` 的指令。
</task>

<output_contract>
- 產出單一完整可執行的 Python 腳本（嚴禁出現省略符號）。
- 確保生成的 HTML/JS 不依賴外部 CDN（即使離線或受限企業網路環境下也能 100% 正常渲染）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ python3 src/lab23_venn_site_gen.py
  [SUCCESS] Generated self-contained Venn Explorer at web/index.html (14,820 bytes)
  $ python3 -m http.server 8080 --directory web
  Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
  ```
  在瀏覽器開啟轉發的 `https://<codespace-name>-8080.app.github.dev/` 後，點擊 `A ⊕ B` 按鈕可見左右新月區域亮起，中間交集保持暗色，且即時計算顯示 `{1, 2, 5, 6}`。
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀 A**：開啟轉發連結出現 `502 Bad Gateway`。
    - **解法**：確認執行 `http.server` 的終端機視窗仍保持運行中（未被 `Ctrl+C` 中斷），且 Port 數字完全一致為 `8080`。
  - **症狀 B**：終端機被 `http.server` 佔用無法輸入其他指令。
    - **解法**：在 VS Code 終端機右上角點擊 `+` 新增第二個終端機分頁，或測試完畢後按 `Ctrl+C` 優雅關閉伺服器。

---

## Lab 24：神經符號自動化批改閘門：在 Codespaces 撰寫 `pytest` 單元測試自動驗證 `DM2026` 作業（替代人工截圖對帳）

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★★
- **Bloom's Level**: **L5 Evaluate（評鑑）** — 徹底淘汰傳統「學生截圖貼 Word、助教人工對帳 30 份作業」的脆弱流程，導入軟體工程級 **Deterministic Test Gate（確定性測試閘門）**：用 `pytest` 對 Lab 16–21 的離散數學模組進行自動化、零模糊空間的斷言驗證。
- **Course Weight**: 9%
- **Prerequisites（前置依賴數：3）**:
  1. 完成 Lab 16, 17, 19, 20, 21（已實作對應函式與 `discrete_toolkit/` 套件）。
  2. 了解 Python `assert` 陳述式基本語法。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 執行 `PYTHONPATH=. pytest -v tests/` 跑完至少 12 個測試案例（包含邊界測試 Edge Cases 如空集合 $\emptyset$ 與邏輯矛盾式，且涵蓋 `@pytest.mark.parametrize` 參數化測試），獲得 `100% PASSED` 且 Exit Code 為 `0` `THEN` 通過 Lab 24；`ELSE` 檢核失敗斷言之實際回傳值與預期數學規格差異。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **安裝測試框架 `pytest`**：在 Codespaces 終端機執行：
   ```bash
   python3 -m pip install --quiet pytest
   mkdir -p tests
   ```
2. **設計測試目錄與 `pytest.ini`**：在專案根目錄建立 `pytest.ini`，設定 `pythonpath = .`，從此執行 `pytest` 不再需要每次手動加上 `PYTHONPATH=.` 前綴。
3. **撰寫邏輯真值表測試（`tests/test_logic.py`）**：使用 `@pytest.mark.parametrize("p, q, expected", [...])` 一次測試 `implies(p, q)` 與 `iff(p, q)` 的全部 4 種真值組合，並測試 `PropositionEvaluator` 判定重言式之準確性。
4. **撰寫集合與冪集測試（`tests/test_sets.py`）**：驗證 `FiniteSet` 的交聯差運算、空集合邊界測試（$\mathcal{P}(\emptyset) = \{\emptyset\}$，基數為 $2^0 = 1$）、以及 5 元素集合冪集基數 $2^5 = 32$。
5. **撰寫二元關係與異常拋出測試（`tests/test_relations.py`）**：使用 `with pytest.raises(ValueError):` 主動測試「輸入越界元素至 `BinaryRelation` 建構子時是否正確拒絕並拋出異常」，證明防禦性設計真實有效！
6. **執行全自動化批改閘門**：執行 `pytest -v`，觀察綠色的 `PASSED` 報表逐項閃耀；刻意把某個函式改錯 1 個符號再跑一次 `pytest`，體驗紅燈（`FAILED`）如何精準定位 Bug 行號，再將其修復回綠燈。
7. **匯出 JUnit XML / 摘要報告**：執行 `pytest -v --junitxml=outputs/test_report.xml` 產生可供助教與 GitHub Actions CI 自動讀取的批改憑證。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是軟體測試工程師（SDET）與自動化評量架構師（Automated Grading Gate Architect）。
</epistemic_role>

<dm2026_context>
- 目標對象：針對 Lab 21 建立的 `discrete_toolkit/` 套件（`FiniteSet`, `BinaryRelation`, `PropositionEvaluator`）建立自動化 `pytest` 批改測試集。
- 核心理念：用確定性 Python 測試（Deterministic Verification）取代人工看截圖對帳，實現零遺漏品質門控。
</dm2026_context>

<embedded_code_or_spec>
請協助我建立以下測試套件檔案：
1. `pytest.ini`：設定 `pythonpath = .` 與 `testpaths = tests`。
2. `tests/test_discrete_toolkit.py`：包含至少 12 個單元測試（建議使用 `@pytest.mark.parametrize`），覆蓋：
   - `FiniteSet`: 空集合冪集 `len(FiniteSet(set()).power_set()) == 1`、標準 4 元素冪集基數 16、排容原理、`&` 與 `|` 運算子。
   - `BinaryRelation`: 等價關係判定（模同餘）、偏序關係判定（整除關係）、恆等關係同時為 Symmetric 與 Antisymmetric 之細膩驗證、越界序對觸發 `pytest.raises(ValueError)`、以及關係合成 `compose()`。
   - `PropositionEvaluator`: 蘊含真值 4 組合、De Morgan 重言式分類判定。
</embedded_code_or_spec>

<task>
撰寫完整的 `pytest.ini` 與 `tests/test_discrete_toolkit.py`，並說明助教如何透過單一指令 `pytest -q` 在 1 秒內自動批改整個倉庫的作業正確性。
</task>

<output_contract>
- 輸出完整可直接執行的測試檔案，零 placeholder。
- 每個測試函式皆須有清晰的 docstring 說明驗證的離散數學定理或邊界條件。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ pytest -v
  ========================= test session starts ==========================
  collected 14 items

  tests/test_discrete_toolkit.py::test_implies_truth_table[True-True-True] PASSED
  tests/test_discrete_toolkit.py::test_implies_truth_table[True-False-False] PASSED
  tests/test_discrete_toolkit.py::test_implies_truth_table[False-True-True] PASSED
  tests/test_discrete_toolkit.py::test_implies_truth_table[False-False-True] PASSED
  tests/test_discrete_toolkit.py::test_empty_power_set PASSED
  tests/test_discrete_toolkit.py::test_finiteset_inclusion_exclusion PASSED
  tests/test_discrete_toolkit.py::test_relation_identity_both_sym_and_antisym PASSED
  tests/test_discrete_toolkit.py::test_relation_partial_order_divisibility PASSED
  tests/test_discrete_toolkit.py::test_relation_equivalence_mod3 PASSED
  tests/test_discrete_toolkit.py::test_relation_invalid_domain_raises PASSED
  ...
  ========================== 14 passed in 0.08s ==========================
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀**：`pytest` 找不到 `discrete_toolkit` 或回傳 `collected 0 items`。
  - **解法**：確認測試檔名開頭為 `test_`（例如 `test_discrete_toolkit.py`），測試函式開頭亦必須為 `test_`，且專案根目錄存在 `pytest.ini`（含 `pythonpath = .`）。

---

## Lab 25：客製化 `DM2026` Dockerfile 與 Prebuild 加速策略（預先編譯 `numpy` + `matplotlib` 縮短冷啟動）

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★★
- **Bloom's Level**: **L5 Evaluate（評鑑）** — 理解「每次啟動 Codespace 都要手動 `pip install numpy matplotlib pytest`」會浪費寶貴課堂時間與學生 2-core 運算配額；透過設定 `.devcontainer/devcontainer.json`、`Dockerfile` 與 `requirements.txt`，實作環境即代碼（Environment-as-Code）與 Prebuild 預先建置架構。
- **Course Weight**: 6%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 22 與 Lab 24（明確知道本課程需要 `numpy`, `matplotlib`, `pytest`, `ipykernel`）。
  2. 了解容器映像檔（Container Image）與基礎 Linux `apt-get` / `pip` 層級快取概念。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` `.devcontainer/devcontainer.json` 通過 JSON 語法檢查、`.devcontainer/Dockerfile` 正確鎖定 Python 3.11 並預裝 `requirements.txt` 與 VS Code Python/Jupyter 延伸套件，且執行 `docker build` 驗證（或 `devcontainer` JSON Schema 檢核）零語法錯誤 `THEN` 通過 Lab 25；`ELSE` 檢核 `Dockerfile` 指令大小寫與層快取順序（`COPY requirements.txt` 應早於複製整份原始碼，避免改動程式就觸發全套重編）。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立 `.devcontainer/` 與依賴鎖定檔**：在專案根目錄建立 `.devcontainer/devcontainer.json`、`.devcontainer/Dockerfile` 與 `requirements.txt`。
2. **精確鎖定 Python 套件清單**：在 `requirements.txt` 明列所需版本下限，避免無上限飄移：
   ```text
   numpy>=1.26,<3.0
   matplotlib>=3.8,<4.0
   pytest>=8.0,<9.0
   ipykernel>=6.29,<7.0
   ```
3. **編寫 Layer-Cache 最佳化之 `Dockerfile`**：以官方 `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm` 為基底，先複製 `requirements.txt` 並執行 `pip install --no-cache-dir -r requirements.txt`（同時選配安裝 `fonts-noto-cjk` 徹底根治中文字型缺字！）。
4. **配置 `devcontainer.json` 自動化體驗**：
   - 指定 `"build": { "dockerfile": "Dockerfile", "context": ".." }`。
   - 在 `"customizations.vscode.extensions"` 自動宣告 `ms-python.python`、`ms-python.vscode-pylance`、`ms-toolsai.jupyter`、`GitHub.copilot`。
   - 預先開啟 `"forwardPorts": [8080]`，配合 Lab 23 一啟動即就緒！
5. **設定 GitHub Codespaces Prebuild 策略（理論與設定）**：了解如何在個人/課程 Repo 的 `Settings -> Codespaces -> Set up prebuild` 設定當 `main` 分支之 `.devcontainer/` 或 `requirements.txt` 異動時，由 GitHub Actions 在雲端預先編譯好映像檔快照（Snapshot），讓學生上課開啟 `2-core` Codespace 從 4 分鐘縮短至 **30 秒內秒開**！
6. **在本地/容器驗證 JSON 與 Dockerfile 語法**：利用 Python 內建 `json.tool` 檢查 `devcontainer.json` 是否為合法標準 JSON（不可有多餘尾逗號），並以靜態檢查腳本驗證檔案齊備度。
7. **確認不浪費額度的小秘訣**：注意若在已有 Codespace 內測試大面積修改 `Dockerfile`，可先確認邏輯正確後再觸發 **Rebuild Container**，或透過 `Lab 27` 合併至主倉庫由 Prebuild 統一構建。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是專精 DevContainers、Docker Layer Caching 與 GitHub Codespaces Prebuilds 效能調校的雲端基礎設施工程師。
</epistemic_role>

<dm2026_context>
- 目標倉庫：DM2026 離散數學課程倉庫
- 痛點：全班同學每次新建 2-core Codespace 時，若各自跑 `pip install numpy matplotlib` 與安裝中文字型，既慢又消耗有限免費額度；講師於 4-core fantastic-dollop 環境亦需確保與學生端環境 100% 一致（Zero "Works on my machine" drift）。
</dm2026_context>

<embedded_code_or_spec>
請產出以下 3 個環境設定檔與 1 個驗證腳本：
1. `requirements.txt`：包含 `numpy`, `matplotlib`, `pytest`, `ipykernel`。
2. `.devcontainer/Dockerfile`：基於 `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm`，預裝 `requirements.txt` 並利用 Docker Build Cache 最佳化順序；同時清理 `apt` 快取保持映像檔精瘦。
3. `.devcontainer/devcontainer.json`：無註解、無 trailing comma 的標準 JSON，宣告 Python/Jupyter/Copilot 擴充套件、`forwardPorts: [8080]` 與 `postCreateCommand: "python3 --version && pytest --version"`。
4. `src/lab25_verify_env.py`：一鍵檢查 `devcontainer.json` 合法性、檢查 `numpy`/`matplotlib`/`pytest` 是否已就緒，並估算安裝後對容器磁碟的影響。
</embedded_code_or_spec>

<task>
產出上述全部 4 個檔案之完整內容，並附上步驟說明如何在 GitHub Repository Settings 啟用 Prebuild，將課堂冷啟動時間大幅縮短。
</task>

<output_contract>
- `.devcontainer/devcontainer.json` 必須能通過 `python3 -m json.tool` 驗證（禁止 JSONC 註解或尾隨逗號）。
- 繁體中文解說 Docker Layer快取原理（為何 `COPY requirements.txt` 要放在最前面）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ python3 -m json.tool .devcontainer/devcontainer.json > /dev/null && echo "JSON VALID"
  JSON VALID
  $ python3 src/lab25_verify_env.py
  [OK] numpy 2.x installed
  [OK] matplotlib 3.x installed
  [OK] pytest 8.x installed
  [OK] ipykernel 6.x installed
  [OK] .devcontainer/Dockerfile & devcontainer.json syntax verified!
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀**：`Rebuild Container` 失敗，回報 `devcontainer.json parse error`。
  - **解法**：雖然 VS Code 支援 JSON with Comments (JSONC)，但部分自動化工具與 parser 不容許尾隨逗號（Trailing Commas）或註解。請永遠執行 `python3 -m json.tool .devcontainer/devcontainer.json` 確保嚴格合規！

---

## Lab 26：Codespaces 內建 GitHub Copilot / AI Agent 輔助除錯與時間複雜度重構實戰

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★☆
- **Bloom's Level**: **L4 Analyze（分析）** — 學會不盲從 AI 程式碼、而是以「結構化語境提示詞＋實測基準（Benchmarking）」驅動 Codespaces 內的 GitHub Copilot / AI 助手，將高複雜度離散演算法（例如 $O(n^3)$ 遞移閉包暴力搜尋或 $O(n^2)$ 重複元素檢查）重構為 $O(n)$ 雜湊查找或 Floyd-Warshall / 矩陣加速版，並用 `time.perf_counter()` 實測前後加速比。
- **Course Weight**: 6%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 20 與 Lab 24（能撰寫關係/集合演算法並用 `pytest` 保護正確性）。
  2. 理解 Big-O 時間複雜度基礎（$O(n^3)$ vs $O(n^2)$ vs $O(n)$）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 學生針對 `src/lab26_complexity_refactor.py` 中的慢速暴力演算法完成優化重構、通過原本全部等價性斷言測試（確保「加速不改錯語意」），且實測 $n=300$ 節點或 $n=10,000$ 筆資料時取得至少 **10× 以上** 之實測加速比 `THEN` 通過 Lab 26；`ELSE` 檢核優化前後輸出是否仍完全等價（Semantic Equivalence）。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **建立效能基準與基準慢速版本**：建立 `src/lab26_complexity_refactor.py`，放入兩個教學用「刻意慢速（Naive）」離散數學函式：
   - **案例 A（兩數之和存在性判定 / 集合查找）**：給定 $n=10,000$ 筆數字與目標值 $K$，使用雙層迴圈 $O(n^2)$ 尋找是否存在 $a + b = K$。
   - **案例 B（圖形可達性 / 遞移檢驗升級）**：給定 $n=250$ 個節點的關係矩陣，使用暴力遞迴/重複掃描序對配對，對比鄰接集合查表或動態規劃。
2. **運用 `pytest` 鎖定黃金基線（Golden Baseline）**：先撰寫斷言確認兩個 Naive 函式在小規模測試資料上 100% 正確——這正是軟體工程的鐵律：**「先有測試鎖住正確性，才請 AI 重構效能」**。
3. **在 Codespaces 開啟 Copilot Chat / AI 面板**：選取 `find_pair_naive` 與 `has_triangle_naive`（偵測有向圖是否存在長度為 3 的環或三元遞移）函式，按下 `Ctrl+I`（Inline Chat）或開啟側邊 Chat，貼入本 Lab 下方提供的 XML Bento 提示詞。
4. **審核 AI 產出的複雜度重構方案**：要求 AI 說明重構後的時間複雜度（Time Complexity）與空間複雜度（Space Complexity）權衡（Space-Time Tradeoff），例如以 `set` 雜湊表將 $O(n^2)$ 降維至 $O(n)$；以及用鄰接集合交集檢查將三元檢查降維。
5. **執行實測 Benchmark**：利用 Python 標準庫 `time.perf_counter()` 在相同隨機種子資料集上分別計時 Naive 與 Optimized 版本，驗證兩者回傳值完全一致且印出 Speedup 倍數。
6. **檢查無 AI 幻覺（Anti-Hallucination Audit）**：逐行檢視 AI 寫出的邊界條件（例如 $a + b = K$ 時，是否誤把同一個元素重複使用兩次，如 $K=10$ 且陣列只有一個 `5`！）。
7. **存檔並執行驗證**：於終端機執行 `python3 src/lab26_complexity_refactor.py`，記錄量化加速成果。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是專精演算法時間複雜度分析（Big-O Analysis）與安全重構（Test-Protected Refactoring）的 AI Pair Programmer。
</epistemic_role>

<dm2026_context>
- 場景：在 GitHub Codespaces 2-core 環境中，對離散數學演算法進行效能重構，同時保證語意 100% 等價且不產生「同索引重複取用」等邊界 Bug。
</dm2026_context>

<embedded_code_or_spec>
以下兩段 Naive 實作在資料量變大時會造成 2-core Codespace CPU 瓶頸，請協助重構並附帶 Benchmark：

~~~python
def has_pair_sum_naive(nums: list[int], target: int) -> bool:
    """O(n^2) brute-force check if two distinct indices i != j have nums[i] + nums[j] == target."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

def count_common_neighbors_naive(adj_list: dict[int, list[int]], u: int, v: int) -> int:
    """O(|N(u)| * |N(v)|) naive loop to count common neighbors in a graph."""
    count = 0
    for x in adj_list.get(u, []):
        for y in adj_list.get(v, []):
            if x == y:
                count += 1
    return count
~~~
</embedded_code_or_spec>

<task>
1. 針對上述兩個函式分別寫出優化版本 `has_pair_sum_fast`（時間複雜度 $O(n)$）與 `count_common_neighbors_fast`（使用 Python `set` 交集運算 `len(set_u & set_v)`）。
2. 嚴格防範邊界陷阱：當 `nums = [5]`、`target = 10` 時，`has_pair_sum_fast` 必須回傳 `False`（因為必須是不同索引 `i != j`）。
3. 撰寫完整的 `src/lab26_complexity_refactor.py`，包含黃金邊界測試斷言與 `n = 8000` 之 `time.perf_counter()` 實測對比報表。
</task>

<output_contract>
- 輸出完整可直接執行的 `src/lab26_complexity_refactor.py`。
- 附上「AI 程式碼審查 3 問檢核表」（索引唯一性、重複元素處理、空輸入邊界）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ python3 src/lab26_complexity_refactor.py
  [Unit Guards] Single element [5], target 10 -> False (PASS)
  [Unit Guards] Duplicate [5, 5], target 10  -> True  (PASS)
  [Benchmark n=8000 Pair Sum]
    Naive O(n^2): 1.2450 s -> Result: True
    Fast  O(n)  : 0.0004 s -> Result: True
    Speedup     : 3112.5x faster!
  [Benchmark Graph Common Neighbors |N|=5000]
    Naive O(N^2): 0.4820 s -> Common: 1248
    Fast  O(N)  : 0.0003 s -> Common: 1248
    Speedup     : 1606.7x faster!
  ```
- **防呆與排錯檢核（Troubleshooting）**：
  - **常見陷阱**：若 AI 把 `has_pair_sum_fast` 寫成先把整個 `nums` 丟進 `seen = set(nums)` 再遍歷檢查 `target - x in seen`，這在 `nums = [5], target = 10` 時會錯判成 `True`！正確寫法是**邊走邊存**：先檢查 `(target - x) in seen`，若無才 `seen.add(x)`。這就是為何人類工程師必須做 Edge-Case Audit。

---

## Lab 27：多人協作與 Pull Request 閉環：從個人 Fork 發起 PR 貢獻至 `Grace-TA/DM2026` 並進行 Code Review

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★★
- **Bloom's Level**: **L5 Evaluate（評鑑）** — 熟練開源協作與現代軟體團隊的 Git 分支模型（Feature Branch Workflow）：從個人 Fork 建立功能分支、同步上游（`upstream`）、在通過 `pytest` 閘門後推送至遠端並發起結構化的 **Pull Request (PR)** 至 `Grace-TA/DM2026`（或模擬同儕相互 PR Code Review）。
- **Course Weight**: 7%
- **Prerequisites（前置依賴數：2）**:
  1. 完成 Lab 24 與 Lab 25（擁有通過 `pytest` 的程式碼與標準化專案結構）。
  2. 擁有個人 Fork 倉庫（`<your-username>/DM2026`）及與上游 `https://github.com/Grace-TA/DM2026` 之連結關係。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 學生能在非 `main` 分支（如 `feat/student-id-discrete-toolkit`）完成至少 1 筆乾淨 Commit、設定並 fetch `upstream` 確認無合併衝突（Zero Merge Conflicts）、跑完 `pytest` 全數通過後推上個人 Fork，並產出含 **PR Summary + Test Evidence + Checklist** 之 Pull Request（實發至課程指定上游或同儕 Fork 演練） `THEN` 通過 Lab 27；`ELSE` 檢核 `git remote -v` 與目前所在分支 `git branch --show-current`。

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **盤點遠端倉庫設定**：在 Codespaces 終端機執行 `git remote -v`，確認 `origin` 指向你的個人 Fork（`https://github.com/<your-username>/DM2026.git`）。若尚未設定上游教師倉庫，新增 `upstream`：
   ```bash
   git remote add upstream https://github.com/Grace-TA/DM2026.git
   git fetch upstream
   ```
2. **禁止直接在 `main` 開發，建立功能分支**：從最新主線切出專屬分支（將 `student_id` 換成你的學號）：
   ```bash
   git checkout -b feat/lab27-student_id-dm-toolkit
   ```
3. **與上游主線同步（防止衝突）**：執行 `git merge upstream/main`（若提示無關歷史或已最新則確認狀態）；倘若出現任何衝突，使用 VS Code 內建的 3-Way Merge Editor 解決後重新測試。
4. **執行合併前強制品質閘門（Pre-PR Quality Gate）**：執行 `pytest -v`，確保所有測試在本次分支改動後依然 100% 綠燈通過，且無暫存垃圾檔（如 `__pycache__/` 應被 `.gitignore` 排除）。
5. **整理 `.gitignore` 並提交乾淨 Commit**：確保 `.gitignore` 排除 `__pycache__/`, `*.pyc`, `.pytest_cache/`, `outputs/*.png`（視作業規定決定是否忽略暫存圖檔）後，執行：
   ```bash
   git status
   git add discrete_toolkit/ tests/ pytest.ini src/ .gitignore
   git commit -m "feat(dm2026): add discrete_toolkit OOP suite and pytest verification"
   ```
6. **推送功能分支至個人 Fork**：
   ```bash
   git push -u origin feat/lab27-student_id-dm-toolkit
   ```
7. **發起 Pull Request 與同儕 Code Review**：前往 GitHub 網頁點選 **Compare & pull request**（選擇 Base repository: `Grace-TA/DM2026` 或模擬對練倉庫，Head repository: `<your-username>/DM2026` 的功能分支）；依下方提示詞產出標準 PR 描述並指派 Reviewer。

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是精通 Git 分支協作（Fork & Pull Request Workflow）與高品質 Code Review 規範的開源專案維護者（Maintainer）。
</epistemic_role>

<dm2026_context>
- 上游倉庫 (upstream)：https://github.com/Grace-TA/DM2026
- 學生端 (origin)：https://github.com/<your-username>/DM2026 (2-core Codespace)
- 任務目標：將 Lab 21 的 `discrete_toolkit/` 與 Lab 24 的 `tests/` 透過標準 Pull Request 流程提交審查，並建立防呆 `.gitignore`。
</dm2026_context>

<embedded_code_or_spec>
請提供以下兩項產物：
1. 適合 `DM2026` Python 專案的標準 `.gitignore` 內容（排除 `__pycache__/`, `.pytest_cache/`, `*.py[cod]`, `.venv/`, `.DS_Store`）。
2. 一份結構化、可直接貼上 GitHub Pull Request 頁面的 PR Description 範本（Markdown 格式），以及一份 5 點 Code Review 自檢與互評清單（涵蓋 Type Hints、Docstrings、Edge Cases、Test Coverage、Zero Secrets Leak）。
</embedded_code_or_spec>

<task>
1. 輸出標準 `.gitignore` 檔案內容。
2. 產出中英雙語的 PR 範本（含 `## Summary`, `## Changes`, `## Verification (pytest output)`, `## Reviewer Checklist`）。
3. 說明若使用 GitHub CLI (`gh pr create`) 在 Codespaces 終端機一行指令建立 PR 的做法。
</task>

<output_contract>
- 不可要求停用 SSL 驗證或強制覆寫上游歷史（嚴禁教導 `git push --force` 至共用分支）。
- 繁體中文搭配標準 Git 術語（Fork, Upstream, Origin, Feature Branch, Fast-forward, Code Review）。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ git branch --show-current
  feat/lab27-b1150001-dm-toolkit
  $ git status -s
  nothing to commit, working tree clean
  $ git log -1 --oneline
  a4f9c21 feat(dm2026): add discrete_toolkit OOP suite and pytest verification
  ```
  在 GitHub PR 頁面可見 `Files changed` 僅包含乾淨的原始碼與測試檔（無 `__pycache__` 二進位快取污染），且 PR 描述內附有 `14 passed` 測試截圖/紀錄。
- **防呆與排錯檢核（Troubleshooting）**：
  - **症狀 A**：執行 `git push` 時發現 `origin` 誤設為 `Grace-TA/DM2026` 導致出現 `Permission denied (403)`！
    - **解法**：你開到了教師原倉庫的 Codespace 或 clone 了原網址而非你自己的 Fork。執行 `git remote set-url origin https://github.com/<your-username>/DM2026.git` 修正為你自己的 Fork 後即可推送。
  - **症狀 B**：不小心把 `__pycache__/*.pyc` 已經 commit 進去了怎麼辦？
    - **解法**：先在 `.gitignore` 加入 `__pycache__/`，再執行 `git rm -r --cached __pycache__` 並補一個新 commit 即可從追蹤名單移除（本機檔案不會消失）。

---

## Lab 28：終極 Hero Capstone — 打造「DM2026 雲端離散數學實驗室」＋課後配額清零歸位儀式（`Commit -> Push -> Verify -> Delete Codespace`）

### 🎯 學習目標與量化指標（L.A.W. Anchored）
- **Difficulty**: ★★★（總整合大魔王關卡）
- **Bloom's Level**: **L6 Create（創造）** — 將前 27 個 Labs 鍛造出的離散數學引擎（Truth Table、Set Power Set、Binary Relation、Matplotlib 視覺化與 HTML/SVG 互動站）整合為單一統整入口實驗室 `dm2026_hero_lab.py`（具備一鍵跑完所有計算、繪圖、測試並生成總結報告之 Pipeline），最後嚴格執行 **「課後配額清零歸位儀式」**，保護個人免費 120 core-hours 額度不無謂流逝！
- **Course Weight**: 7%（學期核心成果總驗收）
- **Prerequisites（前置依賴數：4）**:
  1. 完成 Lab 15–22（具備 `WEEK01`–`WEEK03` 完整離散數學與視覺化能力）。
  2. 完成 Lab 23–24（具備靜態網頁生成與 `pytest` 自動批改門檻）。
  3. 完成 Lab 25 與 Lab 27（具備專案結構化與 Git Push 上傳紀律）。
- **Pass Threshold（IF-THEN 判定契約）**:
  - `IF` 一鍵執行總控腳本 `python3 src/lab28_hero_capstone.py` 能依序串接：(1) `discrete_toolkit` 核心運算、(2) 產出 `outputs/` 兩張 300-DPI PNG、(3) 生成整合型 `web/hero_report.html` 總覽儀表板、(4) 觸發 `pytest` 全數通過、且學生最後確實完成 `Commit -> Push -> Verify on GitHub Web -> Delete Codespace` 四步歸位儀式（遠端 GitHub 頁面可見最新程式碼與時間戳記） `THEN` 通過 Lab 28 與整個 Workshop；`ELSE` 絕對禁止在未驗證 Push 成功前刪除 Codespace！

### 🛠️ 學生完整操作步驟（Complete Student Guide）
1. **撰寫終極整合中樞 `src/lab28_hero_capstone.py`**：設計一個主控 Orchestrator CLI，串聯並展示整套課程精華：
   - 呼叫 `discrete_toolkit` 的 `PropositionEvaluator`、`FiniteSet`、`BinaryRelation` 輸出關鍵離散數學驗證結論。
   - 產出高畫質 Matplotlib 4 相位三角波與單位圓圖表至 `outputs/`。
   - 整合產出最終單頁學習成果儀表板 `web/hero_report.html`（自動嵌入實驗結果數據、數學恆等式總表、與 UTC+8 學期完訓時間戳記）。
   - 透過 `subprocess.run(["pytest", "-q"])` 內嵌執行自動化品質閘門，僅當 Exit Code == `0` 時才印出 `[HERO CERTIFIED]`！
2. **撰寫專案總門面 `README.md` 摘要段落**：在專案檔案總結中記錄你的環境規格（Student `2-core` Codespace）、測試指令（`pytest -v`）與 Hero Capstone 一鍵執行指令。
3. **執行終極整合驗收**：於終端機執行：
   ```bash
   PYTHONPATH=. python3 src/lab28_hero_capstone.py
   ```
   確認所有子步驟綠燈通過且無任何 Exception。
4. **執行歸位儀式 Step 1 — Commit（封存所有心血）**：
   ```bash
   git status
   git add .
   git commit -m "chore(capstone): complete DM2026 Hero Lab 15-28 integration"
   ```
5. **執行歸位儀式 Step 2 — Push（同步至 GitHub 雲端永生保存）**：
   ```bash
   git push origin HEAD
   ```
   務必親眼看到終端機回傳分支推送成功訊息（無 Rejected / Error）。
6. **執行歸位儀式 Step 3 — Verify（網頁端雙重確認，黃金防呆鐵律！）**：
   打開瀏覽器登入 `https://github.com/<your-username>/DM2026`，切換到你剛推送的分支，親眼確認 `discrete_toolkit/`、`tests/`、`src/lab28_hero_capstone.py` 與最新 Commit 時間確實已出現在 GitHub 網頁上！（**絕不憑感覺假設已上傳**）
7. **執行歸位儀式 Step 4 — Delete Codespace（配額清零歸位！）**：
   確認遠端 GitHub 網頁已安全存檔後，前往 `https://github.com/codespaces`，找到你剛才使用的 `2-core` Codespace，點擊右側 `...` 選單 -> **Delete**。
   - **為何要 Delete 而不是只 Stop？**：Stopped 狀態雖不再消耗 `2-core` CPU 計算配額（120 core-hours/月），但仍會持續佔用免費的 **Storage 儲存空間配額**（15 GB-month）；只要程式碼都已 Push 回 GitHub 倉庫，刪除容器即可實現 **CPU + Storage 雙歸零**，下次上課 30 秒內就能透過 Prebuild 重新誕生一個乾淨無垢的容器！

### 📋 完整語境提示詞（Complete Context Prompt）

```markdown
<epistemic_role>
你是 Muse Academy（繆思學院）的首席系統總工程師，負責設計「DM2026 雲端離散數學實驗室」的終極一鍵整合腳本與課後安全歸位自動化檢查程序。
</epistemic_role>

<dm2026_context>
- 總整目標：把 WEEK01–WEEK03 遷移成果（`discrete_toolkit/`, Matplotlib 視覺化, SVG/HTML 報告, `pytest` 批改閘門）整合為單一 Hero Capstone Pipeline。
- 運維鐵律：學生使用 2-core 免費配額 Codespace，每次下課必須執行「Commit -> Push -> Verify -> Delete Codespace」四步儀式，避免 Storage 與 Core-hour 配額枯竭。
</dm2026_context>

<embedded_code_or_spec>
請實作 `src/lab28_hero_capstone.py`，執行後依序完成以下 5 個 Stage：
- Stage 1：呼叫 `discrete_toolkit`（`FiniteSet`, `BinaryRelation`, `PropositionEvaluator`）計算並收集離散數學驗證摘要字典。
- Stage 2：調用無頭 Matplotlib（`Agg`）生成或確認 `outputs/lab22_unit_circle.png` 存在且非空。
- Stage 3：執行 `subprocess.run([sys.executable, "-m", "pytest", "-q"], check=False)` 自動驗證所有單元測試，捕捉通過數量與 Exit Code。
- Stage 4：生成自足暗黑風格結業報告 `web/hero_report.html`（顯示三大模組狀態卡片、測試結果、以及 UTC+8 完訓時間戳記）。
- Stage 5：自動執行只讀 Git 安全檢查（`git status --porcelain` 與 `git log -1 --oneline`），若偵測到還有未 Commit/Push 的檔案，主動在終端機印出紅色警告提示「⚠️ 尚有未推送變更，禁止刪除 Codespace！」。
</embedded_code_or_spec>

<task>
1. 撰寫完整可執行的 `src/lab28_hero_capstone.py`（Zero placeholders）。
2. 提供一份終端機「四步歸位儀式（Commit -> Push -> Verify -> Delete）」的逐步執行指令清單。
</task>

<output_contract>
- Python 程式碼必須跨平台兼容並明確處理 `PYTHONPATH`（自動將專案根目錄加入 `sys.path`）。
- 繁體中文清楚解釋為何「Stopped」仍消耗 Storage 配額而「Push 後 Delete」才是免費額度最佳化（Zero-Quota-Waste）的標準實踐。
</output_contract>
```

### ✅ 驗收標準與防呆檢核
- **預期執行輸出（Expected Output）**：
  ```text
  $ python3 src/lab28_hero_capstone.py
  ============================================================
  DM2026 HERO CAPSTONE ORCHESTRATOR (UTC+8: 2026-10-05 17:10:00)
  ============================================================
  [Stage 1] discrete_toolkit Verification -> PASS (Set/Relation/Logic)
  [Stage 2] Headless Visualization Check -> PASS (outputs/lab22_unit_circle.png)
  [Stage 3] Pytest Quality Gate          -> PASS (exit_code=0)
  [Stage 4] Hero Dashboard Generated     -> web/hero_report.html (6,412 bytes)
  [Stage 5] Git Working Tree Check       -> WARNING: Uncommitted changes detected!
            Run: git add . && git commit -m "..." && git push origin HEAD
            Verify on GitHub web BEFORE deleting your Codespace!
  ============================================================
  ```
  執行完 `git add . && git commit && git push` 後再跑一次確認 Stage 5 顯示 `CLEAN & SYNCED`，接著至 GitHub 網頁確認無誤並安全刪除 Codespace！
- **防呆與排錯檢核（Troubleshooting）**：
  - **生死紅線（Critical Warning）**：**絕對禁止在 `git push` 失敗或未上 GitHub 網頁確認前點擊 `Delete Codespace`！** 一旦容器被刪除，容器內尚未 Push 的所有檔案（包含你的 `src/` 與 `notebooks/`）將永久消失且無法還原。務必牢記口訣：**Commit → Push → Verify on Web → Delete**！
  - **配額估算備忘**：GitHub 個人免費方案每月提供 120 core-hours（即 `2-core` 容器可跑 60 小時/月）與 15 GB-month 免費儲存空間；養成每次實習結束執行歸位儀式的習慣，一學期 18 週每週實作 3 小時（約 54 小時/學期，平均 13.5 小時/月）將游刃有餘、永遠 $0.00 費用！

---

## 📊 Book 4 學習成效總結與下一步建議（Next Actions）

完成 Lab 15 至 Lab 28 後，你已成功將 `Grace-TA/DM2026` 從「單純瀏覽 Google Colab 筆記」進化為具備 **OOP 套件架構、無頭科學視覺化、SVG 互動網頁、自動化 `pytest` 批改閘門、DevContainer Prebuild、AI 複雜度重構與 Fork/PR 協作閉環** 的現代雲端離散數學工程師！

| # | 下一步高影響力行動（Action） | 預估時間 | 對學生／教師之核心價值（Impact） | 三把火融合度（Fusion Level） |
|:-:|:----------------------------|:--------:|:--------------------------------|:----------------------------|
| 1 | 為 `Grace-TA/DM2026` 啟用 GitHub Actions CI（`.github/workflows/ci.yml`）自動對學生 PR 跑 `pytest` | 30 分鐘 | 實現 100% 零人工介入的自動作業批改，徹底淘汰截圖對帳 | 教學 × 溫故（工程紀律自動化） |
| 2 | 將 `discrete_toolkit/` 擴充至圖論（Graph BFS/DFS、Dijkstra 最短路徑與樹狀結構） | 2 小時 | 無縫銜接離散數學期中／期末進階章節實作 | 教學 × 修行（結構化思維演進） |
| 3 | 使用 `web/index.html` 與 `web/hero_report.html` 在課堂以講師 `4-core` Codespace (`fantastic-dollop`) 進行 Live 互動教學 | 15 分鐘 | 學生用手機或筆電打開轉發網址即可即時操作溫氏圖與驗算 | 智慧融合（教學 × 修行 × 溫故） |
