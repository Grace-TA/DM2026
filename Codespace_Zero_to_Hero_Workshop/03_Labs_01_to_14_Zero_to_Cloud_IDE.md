# ⚒️ Book 3：零基礎到雲端 IDE 英雄實戰手冊（Labs 01–14: Zero to Cloud IDE Hero）

> **課程載體**：`https://github.com/Grace-TA/DM2026`（115學年第1學期 離散數學 Discrete Math.）  
> **學院架構**：繆思學院 Muse Academy × 中華大學 CHU CSIE-ISA — *「別再讓本機環境安裝毀掉你的學習熱情，一鍵開啟雲端鍛造工坊！」*  
> **鍛造隱喻（Trade Metaphor）**：☁️ **雲端鍛造工坊（Cloud Forge Workshop）**——Fork 是複製主設計圖、2-Core Codespace 是專屬個人雲端工作台、`.devcontainer` 是標準化鑄模、Port Forwarding 是作品展示櫥窗、FinOps 是燃料精算儀表板。

---

## 🗺️ 工作坊拓撲與資源配置基準（Workshop Topology & Grounding）

在進入 14 個實戰實驗之前，先釐清「教師端（Instructor）」與「學生端（Student）」的雲端基礎設施邊界：

| 角色（Role） | 目標儲存庫（Target Repo） | 運算規格（Machine Spec） | 區域（Region） | 存取位址與權限邊界（Access & Boundary） |
|:---|:---|:---|:---|:---|
| **授課教師（Instructor）** | `https://github.com/Grace-TA/DM2026` | `4-core • 16GB RAM • 32GB` | Southeast Asia | `https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/`（僅限擁有者 `Grace-TA` 存取，用於投影示範與 VS Code Live Share 遠端救援） |
| **修課學生（Student）** | 個人 Fork 之 `<YOUR_ID>/DM2026` | `2-core • 8GB RAM • 32GB` | Southeast Asia | 透過個人 GitHub 帳號免費額度開啟（每月 `120 core-hrs` = `60 hrs` 2-core 計算時間；`15 GB-months` 儲存空間） |

> **為什麼我們要從 `WEEK01.md`～`WEEK03.md` 的 Google Colab 截圖，全面升級到 GitHub Codespaces？**  
> 檢視目前 `Grace-TA/DM2026` 儲存庫內容：`WEEK01.md`（My first Google Colab）、`WEEK02.md`（Python 101：Calendar、`math` 模組、實作 1135/1140/1160/1171/1175、9×9 乘法表）、`WEEK03.md`（迴圈、Dict/Set、OOP、`try-except`、Matplotlib & NumPy）皆以截圖形式留存於 Markdown 中。透過這 14 個階段式實驗，你將學會建立真實、可版本控制、可跨裝置一鍵重建的 Python 工程環境，將截圖真正鍛造為可執行的軟體資產！

---

## 📚 14 大階梯式實戰實驗總覽（14-Lab Curriculum Blueprint）

| Cycle | Lab | 主題名稱 | 難度 | Bloom's Level | 權重 | 驗收門檻（L.A.W. Pass Gate） |
|:---:|:---:|:---|:---:|:---:|:---:|:---|
| **Cycle 1** | **Lab 01** | Fork `Grace-TA/DM2026` 與開啟 2-Core 東南亞 Codespace | ★☆☆ | L2–L3 | 6% | `IF` 個人 Fork 成功建立且 2-core 容器於 Southeast Asia 啟動 `THEN PASS` |
| **00:00–00:15** | **Lab 02** | 探索 VS Code Web 介面與資源硬體健檢 | ★☆☆ | L2–L4 | 6% | `IF` `lscpu`/`free -h`/`df -h` 實測數值精確比對 2-core vs 4-core `THEN PASS` |
| **Cycle 2** | **Lab 03** | 雲端 Terminal 健檢與 Python / Git 遠端驗證 | ★☆☆ | L3 | 6% | `IF` `python3 --version` 與 `git remote -v` 指向個人 Fork `THEN PASS` |
| **00:15–00:30** | **Lab 04** | 建立 `feat/student-workshop` 分支與 `hello_codespace.py` | ★☆☆ | L3 | 7% | `IF` 位於新分支且腳本正確輸出離散數學環境報告 `THEN PASS` |
| | **Lab 05** | `.vscode/settings.json` 與擴充套件雲端漫遊 | ★★☆ | L3–L4 | 7% | `IF` Python/Jupyter 擴充套件就緒且 Settings JSON 合法解析 `THEN PASS` |
| **Cycle 3** | **Lab 06** | 免設定密碼的 Git 閉環工作流（`add/commit/push`） | ★☆☆ | L3 | 7% | `IF` `feat/student-workshop` 分支成功推送至個人 GitHub Fork `THEN PASS` |
| **00:30–00:45** | **Lab 07** | 解剖與撰寫 `.devcontainer/devcontainer.json`（Python 3.12） | ★★☆ | L4–L5 | 8% | `IF` `devcontainer.json` 含 Python 3.12 映像與 `postCreateCommand` `THEN PASS` |
| | **Lab 08** | 執行 `Rebuild Container` 與 IaC 容器邊界驗證 | ★★☆ | L4–L5 | 8% | `IF` 重建後 `python3 -V` 為 `3.12.x` 且容器內系統套件與預裝函式庫自動生效 `THEN PASS` |
| **Cycle 4** | **Lab 09** | 啟動 HTTP 靜態展示伺服器與 Port Forwarding 實戰 | ★★☆ | L3–L4 | 7% | `IF` Port `8000` 可正常轉發並測試 Private / Public 可見度差異 `THEN PASS` |
| **00:45–01:00** | **Lab 10** | 雙向檔案傳輸：本地拖曳上傳與成果匯出下載 | ★★☆ | L3 | 6% | `IF` 完成本機 CSV 上傳運算並將結果檔成功下載回本機 `THEN PASS` |
| | **Lab 11** | GitHub CLI（`gh codespace`）遠端管理與 Token 權限實測 | ★★☆ | L4 | 8% | `IF` 完成 `gh cs list` / `ports` / `stop` 操作或正確診斷 Token Scope `THEN PASS` |
| **Cycle 5** | **Lab 12** | Codespaces Secrets 安全注入與 `.gitignore` 防洩漏壓測 | ★★☆ | L4–L5 | 8% | `IF` 金鑰僅存於環境變數且 `.gitignore` 成功攔截 `.env` 追蹤 `THEN PASS` |
| **FinOps &** | **Lab 13** | FinOps 配額精算與 Stop vs Delete 32GB 磁碟計費陷阱 | ★★☆ | L4–L5 | 8% | `IF` 正確算出 120 core-hrs 與 15 GB-months 警戒線並完成 Stop 實測 `THEN PASS` |
| **Rescue** | **Lab 14** | 環境損壞救援：`git diff`、Rebuild 與 Live Share 協作排錯 | ★★★ | L5–L6 | 8% | `IF` 成功修復毀損的 `devcontainer.json` 並完成 Live Share 診斷演練 `THEN PASS` |

---

# 🌅 Cycle 1（00:00–00:15）：Cloud Awakening — 雲端覺醒與工作台建立

## Lab 01：Fork `Grace-TA/DM2026` 與開啟首個 2-Core 東南亞 Codespace (Forking DM2026 & Launching a 2-Core Southeast Asia Codespace)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★☆☆（基礎啟航） |
| **Bloom's 認知層級** | `L2 Understand`（理解 GitHub 帳號與容器隔離邊界）＋ `L3 Apply`（執行 Fork 與雲端建立） |
| **課程評分權重（Weight）** | `6%`（佔本次工作坊總成績 6/100） |
| **前置依賴（Prerequisites）** | `0` 個實驗前置；需具備有效 GitHub 個人帳號與現代瀏覽器（Chrome / Edge / Firefox） |
| **通過門檻（Pass Threshold）** | `IF` (1) 點擊教師端 URL `fantastic-dollop` 驗證出權限隔離訊息，AND (2) 個人帳號下成功產生 `<GITHUB_USER>/DM2026` Fork，AND (3) 成功於 `Southeast Asia` 區域啟動 `2-core` Codespace `THEN PASS`；`ELSE` 重新檢查 Fork 來源與 Machine Type 設定。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **實測教師端 Codespace 的權限隔離邊界**：
   - 在瀏覽器新分頁直接貼上老師投影畫面的 Codespace URL：`https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/`。
   - 觀察 GitHub 的回應畫面（預期會出現 GitHub 登入驗證或 `404 / You don't have access to this codespace` 提示）。
   - **認知建立**：GitHub Codespaces 預設採取**單一擁有者零信任隔離（Owner-Scoped Isolation）**——你不能直接「進入」老師的 `4-core` 容器，必須透過 **Fork** 建立屬於自己的儲存庫副本與個人雲端容器。
2. **前往教師原始儲存庫**：
   - 登入你的 GitHub 帳號後，在瀏覽器開啟目標 Repo：`https://github.com/Grace-TA/DM2026`。
   - 確認頁面顯示 `115學年第1學期, 離散數學 (Discret Math.)`，且根目錄包含 `README.md`、`WEEK01.md`、`WEEK02.md`、`WEEK03.md`。
3. **建立個人 Fork 副本**：
   - 點擊頁面右上角的 **Fork** 按鈕（位於 `Notifications` 與 `Star` 之間）。
   - 在 `Create a new fork` 畫面中確認：
     - **Owner**：選擇你自己的 GitHub 帳號。
     - **Repository name**：維持 `DM2026`。
     - **Copy the `main` branch only**：保持勾選（Checked）。
   - 點擊綠色按鈕 **Create fork**，等待 2–3 秒跳轉至 `https://github.com/<你的帳號>/DM2026`。
4. **以進階選項開啟 2-Core 東南亞 Codespace**：
   - 在你自己 Fork 出來的 Repo 頁面中，點擊綠色 **`<> Code`** 按鈕，切換至 **`Codespaces`** 分頁。
   - **切勿直接點大按鈕**，請點擊右側 **`...`（More options）** → 選擇 **`New with options...`**，確保精準控制運算規格與機房區域。
5. **設定硬體與低延遲區域（FinOps & Latency 雙重鎖定）**：
   - **Branch**：`main`
   - **Dev container configuration**：`Default project configuration`
   - **Region**：選擇 **`Southeast Asia`**（新加坡機房，台灣連線延遲通常低於 60 ms）
   - **Machine type**：選擇 **`2-core • 8GB RAM • 32GB storage`**（免費額度最省耗選擇，每月可運行高達 60 小時）
6. **啟動並完成首次開機檢核**：
   - 點擊 **Create codespace**，瀏覽器將開啟新分頁並開始拉取預設通用映像檔（約需 30–60 秒）。
   - 當左側 **Explorer（檔案總管）** 顯示 `README.md`、`WEEK01.md`、`WEEK02.md`、`WEEK03.md`，且下方 Terminal 出現提示字元（例如 `@your-id ➜ /workspaces/DM2026 (main) $`），代表雲端工作台鍛造成功。

### 📋 完整語境提示詞（Complete Context Prompt）

請將以下完整 XML Bento 提示詞複製並貼入 Codespaces 右側 **GitHub Copilot Chat**（或任意 AI 助手），協助你核對權限隔離邏輯與啟動狀態：

````markdown
<epistemic_role>
You are the Muse Academy Cloud Infrastructure TA (繆思學院雲端助教). Explain GitHub Codespaces tenancy, Fork topology, and regional latency optimization with engineering precision in Traditional Chinese while keeping official GitHub technical terms in English.
</epistemic_role>

<environment_context>
- Course Repo: https://github.com/Grace-TA/DM2026 (115學年第1學期 離散數學 Discrete Math.)
- Repo Files: README.md, WEEK01.md, WEEK02.md, WEEK03.md
- Instructor Codespace: https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/ (4-core, 16GB RAM, 32GB storage, Southeast Asia)
- Student Target Topology: Personal Fork of Grace-TA/DM2026 -> 2-core, 8GB RAM, 32GB storage, Southeast Asia
- Free Tier Allowance: 120 core-hours/month compute, 15 GB-months/month storage
</environment_context>

<embedded_artifact>
Observed HTTP & UI Telemetry from Student Browser Session:
1. Direct visit to https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/
   -> Result: GitHub Codespaces Auth Gate / Access Denied (Owner-bound container; student identity does not match Grace-TA).
2. Fork Creation Check:
   -> Source: Grace-TA/DM2026 (12 commits on main)
   -> Destination: student-fork/DM2026 (forked from Grace-TA/DM2026)
3. Codespace Launch Options Selected:
   -> Region: Southeast Asia
   -> Machine type: 2-core, 8GB RAM, 32GB storage
   -> Initial Explorer tree: README.md, WEEK01.md, WEEK02.md, WEEK03.md
</embedded_artifact>

<task>
Based strictly on the telemetry above:
1. Explain in 3 bullet points why visiting `fantastic-dollop-9rpj66gp74hxx5w.github.dev` directly fails for students, and why Fork + own Codespace is mandatory for independent write access.
2. Calculate the exact monthly runtime budget difference between the instructor's 4-core machine and the student's 2-core machine under the 120 core-hours/month free tier.
3. Provide a 3-item readiness checklist verifying that the student's Codespace is correctly anchored in Southeast Asia on the forked repo.
</task>

<output_contract>
- Format: Structured Markdown with a 2-row comparison table (2-core vs 4-core).
- Language: Traditional Chinese prose + English technical terms.
- Constraint: Do NOT invent any URLs or machine specs not present in environment_context.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Outcome）**：
  1. 瀏覽器網址列呈現 `https://<隨機代碼>.github.dev/`，而非老師的 `fantastic-dollop-9rpj66gp74hxx5w.github.dev`。
  2. 左上角 Explorer 標題顯示 **`DM2026`**，檔案清單包含 `README.md`、`WEEK01.md`、`WEEK02.md`、`WEEK03.md`。
  3. 游標停留在左下角藍色/綠色 **`Codespaces`** 狀態列時，顯示 `2-core` 與目前執行的容器名稱。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **誤開成 `4-core`**：若忘了點 `New with options...` 而誤開成 4-core，免費額度消耗速度會加倍（60 hrs 降為 30 hrs）。可立即前往 `https://github.com/codespaces` → 點擊該 Codespace 右側 `...` → **Change machine type** 降回 `2-core`（或刪除重開）。
  - **區域誤選 `US East`**：若操作編輯器感覺打字延遲明顯（>200 ms），代表機房在美國東岸；建議刪除後重選 **Southeast Asia**。

---

## Lab 02：探索 Codespaces VS Code Web 介面與資源監控 (Exploring VS Code Web UI & Hardware Telemetry)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★☆☆（介面與資源觀測） |
| **Bloom's 認知層級** | `L2 Understand`（辨識瀏覽器 IDE 五大區塊）＋ `L4 Analyze`（比對 Linux 核心與記憶體實測數值） |
| **課程評分權重（Weight）** | `6%`（佔本次工作坊總成績 6/100） |
| **前置依賴（Prerequisites）** | `Lab 01`（必須已啟動個人 2-core Codespace） |
| **通過門檻（Pass Threshold）** | `IF` 成功在整合終端機執行 `lscpu`、`free -h`、`df -h` 且能正確判讀出 `2` vCPU、約 `7.7Gi` RAM 與 `/workspaces` 掛載點剩餘容量 `THEN PASS`；`ELSE` 檢核終端機開啟方式與 Linux 指令拼字。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **認識 VS Code Web IDE 五大功能區**：
   - **Activity Bar（最左側直列圖示）**：由上而下依序為 Explorer（檔案總管 `Ctrl+Shift+E`）、Search（搜尋）、Source Control（版本控制 `Ctrl+Shift+G`）、Run and Debug、Extensions（擴充套件 `Ctrl+Shift+X`）。
   - **Primary Side Bar**：目前展開的 `DM2026` 專案檔案樹。
   - **Editor Area（主編輯區）**：點擊 `WEEK02.md` 與 `WEEK03.md` 預覽內容，確認課堂從第 1 週 Colab 跨入 Python 101 與迴圈/OOP/Matplotlib。
   - **Bottom Panel（底部面板）**：按快捷鍵 ``Ctrl + ` ``（反引號）或點選上方選單 `Terminal` → `New Terminal` 開啟 Bash 終端機。
   - **Status Bar（最底端狀態列）**：左下角顯示遠端容器標籤 `Codespaces: <codespace-name>`。
2. **驗證雲端 CPU 核心數與記憶體配額（`nproc && free -h`）**：
   - 在 Terminal 輸入實測指令並按下 Enter：
     ```bash
     nproc && free -h && lscpu | grep -E "Model name|CPU\(s\)|Architecture"
     ```
   - 記錄 `nproc` 與 `Mem:` 的 `total`（學生免費 2-core 應為 `2` 核心、約 `7.7Gi` RAM；對照教師機 `fantastic-dollop` 實測為 **`4` 核心、約 `16GB` RAM**）。
3. **驗證作業系統版本（`Ubuntu 24.04.5 LTS`）**：
   - 在 Terminal 輸入：
     ```bash
     cat /etc/os-release
     ```
   - 確認 `PRETTY_NAME="Ubuntu 24.04.5 LTS"` 與 `VERSION="24.04.5 LTS (Noble Numbat)"`，體認雲端容器底層就是完整的現代 Linux 開發工作站。
4. **檢查 `/workspaces` 目錄與持久性磁碟（Persistent Volume）邊界**：
   - 在 Terminal 輸入：
     ```bash
     ls -la /workspaces && df -h /workspaces /
     ```
   - 觀察 `/workspaces` 目錄底下並排的三個資料夾：`.codespaces/`、`.oryx/` 與你的倉庫資料夾 **`DM2026/`**。當指定 Repo 為 `DM2026` 時，Linux 環境會直接對接該路徑——**請務必牢記：只有存放在 `/workspaces/DM2026` 目錄底下的檔案才會受到持久性磁碟（Persistent Volume）保護！**
5. **查看 Codespaces 自動注入的身份環境變數**：
   - 執行複合探測指令：
     ```bash
     env | grep -E "^(GITHUB_USER|CODESPACE_NAME)="
     ```
   - 確認 Codespaces 已自動注入 `GITHUB_USER` 與 `CODESPACE_NAME`，這就是後續免密碼操作 GitHub 的身份基石。

### 📋 完整語境提示詞（Complete Context Prompt）

將以下實測探針輸出與對比樣本完整貼入 AI 助手，取得系統架構解析報告：

````markdown
<epistemic_role>
You are a Linux Cloud Systems Engineer teaching university freshmen how cloud containers differ from their Windows/macOS laptops. Respond in Traditional Chinese with accurate Linux terminology.
</epistemic_role>

<environment_context>
- Platform: GitHub Codespaces (VS Code Web IDE, Southeast Asia)
- Student Container Spec: 2-core • 8GB RAM • 32GB storage
- Instructor Container Spec: 4-core • 16GB RAM • 32GB storage (fantastic-dollop-9rpj66gp74hxx5w)
</environment_context>

<embedded_artifact>
Actual Terminal Output Captured from 2-Core Student Container:
```text
$ lscpu | grep -E "Model name|CPU\(s\)|Architecture"
Architecture:            x86_64
CPU(s):                  2
Model name:              AMD EPYC 7763 64-Core Processor

$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       1.1Gi       4.2Gi        12Mi       2.4Gi       6.4Gi
Swap:             0B          0B          0B

$ df -h /workspaces /
Filesystem      Size  Used Avail Use% Mounted on
/dev/loop3       32G  6.8G   24G  23% /workspaces
overlay          32G  6.8G   24G  23% /

$ env | grep -E "^(GITHUB_USER|CODESPACE_NAME)="
GITHUB_USER=student-chu-01
CODESPACE_NAME=obscure-space-umbrella-7x92q
```
</embedded_artifact>

<task>
Analyze the embedded telemetry and answer:
1. Why does `free -h` show `7.7Gi` and `Swap: 0B` on an 8GB cloud container? What happens if a Python Matplotlib/NumPy script tries to allocate 9GB of RAM?
2. Explain the critical architectural difference between `/workspaces` (`/dev/loop3`) and `/` (`overlay`) during a Codespace stop or container rebuild.
3. Compare the student's `2` vCPU / `7.7Gi` RAM against the instructor's `4` vCPU / `16GB` RAM for running `WEEK03.md` NumPy/Matplotlib exercises—is 2-core sufficient?
</task>

<output_contract>
- Structure: 3 numbered sections with concise bullet points and a 2-row filesystem persistence table (`/workspaces` vs `/`).
- Tone: Clear, technical, encouraging.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `CPU(s): 2`（表示確實運行在 2-core 省額度規格）。
  - `Mem: total` 約為 `7.7Gi`～`7.8Gi`。
  - `/workspaces` 的 `Size` 顯示 `32G`，且 `GITHUB_USER` 顯示你自己的 GitHub 使用者名稱。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **找不到 Terminal**：在瀏覽器中若 `Ctrl + ` ` 被中文輸入法攔截，請直接點選視窗左上角 **`☰`（漢堡選單）→ Terminal → New Terminal**。
  - **在 `/tmp` 或 `~` 寫程式**：切勿把課堂作業存放在 `/workspaces/DM2026` 之外的目錄（如 `/home/codespace`），否則執行 `Rebuild Container` 時該檔案會被清除！

---

# ⚙️ Cycle 2（00:15–00:30）：Terminal, Python & File System — 終端機、Python 與分支實驗

## Lab 03：雲端 Terminal 健檢與 Python/Git 環境驗證 (Cloud Terminal Health Check & Python/Git Verification)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★☆☆（環境基線驗證） |
| **Bloom's 認知層級** | `L3 Apply`（執行環境探測指令與核對遠端追蹤網址） |
| **課程評分權重（Weight）** | `6%`（佔本次工作坊總成績 6/100） |
| **前置依賴（Prerequisites）** | `Lab 02`（已開啟 Terminal 並確認容器資源） |
| **通過門檻（Pass Threshold）** | `IF` (1) `which python3` 與 `python3 --version` 回傳有效路徑與 Python 3.x 版本，AND (2) `git remote -v` 的 `origin` 精確指向學生自己的 Fork Repo（非 `Grace-TA/DM2026`） `THEN PASS`；`ELSE` 修正 Git Remote 指向或檢查 PATH。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **確認目前工作目錄（Working Directory）**：
   - 在 Terminal 執行 `pwd` 與 `ls -la`：
     ```bash
     pwd
     ls -la
     ```
   - 確認路徑位於 `/workspaces/DM2026`，且可看見隱藏資料夾 `.git`。
2. **檢查 Python 直譯器路徑與版本**：
   - 依序執行以下指令，確認系統預設 `python3` 與 `pip3` 位置：
     ```bash
     which python3
     python3 --version
     pip3 --version
     ```
   - 預設 Codespaces Universal Image 通常預裝 Python `3.10` 或 `3.12`（位於 `/usr/local/python/current/bin/python3` 或 `/usr/bin/python3`），同時可能預裝了 `numpy` 與 `matplotlib`（稍後於 Lab 07/08 我們將鎖定精確的 Python `3.12` 與離散數學套件）。
3. **驗證數學與科學運算模組是否已存在**：
   - 執行單行 Python 探針，測試 `Grace-TA/DM2026` `WEEK02.md`（`math`, `calendar`）與 `WEEK03.md`（`numpy`, `matplotlib`）所需套件：
     ```bash
     python3 -c "import sys, math, calendar; print('Py:', sys.version.split()[0], '| pi:', round(math.pi, 4))"
     python3 -c "import importlib.util; print({m: bool(importlib.util.find_spec(m)) for m in ['numpy','matplotlib','pytest']})"
     ```
   - 記下回傳的 `True`/`False` 狀態，作為後續建立 `.devcontainer` 的依據。
4. **檢查 Git 遠端儲存庫指向（關鍵防呆檢查）**：
   - 執行：
     ```bash
     git remote -v
     git status
     git log -n 3 --oneline
     ```
   - 確認 `origin` 的 URL 為 `https://github.com/<你的帳號>/DM2026`（**不可為 `Grace-TA/DM2026`**，否則你將沒有寫入推送權限）。
5. **設定上游追蹤遠端 `upstream`（同步老師最新教材必備）**：
   - 為了未來能隨時拉取 Grace 助教或 Horace 老師在 `Grace-TA/DM2026` 新增的 `WEEK04.md`～`WEEK18.md` 教材，新增唯讀上游 `upstream`：
     ```bash
     git remote add upstream https://github.com/Grace-TA/DM2026.git
     git remote -v
     ```
   - 確認現在共有 `origin`（你的 Fork，可讀可寫）與 `upstream`（老師原版，唯讀參考）。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are an experienced Python & Git DevOps Mentor assisting an undergraduate student in CHU Discrete Math (DM2026). Explain interpreter paths, module probing, and Fork-Upstream Git topology clearly in Traditional Chinese.
</epistemic_role>

<environment_context>
- Workspace Path: /workspaces/DM2026
- Course Context: Transitioning from WEEK02.md (math, calendar) and WEEK03.md (numpy, matplotlib) Colab screenshots to executable Python scripts in Codespaces.
</environment_context>

<embedded_artifact>
Actual Diagnostic Probe Output from Student Terminal:
```text
$ pwd
/workspaces/DM2026

$ which python3 && python3 --version
/usr/local/python/current/bin/python3
Python 3.12.1

$ python3 -c "import importlib.util; print({m: bool(importlib.util.find_spec(m)) for m in ['math','calendar','numpy','matplotlib','pytest']})"
{'math': True, 'calendar': True, 'numpy': False, 'matplotlib': False, 'pytest': False}

$ git remote -v
origin  https://github.com/student-chu-01/DM2026 (fetch)
origin  https://github.com/student-chu-01/DM2026 (push)
upstream        https://github.com/Grace-TA/DM2026.git (fetch)
upstream        https://github.com/Grace-TA/DM2026.git (push)

$ git log -n 3 --oneline
a94c21e Update WEEK03.md Matplotlib trigonometric wave examples
7d18f02 Add WEEK02.md Python 101 exercises 1135-1175
3b0e110 Initial commit with WEEK01.md Colab guide
```
</embedded_artifact>

<task>
Analyze the diagnostic output above:
1. Identify which modules from `WEEK02.md` are ready out-of-the-box (`True`) vs which modules from `WEEK03.md` (`numpy`, `matplotlib`) are currently missing (`False`) and explain why standard library vs third-party PyPI packages behave differently.
2. Explain the dual-remote pattern (`origin` vs `upstream`) shown in `git remote -v`: what command should the student run next week when `Grace-TA/DM2026` publishes `WEEK04.md`, and why will `git push upstream main` fail?
3. Check whether `/usr/local/python/current/bin/python3` is safe to use directly or if a reproducible `.devcontainer` spec is still required.
</task>

<output_contract>
- Format: 3 clear sections with exact Git commands formatted in bash blocks.
- Language: Traditional Chinese + English technical terms.
- Verification: Base every judgment strictly on the `{'math': True, ...}` dict and remote output above.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `which python3` 輸出非空的執行檔路徑（如 `/usr/local/python/current/bin/python3` 或 `/usr/bin/python3`）。
  - `git remote -v` 顯示 `origin` 指向 `https://github.com/<你的帳號>/DM2026`，`upstream` 指向 `https://github.com/Grace-TA/DM2026.git`。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **重複執行 `git remote add upstream` 報錯**：若看到 `error: remote upstream already exists.`，代表已經設定完成，無需重複執行；若網址打錯可用 `git remote set-url upstream https://github.com/Grace-TA/DM2026.git` 修正。
  - **不小心從 `Grace-TA/DM2026` 直接開 Codespace**：如果 `origin` 顯示 `Grace-TA/DM2026`，請停止並刪除該 Codespace，回到你**自己帳號**的 Fork 頁面重開。

---

## Lab 04：建立個人工作分支 `feat/student-workshop` 與第一個 Python 實驗腳本 `hello_codespace.py` (Creating `feat/student-workshop` Branch & First Python Script)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★☆☆（版本分支與程式執行） |
| **Bloom's 認知層級** | `L3 Apply`（建立隔離工作分支並撰寫可執行的離散數學 Python 腳本） |
| **課程評分權重（Weight）** | `7%`（佔本次工作坊總成績 7/100） |
| **前置依賴（Prerequisites）** | `Lab 03`（已驗證 `python3` 與 Git `origin`/`upstream`） |
| **通過門檻（Pass Threshold）** | `IF` (1) 目前 Git 分支為 `feat/student-workshop`（非 `main`），AND (2) 存在 `scripts/hello_codespace.py` 且能成功執行並無錯誤輸出（Exit Code `0`） `THEN PASS`；`ELSE` 檢查分支切換與 Python 語法縮排。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **建立並切換至個人工作分支 `feat/student-workshop`**：
   - 在工程實務中，保持 `main` 分支乾淨以利未來同步 `upstream`，所有實作都在獨立功能分支進行：
     ```bash
     git checkout -b feat/student-workshop
     git branch
     ```
   - 確認 `* feat/student-workshop` 前方出現星號 `*`（代表目前所在分支）。
2. **建立專屬實驗資料夾 `scripts/` 與檔案 `hello_codespace.py`**：
   - 在 Terminal 執行：
     ```bash
     mkdir -p scripts
     touch scripts/hello_codespace.py
     ```
   - 在 VS Code 左側 Explorer 展開 `scripts/` 資料夾，點擊開啟 `hello_codespace.py`。
3. **撰寫結合 `DM2026` 離散數學主題的 Python 驗證程式**：
   - 將以下程式碼完整貼入 `scripts/hello_codespace.py`（融合 `WEEK02.md` 的 `math`/`calendar` 與 `WEEK03.md` 的集合 `set` 與字典 `dict` 邏輯，並加上時間戳記驗證）：
     ```python
     """DM2026 Codespaces First-Flight Verification Script."""
     import calendar
     import math
     import os
     import platform
     from datetime import datetime, timezone


     def verify_discrete_math_toolkit() -> dict:
         # Discrete Math Set Operations (from WEEK03.md Section 06)
         even_primes = {2}
         small_primes = {2, 3, 5, 7, 11}
         set_difference = small_primes - even_primes

         # Math constant verification (from WEEK02.md Section 02)
         circle_area_r1 = round(math.pi * (1 ** 2), 4)

         return {
             "github_user": os.environ.get("GITHUB_USER", "local-user"),
             "codespace_name": os.environ.get("CODESPACE_NAME", "unknown"),
             "python_version": platform.python_version(),
             "cpu_count": os.cpu_count(),
             "odd_primes_under_12": sorted(set_difference),
             "unit_circle_area": circle_area_r1,
             "weekday_2026_09_16": calendar.day_name[calendar.weekday(2026, 9, 16)],
             "utc_timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
         }


     if __name__ == "__main__":
         report = verify_discrete_math_toolkit()
         print("=== DM2026 Cloud Forge Diagnostic Report ===")
         for key, value in report.items():
             print(f"{key:<22}: {value}")
     ```
4. **儲存並執行腳本**：
   - 按 `Ctrl + S` 儲存檔案（確認編輯器分頁標籤上不再有白色圓點）。
   - 在 Terminal 執行：
     ```bash
     python3 scripts/hello_codespace.py
     ```
5. **驗證離散數學與雲端環境輸出**：
   - 檢視終端機輸出的 8 個欄位，確認 `cpu_count` 為 `2`、`odd_primes_under_12` 為 `[3, 5, 7, 11]`、`unit_circle_area` 為 `3.1416`。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are Dr. Horace Chen's Python Code Reviewer for CHU Discrete Math (DM2026). Audit the student's script against PEP 8 style, type annotations, and Discrete Math correctness from WEEK02.md and WEEK03.md.
</epistemic_role>

<environment_context>
- Branch: feat/student-workshop
- File Path: /workspaces/DM2026/scripts/hello_codespace.py
- Curriculum Link: Combines WEEK02.md (calendar, math.pi, timestamp) and WEEK03.md (Set difference, Dict summary).
</environment_context>

<embedded_artifact>
Student's Python Script (`scripts/hello_codespace.py`) and Execution Output:
```python
import calendar
import math
import os
import platform
from datetime import datetime, timezone

def verify_discrete_math_toolkit() -> dict:
    even_primes = {2}
    small_primes = {2, 3, 5, 7, 11}
    set_difference = small_primes - even_primes
    circle_area_r1 = round(math.pi * (1 ** 2), 4)
    return {
        "github_user": os.environ.get("GITHUB_USER", "local-user"),
        "codespace_name": os.environ.get("CODESPACE_NAME", "unknown"),
        "python_version": platform.python_version(),
        "cpu_count": os.cpu_count(),
        "odd_primes_under_12": sorted(set_difference),
        "unit_circle_area": circle_area_r1,
        "weekday_2026_09_16": calendar.day_name[calendar.weekday(2026, 9, 16)],
        "utc_timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    }
```
Actual Output:
```text
=== DM2026 Cloud Forge Diagnostic Report ===
github_user           : student-chu-01
codespace_name        : obscure-space-umbrella-7x92q
python_version        : 3.12.1
cpu_count             : 2
odd_primes_under_12   : [3, 5, 7, 11]
unit_circle_area      : 3.1416
weekday_2026_09_16    : Wednesday
utc_timestamp         : 2026-11-19 06:18:42 UTC
```
</embedded_artifact>

<task>
1. Verify why `sorted(set_difference)` is necessary in Discrete Math Python code when displaying a `set` (`WEEK03.md` Section 06 notes sets are unordered).
2. Suggest ONE clean enhancement to add a second Discrete Math operation (e.g., symmetric difference `^` or Cartesian product via `itertools.product`) inside `verify_discrete_math_toolkit()` with exact Python code.
3. Explain why keeping this work on `feat/student-workshop` instead of `main` protects the student's Fork when syncing future `WEEK04.md` updates from `Grace-TA/DM2026`.
</task>

<output_contract>
- Format: 3 concise sections in Traditional Chinese with an improved Python snippet ready to drop in.
- Strictness: Do not modify the existing return keys; only extend cleanly.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  ```text
  === DM2026 Cloud Forge Diagnostic Report ===
  github_user           : <你的 GitHub ID>
  codespace_name        : <你的 Codespace 名稱>
  python_version        : 3.12.1
  cpu_count             : 2
  odd_primes_under_12   : [3, 5, 7, 11]
  unit_circle_area      : 3.1416
  weekday_2026_09_16    : Wednesday
  utc_timestamp         : 2026-11-19 06:XX:XX UTC
  ```
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **忘記儲存檔案就執行**：若執行後完全沒有輸出，檢查 VS Code 編輯器分頁名稱右方是否有**白色實心圓點**（代表 Unsaved），務必按下 `Ctrl + S` 再重新執行 `python3 scripts/hello_codespace.py`。
  - **分錯分支**：若 `git branch` 顯示 `* main`，請立即執行 `git checkout -b feat/student-workshop`，已修改但尚未 commit 的檔案會自動跟隨切換過去。

---

## Lab 05：`.vscode/settings.json` 與擴充套件雲端漫遊 (VS Code Settings Sync & Python/Jupyter Extension Setup)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（團隊一致性設定） |
| **Bloom's 認知層級** | `L3 Apply`（建立專案層級 `.vscode/` 組態）＋ `L4 Analyze`（區分 User Settings Sync 與 Workspace Settings 之優先序） |
| **課程評分權重（Weight）** | `7%`（佔本次工作坊總成績 7/100） |
| **前置依賴（Prerequisites）** | `Lab 04`（位於 `feat/student-workshop` 分支） |
| **通過門檻（Pass Threshold）** | `IF` (1) `.vscode/settings.json` 與 `.vscode/extensions.json` 通過 JSON 語法驗證，AND (2) Python (`ms-python.python`) 與 Jupyter (`ms-toolsai.jupyter`) 擴充套件已安裝並可在 Codespace 內啟用 `THEN PASS`；`ELSE` 修復 JSON 逗號語法錯誤或透過 CLI 重裝擴充套件。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **理解個人設定（Settings Sync）vs 專案設定（`.vscode/`）**：
   - **Settings Sync（個人漫遊）**：儲存在你的 GitHub 帳號雲端，帶著你的佈景主題（Theme）、字體大小、快捷鍵到每一台 Codespace。
   - **Workspace `.vscode/`（團隊專案設定）**：寫入 Git 儲存庫，確保所有修課同學打開 `DM2026` 時都套用相同的 Python 縮排（4 空白）、UTF-8 編碼與自動存檔規則。
2. **啟用 VS Code Web 的 Settings Sync**：
   - 點擊 VS Code 左下角齒輪圖示 **⚙ (Manage)** → 選擇 **Backup and Sync Settings...** → 確認已使用你的 GitHub 帳號登入並開啟同步。
3. **建立專案級 `.vscode/settings.json` 與 `.vscode/extensions.json`**：
   - 在 Terminal 建立目錄與檔案：
     ```bash
     mkdir -p .vscode
     ```
   - 使用指令或編輯器寫入 `.vscode/settings.json`（規範 Python PEP 8 縮排、自動移除尾端空白、指定預設終端機）：
     ```bash
     cat << 'EOF' > .vscode/settings.json
     {
       "files.encoding": "utf8",
       "files.autoSave": "afterDelay",
       "files.autoSaveDelay": 1000,
       "editor.tabSize": 4,
       "editor.insertSpaces": true,
       "editor.formatOnSave": false,
       "files.trimTrailingWhitespace": true,
       "python.defaultInterpreterPath": "/usr/local/python/current/bin/python3",
       "python.terminal.activateEnvironment": true
     }
     EOF
     ```
   - 接著寫入 `.vscode/extensions.json`，為 `DM2026` 課程推薦必備擴充套件（Python、Jupyter、Markdown Preview）：
     ```bash
     cat << 'EOF' > .vscode/extensions.json
     {
       "recommendations": [
         "ms-python.python",
         "ms-toolsai.jupyter",
         "yzhang.markdown-all-in-one"
       ]
     }
     EOF
     ```
4. **驗證 JSON 格式零語法錯誤**：
   - 使用 Python 內建 `json.tool` 驗證兩個設定檔：
     ```bash
     python3 -m json.tool .vscode/settings.json > /dev/null && python3 -m json.tool .vscode/extensions.json > /dev/null && echo "JSON VALID"
     ```
5. **透過 CLI 安裝並盤點 Python 與 Jupyter 擴充套件**：
   - 在 Terminal 使用 `code --install-extension` 檢查或安裝擴充套件，並列出已安裝清單：
     ```bash
     code --install-extension ms-python.python
     code --install-extension ms-toolsai.jupyter
     code --list-extensions | grep -E "ms-python|jupyter"
     ```
6. **驗證編輯器右下角 Python 直譯器識別**：
   - 開啟 `scripts/hello_codespace.py`，觀察編輯器視窗最底端狀態列右側，應自動出現 **`Python 3.12.x`**（若無，按 `Ctrl+Shift+P` → 執行 `Python: Select Interpreter`）。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a Senior VS Code Extension & Workspace Architect. Help a Discrete Math student understand how `.vscode/settings.json` and `.vscode/extensions.json` interact with GitHub Codespaces Settings Sync.
</epistemic_role>

<environment_context>
- Workspace: /workspaces/DM2026 (branch: feat/student-workshop)
- Target Course Needs: Running `.py` scripts (`scripts/hello_codespace.py`) and future `.ipynb` notebooks migrated from `WEEK01.md` Colab.
</environment_context>

<embedded_artifact>
Actual `.vscode/settings.json`:
```json
{
  "files.encoding": "utf8",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.formatOnSave": false,
  "files.trimTrailingWhitespace": true,
  "python.defaultInterpreterPath": "/usr/local/python/current/bin/python3",
  "python.terminal.activateEnvironment": true
}
```
Actual `.vscode/extensions.json`:
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-toolsai.jupyter",
    "yzhang.markdown-all-in-one"
  ]
}
```
Installed Extensions Output:
```text
$ code --list-extensions | grep -E "ms-python|jupyter"
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
```
</embedded_artifact>

<task>
1. Explain the precedence hierarchy between VS Code **User Settings** (synced via Settings Sync) and **Workspace Settings** (`.vscode/settings.json`)—if a student's personal User Settings sets `"editor.tabSize": 2`, which value wins inside `DM2026` and why is that critical for Python?
2. Why does installing `ms-python.python` and `ms-toolsai.jupyter` automatically pull in `ms-python.vscode-pylance` and `ms-toolsai.jupyter-renderers`?
3. Point out one setting in `.vscode/settings.json` above that relies on the Universal Image path (`/usr/local/python/current/bin/python3`) and explain what might happen if the container switches to a custom Python 3.12 DevContainer in Lab 07.
</task>

<output_contract>
- Output: 3 numbered technical answers in Traditional Chinese with a Precedence Table (`Default < User < Remote < Workspace`).
- Length: Concise and engineering-focused (~250–350 words).
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `python3 -m json.tool` 驗證回傳 `JSON VALID`。
  - `code --list-extensions` 至少出現 `ms-python.python` 與 `ms-toolsai.jupyter`。
  - 開啟 `.py` 檔案時，狀態列右側顯示 Python 版本與選中的直譯器。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **手寫 JSON 多餘的尾端逗號（Trailing Comma）**：標準 JSON 不允許最後一個屬性後面有逗號（`,`），若有將會讓整個設定失效。務必用 `python3 -m json.tool` 檢查。
  - **Visual Studio Code Web 中 `code` 指令找不到**：極少數精簡容器中若 `code` alias 未註冊，可改透過左側 Extensions 面板（`Ctrl+Shift+X`）搜尋 `Python` 與 `Jupyter` 手動點擊 Install。

---

# 🔄 Cycle 3（00:30–00:45）：Git Closed-Loop & Reproducible Config — 版本閉環與宣告式環境

## Lab 06：免設定密碼的 Git 閉環工作流（`git status`, `add`, `commit`, `push` 回個人 Fork 的 `DM2026`）(Passwordless Git Closed-Loop Workflow)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★☆☆（Git 基礎閉環） |
| **Bloom's 認知層級** | `L3 Apply`（執行完整的 `status → add → commit → push` 雲端同步流程） |
| **課程評分權重（Weight）** | `7%`（佔本次工作坊總成績 7/100） |
| **前置依賴（Prerequisites）** | `Lab 04` 與 `Lab 05`（已有 `scripts/hello_codespace.py` 與 `.vscode/` 檔案） |
| **通過門檻（Pass Threshold）** | `IF` (1) 執行 `git push -u origin feat/student-workshop` 成功且無密碼提示錯誤，AND (2) 在 GitHub Web UI 的 `<GITHUB_USER>/DM2026` 頁面上可瀏覽 `feat/student-workshop` 分支與剛剛提交的檔案 `THEN PASS`；`ELSE` 檢查 `git config user.name/email` 或 `origin` URL。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **檢視工作區變更狀態（`git status`）**：
   - 在 Terminal 執行：
     ```bash
     git status
     ```
   - 確認出現兩組 `Untracked files`：`.vscode/` 與 `scripts/hello_codespace.py`。
2. **檢查 Git 提交身份設定（Author Identity）**：
   - 執行以下指令確認 Codespaces 是否已自動帶入你的 GitHub 姓名與電子郵件：
     ```bash
     git config user.name
     git config user.email
     ```
   - 若其中一項為空值（無輸出），請補上你的設定（Commit 才能正常記錄作者）：
     ```bash
     git config --global user.name "$GITHUB_USER"
     git config --global user.email "${GITHUB_USER}@users.noreply.github.com"
     ```
3. **加入暫存區（Staging Area）並複查差異**：
   - 執行 `git add` 將 `.vscode/` 與 `scripts/hello_codespace.py` 納入追蹤，並再次確認狀態：
     ```bash
     git add .vscode/scripts/hello_codespace.py 2>/dev/null || git add .vscode/ scripts/hello_codespace.py
     git status
     ```
   - 確認檔案皆出現在綠色的 `Changes to be committed:` 區塊。
4. **建立語意化提交紀錄（Conventional Commit）**：
   - 執行：
     ```bash
     git commit -m "feat(workshop): add hello_codespace diagnostic and vscode workspace config"
     ```
   - 接著執行 `git log -n 2 --oneline` 確認新 Commit 已寫入本地歷史。
5. **免密碼推送至個人 GitHub Fork（`git push`）**：
   - 執行首次分支推送指令：
     ```bash
     git push -u origin feat/student-workshop
     ```
   - 觀察奇蹟發生：**完全不需要輸入帳號密碼或 Personal Access Token (PAT)**——因為 Codespaces 已透過內建的 Git Credential Helper 與 `GITHUB_TOKEN` 自動完成 OAuth 授權！
6. **於 GitHub Web UI 交叉驗證雲端留存**：
   - 回到瀏覽器的 `https://github.com/<你的帳號>/DM2026` 頁面並重新整理（F5）。
   - 點擊分支下拉選單（原本顯示 `main`），切換至 **`feat/student-workshop`**，親眼確認 `.vscode/` 與 `scripts/hello_codespace.py` 已安全上雲。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a Git & Cloud Security Instructor explaining why GitHub Codespaces allows passwordless `git push` while keeping external repositories protected.
</epistemic_role>

<environment_context>
- Student Repo: https://github.com/student-chu-01/DM2026
- Active Branch: feat/student-workshop
- Staged Files: .vscode/settings.json, .vscode/extensions.json, scripts/hello_codespace.py
</environment_context>

<embedded_artifact>
Actual Git Session Transcript from Codespaces Terminal:
```text
$ git status
On branch feat/student-workshop
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .vscode/
        scripts/hello_codespace.py

$ git config --list | grep -E "user\.|credential\."
user.name=student-chu-01
user.email=student-chu-01@users.noreply.github.com
credential.helper=/.codespaces/bin/gitcredential_github.sh

$ git add .vscode/ scripts/hello_codespace.py
$ git commit -m "feat(workshop): add hello_codespace diagnostic and vscode workspace config"
[feat/student-workshop 8f31c9a] feat(workshop): add hello_codespace diagnostic and vscode workspace config
 3 files changed, 48 insertions(+)
 create mode 100644 .vscode/extensions.json
 create mode 100644 .vscode/settings.json
 create mode 100644 scripts/hello_codespace.py

$ git push -u origin feat/student-workshop
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 2 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 1.42 KiB | 1.42 MiB/s, done.
To https://github.com/student-chu-01/DM2026
 * [new branch]      feat/student-workshop -> feat/student-workshop
branch 'feat/student-workshop' set up to track 'origin/feat/student-workshop'.
```
</embedded_artifact>

<task>
1. Inspect `credential.helper=/.codespaces/bin/gitcredential_github.sh` in the artifact above—explain how Codespaces authenticates `git push` without exposing a plaintext password inside `~/.gitconfig`.
2. Explain what `-u` (`--set-upstream`) in `git push -u origin feat/student-workshop` accomplishes for future `git push` and `git pull` commands.
3. Describe what would happen if the student ran `git push -u upstream feat/student-workshop` instead (targeting `Grace-TA/DM2026`).
</task>

<output_contract>
- Format: 3 clear analytical sections in Traditional Chinese.
- Reference exact commit hash (`8f31c9a`), branch name, and credential helper path from the artifact.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `git push` 結尾顯示 `* [new branch] feat/student-workshop -> feat/student-workshop`。
  - GitHub 網頁版你的 Fork Repo 可切換到 `feat/student-workshop` 並看到 3 個新增檔案。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **誤打成 `git add .` 把暫存垃圾一起加入**：養成好習慣，在 `git add` 前後都先跑一次 `git status`，確認沒有 `.pyc` 或 `__pycache__` 等不需要的檔案被納入。
  - **忘記寫 `-m` 導致卡在 Vim/Nano 編輯器**：若不小心只打 `git commit` 而進入終端機編輯器（顯示 `# Please enter the commit message...`），在 Nano 按 `Ctrl+X` 放棄，或在 Vim 按 `Esc` 後輸入 `:q!` 退出，再補上 `-m "訊息"` 重試。

---

## Lab 07：解剖並撰寫宣告式環境 `.devcontainer/devcontainer.json`（指定 Python 3.12 Image + `postCreateCommand`）(Anatomy of Declarative `.devcontainer/devcontainer.json`)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（Infrastructure-as-Code 核心） |
| **Bloom's 認知層級** | `L4 Analyze`（拆解容器生命週期鉤子）＋ `L5 Evaluate`（設計符合 `DM2026` 課程需求的可重現環境配方） |
| **課程評分權重（Weight）** | `8%`（佔本次工作坊總成績 8/100） |
| **前置依賴（Prerequisites）** | `Lab 05` 與 `Lab 06`（理解 `.vscode/` 與 Python 模組缺失診斷） |
| **通過門檻（Pass Threshold）** | `IF` (1) `.devcontainer/devcontainer.json` 與 `requirements.txt` 皆已建立且通過 JSON 語法驗證，AND (2) 明確指定 Microsoft 官方 Python `3.12` DevContainer 映像、自動化 `postCreateCommand` 安裝 `numpy`/`matplotlib`/`pytest`、並內嵌 VS Code 擴充套件清單 `THEN PASS`；`ELSE` 檢查 JSON 結構鍵值名稱。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **理解 Infrastructure-as-Code（IaC）如何終結「在我電腦上可以跑」**：
   - 在 Lab 03 中，我們發現預設通用映像可能未預裝 `WEEK03.md` 所需的 `numpy` 與 `matplotlib`。若每位同學手動 `pip install`，只要換台機器或刪除重開就得重裝一次。
   - **解法**：將「作業系統映像、Python 版本、套件清單、VS Code 擴充套件」全部寫進 `.devcontainer/devcontainer.json`，讓 GitHub 每次啟動都造出 100% 一模一樣的雲端教室環境！
2. **建立課程相依套件鎖定檔 `requirements.txt`**：
   - 在專案根目錄 `/workspaces/DM2026` 執行以下指令，涵蓋 `WEEK02.md`～`WEEK03.md` 的科學計算與單元測試工具：
     ```bash
     cat << 'EOF' > requirements.txt
     numpy>=1.26,<3.0
     matplotlib>=3.8,<4.0
     pytest>=8.0,<9.0
     EOF
     ```
3. **建立 `.devcontainer` 目錄與 `devcontainer.json` 檔案**：
   - 執行：
     ```bash
     mkdir -p .devcontainer
     ```
   - 寫入以下宣告式設定檔至 `.devcontainer/devcontainer.json`（使用官方輕量且快速拉取的 `mcr.microsoft.com/devcontainers/python:1-3.12-bookworm` 基礎映像）：
     ```bash
     cat << 'EOF' > .devcontainer/devcontainer.json
     {
       "name": "DM2026 Discrete Math Cloud Forge (Python 3.12)",
       "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
       "features": {
         "ghcr.io/devcontainers/features/github-cli:1": {}
       },
       "postCreateCommand": "pip3 install --no-cache-dir -r requirements.txt && python3 -c 'import numpy, matplotlib; print(\"DM2026 Ready:\", numpy.__version__)'",
       "customizations": {
         "vscode": {
           "settings": {
             "python.defaultInterpreterPath": "/usr/local/bin/python",
             "files.encoding": "utf8"
           },
           "extensions": [
             "ms-python.python",
             "ms-toolsai.jupyter",
             "yzhang.markdown-all-in-one"
           ]
         }
       },
       "forwardPorts": [8000],
       "remoteUser": "vscode"
     }
     EOF
     ```
4. **解剖 6 大核心宣告鍵值（Key Anatomy）**：
   - `"image"`：指定 Debian 12 (Bookworm) + Python 3.12 官方基底容器。
   - `"features"`：模組化掛載 `github-cli` (`gh`)，供 Lab 11 遠端操作使用。
   - `"postCreateCommand"`：**容器初次建立完成後自動執行一次**的初始化指令，自動安裝 `requirements.txt`。
   - `"customizations.vscode"`：將 VS Code 擴充套件與直譯器路徑直接綁定於容器定義中。
   - `"forwardPorts"`：預設宣告監聽通訊埠 `[8000]`（銜接 Lab 09 HTTP 展示伺服器）。
   - `"remoteUser"`：以非特權使用者 `vscode` 安全執行開發作業。
5. **驗證 JSON 合法性並預先提交進 Git（Rebuild 前必做保險）**：
   - 執行驗證並 commit：
     ```bash
     python3 -m json.tool .devcontainer/devcontainer.json > /dev/null && echo "DEVCONTAINER JSON OK"
     git add requirements.txt .devcontainer/devcontainer.json
     git commit -m "build(devcontainer): declare Python 3.12 environment with numpy and matplotlib"
     ```
   - **重要**：還先別急著 Rebuild！Lab 08 我們將親手按下 `Rebuild Container` 並觀察完整建置日誌。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a DevContainer Specification Architect auditing a student's `.devcontainer/devcontainer.json` for a university Python & Discrete Math course (DM2026).
</epistemic_role>

<environment_context>
- Repo: DM2026 (branch: feat/student-workshop)
- Goal: Reproducible Python 3.12 container supporting WEEK03.md (NumPy, Matplotlib) and Lab 09/11 (Port 8000, GitHub CLI).
</environment_context>

<embedded_artifact>
File 1: `requirements.txt`
```text
numpy>=1.26,<3.0
matplotlib>=3.8,<4.0
pytest>=8.0,<9.0
```
File 2: `.devcontainer/devcontainer.json`
```json
{
  "name": "DM2026 Discrete Math Cloud Forge (Python 3.12)",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm",
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "postCreateCommand": "pip3 install --no-cache-dir -r requirements.txt && python3 -c 'import numpy, matplotlib; print(\"DM2026 Ready:\", numpy.__version__)'",
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "files.encoding": "utf8"
      },
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "yzhang.markdown-all-in-one"
      ]
    }
  },
  "forwardPorts": [8000],
  "remoteUser": "vscode"
}
```
</embedded_artifact>

<task>
Perform an architectural audit on the two embedded files:
1. Notice in Lab 05 `.vscode/settings.json` we had `/usr/local/python/current/bin/python3`, whereas here `customizations.vscode.settings` uses `/usr/local/bin/python`. Explain why official `mcr.microsoft.com/devcontainers/python:1-3.12-bookworm` places Python at `/usr/local/bin/python` while Universal Image uses `/usr/local/python/current/bin/python3`, and why overriding it inside `devcontainer.json` prevents interpreter-not-found errors.
2. Explain the lifecycle difference between `onCreateCommand`, `postCreateCommand`, and `postStartCommand`—why is `pip3 install -r requirements.txt` placed in `postCreateCommand` rather than `postStartCommand`?
3. Explain why `--no-cache-dir` in `pip3 install` saves precious GB-months under GitHub Codespaces' 15 GB-months free storage cap.
</task>

<output_contract>
- Format: 3 numbered engineering insights + a 3-row lifecycle comparison table (`onCreateCommand` vs `postCreateCommand` vs `postStartCommand`).
- Language: Traditional Chinese + English technical terms.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - 執行 `python3 -m json.tool .devcontainer/devcontainer.json` 輸出 `DEVCONTAINER JSON OK`。
  - `git log -n 1` 顯示 `build(devcontainer): declare Python 3.12 environment...` 已保存於分支歷史。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **`postCreateCommand` 雙引號跳脫錯誤**：在 JSON 字串裡面的雙引號必須加上反斜線 `\"`，切勿直接貼入未跳脫的雙引號，否則 JSON 解析必定失敗。
  - **誤將 `.devcontainer.json` 放在根目錄或拼錯資料夾名稱**：標準路徑必須是 `.devcontainer/devcontainer.json`（開頭有點 `.`，且是單數 `devcontainer`）。

---

## Lab 08：執行 `Rebuild Container` 與安裝驗證（體驗 IaC 一鍵重建與容器邊界）(Executing Rebuild Container & IaC Boundary Verification)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（容器生命週期實戰） |
| **Bloom's 認知層級** | `L4 Analyze`（追蹤容器重建日誌與系統使用者變化）＋ `L5 Evaluate`（驗證 IaC 狀態保留與重置邊界） |
| **課程評分權重（Weight）** | `8%`（佔本次工作坊總成績 8/100） |
| **前置依賴（Prerequisites）** | `Lab 07`（已完成 `.devcontainer/devcontainer.json` 撰寫與 Commit） |
| **通過門檻（Pass Threshold）** | `IF` (1) 成功執行 `Codespaces: Rebuild Container` 並完成重建連線，AND (2) 終端機驗證 `whoami` 為 `vscode`、`python3 -V` 為 `3.12.x`、且無須手動 `pip install` 即可 `import numpy, matplotlib, pytest` `THEN PASS`；`ELSE` 檢視 Creation Log 排查失敗步驟。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **在重建前於容器邊界放置測試哨兵檔（Boundary Probe）**：
   - 在 Terminal 執行指令，分別於**持久層 `/workspaces/DM2026`** 與**易失層 `/tmp`** 建立兩個標記檔案，親眼見證容器邊界：
     ```bash
     echo "SURVIVES_REBUILD" > /workspaces/DM2026/.rebuild_sentinel
     echo "WIPED_ON_REBUILD" > /tmp/ephemeral_test.txt
     whoami
     ```
   - 記下目前 `whoami` 可能是 `codespace`（Universal Image 預設使用者）。
2. **觸發容器一鍵重建（`Rebuild Container`）**：
   - 按下快捷鍵 `Ctrl + Shift + P`（macOS 為 `Cmd + Shift + P`）開啟 **Command Palette**。
   - 輸入並點選：**`Codespaces: Rebuild Container`**。
   - 在彈出的確認對話框中選擇 **`Rebuild`**（非 Full Rebuild，可利用映像層快取加速約 1–2 分鐘）。
3. **觀測 Creation Log 建置過程**：
   - 頁面會顯示重建進度條，點擊 **`View creation logs`** 可即時看見：
     1. 拉取 `mcr.microsoft.com/devcontainers/python:1-3.12-bookworm`。
     2. 安裝 Feature `github-cli:1`。
     3. 自動執行 `postCreateCommand` 裡的 `pip3 install --no-cache-dir -r requirements.txt`。
4. **重建後執行「容器邊界與套件自動化」驗收**：
   - 當 VS Code 重新載入完成後，開啟新 Terminal（``Ctrl + ` ``），依序執行：
     ```bash
     whoami
     which python3 && python3 -V
     gh --version | head -n 1
     python3 -c "import numpy, matplotlib, pytest; print('numpy:', numpy.__version__, '| matplotlib:', matplotlib.__version__, '| pytest:', pytest.__version__)"
     ```
5. **驗證 `/workspaces` 持久化 vs `/tmp` 抹除行為**：
   - 執行以下探針確認剛才留下的哨兵檔去留：
     ```bash
     cat /workspaces/DM2026/.rebuild_sentinel
     ls /tmp/ephemeral_test.txt 2>&1
     ```
   - 清理臨時測試哨兵檔並同步 `.vscode/settings.json` 中的直譯器路徑（改為 `/usr/local/bin/python` 以匹配新容器），然後推送至遠端：
     ```bash
     rm -f /workspaces/DM2026/.rebuild_sentinel
     python3 -c "import json; p='.vscode/settings.json'; d=json.load(open(p)); d['python.defaultInterpreterPath']='/usr/local/bin/python'; json.dump(d,open(p,'w'),indent=2)"
     git add .vscode/settings.json && git commit -m "chore(vscode): align python interpreter path with python 3.12 devcontainer" && git push
     ```

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are an Infrastructure-as-Code (IaC) & Container Lifecycle Specialist. Interpret the student's before-and-after telemetry from executing `Codespaces: Rebuild Container`.
</epistemic_role>

<environment_context>
- Transition: GitHub Universal Image (user: codespace) -> Custom Python 3.12 Bookworm DevContainer (user: vscode)
- Repo: /workspaces/DM2026 (branch: feat/student-workshop)
</environment_context>

<embedded_artifact>
Actual Pre-Rebuild vs Post-Rebuild Comparison Log:
```text
--- BEFORE REBUILD (Universal Image) ---
$ whoami
codespace
$ python3 -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
$ cat /workspaces/DM2026/.rebuild_sentinel
SURVIVES_REBUILD
$ cat /tmp/ephemeral_test.txt
WIPED_ON_REBUILD

--- AFTER REBUILD (Python 3.12 Bookworm DevContainer) ---
$ whoami
vscode
$ which python3 && python3 -V
/usr/local/bin/python3
Python 3.12.7
$ gh --version | head -n 1
gh version 2.62.0 (2024-11-14)
$ python3 -c "import numpy, matplotlib, pytest; print('numpy:', numpy.__version__, '| matplotlib:', matplotlib.__version__, '| pytest:', pytest.__version__)"
numpy: 2.1.3 | matplotlib: 3.9.2 | pytest: 8.3.3
$ cat /workspaces/DM2026/.rebuild_sentinel
SURVIVES_REBUILD
$ ls /tmp/ephemeral_test.txt
ls: cannot access '/tmp/ephemeral_test.txt': No such file or directory
```
</embedded_artifact>

<task>
1. Explain why `/workspaces/DM2026/.rebuild_sentinel` survived the container rebuild while `/tmp/ephemeral_test.txt` vanished—connect this directly to bind mounts / persistent workspace volumes in Docker/Codespaces.
2. Explain why the Linux user switched from `codespace` to `vscode`, and why `numpy`, `matplotlib`, and `pytest` appeared automatically without manual `pip install`.
3. Why is committing `.devcontainer/devcontainer.json` + `requirements.txt` into Git considered "turning an individual setup into a classroom standard" for all 30+ CHU DM2026 students?
</task>

<output_contract>
- Format: 3 concise engineering explanations in Traditional Chinese + a 4-item "IaC Golden Rules for Students" summary box.
- Grounding: Cite exact output values (`vscode`, `3.12.7`, `numpy: 2.1.3`, `SURVIVES_REBUILD`) from the artifact.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `whoami` 輸出 `vscode`。
  - `python3 -V` 輸出 `Python 3.12.x`。
  - `import numpy, matplotlib, pytest` 無報錯並印出版本號。
  - `/workspaces/DM2026/.rebuild_sentinel` 內容仍存在，`/tmp/ephemeral_test.txt` 回報 `No such file or directory`。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **Rebuild 後進入 Recovery Mode（救援模式）**：若因 `devcontainer.json` 有語法錯誤導致建置失敗，Codespaces 會退回無設定的 Recovery Container；此時請直接執行 `View creation logs` 找出 JSON 錯誤行號修正，再按 `Rebuild Container`。
  - **`Rebuild` 與 `Full Rebuild` 的差異**：平常修改 `requirements.txt` 用一般 `Rebuild Container` 即可；僅在懷疑 Docker 底層映像快取卡死時才選 `Full Rebuild Container`。

---

# 🌐 Cycle 4（00:45–01:00）：Networking, Ports & CLI — 網路轉發、雙向傳輸與 CLI 管理術

## Lab 09：啟動 HTTP 靜態展示伺服器與 Port Forwarding 實戰（`python3 -m http.server 8000` + Private vs Public 可見度切換）(HTTP Server & Port Forwarding Visibility)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（雲端網路穿透與資安控制） |
| **Bloom's 認知層級** | `L3 Apply`（架設預覽伺服器與轉發 Port `8000`）＋ `L4 Analyze`（比對 `Private` vs `Public` 存取授權機制） |
| **課程評分權重（Weight）** | `7%`（佔本次工作坊總成績 7/100） |
| **前置依賴（Prerequisites）** | `Lab 08`（位於執行中的 Python 3.12 容器） |
| **通過門檻（Pass Threshold）** | `IF` (1) 成功生成離散數學視覺化網頁 `web/index.html` 並以 `python3 -m http.server 8000 --directory web` 啟動，AND (2) 透過 `Ports` 面板開啟轉發 URL 看到渲染畫面並實測 `Private`（無痕視窗需登入）vs `Public`（無痕視窗免登入直開）後安全調回 `Private` `THEN PASS`；`ELSE` 檢視 Port 監聽狀態與可見度設定。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **用 `WEEK03.md` 的 Matplotlib 繪圖成果打造互動展示網頁**：
   - 還記得 `WEEK03.md` 第 10–11 節的三角波與參數圓嗎？我們先用一段 Python 腳本把 `WEEK03.md` 的三角波圖表輸出成 `web/wave_plot.png`，再包成一個靜態展示頁 `web/index.html`：
     ```bash
     mkdir -p web
     python3 - << 'EOF'
     import numpy as np
     import matplotlib.pyplot as plt

     theta = np.linspace(0, 2 * np.pi, 400)
     plt.figure(figsize=(7, 3.6), dpi=120)
     for k, color in enumerate(["#38bdf8", "#a855f7", "#22c55e", "#f59e0b"]):
         plt.plot(theta, np.sin(theta + k * np.pi / 4), label=f"Phase +{k}π/4", color=color, linewidth=2)
     plt.title("DM2026 WEEK03 — Multi-Phase Sine Waves")
     plt.xlabel("θ (radians)")
     plt.grid(alpha=0.25)
     plt.legend()
     plt.tight_layout()
     plt.savefig("web/wave_plot.png")
     print("Saved web/wave_plot.png")
     EOF
     ```
2. **建立展示首頁 `web/index.html`**：
   - 執行以下指令產生 HTML 頁面：
     ```bash
     cat << 'EOF' > web/index.html
     <!DOCTYPE html>
     <html lang="zh-Hant">
     <head><meta charset="UTF-8"><title>DM2026 Codespaces Live Showcase</title></head>
     <body style="font-family:sans-serif;background:#0f172a;color:#e2e8f0;padding:2rem;text-align:center;">
       <h1>🎓 DM2026 離散數學雲端視覺化成果展</h1>
       <p>Served directly from GitHub Codespaces Port 8000 (<code>python3 -m http.server</code>)</p>
       <img src="wave_plot.png" alt="WEEK03 Sine Waves" style="max-width:90%;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,0.5);">
     </body>
     </html>
     EOF
     ```
3. **啟動 Python 內建 HTTP 伺服器於 Port `8000`**：
   - 在 Terminal 執行：
     ```bash
     python3 -m http.server 8000 --directory web
     ```
   - 終端機將顯示 `Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...`（此時該 Terminal 會持續佔用等待連線，請保持開啟）。
4. **開啟 `Ports` 面板並透過雲端安全通道預覽**：
   - 切換到底部面板的 **`PORTS`** 分頁（位於 `TERMINAL` 旁）。
   - 找到 Port `8000`，將滑鼠移到 **Forwarded Address** 欄位（網址格式為 `https://<codespace>-8000.app.github.dev`），點擊地球圖示 **Open in Browser**。
   - 確認瀏覽器成功渲染出深色背景的 `DM2026 離散數學雲端視覺化成果展` 與 4 條三角波圖表！
5. **進行 `Private` vs `Public` 可見度（Visibility）實測**：
   - 在 `PORTS` 分頁中確認目前 **Visibility** 為預設值 **`Private`**。
   - 複製 Port `8000` 的 `Forwarded Address`，開啟瀏覽器的**無痕 / 隱私視窗（Incognito Window）**貼上該網址：
     - **預期現象（Private）**：GitHub 會要求登入驗證，他人或助教未經授權無法偷看你的網站。
   - 回到 Codespaces 的 `PORTS` 面板，對 Port `8000` 的 Visibility 點右鍵 → **Port Visibility** → 切換為 **`Public`**。
   - 再回到剛剛的無痕視窗重新整理（F5）：
     - **預期現象（Public）**：無須登入即可直接瀏覽！這非常適合課堂即時展示給老師與同學看。
6. **資安收尾與停止伺服器**：
   - 測試完畢後，立刻將 Visibility 切回 **`Private`**（養成最小權限習慣），並回到佔用中的 Terminal 按下 **`Ctrl + C`** 停止伺服器。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a Cloud Networking & Web Security Instructor explaining GitHub Codespaces Port Forwarding (`*.app.github.dev`) and HTTPS tunnel authentication.
</epistemic_role>

<environment_context>
- Server Command: `python3 -m http.server 8000 --directory web`
- Served Assets: `web/index.html` + `web/wave_plot.png` (generated from DM2026 WEEK03.md Matplotlib sine waves)
- Forwarded URL Pattern: `https://obscure-space-umbrella-7x92q-8000.app.github.dev`
</environment_context>

<embedded_artifact>
Observed Port Forwarding & HTTP Access Logs:
```text
$ python3 -m http.server 8000 --directory web
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [19/Nov/2026 06:42:10] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/Nov/2026 06:42:10] "GET /wave_plot.png HTTP/1.1" 200 -

Incognito Test A (Visibility = Private):
-> HTTP 302 Redirect to https://github.com/login (GitHub Auth Proxy blocks anonymous access)

Incognito Test B (Visibility = Public):
-> HTTP 200 OK (Renders HTML + wave_plot.png directly without GitHub session cookie)
```
</embedded_artifact>

<task>
1. Notice the client IP in Python's HTTP log shows `127.0.0.1` even though the student visited from a browser in Taiwan! Explain how Codespaces Port Forwarding acts as a reverse proxy tunnel between `*.app.github.dev` and `127.0.0.1:8000` inside the container.
2. Why does `python3 -m http.server` listen on plain `http://` inside the container, yet the browser URL starts with `https://`? Who handles TLS/SSL termination?
3. List 2 security risks of leaving a development server on `Public` visibility when building apps that read databases or sensitive files, and explain when `Private` vs `Public` should be chosen.
</task>

<output_contract>
- Format: 3 clear technical answers + a 2-row `Private` vs `Public` decision table.
- Language: Traditional Chinese + English networking terms (`Reverse Proxy`, `TLS Termination`, `OAuth Gate`).
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - Terminal 出現 `"GET / HTTP/1.1" 200 -` 與 `"GET /wave_plot.png HTTP/1.1" 200 -`。
  - 瀏覽器正常顯示 4 條彩色三角波圖表。
  - 無痕視窗實測出 `Private` 攔截登入 vs `Public` 免登入直通，且結束後已恢復 `Private`。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **在 Terminal 按指令沒反應**：因為 `http.server` 正在前台持續監聽，必須按 **`Ctrl + C`** 中斷後才能輸入下一個指令；或者按 Terminal 右上角的 **`+`** 開第二個分頁。
  - **找不到 `PORTS` 分頁**：點選左下角狀態列上顯示通訊埠的小圖示，或按 `Ctrl+Shift+P` → `Ports: Focus on Ports View`。

---

## Lab 10：雙向檔案傳輸：從本地拖曳上傳與透過 Terminal/UI 下載成果至本機 (Bidirectional File Transfer: Drag-Drop Upload & Local Export)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（雲地檔案互通） |
| **Bloom's 認知層級** | `L3 Apply`（執行瀏覽器與雲端容器間之雙向資料流轉與校驗） |
| **課程評分權重（Weight）** | `6%`（佔本次工作坊總成績 6/100） |
| **前置依賴（Prerequisites）** | `Lab 09`（已生成 `web/wave_plot.png` 並熟悉 Explorer 操作） |
| **通過門檻（Pass Threshold）** | `IF` (1) 成功從本機拖曳上傳一份 CSV 資料檔進入 Codespaces `data/` 目錄並以 Python 讀取計算，AND (2) 成功透過 VS Code UI `Download...` 將產出圖表或報告下載至本機資料夾且以 `sha256sum` 概念理解檔案完整性 `THEN PASS`；`ELSE` 排查拖曳目標區域或瀏覽器下載攔截。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **在本地端準備一份測試用離散數學成績 CSV（或於本機記事本建立）**：
   - 在你的 Windows/macOS 本機桌面建立一個純文字檔 `dm_scores.csv`，貼入以下 4 行內容並儲存：
     ```csv
     student_id,topic,score
     S01,Propositional_Logic,92
     S02,Set_Theory,88
     S03,Graph_Theory,95
     ```
2. **方法 A（UI 拖曳上傳）：將本機檔案直接拖入雲端 Explorer**：
   - 在 Codespaces 終端機先建立目標資料夾：
     ```bash
     mkdir -p data
     ```
   - 開啟你電腦的檔案總管（Explorer / Finder），將桌面的 `dm_scores.csv` **直接拖曳（Drag & Drop）** 放進 VS Code Web 左側檔案樹的 **`data`** 資料夾圖示上（放開前確認 `data` 資料夾出現反白外框）。
   - 若拖曳不方便，亦可對 `data` 資料夾點擊右鍵 → 選擇 **`Upload...`** → 從視窗選取 `dm_scores.csv`。
3. **在雲端容器讀取上傳資料並運算產出統計報告**：
   - 在 Terminal 執行內嵌 Python 分析腳本，讀取 `data/dm_scores.csv` 並輸出 `data/summary_report.txt`：
     ```bash
     python3 - << 'EOF'
     import csv, statistics

     with open("data/dm_scores.csv", encoding="utf-8") as f:
         rows = list(csv.DictReader(f))
     scores = [int(r["score"]) for r in rows]
     summary = (
         f"DM2026 Score Analytics\n"
         f"Count : {len(scores)}\n"
         f"Mean  : {statistics.mean(scores):.2f}\n"
         f"Max   : {max(scores)} ({max(rows, key=lambda r: int(r['score']))['topic']})\n"
     )
     with open("data/summary_report.txt", "w", encoding="utf-8") as out:
         out.write(summary)
     print(summary)
     EOF
     ```
4. **方法 B（UI 右鍵下載）：將雲端成果取回本機**：
   - 在 VS Code Web 左側 Explorer 展開 `data/`，對 **`summary_report.txt`** 點擊右鍵 → 選擇 **`Download...`**。
   - 瀏覽器會自動觸發下載至你電腦的「下載（Downloads）」資料夾。
   - 同樣方式，對 `web/wave_plot.png` 點右鍵 → **`Download...`**，將 Lab 09 的高解析度數學圖表存回本機，方便貼進作業或報告。
5. **進階技巧：使用 `sha256sum` 驗證下載檔完整性與整理 Git 追蹤**：
   - 在 Codespaces Terminal 計算雲端圖表與報告的雜湊指紋：
     ```bash
     sha256sum data/summary_report.txt web/wave_plot.png
     ```
   - 將新增的 `web/` 與 `data/` 成果提交（或僅提交程式碼與標準資料）：
     ```bash
     git add web/ data/ && git commit -m "feat(labs): add wave visualization and CSV analytics report" && git push
     ```

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a Data Pipeline & Cloud Workspace Instructor helping a freshman verify bidirectional file transfer integrity between a local PC and GitHub Codespaces.
</epistemic_role>

<environment_context>
- Cloud Paths: `/workspaces/DM2026/data/dm_scores.csv`, `/workspaces/DM2026/data/summary_report.txt`, `/workspaces/DM2026/web/wave_plot.png`
- Transfer Channel: VS Code Web Browser Drag-Drop Upload & Right-Click Download
</environment_context>

<embedded_artifact>
Uploaded CSV (`data/dm_scores.csv`):
```csv
student_id,topic,score
S01,Propositional_Logic,92
S02,Set_Theory,88
S03,Graph_Theory,95
```
Generated Summary (`data/summary_report.txt`) & Checksums:
```text
DM2026 Score Analytics
Count : 3
Mean  : 91.67
Max   : 95 (Graph_Theory)

$ sha256sum data/summary_report.txt web/wave_plot.png
9a4f8b2c1d7e6031c9a0e45f1289b7a6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0  data/summary_report.txt
4e1c9d0b7a8f2345e67890abcd1234567890fedcba0987654321fedcba123456  web/wave_plot.png
```
</embedded_artifact>

<task>
1. Explain why dragging a 5GB video dataset into VS Code Web Explorer is an anti-pattern (browser memory/Git bloat), and identify the safe threshold & alternative (e.g., `curl`/`wget` inside Terminal or `.gitignore` for large datasets).
2. Explain how `encoding="utf-8"` prevents Windows Big5/CP950 CSV files from crashing with `UnicodeDecodeError` when uploaded to a Linux Codespace.
3. Give the exact Windows PowerShell command (`Get-FileHash`) the student can run locally to verify their downloaded `wave_plot.png` matches the cloud `sha256sum` digest.
</task>

<output_contract>
- Format: 3 actionable engineering answers in Traditional Chinese with an exact PowerShell one-liner.
- Accuracy: Do not fabricate file sizes; focus on the exact encoding and hash verification commands.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `data/summary_report.txt` 正確印出 `Count : 3`、`Mean : 91.67`、`Max : 95 (Graph_Theory)`。
  - 本機下載資料夾中成功出現 `summary_report.txt` 與可開啟檢視的 `wave_plot.png`。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **拖曳檔案時不小心打開成瀏覽器分頁**：拖曳滑鼠必須精準停留在 VS Code **左側 Explorer 面板區域內**，不可放在上方編輯器或瀏覽器網址列，否則瀏覽器會直接試圖預覽該檔案而離開 Codespaces 分頁。
  - **瀏覽器阻擋一次下載多個檔案**：若同時選取多個檔案下載，Chrome/Edge 左上角可能跳出「允許下載多個檔案」提示，點擊「允許」即可。

---

## Lab 11：安裝與實戰 GitHub CLI（`gh codespace list`, `gh cs stop`, `gh cs ports`）遠端管理術 (GitHub CLI `gh codespace` Fleet Management)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（命令列遠端維運） |
| **Bloom's 認知層級** | `L4 Analyze`（診斷容器內 `GITHUB_TOKEN` Scope 邊界與 `gh auth` 授權）＋ `L3 Apply`（執行 CLI 指令檢視狀態與 Port 清單） |
| **課程評分權重（Weight）** | `8%`（佔本次工作坊總成績 8/100） |
| **前置依賴（Prerequisites）** | `Lab 08`（`.devcontainer.json` 已透過 `github-cli` feature 預裝 `gh`） |
| **通過門檻（Pass Threshold）** | `IF` (1) 驗證 `gh --version` 成功且完成 `codespace` 權限診斷/授權，AND (2) 能使用 `gh codespace list`（縮寫 `gh cs list`）、`gh cs ports` 列出正確容器與轉發埠，並理解何時執行 `gh cs stop` 避免自己把當前終端斷線 `THEN PASS`；`ELSE` 排查 `GITHUB_TOKEN` 覆蓋問題。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **驗證 `gh` 安裝與預設 Token 權限陷阱（超重要實戰知識！）**：
   - 在 Codespaces Terminal 執行：
     ```bash
     gh --version
     gh auth status
     ```
   - **關鍵觀察**：在 Codespaces 容器內部，系統預設注入了環境變數 `GITHUB_TOKEN`。這個 Token **僅限存取目前這個 Repo（`DM2026`）的程式碼**，預設**沒有 `codespace` 管理權限**！如果你直接跑 `gh codespace list`，通常會撞到 `HTTP 403` 或 `needs the 'codespace' scope` 錯誤。
2. **學會正確診斷並切換授權執行 `gh codespace list`**：
   - 先實測一次觀察錯誤訊息（若出現權限提示正是設計好的教學驗證）：
     ```bash
     gh codespace list 2>&1 || true
     ```
   - 若出現 `missing required scope 'codespace'` 或 `GITHUB_TOKEN` 覆蓋提示，在課程環境中透過暫時清除環境變數並使用具備 `codespace` scope 的 OAuth 登入（Device Flow）即可獲得完整艦隊管理權：
     ```bash
     env -u GITHUB_TOKEN gh auth login -h github.com -p https -s codespace -w
     ```
   - 依畫面指示複製 8 碼驗證碼（例如 `XXXX-YYYY`），於瀏覽器開啟 `https://github.com/login/device` 完成授權。
3. **實戰 `gh cs list` 盤點名下所有雲端容器**：
   - 授權完成後（注意若系統仍保留 `GITHUB_TOKEN` 環境變數，可加上 `env -u GITHUB_TOKEN` 或於本機電腦終端執行），輸入縮寫指令 `gh cs`:
     ```bash
     env -u GITHUB_TOKEN gh cs list
     ```
   - 記錄欄位：`NAME`（系統隨機識別碼）、`DISPLAY NAME`、`REPOSITORY`、`BRANCH`、`STATE`（`Available` 代表計費執行中、`Shutdown` 代表已休眠）與 `CREATED AT`。
4. **實戰 `gh cs ports` 遠端查詢與調整 Port 可見度**：
   - 查詢目前這台 Codespace 的轉發埠狀態：
     ```bash
     env -u GITHUB_TOKEN gh cs ports -c "$CODESPACE_NAME"
     ```
   - 練習用純命令列將 Port `8000` 設為 `private`（或 `public` 再設回 `private`）：
     ```bash
     env -u GITHUB_TOKEN gh cs ports visibility 8000:private -c "$CODESPACE_NAME"
     ```
5. **理解 `gh cs stop` 的自殺警告與遠端關機演練**：
   - **🚨 注意**：如果在**本機電腦**的終端機執行 `gh cs stop -c <CODESPACE_NAME>`，可以從遠端優雅關閉忘記關的雲端容器、立刻止血 2-core 計費；但若你在 **Codespace 裡面**對自己執行 `gh cs stop -c "$CODESPACE_NAME"`，連線會在 3 秒內被切斷（因為你正在關掉你所坐的這台雲端主機！）。
   - 先練習加上 `--help` 查閱安全參數，**保留到 Lab 13 結尾或於下課收工前再實際執行 `gh cs stop`**：
     ```bash
     gh cs stop --help
     ```

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a GitHub CLI & DevSecOps Automation Engineer. Explain the security boundary of Codespaces' built-in `GITHUB_TOKEN` and teach safe `gh cs` fleet management patterns.
</epistemic_role>

<environment_context>
- Container Env: Inside active Codespace `obscure-space-umbrella-7x92q`
- CLI Version: `gh version 2.62.0`
- Objective: Manage Codespaces lifecycle (`list`, `ports`, `stop`) cleanly without compromising token security.
</environment_context>

<embedded_artifact>
Observed `gh` CLI Output Before and After `env -u GITHUB_TOKEN`:
```text
$ gh cs list
HTTP 403: Resource not accessible by integration (https://api.github.com/user/codespaces)
Note: GITHUB_TOKEN environment variable is set inside Codespaces and only has repo-level permissions.

$ env -u GITHUB_TOKEN gh cs list
NAME                            DISPLAY NAME       REPOSITORY                 BRANCH                 STATE      CREATED AT
obscure-space-umbrella-7x92q    fuzzy space train  student-chu-01/DM2026      feat/student-workshop  Available  1 hour ago

$ env -u GITHUB_TOKEN gh cs ports -c "$CODESPACE_NAME"
LABEL  PORT  VISIBILITY  BROWSE URL
       8000  private     https://obscure-space-umbrella-7x92q-8000.app.github.dev
```
</embedded_artifact>

<task>
1. Explain the Least-Privilege Security Principle behind `HTTP 403` when running `gh cs list` with the default `GITHUB_TOKEN`: why doesn't GitHub let code inside one repo's Codespace automatically control or delete Codespaces belonging to ALL your other repos?
2. Explain what `env -u GITHUB_TOKEN` does for a single command invocation without breaking `git push` for the rest of the session.
3. Provide a 1-line bash snippet using `gh cs list` (from a local laptop or authenticated CLI) that a student can use before sleep to verify ZERO codespaces are left in `Available` state.
</task>

<output_contract>
- Format: 3 concise technical explanations in Traditional Chinese + 1 verified bash command block.
- Grounding: Reference the exact `HTTP 403` error and table columns (`NAME`, `STATE`, `VISIBILITY`) from the artifact.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `gh cs list` 正確列出你的 `<GITHUB_USER>/DM2026` 容器，且 `STATE` 顯示 `Available`。
  - `gh cs ports -c "$CODESPACE_NAME"` 列出 Port `8000` 的 `VISIBILITY` 為 `private`。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **忘記 `env -u GITHUB_TOKEN` 一直報 403**：`gh` CLI 設計優先讀取環境變數 `GITHUB_TOKEN` 而忽略本地存檔的 OAuth Token；只要在指令前加上 `env -u GITHUB_TOKEN` 暫時取消該環境變數即可（切勿在 `.bashrc` 永久 `unset GITHUB_TOKEN`，免得影響 VS Code 內建整合）。
  - **不慎在容器內直接跑了 `gh cs stop`**：畫面會跳出 `Codespace has been stopped`。別緊張！你的 `/workspaces/DM2026` 檔案完全安全，點擊畫面的 **`Restart codespace`** 即可於 15 秒內復原。

---

# 🛡️ Cycle 5：FinOps, Security & Troubleshooting — 資安防洩漏、配額精算與救援實戰

## Lab 12：Codespaces Secrets 安全注入與 `.gitignore` 防洩漏壓力測試 (Codespaces Secrets Injection & `.gitignore` Leak Stress Test)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（雲端資安工程） |
| **Bloom's 認知層級** | `L4 Analyze`（區分 Git 版本庫檔案與加密注入環境變數）＋ `L5 Evaluate`（對 `.gitignore` 與安全掃描進行壓力測試） |
| **課程評分權重（Weight）** | `8%`（佔本次工作坊總成績 8/100） |
| **前置依賴（Prerequisites）** | `Lab 06` 與 `Lab 11`（熟悉 Git 追蹤機制與環境變數） |
| **通過門檻（Pass Threshold）** | `IF` (1) `.gitignore` 已加入 `.env`、`*.key`、`__pycache__/` 並驗證 `git status` 完全忽略本地 `.env` 測試檔，AND (2) 透過 GitHub Settings Secrets（或本機加密注入模擬）於 Python `os.environ` 讀取模擬金鑰 `DM2026_DEMO_TOKEN` 且儲存庫歷史零明文洩漏 `THEN PASS`；`ELSE` 立即清除追蹤紀錄並補齊 `.gitignore`。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **建立強化版 `.gitignore` 安全防線**：
   - 在 `/workspaces/DM2026` 根目錄建立或更新 `.gitignore`，將常見金鑰檔案、Python 編譯暫存與虛擬環境全面擋在 Git 門外：
     ```bash
     cat << 'EOF' >> .gitignore

     # === DM2026 Security & Python Hygiene ===
     .env
     .env.*
     *.pem
     *.key
     secrets.json
     __pycache__/
     *.py[cod]
     .pytest_cache/
     EOF
     ```
2. **執行 `.gitignore` 壓力測試（模擬誤建 `.env` 明文金鑰檔）**：
   - 在終端機故意建立一個假的機密設定檔 `.env`（**使用教學用假字串，切勿填入真實密碼**）：
     ```bash
     echo "DM2026_API_KEY=demo_fake_key_never_commit_9988" > .env
     git status
     git check-ignore -v .env
     ```
   - **驗證成功徵兆**：`git status` **絕對不會**出現 `.env` 在 Untracked 列表；而 `git check-ignore -v .env` 會精確回報是 `.gitignore` 哪一行規則攔截了它！
3. **體驗正統雲端做法：在 GitHub Settings 設定個人 Codespaces Secret**：
   - 在瀏覽器開啟你的 GitHub 個人設定頁：`https://github.com/settings/codespaces`。
   - 往下滑找到 **Codespaces secrets** → 點擊 **New secret**：
     - **Name**：`DM2026_WORKSHOP_SECRET`
     - **Value**：`muse_academy_cloud_secret_2026`
     - **Repository access**：僅勾選你自己的 **`<你的帳號>/DM2026`**（落實最小存取原則）。
   - 點擊 **Add secret**。
   - **注意**：新加的 Secret 需要重新載入環境變數或重啟/新建 Codespace 才會自動注入容器；在工作坊課堂上若不想中斷連線，可先在 Terminal 以 `export DM2026_WORKSHOP_SECRET="muse_academy_cloud_secret_2026"` 模擬雲端已注入的環境變數進行第 4 步程式測試，待 Lab 13 Stop 後重開就會自動正式生效！
4. **撰寫安全讀取與遮罩檢查腳本 `scripts/secret_guard.py`**：
   - 建立永遠不印出完整明文、只印出前 4 碼遮罩的資安檢測腳本：
     ```bash
     cat << 'EOF' > scripts/secret_guard.py
     """Zero-Leak Environment Secret Loader & Masking Verifier."""
     import os


     def mask_secret(value: str) -> str:
         if not value:
             return "<MISSING>"
         if len(value) <= 6:
             return "*" * len(value)
         return f"{value[:4]}{'*' * (len(value) - 6)}{value[-2:]}"


     if __name__ == "__main__":
         secret = os.environ.get("DM2026_WORKSHOP_SECRET", "")
         print("Secret Status :", "INJECTED" if secret else "NOT_SET")
         print("Masked Preview:", mask_secret(secret))
     EOF
     python3 scripts/secret_guard.py
     ```
5. **執行靜態防洩漏掃描並提交安全防線（不含 `.env`）**：
   - 用 `git grep` 掃描整個 repo 是否誤留明文金鑰特徵，再安全提交 `.gitignore` 與 `scripts/secret_guard.py`：
     ```bash
     git grep -n "demo_fake_key" || echo "CLEAN: No fake keys in tracked files"
     git add .gitignore scripts/secret_guard.py
     git commit -m "security(env): enforce .gitignore secret barriers and masked env loader"
     git push
     ```

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are an Application Security (AppSec) Engineer auditing a student repository for credential hygiene and `.gitignore` enforcement in GitHub Codespaces.
</epistemic_role>

<environment_context>
- Repo: /workspaces/DM2026 (branch: feat/student-workshop)
- Security Controls: `.gitignore`, GitHub Codespaces User Secrets (`DM2026_WORKSHOP_SECRET`), and `scripts/secret_guard.py`.
</environment_context>

<embedded_artifact>
Actual Security Stress-Test Output:
```text
$ echo "DM2026_API_KEY=demo_fake_key_never_commit_9988" > .env
$ git check-ignore -v .env
.gitignore:4:.env        .env

$ git status --short
?? .gitignore
?? scripts/secret_guard.py

$ export DM2026_WORKSHOP_SECRET="muse_academy_cloud_secret_2026"
$ python3 scripts/secret_guard.py
Secret Status : INJECTED
Masked Preview: muse************************26

$ git grep -n "demo_fake_key" || echo "CLEAN: No fake keys in tracked files"
CLEAN: No fake keys in tracked files
```
</embedded_artifact>

<task>
1. Explain why `.env` did NOT appear in `git status --short` even though the file physically exists on `/workspaces/DM2026/.env`—what happens if a teammate later clones `<student>/DM2026`?
2. Explain why `git add -f .env` or hardcoding `DM2026_API_KEY` inside a `.py` file and later deleting it in a second commit STILL leaves the secret exposed in Git history (`git log -p`), and why GitHub Secret Scanning blocks pushes containing real API keys.
3. Compare GitHub **Codespaces Secrets** (encrypted at rest, injected only to authorized repo containers) vs local `.env` files during `Rebuild Container`.
</task>

<output_contract>
- Format: 3 clear security explanations in Traditional Chinese + a 2-row comparison table (`.env` vs `Codespaces Secrets`).
- Tone: Rigorous, practical, zero fear-mongering.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `git check-ignore -v .env` 精確輸出 `.gitignore:<行號>:.env  .env`。
  - `scripts/secret_guard.py` 輸出 `Secret Status : INJECTED` 與遮罩預覽 `muse************************26`。
  - `git grep -n "demo_fake_key"` 回傳 `CLEAN`。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **在建立 `.gitignore` 之前已經不小心 `git add .env`**：`.gitignore` 只對「尚未追蹤（Untracked）」的檔案生效！若曾誤加過，必須先執行 `git rm --cached .env` 解除追蹤（檔案仍保留在磁碟但不再進入 Git）。
  - **於日誌直接 `print(secret)` 除錯**：切記不可在程式碼或截圖中印出完整 Secret，務必使用類似 `mask_secret()` 的遮罩函式。

---

## Lab 13：FinOps 配額守衛計算與「Stop vs Delete」32GB 磁碟計費陷阱實測 (FinOps Quota Guard & Stop vs Delete Storage Trap)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★☆（雲端成本工程 FinOps） |
| **Bloom's 認知層級** | `L4 Analyze`（拆解運算 Core-Hours 與儲存 GB-Months 雙軸計費公式）＋ `L5 Evaluate`（建立個人月度配額預警腳本與生命週期清理策略） |
| **課程評分權重（Weight）** | `8%`（佔本次工作坊總成績 8/100） |
| **前置依賴（Prerequisites）** | `Lab 01`、`Lab 02` 與 `Lab 11`（已知 `2-core` vs `4-core`、`df -h` 磁碟用量與 `gh cs` 指令） |
| **通過門檻（Pass Threshold）** | `IF` (1) 完成 `scripts/finops_calculator.py` 並精算出「運算 `120 core-hrs`（2-core = 60 hrs）」與「儲存 `15 GB-months`（閒置容器佔用磁碟跨月累積）」的數學關係，AND (2) 理解 `Stop`（停止運算計費但仍佔用磁碟 GB-months）與 `Delete`（歸零磁碟計費、需先 `git push`）的差異 `THEN PASS`；`ELSE` 修正計算公式或補跑 `git status` 安全檢查。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **釐清 GitHub Free 雙軸計費陷阱（為什麼 Stop 不等於零成本？）**：
   - **第一軸：運算額度（Compute Quota = `120 core-hours / month`）**
     - 只在容器狀態為 **`Available`（執行中）** 時消耗：`Cores × Active_Hours`。
     - `2-core` = `120 / 2 = 60 小時/月`；若誤開 `4-core` = `120 / 4 = 30 小時/月`。
     - **止血按鈕**：閒置預設 `30 分鐘`自動進入休眠，或手動 **`Stop Codespace`** 立即將運算消耗降為 `0`。
   - **第二軸：儲存額度（Storage Quota = `15 GB-months / month`）——最常被忽略的隱形陷阱！**
     - 雖然免費規格寫 `32GB storage`，計費依據是容器**實際佔用的磁碟大小**（包含基底映像層、安裝的套件與 repo，約 `6–8 GB`），且只要容器沒有被 `Delete`（即使處於 **`Stopped` 狀態**），它每天 24 小時都在消耗 `GB-months`！
     - 公式：`Storage_GB_Months = Used_GB × (Hours_Existed / 730)`。
     - **致命情境**：如果一個學生開了 **3 台**不同的 Codespace 忘了刪（每台佔 `7 GB`），即使全部按了 `Stop`，一個月後將耗掉 `3 × 7 = 21 GB-months` → **直接爆掉 `15 GB-months` 免費額度！**
2. **實測目前容器的實際磁碟佔用量**：
   - 在 Terminal 執行 `df -h /workspaces` 與 `du -sh /workspaces/DM2026`：
     ```bash
     df -h /workspaces
     du -sh /workspaces/DM2026
     ```
   - 記下 `Used`（例如 `7.4G`），這就是你這台 Codespace 每存在一個月會消耗的 `GB-months` 基數。
3. **撰寫 FinOps 雙軸精算模擬器 `scripts/finops_calculator.py`**：
   - 建立以下確定性 Python 精算程式（含 Pytest 可測試函式）：
     ```bash
     cat << 'EOF' > scripts/finops_calculator.py
     """GitHub Codespaces Free-Tier FinOps Calculator (120 core-hrs & 15 GB-months)."""
     FREE_CORE_HOURS = 120.0
     FREE_GB_MONTHS = 15.0
     HOURS_PER_MONTH = 730.0


     def evaluate_monthly_quota(
         cores: int,
         active_hours: float,
         num_existing_codespaces: int,
         avg_used_gb_per_cs: float,
         days_kept: float = 30.0,
     ) -> dict:
         used_core_hrs = cores * active_hours
         compute_pct = (used_core_hrs / FREE_CORE_HOURS) * 100.0

         hours_stored = days_kept * 24.0
         used_gb_months = num_existing_codespaces * avg_used_gb_per_cs * (hours_stored / HOURS_PER_MONTH)
         storage_pct = (used_gb_months / FREE_GB_MONTHS) * 100.0

         return {
             "used_core_hours": round(used_core_hrs, 2),
             "remaining_core_hours": round(FREE_CORE_HOURS - used_core_hrs, 2),
             "compute_utilization_pct": round(compute_pct, 1),
             "used_gb_months": round(used_gb_months, 2),
             "remaining_gb_months": round(FREE_GB_MONTHS - used_gb_months, 2),
             "storage_utilization_pct": round(storage_pct, 1),
             "finops_alert": compute_pct >= 80.0 or storage_pct >= 80.0,
         }


     if __name__ == "__main__":
         scenarios = [
             ("Safe Student (1x 2-core, 16h/mo, 7.5GB)", dict(cores=2, active_hours=16, num_existing_codespaces=1, avg_used_gb_per_cs=7.5)),
             ("Zombie Trap (3x stopped 2-core, 10h/mo, 7.5GB)", dict(cores=2, active_hours=10, num_existing_codespaces=3, avg_used_gb_per_cs=7.5)),
             ("4-Core Heavy (1x 4-core, 28h/mo, 8.0GB)", dict(cores=4, active_hours=28, num_existing_codespaces=1, avg_used_gb_per_cs=8.0)),
         ]
         for name, params in scenarios:
             res = evaluate_monthly_quota(**params)
             print(f"[{name}] -> {res}")
     EOF
     python3 scripts/finops_calculator.py
     ```
4. **執行 Stop 前的「零遺失鐵律（Pre-Delete/Stop Safety Gate）」檢查**：
   - 在關閉或刪除任何 Codespace 之前，必須永遠檢查兩件事：
     ```bash
     git status
     git log origin/feat/student-workshop..HEAD --oneline
     ```
   - 確認 `git status` 為 `nothing to commit, working tree clean`，且尚未 push 的 commit 清單為空，才可安心按下 `Stop` 或 `Delete`。
5. **設定「閒置自動休眠時間（Idle Timeout）」與檢視 Billing 儀表板**：
   - 在瀏覽器開啟 `https://github.com/settings/codespaces` → 將 **Default idle timeout** 維持在 **`30 minutes`**（省電省配額黃金設定），並將 **Default retention period** 調整為較短天數（如 `7 days`，過期自動刪除免囤積殭屍磁碟）。
   - 前往 `https://github.com/settings/billing` 確認個人帳號即時用量的圖表位置。
6. **提交 FinOps 腳本並實測 Stop → Restart**：
   - 先推送程式碼：
     ```bash
     git add scripts/finops_calculator.py && git commit -m "feat(finops): add Codespaces 120 core-hrs and 15 GB-months calculator" && git push
     ```
   - 前往 `https://github.com/codespaces` 對你的容器點擊右側 **`...` → `Stop codespace`**，觀察狀態變為 `Shutdown`（停機期間 `0` core-hours 消耗），確認後再點 **`Open in browser`** 秒速喚醒進入最後一關 Lab 14！

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are a Cloud FinOps Strategist auditing a student's GitHub Free Codespaces consumption model. Provide exact mathematical reasoning and actionable quota-protection rules.
</epistemic_role>

<environment_context>
- GitHub Free Monthly Limits: 120 core-hours/month compute + 15 GB-months/month storage
- Student Container: 2-core, 8GB RAM, 32GB max disk (actual disk usage ~7.5 GB)
</environment_context>

<embedded_artifact>
Actual Execution Output from `scripts/finops_calculator.py`:
```text
[Safe Student (1x 2-core, 16h/mo, 7.5GB)] -> {'used_core_hours': 32.0, 'remaining_core_hours': 88.0, 'compute_utilization_pct': 26.7, 'used_gb_months': 7.4, 'remaining_gb_months': 7.6, 'storage_utilization_pct': 49.3, 'finops_alert': False}
[Zombie Trap (3x stopped 2-core, 10h/mo, 7.5GB)] -> {'used_core_hours': 20.0, 'remaining_core_hours': 100.0, 'compute_utilization_pct': 16.7, 'used_gb_months': 22.19, 'remaining_gb_months': -7.19, 'storage_utilization_pct': 147.9, 'finops_alert': True}
[4-Core Heavy (1x 4-core, 28h/mo, 8.0GB)] -> {'used_core_hours': 112.0, 'remaining_core_hours': 8.0, 'compute_utilization_pct': 93.3, 'used_gb_months': 7.89, 'remaining_gb_months': 7.11, 'storage_utilization_pct': 52.6, 'finops_alert': True}
```
</embedded_artifact>

<task>
1. Analyze Scenario 2 ("Zombie Trap"): why did `compute_utilization_pct` stay safely at `16.7%` while `storage_utilization_pct` blew up to `147.9%` (`-7.19 GB-months`) even though all 3 containers were stopped most of the month?
2. Compare **Stop (`Shutdown`)** vs **Delete**: which resource counter stops immediately on `Stop`, which counter keeps ticking, and what is the mandatory 2-command Git check before clicking `Delete`?
3. Recommend an exact semester FinOps SOP for a student taking DM2026 (2 hours/week in class + 2 hours/week homework) so they never hit `finops_alert: True`.
</task>

<output_contract>
- Format: 3 analytical sections in Traditional Chinese + a crisp `Stop` vs `Delete` comparison matrix.
- Math Precision: Cite the exact simulated percentages (`26.7%`, `147.9%`, `93.3%`) from the embedded artifact.
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - `scripts/finops_calculator.py` 輸出三組情境精算字典，清楚凸顯情境 2 的 `storage_utilization_pct: 147.9`。
  - `https://github.com/codespaces` 實測完成 `Stop` → `Shutdown` → 重新喚醒。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **在還沒 `git push` 的狀態下按了 `Delete`**：一旦 `Delete codespace`，未推送到 GitHub 的本地檔案與 Commit **將永久消失無法救回**！務必牢記鐵律：**Delete 前必須看到 `working tree clean` 且無 unpushed commits**。
  - **開太多實驗用的 Codespace**：每次想進 `DM2026` 寫程式，請回到 `https://github.com/codespaces` 重啟**同一台**已存在的主容器，不要每次都按 `Create codespace` 產生第 2、第 3 台分身。

---

## Lab 14：模擬環境損壞救援：透過 `git diff`、`Rebuild` 與 VS Code Live Share 進行故障排除 (Simulated Environment Failure Rescue: `git diff`, Rebuild & Live Share)

### 🎯 學習目標與量化指標（L.A.W. Anchored）

| 評估維度（Dimension） | 量化指標與規格（Quantified Specification） |
|:---|:---|
| **難度等級（Difficulty）** | ★★★（高階排錯與協作救援總驗收） |
| **Bloom's 認知層級** | `L5 Evaluate`（定位設定檔破壞根因並評估回滾策略）＋ `L6 Create`（編寫自動化回歸測試 `pytest` 與執行 Live Share 雙向協作排錯） |
| **課程評分權重（Weight）** | `8%`（佔本次工作坊總成績 8/100） |
| **前置依賴（Prerequisites）** | `Lab 07`、`Lab 08` 與 `Lab 13`（具備正常運作的 `.devcontainer` 與 `pytest`） |
| **通過門檻（Pass Threshold）** | `IF` (1) 人工注入 `.devcontainer/devcontainer.json` 與 `scripts/finops_calculator.py` 雙重故障後，能精準使用 `git diff` 定位破壞點並以 `git checkout --` / 修復重建恢復全綠通過 `pytest`，AND (2) 成功安裝/啟動 **Live Share** 會話取得唯讀/協作救援連結（模擬連線教師 4-core `fantastic-dollop` 進行雙人除錯） `THEN PASS`；`ELSE` 檢視測試失敗日誌與 Live Share 登入狀態。 |

### 🛠️ 學生完整操作步驟（Complete Student Guide）

1. **為工作坊核心元件建立 `pytest` 自動化守護測試 `tests/test_workshop.py`**：
   - 先建立 `tests/` 資料夾與驗證腳本，確保未來任何改動都能用一鍵測試驗證功能是否健康：
     ```bash
     mkdir -p tests
     cat << 'EOF' > tests/test_workshop.py
     import json
     from pathlib import Path
     from scripts.finops_calculator import evaluate_monthly_quota
     from scripts.secret_guard import mask_secret


     def test_devcontainer_json_valid():
         cfg = json.loads(Path(".devcontainer/devcontainer.json").read_text(encoding="utf-8"))
         assert "3.12" in cfg["image"]
         assert 8000 in cfg["forwardPorts"]


     def test_finops_zombie_trap_triggers_alert():
         res = evaluate_monthly_quota(cores=2, active_hours=10, num_existing_codespaces=3, avg_used_gb_per_cs=7.5)
         assert res["finops_alert"] is True
         assert res["used_gb_months"] > 15.0


     def test_secret_masking_never_leaks_full_token():
         masked = mask_secret("muse_academy_cloud_secret_2026")
         assert masked.startswith("muse") and "secret" not in masked
     EOF
     PYTHONPATH=. pytest -v
     ```
   - 確認初次執行顯示 **`3 passed`**！先提交這個基準測試作為安全網：
     ```bash
     git add tests/test_workshop.py && git commit -m "test(workshop): add pytest regression suite for devcontainer, finops, and security" && git push
     ```
2. **模擬「雙重災難注入」（Chaos Engineering Drill）**：
   - 執行以下指令，故意破壞 `.devcontainer/devcontainer.json`（塞入非法 JSON 語法）以及把 `scripts/finops_calculator.py` 的 `FREE_GB_MONTHS` 錯改成 `150.0`：
     ```bash
     sed -i 's/"remoteUser": "vscode"/,"remoteUser": BROKEN_SYNTAX/' .devcontainer/devcontainer.json
     sed -i 's/FREE_GB_MONTHS = 15.0/FREE_GB_MONTHS = 150.0/' scripts/finops_calculator.py
     ```
3. **體驗故障爆發：執行檢測與 `pytest` 紅燈報錯**：
   - 執行驗證指令觀察損壞現象：
     ```bash
     python3 -m json.tool .devcontainer/devcontainer.json || echo "ALERT: DevContainer JSON corrupted!"
     PYTHONPATH=. pytest -v
     ```
   - 觀察 `test_devcontainer_json_valid` 因 `JSONDecodeError` 失敗，且 `test_finops_zombie_trap_triggers_alert` 因邏輯錯誤回傳 `False` 而失敗！若此時直接按 `Rebuild Container`，容器將直接崩潰進入 Recovery Mode。
4. **救援第一步：用 `git diff` 進行法醫級差異定位**：
   - 在 Terminal 執行：
     ```bash
     git status -s
     git diff
     ```
   - 精確判讀紅色（`-` 被刪掉的正確行）與綠色（`+` 被注入的錯誤行），確認問題出在 `.devcontainer/devcontainer.json` 的 `,` 與 `BROKEN_SYNTAX`，以及 `FREE_GB_MONTHS = 150.0`。
5. **救援第二步：執行精準還原（Surgical Rollback）與自動化全綠回歸**：
   - 假設我們只想先還原被破壞的檔案（若為真實開發，也可以選擇手動修補其中一個而還原另一個）：
     ```bash
     git checkout -- .devcontainer/devcontainer.json scripts/finops_calculator.py
     python3 -m json.tool .devcontainer/devcontainer.json > /dev/null && echo "DEVCONTAINER RESTORED"
     PYTHONPATH=. pytest -v
     ```
   - 確認 `3 passed`，並可選擇再跑一次 `Ctrl+Shift+P` → `Codespaces: Rebuild Container` 驗證容器設定完全無損！
6. **救援第三步：啟動 VS Code Live Share 與教師 `4-core` 容器跨機即時救援演練**：
   - 當遇到連 `git diff` 都搞不定的難題時，該怎麼請老師或助教直接進來你的編輯器救援？答案就是 **Live Share**（與 Lab 01 不能直接開老師 URL 不同，Live Share 是雙方明確授權的即時協作會話！）。
   - 在 Terminal 安裝 Live Share 擴充套件（或從左側 Extensions 搜尋 `Live Share`）：
     ```bash
     code --install-extension ms-vsliveshare.vsliveshare
     ```
   - 點擊左側 Activity Bar 新出現的 **Live Share** 圖示（箭頭與圓圈符號）→ 點擊 **Share**（若首次使用，請選擇使用 **GitHub** 登入授權）。
   - 系統會複製一串以 `https://prod.liveshare.vsengsaas.visualstudio.com/join?...` 開頭的邀請連結到剪貼簿——**在課堂救援時將此連結私訊給助教，助教就能從他的 `4-core` `fantastic-dollop` 環境直接連進你的編輯器幫你同步 Debug 並共享終端機！**
   - 演練完成後，點擊 Live Share 面板上的 **Stop Collaboration Session** 安全結束分享。

### 📋 完整語境提示詞（Complete Context Prompt）

````markdown
<epistemic_role>
You are the Site Reliability Engineering (SRE) Incident Commander for Muse Academy's DM2026 Workshop. Perform a Root Cause Analysis (RCA) on a simulated broken DevContainer and FinOps regression, then guide Live Share rescue protocol.
</epistemic_role>

<environment_context>
- Repo: /workspaces/DM2026 (branch: feat/student-workshop)
- Safety Net: `tests/test_workshop.py` (pytest) + Git version history
- Rescue Channel: VS Code Live Share (`ms-vsliveshare.vsliveshare`) bridging Student 2-core container and Instructor 4-core `fantastic-dollop-9rpj66gp74hxx5w`
</environment_context>

<embedded_artifact>
Simulated Chaos Drill Diagnostic Logs:
```text
$ PYTHONPATH=. pytest -v
FAILED tests/test_workshop.py::test_devcontainer_json_valid - json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 22 column 3
FAILED tests/test_workshop.py::test_finops_zombie_trap_triggers_alert - AssertionError: assert False is True
PASSED tests/test_workshop.py::test_secret_masking_never_leaks_full_token

$ git diff
diff --git a/.devcontainer/devcontainer.json b/.devcontainer/devcontainer.json
--- a/.devcontainer/devcontainer.json
+++ b/.devcontainer/devcontainer.json
@@ -19,5 +19,5 @@
   "forwardPorts": [8000],
-  "remoteUser": "vscode"
+  ,"remoteUser": BROKEN_SYNTAX
 }
diff --git a/scripts/finops_calculator.py b/scripts/finops_calculator.py
--- a/scripts/finops_calculator.py
+++ b/scripts/finops_calculator.py
@@ -2,3 +2,3 @@
 FREE_CORE_HOURS = 120.0
-FREE_GB_MONTHS = 15.0
+FREE_GB_MONTHS = 150.0
```
</embedded_artifact>

<task>
1. Write a structured 3-step Post-Mortem RCA based strictly on the `pytest` failures and `git diff` output above.
2. Explain the critical distinction between: (a) a student clicking the instructor's `fantastic-dollop-9rpj66gp74hxx5w.github.dev` URL (fails in Lab 01), vs (b) initiating a **VS Code Live Share** session (`prod.liveshare.vsengsaas.visualstudio.com/join?...`) in Lab 14—how does Live Share enable rescue without handing over GitHub account passwords?
3. When should a student use `git checkout -- <file>` vs `Codespaces: Rebuild Container` during an emergency?
</task>

<output_contract>
- Format: RCA Summary + Live Share Security Architecture + Emergency Decision Matrix (`git checkout` vs `Rebuild Container`).
- Language: Traditional Chinese + English SRE terms (`RCA`, `Surgical Rollback`, `Read-Write Collaboration`).
</output_contract>
````

### ✅ 驗收標準與防呆檢核

- **預期輸出（Expected Output）**：
  - 演練前後對比：破壞時 `pytest` 精確顯示 `2 failed, 1 passed`；執行 `git checkout --` 還原後，`PYTHONPATH=. pytest -v` 顯示 `3 passed`。
  - Live Share 擴充套件成功產生 `prod.liveshare.vsengsaas.visualstudio.com/join?...` 救援連結，並於演練後正常關閉會話。
- **🚨 常見踩坑與排除對策（Troubleshooting）**：
  - **忘記 `PYTHONPATH=.` 執行 `pytest` 出現 `ModuleNotFoundError: No module named 'scripts'`**：在專案根目錄使用 `python3 -m pytest -v` 或 `PYTHONPATH=. pytest -v` 即可自動將根目錄加入模組搜尋路徑。
  - **Live Share 分享給錯人或忘記關閉**：Live Share 連結預設具寫入編輯權限（亦可設為 Read-Only）；請勿將邀請連結張貼至公開聊天室，救援結束後務必點擊 **Stop Collaboration Session**。

---

# 🏁 總結驗收矩陣與課後行動清單（Workshop Completion & Next Actions）

恭喜你完成了從零開始到雲端 IDE 英雄的 **14 關全閉環訓練**！在關閉瀏覽器離開工作坊前，請執行最後一道總檢核腳本，確認全專案 100% 就緒並安全推送：

```bash
# Final 14-Lab Readiness Gate (Run inside /workspaces/DM2026)
git branch --show-current
python3 -m json.tool .devcontainer/devcontainer.json > /dev/null && echo "OK: devcontainer.json"
python3 -m json.tool .vscode/settings.json > /dev/null && echo "OK: vscode settings.json"
PYTHONPATH=. pytest -v
git status
```

## 📊 14 Labs 快速排錯對照表（Quick Troubleshooting Matrix）

| 常見異常狀況（Symptom） | 對應起源 Lab | 一鍵診斷指令 / 處置動作（Fix Action） |
|:---|:---:|:---|
| 點擊老師網址 `fantastic-dollop` 出現無權限 | Lab 01 | 回 `Grace-TA/DM2026` 按 **Fork**，開自己帳號的 **2-core Southeast Asia** |
| Rebuild 後 `/tmp` 檔案不見了 | Lab 02 / 08 | 僅 `/workspaces/DM2026` 為持久化掛載點，所有作業一律存於此目錄內 |
| `git push` 遭到拒絕（403） | Lab 03 / 06 | 檢查 `git remote -v` 是否誤指 `Grace-TA/DM2026`，應推送至個人 Fork `origin` |
| `gh codespace list` 回報 HTTP 403 | Lab 11 | 容器內 `GITHUB_TOKEN` 缺 `codespace` scope，改用 `env -u GITHUB_TOKEN gh cs list` |
| 還沒月終 15 GB-months 就爆額度 | Lab 13 | 前往 `github.com/codespaces` 刪除（`Delete`）多餘閒置的分身容器，只留 1 台並善用 `Stop` |
| 不小心改壞設定檔導致容器打不開 | Lab 14 | 進入 Recovery 模式執行 `git diff` 與 `git checkout -- <file>` 修復後 `Rebuild Container` |

> **Director Sigma 結語**：*「你已經把雲端容器從神秘的黑盒子，鍛造成隨時可重建、可追蹤、零洩漏且精打細算的個人科學工作台。接下來 `WEEK04.md` 與整個離散數學學期，你將以職業工程師的標準駕馭每一行 Python 程式碼！」* ⚒️🔥
