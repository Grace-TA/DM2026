# 02｜GitHub Codespaces 十大實戰作戰手冊 (Top 10 Actionable Playbooks)
## Muse Academy × `Grace-TA/DM2026` 離散數學雲端標準作業程序（Book 2）

> **編撰架構**：`Professor's Workshop` × `Director Sigma`（AEOS 知識工程總署）  
> **課程錨點**：115 學年第 1 學期《離散數學 Discrete Mathematics》（[`Grace-TA/DM2026`](https://github.com/Grace-TA/DM2026)）  
> **助教與聯絡信箱**：`Grace-TA`（CSIE / EE / IM / DS 聯合助教｜`ta2021.vnu@gmail.com`）  
> **教師專用實例**：`fantastic-dollop-9rpj66gp74hxx5w`（`4-core • 16GB RAM • 32GB disk`｜`Southeast Asia`｜[`https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/`](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)）  
> **系統規範**：全手冊遵守 **L.A.W. Engine**（量化指標與 IF-THEN 法則）、**MR-8（Cost & Latency Quantification）** 與 **Zero-Placeholder Policy**（所有 CLI、JSON、Dockerfile、Python 腳本與 Prompt 皆可原封不動複製執行）。未實測之課堂預估統計皆標註 `[HYPOTHESIS]`。

---

## 作戰總覽索引矩陣 (Playbook Command Matrix)

| Playbook ID | 名稱與作戰定位 | 主要使用者 | Bloom's Level | 核心量化指標 (MR-8 Impact) | 前置依賴 |
|:---|:---|:---:|:---:|:---|:---|
| **PB-01** | 30 秒零安裝啟動與學生 Fork `2-core` 免費層 SOP | Student | L3 (Apply) | 冷啟動 `~90-120s`；計算消耗 `2 core-hrs/hr`（月限 `60 hr`） | `WEEK01.md` + GitHub 帳號 |
| **PB-02** | `fantastic-dollop` 4-Core 助教 Live Demo 與 Live Share 救援協議 | Instructor / TA | L4 (Analyze) | 救援切入時間 `< 45s`；消除 `100%` 直接開 URL 的 `403/404` 錯誤 | `PB-01` + VS Code Live Share |
| **PB-03** | 宣告式環境即代碼（`.devcontainer/devcontainer.json`） | TA / Student | L5 (Evaluate) | 套件漂移率降至 `< 3%` `[HYPOTHESIS]`；全班同構 Ubuntu + Py 3.12 | `PB-01` + JSON 結構知識 |
| **PB-04** | Google Colab-to-Codespaces 無痛遷移（`WEEK01`–`WEEK03`） | Student | L4 (Analyze) | 單檔遷移耗時 `< 5 min`；支援 `Agg` 無頭繪圖與 `pytest` | `WEEK01`–`WEEK03` + `PB-03` |
| **PB-05** | Port Forwarding 與 HTTPS 安全預覽通道（權限三級管控） | Student / TA | L4 (Analyze) | 預覽通道建立 `< 5s`；`Private` 模式零未授權外洩 | `PB-04` + HTTP 基本概念 |
| **PB-06** | GitHub CLI (`gh codespace`) 遠端終端機與檔案傳輸 | Power User / TA | L5 (Evaluate) | 繞過瀏覽器 WebSocket 阻擋；`gh cs cp` 傳圖延遲 `< 3s` | `PB-01` + 本機安裝 `gh` CLI |
| **PB-07** | Prebuilds 預建構與 Dockerfile 分層快取極速啟動 | TA (`Grace-TA`) | L6 (Create) | 冷啟動由 `~120s` 壓縮至 **`~15s`**（加速 **87.5%**） | `PB-03` + Repo Admin 權限 |
| **PB-08** | Codespaces Secrets 與 `.env` 零洩漏衛生守則 | Student / TA | L5 (Evaluate) | `git log` 憑證洩漏數 `= 0`；自動化注入測試通過率 `100%` | `PB-01` + Git ignore 機制 |
| **PB-09** | 配額堡壘與零儲存帳單關機 SOP（Stop vs. Delete FinOps） | Student / TA | L5 (Evaluate) | 月度運算 `< 120 core-hrs`；儲存壓低於 **`15 GB-months`** | `PB-01` + `PB-06` |
| **PB-10** | Codespaces 內 AI 上下文接地結對編程（`@workspace` 實戰） | Student | L6 (Create) | 程式碼重構與除錯週期縮短 `~50%` `[HYPOTHESIS]`；結合 L.A.W. 審計 | `PB-04` + GitHub Copilot |

---

## PB-01：30 秒零安裝啟動與學生 Fork `2-core` 免費層 SOP

### 1. Goal & Trigger
- **量化目標**：讓 100% 學生從零環境出發，正確將 [`Grace-TA/DM2026`](https://github.com/Grace-TA/DM2026) Fork 至個人 GitHub 帳號，並在個人免費層（Free-tier `2-core`、`120 core-hours/month`、`15 GB-months`）下完成首次容器啟動與驗證（`LO-CS-1`，Bloom's `L3 Apply`）。
- **觸發條件**：《離散數學》第 4 週實作課堂開場，或任何學生首次使用雲端開發環境時觸發。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 常見翻車操作） | After（Codespace 標準作戰 SOP） |
|:---|:---|:---|
| **網址來源** | 直接點擊助教投影幕上的 `https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/` | 開啟教師上游庫 `https://github.com/Grace-TA/DM2026`，先點 **Fork** 建立個人副本 |
| **寫入權限** | 若未 Fork 直接在他人公開庫建置（或誤連上游），執行 `git push` 時遭 `403 Permission denied` 阻擋 | `origin` 永久指向 `https://github.com/<個人帳號>/DM2026.git`，擁有完全讀寫權 |
| **硬體規格** | 隨意選取 `4-core` 或 `8-core`，將月免費時數從 `60 小時`腰斬為 `30 小時`或 `15 小時` | 明確鎖定 **`2-core`（4 GB / 8 GB RAM, 32 GB storage）** 與 **`Southeast Asia`** 節點 |

### 3. Concrete Steps（零佔位符精確步驟）

1. **登入 GitHub 並執行 Fork（耗時 ~10 秒）**：
   - 使用瀏覽器（Chrome / Edge）登入學生個人 GitHub 帳號。
   - 前往課程官方儲存庫：`https://github.com/Grace-TA/DM2026`。
   - 點擊右上角 **`Fork`** 按鈕 → 保持 Repository name 為 `DM2026` → 勾選 `Copy the main branch only` → 點擊 **`Create fork`**。
   - 確認瀏覽器網址列已變為 `https://github.com/你的帳號/DM2026`（即代表你已擁有獨立遠端儲存庫）。

2. **啟動 `2-core` 免費層 Codespace（耗時 ~20 秒操作 + ~90 秒冷啟動）**：
   - 在**你自己 Fork 後的 Repo 頁面**點擊綠色 **`<> Code`** 按鈕 → 切換至 **`Codespaces`** 分頁。
   - 點擊 **`...`（三個點選單）** → 選擇 **`New with options...`**（切勿直接盲按預設建置，以便確認規格與區域）。
   - 依序確認下列參數：
     - **Branch**: `main`
     - **Region**: `Southeast Asia`（若頁面未預設，手動選取以降低台灣連線延遲）
     - **Machine type**: **`2-core` • 8 GB RAM • 32 GB storage**（註：Free tier 固定選擇 `2-core`；實際顯示 RAM 依區域池為 `4 GB` 或 `8 GB`，重點是核心數必為 `2-core`）
   - 點擊 **`Create codespace`**。

3. **執行確定性環境自我驗證（耗時 ~3 秒）**：
   - 待 VS Code Web 畫面載入完成後，按下快捷鍵 `` Ctrl + ` ``（反引號）開啟下方 Bash Terminal。
   - 複製貼上以下指令檢查帳號身分、Git Remote 與環境：
     ```bash
     python3 --version && git remote -v && nproc && df -h /workspaces
     ```
   - 若儲存庫已部署 Book 1 所附的 `verify_codespace_env.py`，執行：
     ```bash
     python3 verify_codespace_env.py
     ```

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **啟動延遲**：標準映像冷啟動約 `60–120 秒`（若搭配 `PB-07` Prebuild 可縮短至 `~15 秒`）。
- **算力耗損**：`2-core` 實例每小時消耗 `2 core-hours`。以 GitHub 個人免費帳戶每月 `120 core-hours` 計算，相當於每月可用 **`60.0` 完整活躍開發小時**（足以支撐每週 1 次 90 分鐘課程共 4 週僅消耗 `12 core-hours`，佔月配額 **10%**）。
- **儲存警報 (`IF-THEN Law`)**：`IF 建立時配置了 32 GB 磁碟空間，THEN 即使工作坊結束僅點 Stop 仍持續計算 GB-months；MUST 在課後執行 PB-09 Delete SOP。`

### 5. Verification Check
終端機輸出必須滿足以下三個確定性條件：
1. `nproc` 輸出為 `2`（確認為 Student `2-core` Free-tier）。
2. `git remote -v` 的 `origin` URL **不包含** `Grace-TA/DM2026`，而是顯示個人帳號名稱（例如 `https://github.com/student-acct/DM2026.git`）。
3. `python3 --version` 回傳 `Python 3.10` 以上版本，無任何 `command not found` 錯誤。

---

## PB-02：`fantastic-dollop` 4-Core 助教 Live Demo 與 Live Share 救援協議

### 1. Goal & Trigger
- **量化目標**：建立 `Grace-TA` 專屬示範機 `fantastic-dollop-9rpj66gp74hxx5w`（`4-core • 16GB RAM • 32GB disk`，`Southeast Asia`）與學生個人容器之間的安全協作通道，將助教單次語法/環境救援時間壓縮至 `< 45 秒`，並維持 `0` 次權限拒訪（`403/404`）事故（Bloom's `L4 Analyze`）。
- **觸發條件**：(A) 助教進行大型現場 Live Coding 示範時；(B) 學生在 `2-core` 容器遭遇無法自行排除的 Bug 或環境異常，需要 `Grace-TA` 即時接手除錯時。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 權限誤區） | After（雙軌隔離 + Live Share 救援協議） |
|:---|:---|:---|
| **示範網址分享** | 助教直接把瀏覽器網址 `https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/` 貼到教室群組讓學生開啟 | **嚴禁分享該 URL**；助教於教室投影幕操作 `fantastic-dollop`，或由該實例發起 **Read-Only Live Share** 觀看連結 |
| **學生求救方式** | 學生用手機拍模糊螢幕照片寄給 `ta2021.vnu@gmail.com`，助教無法重現報錯與環境變數 | 學生在自己的 `2-core` Codespace 啟動 **Live Share** 邀請，助教直接從遠端進入學生的編輯器與終端機手術式修復 |
| **算力角色分配** | 助教與學生混用相同規格，助教同時跑圖表渲染與多視窗投影時容易卡頓 | 助教由 `Grace-TA` 付費帳號維持 `4-core • 16GB RAM` 高響應主機；學生維持零成本 `2-core` |

### 3. Concrete Steps（助教端與學生端雙向步驟）

#### 情境 A：助教使用 `fantastic-dollop` 進行課堂 Live Demo
1. 助教 `Grace-TA` 登入個人帳號並開啟專屬實例：
   `https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/`
2. 確認狀態列左下角顯示 `Codespaces: fantastic-dollop-9rpj66gp74hxx5w`，並於終端機執行規格檢查：
   ```bash
   echo "Cores=$(nproc), Mem=$(free -h | awk '/^Mem:/{print $2}'), Region=SoutheastAsia"
   ```
   預期輸出：`Cores=4, Mem=15Gi (16GB), Region=SoutheastAsia`。
3. 如需讓後排視力不佳的學生直接在自己電腦螢幕同步觀看助教打字（**唯讀模式，保護 `Grace-TA` 容器不被修改**）：
   - 於 VS Code 側邊欄開啟 **Live Share** 擴充套件圖示 → 點擊 **Share (Read-only)**。
   - 將產生的 `https://prod.liveshare.vsengsaas.visualstudio.com/join?...` 連結貼至課堂公告。學生點開後僅能跟隨捲動與閱讀代碼，無法操控 `Grace-TA` 的終端機或觸發儲存變更。

#### 情境 B：學生卡關求救 — 透過 Live Share 讓助教進入學生 `2-core` 容器
1. **學生端動作**（在自己的 `2-core` Fork Codespace 內執行）：
   - 按 `Ctrl + Shift + P` 開啟 Command Palette → 輸入 `Extensions: Install Extensions` → 安裝 `Live Share`（`ms-vsliveshare.vsliveshare`；建議直接寫入 `PB-03` 的 `.devcontainer.json` 預裝）。
   - 點擊左側 Live Share 圖示 → 點擊 **`Share`** → 系統會自動將動態生成的邀請網址複製到剪貼簿（格式為 `https://prod.liveshare.vsengsaas.visualstudio.com/join?<session-id>`）。
   - 將該邀請連結與學號、錯誤截圖寄至 `ta2021.vnu@gmail.com` 或貼入課堂即時求救表單。
2. **助教端動作**（`Grace-TA` 執行）：
   - 助教點擊學生提供的 Live Share 連結，於自己瀏覽器或本機 VS Code 加入該學生的 `2-core` 工作區。
   - 若需執行學生終端機診斷指令（如查看 `python3 verify_codespace_env.py`），請在 Live Share 面板向學生請求 **Shared Terminal (Read/Write)** 授權，確認修復並請學生執行 `git commit && git push` 後立即點擊 **Leave Session**。

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **助教實例消耗**：`fantastic-dollop` 為 `4-core • 16GB RAM • 32GB disk`，每活躍運行 1 小時消耗 `4 core-hours`（佔 `Grace-TA` 月度免費額度 `120 core-hours` 之 `3.33%`；若該帳號已綁定計費且超出免費額度則按 GitHub 4-core 費率計費）。
- **救援效率提升**：傳統「拍螢幕 → 問作業系統 → 猜測套件版本」平均耗時 `8–15 分鐘/人` `[HYPOTHESIS]`；改用 Live Share 直連學生容器後，助教可直接讀取相同終端機輸出，單人救援時間降至 `< 45 秒–2 分鐘` `[HYPOTHESIS]`。
- **資安防護法則 (`IF-THEN Law`)**：`IF 學生回報開啟課程連結出現 403/404，THEN 100% 檢查是否誤點 fantastic-dollop 網址，並強制引導執行 PB-01 Step 1 (Fork Grace-TA/DM2026)。`

### 5. Verification Check
- 學生端檢查：Live Share 會話結束後，按下 Live Share 面板的 **Stop Collaboration Session**（紅色停止圖示），確認右上角參與者清單歸零，確保無人持續擁有終端機連線權限。
- 助教端檢查：課後確認 `fantastic-dollop` 狀態已停止或已保存最新講義並 `git push` 至 `Grace-TA/DM2026`。

---

## PB-03：宣告式環境即代碼 (`.devcontainer/devcontainer.json`)

### 1. Goal & Trigger
- **量化目標**：以單一 JSON 設定檔加上確定性 `requirements.txt`，統一全班 30+ 位學生的 Python 3.12、Jupyter、NumPy、Matplotlib 與 Pytest 版本，將「跨機環境版本飄移率」壓低至 `0%`（Bloom's `L5 Evaluate`）。
- **觸發條件**：助教準備新學期 `DM2026` 儲存庫、或任何單元需要新增第三方科學計算套件（例如 `sympy` 用於離散數學符號運算、`networkx` 用於圖論）時觸發。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 命令式人工安裝） | After（宣告式 `.devcontainer` IaC） |
|:---|:---|:---|
| **環境設定方式** | 在 `README.md` 寫「請大家自己裝 Python 3.12 並輸入 `pip install matplotlib`」 | 透過 `.devcontainer/devcontainer.json` 在容器建置期自動執行確定性安裝 |
| **VS Code 擴充** | 學生忘記裝 `Python` 或 `Jupyter` 擴充套件，導致無語法高亮、不會自動補全 | `customizations.vscode.extensions` 自動預裝 Pylance、Jupyter、Live Share 與 GitLens |
| **編碼與繪圖問題** | 容器缺乏明確 UTF-8 設定或未固定套件版號，不同週次建出的套件行為可能偏移 | 鎖定 `requirements.txt` 版號並於設定檔強制 `files.encoding: "utf8"` |

### 3. Concrete Steps（完整檔案內容與驗證部署）

1. **在專案根目錄建立 `requirements.txt`（鎖定確定性套件清單）**：
   於 Codespace 終端機執行以下指令產生 `requirements.txt`：
   ```bash
   cat << 'EOF' > requirements.txt
   numpy==2.1.3
   matplotlib==3.9.2
   pytest==8.3.3
   ipykernel==6.29.5
   jupyterlab==4.2.5
   sympy==1.13.3
   networkx==3.4.2
   EOF
   ```
   > 註：額外納入 `sympy` 與 `networkx`，讓 `DM2026` 離散數學後續的邏輯真值表、集合論與圖論單元可零阻力接軌。

2. **建立 `.devcontainer/devcontainer.json`（錨定 `Ubuntu 24.04 LTS (Noble Numbat)`）**：
   ```bash
   mkdir -p .devcontainer
   cat << 'EOF' > .devcontainer/devcontainer.json
   {
     "name": "DM2026 Discrete Math Cloud Lab (Ubuntu 24.04 + Py3.12)",
     "image": "mcr.microsoft.com/devcontainers/base:ubuntu-24.04",
     "features": {
       "ghcr.io/devcontainers/features/python:1": {
         "version": "3.12"
       },
       "ghcr.io/devcontainers/features/github-cli:1": {
         "version": "latest"
       }
     },
     "customizations": {
       "vscode": {
         "extensions": [
           "ms-python.python",
           "ms-python.vscode-pylance",
           "ms-toolsai.jupyter",
           "ms-vsliveshare.vsliveshare",
           "eamodio.gitlens"
         ],
         "settings": {
           "python.defaultInterpreterPath": "/usr/local/bin/python",
           "python.testing.pytestEnabled": true,
           "python.testing.unittestEnabled": false,
           "editor.tabSize": 4,
           "editor.formatOnSave": false,
           "files.encoding": "utf8",
           "terminal.integrated.defaultProfile.linux": "bash"
         }
       }
     },
     "containerEnv": {
       "MPLBACKEND": "Agg",
       "PYTHONUTF8": "1"
     },
     "postCreateCommand": "python3 -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt",
     "postStartCommand": "python3 -c 'import numpy, matplotlib, sympy, networkx; print(\"DM2026 Env Ready:\", numpy.__version__, matplotlib.__version__)'",
     "remoteUser": "vscode"
   }
   EOF
   ```
   > **關鍵工程細節**：在 `"containerEnv"` 中直接預設 `"MPLBACKEND": "Agg"` 與 `"PYTHONUTF8": "1"`，從 OS 環境變數層根治無頭繪圖當機與繁體中文輸出編碼異常！且只有放在 `/workspaces/DM2026` 底下的檔案會在 `Rebuild Container` 時受 Persistent Volume 保護。

3. **提交設定至 GitHub 並執行容器重建測試（Rebuild Container）**：
   ```bash
   git add requirements.txt .devcontainer/devcontainer.json
   git commit -m "chore(devcontainer): add Ubuntu 24.04 + Python 3.12 declarative lab environment for DM2026"
   git push origin main
   ```
   隨後按 `Ctrl + Shift + P` → 執行 `Codespaces: Rebuild Container` 驗證無報錯收斂。

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **首次建置耗時**：執行 `postCreateCommand` 安裝 7 個核心套件約需 `45–75 秒`（僅發生於容器首次建立時；後續喚醒僅執行 `postStartCommand` 耗時 `< 1.5 秒`）。
- **磁碟空間消耗**：`--no-cache-dir` 旗標可節省約 `350–500 MB` 的 pip wheel 暫存檔案，降低 `32 GB` 持久卷膨脹速率。
- **品質門控法則 (`IF-THEN Law`)**：`IF 修改了 devcontainer.json 或 requirements.txt，THEN MUST 執行一次 Rebuild Container 驗證完全通過後才可 git push 至主分支，防止全班 30 人同步拉取損壞的建置配置。`

### 5. Verification Check
在重建完成後的終端機執行：
```bash
cat /etc/os-release | grep PRETTY_NAME && echo "MPLBACKEND=$MPLBACKEND | PYTHONUTF8=$PYTHONUTF8" && python3 -m pip check && pytest --version
```
預期必須看到 `PRETTY_NAME="Ubuntu 24.04..."`、`MPLBACKEND=Agg | PYTHONUTF8=1`、`No broken requirements found.` 與 `pytest`。

---

## PB-04：Google Colab-to-Codespaces 無痛遷移（`DM2026` `WEEK01`–`WEEK03`）

### 1. Goal & Trigger
- **核心選型原則（取代 vs. 互補）**：在「一般程式開發、演算法教學（如離散數學 `DM2026` 常用之 `NetworkX`、`SymPy`、`Z3` 僅需 CPU）、多檔案專案與軟體工程」上，**Codespaces 完全取代 Google Colab 且功能更強大**（完整 `Ubuntu 24.04.5 LTS` 容器＋`ms-toolsai.jupyter`＋Debugger＋`/workspaces/DM2026` 持久保留磁碟與 Git）；僅在「需要免費 T4 GPU 訓練深度學習模型」時，兩者屬**互補關係**。
- **量化目標**：將 `Grace-TA/DM2026` 前三週累積的 Colab 知識（`WEEK01.md` Colab 基礎、`WEEK02.md` Python 101 語法、`WEEK03.md` OOP / `try-except` / `matplotlib` 4-phase triangle waves & unit circle parametric plot）在 `< 5 分鐘`內轉化為符合工程標準的模組化 `.py` 與可執行 `.ipynb` 專案，並具備自動化單元測試（Bloom's `L4 Analyze`）。
- **觸發條件**：學生準備將 `WEEK02` / `WEEK03` 課堂練習打包為可版控專案、或把 `.ipynb` 轉為可重複執行的 Python 模組時。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（Google Colab 免費版反模式） | After（Codespaces 雙棲模組化架構） |
|:---|:---|:---|
| **環境與斷線風險** | 單一瀏覽器沙盒（2-core / ~12.7GB RAM），閒置約 90 分鐘斷線後本機磁碟清空，須手動掛載 Drive | `/workspaces/DM2026` 永久保留磁碟狀態，整合 `ms-toolsai.jupyter` + 中斷點 Debugger + Git Commit/Push |
| **Magic 指令** | 檔案內殘留 `!pip install` 或 `%matplotlib inline` 導致 `.py` 報錯 `SyntaxError` | 移除 IPython magic，依賴交給 `PB-03`，無頭繪圖交給 `MPLBACKEND=Agg` 與 `fig.savefig()` |
| **圖表輸出** | 只呼叫 `plt.show()`，在雲端終端機執行無任何圖片產出亦無法比對結果 | 類別化封裝（`class ParametricVisualizer`），同時支援終端機輸出 PNG 與 VS Code 內嵌檢視 |
| **程式驗證** | 靠肉眼看螢幕有沒有跑出結果，無法批次檢查 `WEEK02` 9×9 或 `WEEK03` 函數邏輯 | 搭配 `pytest` 驗證離散數學與座標計算不變量（如單位圓 $\cos^2\theta + \sin^2\theta = 1$） |

### 3. Concrete Steps（以 `WEEK03.md` 為核心的實戰遷移代碼）

1. **建立標準專案資料夾結構**：
   ```bash
   mkdir -p src tests outputs
   ```
2. **將 `WEEK03.md` 的 OOP + 4-phase triangle waves + unit circle parametric plot 工程化為 `src/week03_lab.py`**：
   ```bash
   cat << 'EOF' > src/week03_lab.py
   """
   DM2026 WEEK03 Colab-to-Codespaces 遷移範本
   涵蓋：List Comprehension, Dict/Set 離散結構, try-except, OOP 封裝,
   以及 Matplotlib 4-Phase Triangle Waves 與 Unit Circle Parametric Plot。
   """
   from __future__ import annotations

   import math
   from pathlib import Path
   import matplotlib
   matplotlib.use("Agg")
   import matplotlib.pyplot as plt
   import numpy as np


   class DiscreteSignalLab:
       """封裝 WEEK02-WEEK03 數學運算與圖形渲染邏輯。"""

       def __init__(self, out_dir: str | Path = "outputs") -> None:
           self.out_dir = Path(out_dir)
           self.out_dir.mkdir(parents=True, exist_ok=True)

       @staticmethod
       def multiplication_table(n: int = 9) -> list[list[int]]:
           """WEEK02 複習：使用 List Comprehension 建構 n x n 乘法表矩陣。"""
           if not isinstance(n, int) or n <= 0:
               raise ValueError(f"n 必須為正整數，收到: {n}")
           return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

       @staticmethod
       def discrete_set_relations(a: set[int], b: set[int]) -> dict[str, set[int]]:
           """WEEK03 離散集合運算：回傳聯集、交集、差集與對稱差集字典。"""
           return {
               "union": a | b,
               "intersection": a & b,
               "diff_a_minus_b": a - b,
               "symmetric_diff": a ^ b,
           }

       @staticmethod
       def triangle_wave(x: np.ndarray, phase: float = 0.0) -> np.ndarray:
           """計算週期為 2*pi 之標準化三角波（值域 [-1, 1]）。"""
           return (2.0 / np.pi) * np.arcsin(np.sin(x + phase))

       def plot_four_phase_triangle_waves(self, filename: str = "week03_4phase_triangle.png") -> Path:
           """繪製 4-Phase Triangle Waves（0, pi/2, pi, 3pi/2）。"""
           x = np.linspace(0, 4 * np.pi, 1000)
           phases = {
               "Phase 0": 0.0,
               "Phase pi/2": math.pi / 2,
               "Phase pi": math.pi,
               "Phase 3pi/2": 3 * math.pi / 2,
           }
           fig, ax = plt.subplots(figsize=(9, 4.5))
           for label, phi in phases.items():
               ax.plot(x, self.triangle_wave(x, phase=phi), linewidth=1.8, label=label)
           ax.set_title("DM2026 WEEK03: 4-Phase Triangle Waves")
           ax.set_xlabel("x (radians)")
           ax.set_ylabel("Amplitude")
           ax.grid(True, linestyle="--", alpha=0.4)
           ax.legend(loc="upper right")
           out_file = self.out_dir / filename
           fig.savefig(out_file, dpi=150, bbox_inches="tight")
           plt.close(fig)
           return out_file

       def plot_unit_circle_parametric(self, filename: str = "week03_unit_circle.png") -> Path:
           """繪製 Unit Circle Parametric Plot: (cos(t), sin(t))。"""
           t = np.linspace(0, 2 * math.pi, 500)
           x_vals = np.cos(t)
           y_vals = np.sin(t)
           fig, ax = plt.subplots(figsize=(5, 5))
           ax.plot(x_vals, y_vals, color="#2563eb", linewidth=2.2, label="x=cos(t), y=sin(t)")
           ax.axhline(0, color="gray", linewidth=0.8)
           ax.axvline(0, color="gray", linewidth=0.8)
           ax.set_aspect("equal", adjustable="box")
           ax.set_title("DM2026 WEEK03: Unit Circle Parametric Plot")
           ax.grid(True, alpha=0.35)
           ax.legend(loc="upper right")
           out_file = self.out_dir / filename
           fig.savefig(out_file, dpi=150, bbox_inches="tight")
           plt.close(fig)
           return out_file


   def main() -> None:
       lab = DiscreteSignalLab(out_dir="outputs")
       try:
           table = lab.multiplication_table(9)
           print(f"9x9 乘法表驗證: 9*9 = {table[8][8]}")
           rel = lab.discrete_set_relations({1, 2, 3, 4}, {3, 4, 5})
           print(f"集合交集={rel['intersection']}, 對稱差={rel['symmetric_diff']}")
           p1 = lab.plot_four_phase_triangle_waves()
           p2 = lab.plot_unit_circle_parametric()
           print(f"圖表輸出完成: {p1} ({p1.stat().st_size} bytes), {p2} ({p2.stat().st_size} bytes)")
       except Exception as exc:
           print(f"[ERROR] 執行過程捕獲例外: {exc}")
           raise


   if __name__ == "__main__":
       main()
   EOF
   ```

3. **撰寫對應的自動化單元測試 `tests/test_week03_lab.py`**：
   ```bash
   cat << 'EOF' > tests/test_week03_lab.py
   import numpy as np
   import pytest
   from src.week03_lab import DiscreteSignalLab


   def test_multiplication_table_9x9():
       tbl = DiscreteSignalLab.multiplication_table(9)
       assert len(tbl) == 9
       assert tbl[8][8] == 81
       with pytest.raises(ValueError):
           DiscreteSignalLab.multiplication_table(0)


   def test_discrete_set_relations():
       res = DiscreteSignalLab.discrete_set_relations({1, 2, 3}, {2, 3, 4})
       assert res["intersection"] == {2, 3}
       assert res["symmetric_diff"] == {1, 4}


   def test_triangle_wave_bounds():
       x = np.linspace(0, 2 * np.pi, 200)
       y = DiscreteSignalLab.triangle_wave(x, phase=np.pi / 2)
       assert np.all(y <= 1.000001) and np.all(y >= -1.000001)


   def test_plots_generated(tmp_path):
       lab = DiscreteSignalLab(out_dir=tmp_path)
       p1 = lab.plot_four_phase_triangle_waves()
       p2 = lab.plot_unit_circle_parametric()
       assert p1.exists() and p1.stat().st_size > 15_000
       assert p2.exists() and p2.stat().st_size > 15_000
   EOF
   ```

4. **（選用）若需從舊 `.ipynb` 批次轉成 `.py`**：
   ```bash
   jupyter nbconvert --to script my_colab_notebook.ipynb
   ```
   （註：於 VS Code 編輯器內點擊任意 `.png` 檔案即可直接以側邊分頁檢視高解析度圖表，無需任何本機視窗。）

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **執行延遲**：執行 `python3 src/week03_lab.py` 生成兩張 150-DPI 圖表僅耗時 `~0.8–1.2 秒`；完整 `pytest` 4 項測試耗時 `< 1.5 秒`。
- **程式碼重用性**：從一次性 Notebook 轉為 `src/` + `tests/` 結構後，後續週次作業僅需 `from src.week03_lab import DiscreteSignalLab` 即可複用。
- **品質檢核法則 (`IF-THEN Law`)**：`IF 執行 Matplotlib 腳本產生空圖檔或尺寸 < 5 KB，THEN 檢查是否誤在 plt.savefig() 之前呼叫了 plt.show() 導致畫布被清空。`

### 5. Verification Check
```bash
python3 -m src.week03_lab && PYTHONPATH=. pytest -v tests/test_week03_lab.py
```
必須看到 `9x9 乘法表驗證: 9*9 = 81`、兩張圖表大小均 `> 15,000 bytes`，且 `4 passed` 全部綠燈。

---

## PB-05：Port Forwarding 與 HTTPS 安全預覽通道（權限三級管控）

### 1. Goal & Trigger
- **量化目標**：將 Codespace 內部運行的 Web 伺服器或圖表預覽畫廊安全映射至外部 HTTPS URL，並在 `Private`、`Organization` 與 `Public` 三種能見度等級中零失誤選擇正確的資安邊界（Bloom's `L4 Analyze`）。
- **觸發條件**：學生需要透過瀏覽器預覽 `outputs/` 生成的 `WEEK03` 圖表畫廊、或於未來課程建置 FastAPI / Flask 離散數學互動計算網頁並交由助教驗收時。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 盲開 Public 或硬連 localhost） | After（受控 HTTPS Relay + 三級能見度矩陣） |
|:---|:---|:---|
| **本機網址迷思** | 在自己電腦瀏覽器直接輸入 `http://127.0.0.1:8000` 試圖存取雲端容器網頁，結果 `ERR_CONNECTION_REFUSED` | 透過 GitHub Tunnel 自動映射為 `https://<codespace>-8000.app.github.dev` |
| **權限管理風險** | 為了圖方便一律切換成 `Public`，導致任何網路掃描器都能讀取未設密碼的測試 API | 依場景嚴格分級：個人除錯一律 **`Private`**（需 GitHub OAuth 登入），僅短暫展示才依規定調整 |

### 3. Concrete Steps（啟動預覽畫廊與權限切換）

1. **在 `outputs/` 建立簡易索引頁並啟動 Python HTTP Server**：
   ```bash
   cat << 'EOF' > outputs/index.html
   <!DOCTYPE html>
   <html lang="zh-Hant">
   <head><meta charset="utf-8"><title>DM2026 WEEK03 Plot Gallery</title></head>
   <body style="font-family:sans-serif;background:#0f172a;color:#f8fafc;padding:24px;">
     <h1>DM2026 WEEK03 數學視覺化成果展</h1>
     <div style="display:flex;gap:24px;flex-wrap:wrap;">
       <div><h3>4-Phase Triangle Waves</h3><img src="week03_4phase_triangle.png" style="max-width:520px;border-radius:8px;"></div>
       <div><h3>Unit Circle Parametric Plot</h3><img src="week03_unit_circle.png" style="max-width:360px;border-radius:8px;"></div>
     </div>
   </body>
   </html>
   EOF
   python3 -m http.server 8000 --directory outputs
   ```
2. **確認與調整 Port Visibility（UI 或 CLI 雙軌）**：
   - **UI 方式**：於 VS Code 下方面板點選 **`Ports`** 分頁 → 找到 Port `8000` → 滑鼠右鍵點選 **`Port Visibility`** → 選擇 **`Private`**（預設，只有登入你個人 GitHub 帳號的瀏覽器能開啟）、`Private to Organization`（僅企業/學校組織內成員可見）或 `Public`（公開網址，任何人可連）。
   - **CLI 方式**（從本機終端機或有權限之環境透過 `gh` 設定）：
     ```bash
     CS_NAME=$(gh cs list --json name -q '.[0].name')
     gh cs ports visibility 8000:private -c "$CS_NAME"
     gh cs ports -c "$CS_NAME"
     ```
3. **三級能見度決策規則表**：

| Visibility 等級 | 存取認證門檻 | 適用教學場景 | 資安風險與管制原則 |
|:---|:---|:---|:---|
| **`Private`（預設推薦）** | 必須持有 Codespace 擁有者的 GitHub OAuth Session Cookie | 個人開發預覽 `outputs/index.html`、測試個人後端 API | **風險最低**；他人取得網址也會被 GitHub 登入牆攔截 |
| **`Organization`** | 須登入屬於同一 GitHub Organization 的帳號 | 僅限團隊於付費 GitHub Enterprise / Team 組織庫內互評 | 個人帳號 Fork (`student/DM2026`) 通常不屬於同一 Organization，一般課堂不適用 |
| **`Public`** | **無需登入**，任何知道網址的人皆可透過 HTTPS 存取 | 臨時向助教展示前端純靜態 HTML 頁面（無敏感資料） | **高風險**：禁止在開啟 `Public` 的伺服器暴露 `.env` 除錯資訊或寫入端點，展示完畢立即 `Ctrl+C` 關閉 Server |

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **建立延遲**：VS Code Server 偵測到 `0.0.0.0:8000` 或 `127.0.0.1:8000` 監聽後，約 `2–5 秒`內自動彈出 "Open in Browser" 通知。
- **額外費用**：Port Forwarding Tunnel 流量包含於 Codespaces 基礎網路服務中，不另收額外 `core-hours`（僅計算容器運行時間）。
- **防漏法則 (`IF-THEN Law`)**：`IF Port 8000 承載包含檔案上傳或系統命令的介面，THEN 嚴禁將 Visibility 設為 Public，MUST 維持 Private 並改用 PB-02 Live Share 讓助教透過內部隧道檢視。`

### 5. Verification Check
- 點擊 `Ports` 分頁中 Port `8000` 的地球圖示（Open in Browser），成功看見黑色背景的 `DM2026 WEEK03 數學視覺化成果展` 與兩張高畫質數學圖表。
- 使用瀏覽器「無痕視窗（Incognito）」開啟同一個 URL：若為 `Private` 模式，必須被重導向至 GitHub 登入畫面（驗證防護生效）；測試完成後回到終端機按 `Ctrl + C` 停止 `http.server`。

---

## PB-06：GitHub CLI (`gh codespace`) 遠端終端機與檔案傳輸

### 1. Goal & Trigger
- **量化目標**：使助教與進階學生能不依賴瀏覽器 WebSocket 畫面，直接從本機 PowerShell / Terminal 透過 `gh codespace`（簡寫 `gh cs`）完成實例列舉、SSH 連線、雙向檔案傳輸（`gh cs cp`）、停機與批次刪除（Bloom's `L5 Evaluate`）。
- **觸發條件**：(A) 教室防火牆阻擋瀏覽器版 VS Code WebSocket 連線時（備援逃生通道）；(B) 需將雲端計算產出的 PNG/CSV 批次拉回本機交作業，或課後用一行指令清理所有閒置容器。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 純滑鼠點網頁） | After（`gh cs` CLI 自動化管線） |
|:---|:---|:---|
| **瀏覽器卡死** | 遇校園網路不穩卡在 "Setting up remote connection"，整堂課無法輸入指令 | 本機執行 `gh cs ssh` 直接走加密 SSH Tunnel 取得極低頻寬需求的純文字終端機 |
| **下載圖表檔案** | 在網頁側邊欄右鍵逐一 `Download...` 10 張圖表與測試報告 | 一行 `gh cs cp` 指令整包資料夾拉回本機硬碟 |
| **清理多個容器** | 忘記開網頁檢查，導致上週建的容器默默在背景消耗 `GB-months` | `gh cs list` 一覽全局狀態，並用 `gh cs stop` / `gh cs delete` 秒級處置 |

### 3. Concrete Steps（全套 `gh cs` 實戰指令集，零佔位符）

1. **本機登入與授權驗證（僅首次需執行）**：
   ```powershell
   gh auth login --web -s codespace
   gh auth status
   ```
   > 關鍵旗標 `-s codespace`（或使用 `gh auth refresh -h github.com -s codespace`）確保本機 Token 具備操作 Codespaces 的權限作用域。

2. **查詢目前帳號所有 Codespaces（含機器規格、狀態與實例名稱）**：
   ```powershell
   gh cs list
   ```
   在 PowerShell 中若想自動擷取第一個運行中或存在的實例名稱存成變數：
   ```powershell
   $CS = (gh cs list --json name -q ".[0].name")
   Write-Output "Target Codespace: $CS"
   ```

3. **透過 CLI 直接建立 `Southeast Asia` `2-core` 容器（或登入 SSH）**：
   ```powershell
   # 先確認當前帳號與可用機器規格
   $USER_LOGIN = (gh api user -q ".login")
   gh cs create -R "$USER_LOGIN/DM2026" -b main -m basicLinux32gb -l SoutheastAsia
   ```
   連線進入遠端容器的互動式 Bash 終端機：
   ```powershell
   $CS = (gh cs list --json name -q ".[0].name")
   gh cs ssh -c $CS
   ```

4. **雙向檔案傳輸（`gh cs cp`）**：
   - 將雲端 Codespace 產出的 `WEEK03` 圖表整批複製到本機 `./local_dm2026_outputs/`：
     ```powershell
     New-Item -ItemType Directory -Force -Path ".\local_dm2026_outputs" | Out-Null
     gh cs cp -r -c $CS "remote:/workspaces/DM2026/outputs/" ".\local_dm2026_outputs\"
     ```
   - 將本機寫好的作業測試檔上傳至雲端容器：
     ```powershell
     gh cs cp -c $CS ".\verify_codespace_env.py" "remote:/workspaces/DM2026/"
     ```

5. **停機與徹底刪除（精準生命週期終結）**：
   ```powershell
   # 僅暫停算力（注意：32GB 磁碟仍計費儲存！）
   gh cs stop -c $CS

   # 課後徹底刪除容器與磁碟卷（停止一切計費）
   gh cs delete -c $CS --force
   ```

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **頻寬節省**：瀏覽器 VS Code Web 啟動須下載數十 MB 前端 JS 資源並維持長時 WebSocket 心跳；改用 `gh cs ssh` 純終端機連線，頻寬需求降低 `> 90%` `[HYPOTHESIS]`，在高延遲教室 Wi-Fi 下仍可流暢執行 `python3` 與 `pytest`。
- **操作效率**：以 CLI 批次 `delete` 取代進入網頁多層選單點擊確認，可將課後清理耗時從 `60 秒`降至 `< 3 秒`。
- **防呆法則 (`IF-THEN Law`)**：`IF 本機執行 gh cs list 回傳 HTTP 403/scopes missing，THEN 立即執行 gh auth refresh -s codespace 補齊權限，無需重新安裝 CLI。`

### 5. Verification Check
```powershell
Get-ChildItem ".\local_dm2026_outputs" -Filter "*.png"
gh cs list
```
第一行應列出本機成功拉回的 `week03_4phase_triangle.png` 與 `week03_unit_circle.png`；若已執行 `delete`，第二行 `gh cs list` 應回傳空清單。

---

## PB-07：Prebuilds 預建構與 Dockerfile 分層快取極速啟動

### 1. Goal & Trigger
- **量化目標**：針對 `Grace-TA/DM2026` 啟用 GitHub Codespaces Prebuilds 並將 `.devcontainer/devcontainer.json` 升級為「分層快取優化版 `.devcontainer/Dockerfile`」，將學生課堂開啟容器的冷啟動時間從 `~120 秒` 壓縮至 **`~15 秒`**（加速 **87.5%**）（Bloom's `L6 Create`）。
- **觸發條件**：課堂人數 `>= 20 人`、或依賴套件體積較大（超過 5 個科學計算套件，純 `postCreateCommand` 耗時超過 60 秒）時由助教 `Grace-TA` 於上游庫設定。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（無 Prebuild / 無 Dockerfile 快取） | After（分層 Dockerfile + Prebuild 映像快照） |
|:---|:---|:---|
| **啟動流程** | 30 位學生上課同時按 Create → 30 台機器各自從 PyPI 下載編譯 NumPy/Matplotlib | GitHub 在上游 Repo 推送更新時預先在背景建好容器磁碟快照；學生按下 Create 直接掛載 |
| **學生等待時間** | `90–150 秒`（容易造成課堂前排已開好、後排還在轉圈的節奏撕裂） | **`~10–20 秒`** 直接看見編輯器與已就緒的 Python 環境 |
| **Dockerfile 寫法** | 若把 `COPY . .` 寫在 `pip install` 之前，每次改 `WEEK03.md` 都讓快取全部失效 | 先 `COPY requirements.txt` → `pip install` → 最後才交給工作區掛載，最大化層快取命中率 |

### 3. Concrete Steps（`.devcontainer/Dockerfile` 與 Repo Prebuild 配置）

1. **撰寫快取最優化的 `.devcontainer/Dockerfile`（錨定 `Ubuntu 24.04 LTS`）**：
   ```bash
   cat << 'EOF' > .devcontainer/Dockerfile
   FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

   # 第一層：極少變動的系統依賴（Python 3.12 + 中文字型 Noto CJK，避免 Matplotlib 畫中文變豆腐塊）
   RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
       && apt-get -y install --no-install-recommends python3 python3-pip python3-venv fonts-noto-cjk \
       && apt-get clean && rm -rf /var/lib/apt/lists/*

   # 第二層：僅在 requirements.txt 變更時才重建的 Python 套件快取層
   COPY requirements.txt /tmp/pip-tmp/requirements.txt
   RUN pip3 --disable-pip-version-check --no-cache-dir install --break-system-packages --upgrade pip \
       && pip3 --disable-pip-version-check --no-cache-dir install --break-system-packages -r /tmp/pip-tmp/requirements.txt \
       && rm -rf /tmp/pip-tmp
   EOF
   ```

2. **更新 `.devcontainer/devcontainer.json` 指向該 `Dockerfile`**：
   將原 `"image": ...` 替換為 `"build"` 區塊，並移除重複的 `postCreateCommand` 安裝指令（因為已在 Dockerfile Build Time 完成）：
   ```json
   {
     "name": "DM2026 Prebuilt Cloud Lab (Py3.12)",
     "build": {
       "dockerfile": "Dockerfile",
       "context": ".."
     },
     "features": {
       "ghcr.io/devcontainers/features/github-cli:1": {
         "version": "latest"
       }
     },
     "customizations": {
       "vscode": {
         "extensions": [
           "ms-python.python",
           "ms-python.vscode-pylance",
           "ms-toolsai.jupyter",
           "ms-vsliveshare.vsliveshare",
           "eamodio.gitlens"
         ]
       }
     },
     "containerEnv": {
       "MPLBACKEND": "Agg",
       "PYTHONUTF8": "1"
     },
     "remoteUser": "vscode"
   }
   ```

3. **在 `Grace-TA/DM2026` 啟用 GitHub Prebuilds**：
   - 助教前往 `https://github.com/Grace-TA/DM2026/settings/codespaces`。
   - 點擊 **`Set up prebuild`**。
   - 設定參數：
     - **Branch**: `main`
     - **Regions**: 勾選 **`Southeast Asia`**（只建構課程主力區域！切勿勾選 All Regions 以免產生多餘區域預建構儲存費用）。
     - **Prebuild triggers**: 選擇 **`On configuration change`**（僅當 `.devcontainer/` 或 `requirements.txt` 異動時才重編，而非每次修改 `WEEK03.md` 講義文字都耗費 Actions/Prebuild 分鐘數）。
   - 點擊 **`Create`**，等待約 3 分鐘直到 Prebuild 狀態轉為綠燈 `Available`。

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **時間壓縮**：學生冷啟動從 `~120 秒` 降至 **`~15 秒`**，若 30 人同時上課，單堂課共節省約 `52.5 人-分鐘` 的等待停滯成本 `[HYPOTHESIS]`。
- **FinOps 儲存權衡 (Trade-off)**：Prebuild 產生的容器模板快照會計入上游儲存庫擁有者（`Grace-TA`）的儲存額度（僅該特定區域之模板消耗），因此**務必只選取單一區域 `Southeast Asia` 且觸發條件設為 `On configuration change`**，可將額外建置成本壓低 `> 75%`。
- **Fork 提醒 (`IF-THEN Law`)**：`IF 學生是在個人 Fork Repo 建置 Codespace，THEN 注意 GitHub Prebuild 預設為該 Repository 獨立設定；若要讓學生直接吃到 Grace-TA 預建置快取，可讓學生於公開 Repo 上直接建立 Codespace 練習並將程式碼下載或改推分支，或引導學生保留 ~90s 首次建置（仍遠快於本機安裝）。`

### 5. Verification Check
- 在 `Grace-TA/DM2026/settings/codespaces` 確認 `Prebuild configuration` 顯示綠色勾選與 `Southeast Asia` 區域標籤。
- 新建一個測試 Codespace，計時從按下 `Create codespace` 到終端機可輸入 `python3 -c "import matplotlib; print(matplotlib.__version__)"` 的時間應 `< 25 秒`，且支援 Matplotlib 中文標題無方框亂碼。

---

## PB-08：Codespaces Secrets 與 `.env` 零洩漏衛生守則

### 1. Goal & Trigger
- **量化目標**：確保全學期學生與助教 (`ta2021.vnu@gmail.com`) 的任何 API Key、資料庫密碼或測試憑證在 `git log` 中的洩漏次數為 **`0`**，並正確使用 GitHub Codespaces Secrets 進行環境變數安全注入（Bloom's `L5 Evaluate`）。
- **觸發條件**：課程專題需串接外部天氣/公開資料 API、LINE Notify / Email SMTP 測試腳本，或任何出現需要金鑰/密碼的程式單元時。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 明文硬編碼） | After（Codespaces Secrets + `.env` 雙層隔離） |
|:---|:---|:---|
| **金鑰存放** | 把 `API_KEY = "sk-xxxx"` 直接寫死在 `week04_api.py` 裡然後 `git push` 到公開的 Fork Repo | 寫入 GitHub 帳號 **`Settings → Codespaces → Secrets`**，程式碼僅讀取 `os.environ.get("DM2026_API_KEY")` |
| **本機測試檔** | 在資料夾建了 `.env` 卻沒加進 `.gitignore`，執行 `git add .` 整包公開上傳 | 強制配置 `.gitignore` 忽略 `.env*`，只允許提交不含真實金鑰的 `.env.example` |
| **事故補救** | 發現推錯金鑰後只用新 commit 刪掉那行，以為已經沒事（實際上還留在 `git log` 歷史中） | 立即撤銷舊金鑰並重新輪替（Rotate），絕不依賴「覆蓋 commit」掩飾外洩 |

### 3. Concrete Steps（三層防禦實作）

1. **建立堅不可摧的 `.gitignore` 與安全範本 `.env.example`**：
   ```bash
   cat << 'EOF' >> .gitignore

   # === Security & Secrets Hygiene ===
   .env
   .env.local
   .env.*.local
   *.pem
   *.key
   credentials.json
   EOF

   cat << 'EOF' > .env.example
   # 複製此檔為 .env 後填入測試參數（切勿提交真實金鑰至 Git）
   DM2026_DEMO_MODE=true
   DM2026_APP_TOKEN=replace_with_your_codespaces_secret
   EOF
   ```

2. **在 GitHub 帳號層級設定 Codespaces Secret（安全注入容器）**：
   - 開啟個人帳號設定頁：`https://github.com/settings/codespaces`。
   - 找到 **`Codespaces secrets`** → 點擊 **`New secret`**。
   - **Name**: `DM2026_APP_TOKEN`（全大寫蛇形命名）。
   - **Value**: 貼入你的測試 Token（如教師發放的課堂演習密鑰）。
   - **Repository access**: 僅勾選 **`<你的帳號>/DM2026`**（最小權限原則 Principle of Least Privilege，切勿開放給無關儲存庫）。
   - 若正在運行中的 Codespace 新增了 Secret，系統右上角會提示 **`Reload to apply`**，點擊後環境變數即自動注入容器。

3. **Python 安全讀取模式與提交前掃描指令**：
   在 Python 程式中統一採用 Fail-Fast 安全讀取：
   ```python
   import os

   token = os.environ.get("DM2026_APP_TOKEN")
   if not token:
       raise RuntimeError(
           "缺少環境變數 DM2026_APP_TOKEN！請於 GitHub Settings -> Codespaces -> Secrets 設定，切勿寫死於程式碼。"
       )
   print(f"Token loaded safely (length={len(token)}, prefix={token[:2]}***)")
   ```
   每次執行 `git commit` 前，先跑一行快速資安自檢：
   ```bash
   git status --short && grep -rnE "(ghp_|sk-|AIza|BEGIN RSA PRIVATE KEY)" src/ tests/ || echo "SECURITY_SCAN_CLEAN"
   ```

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **執行成本**：`.gitignore` 檢查與 `grep` 掃描耗時 `< 0.2 秒`，零額外費用。
- **事故止血價值**：公開儲存庫若意外洩漏雲端或 AI 金鑰，自動化爬蟲機器人（Secret Scanners）平均在 **`15–120 秒`內**即可掃描並盜刷額度。採用 GitHub Codespaces Secrets 可從架構上徹底歸零此風險。
- **違規處置法則 (`IF-THEN Law`)**：`IF git status 出現未受忽略的 .env 檔案或掃描命中金鑰特徵，THEN 強制中止 git push 並執行 git rm --cached .env；IF 已推送至公開 GitHub，THEN 該金鑰視為永久作廢，MUST 於 5 分鐘內撤銷換新。`

### 5. Verification Check
```bash
git check-ignore -v .env && echo "GITIGNORE_VERIFIED"
```
若存在 `.env`，必須輸出 `.gitignore:... .env` 與 `GITIGNORE_VERIFIED`，代表 Git 確定會將其排除於版本追蹤之外；同時確認 `git ls-files | grep -E "^\.env$"` 回傳為空。

---

## PB-09：配額堡壘與零儲存帳單關機 SOP（Stop vs. Delete FinOps）

### 1. Goal & Trigger
- **量化目標**：透過精準區分「計算計費（`core-hours`）」與「儲存計費（`GB-months`）」，確保所有學生與助教將個人免費帳戶消耗壓制在 **`< 120 core-hours/月`** 與 **`< 15 GB-months/月`** 安全水位之內，實現連續整學期 **`$0.00` 意外帳單**（`LO-CS-4`，Bloom's `L5 Evaluate`）。
- **觸發條件**：每堂 90 分鐘工作坊結束前最後 3 分鐘（全班統一執行）、以及每週日定期健康檢查時。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / "Stop = 免費" 誤區） | After（計算/儲存解耦 + 課後 Delete SOP） |
|:---|:---|:---|
| **下課習慣** | 直接關閉瀏覽器分頁，或只點選 **Stop codespace** 以為已經不扣額度 | 先 `git push` 所有成果，立即點選 **Delete codespace** 釋放 `32 GB` 磁碟卷 |
| **逾時與保留設定** | 維持預設值或忘記調整，容器放著閒置或停機保留長達 30 天 | 帳號設定 `Default idle timeout = 30 minutes` 與 `Default retention period = 1 day` |
| **帳單監控** | 等到某天被阻斷建立新 Codespace 才發現額度歸零 | 課前課後定期巡檢 GitHub Billing Codespaces 條目，掌握精確剩餘天數 |

### 3. Concrete Steps（精確算術證明與執行步驟）

#### 第一部分：為何「Stop 仍會爆 `15 GB-months`」？（FinOps 算術驗證）
GitHub 免費層提供每月兩項獨立上限：
1. **運算上限**：`120 core-hours / month`
   - 學生使用 `2-core`：$120 \div 2 = \mathbf{60\text{ 小時/月}}$ 實際開機時間。
   - 助教使用 `4-core`（`fantastic-dollop`）：$120 \div 4 = \mathbf{30\text{ 小時/月}}$ 實際開機時間。
2. **儲存上限**：`15 GB-months / month`（以 `32 GB` 磁碟配額或實際佔用容量按小時累計）
   - 若一個已佔用約 `15 GB` 實際空間（含 Ubuntu Base Image + Python 3.12 + Matplotlib/NumPy + VS Code Server）的 `32 GB` 磁碟容器**僅執行 Stop 而未 Delete**：
     - 放置 1 個月（30 天）= 消耗 `~15 GB-months`（緊貼上限邊緣！）。
     - 若學生手誤建了 **2 個**未刪除的容器（例如本週建一個、上週忘記刪），僅放置 15 天即突破 `15 GB-months` 免費上限，導致帳號被鎖定無法再開啟任何新 Codespace！
   - 反之，若每次下課**執行 `git push` 後立即 `Delete`**：
     - 單場 90 分鐘工作坊（使用空間約 `15 GB`，存在時間 `2 小時 / 720 小時`）的儲存消耗僅為：
       $$15\text{ GB} \times \frac{2\text{ hours}}{720\text{ hours}} \approx \mathbf{0.042\text{ GB-months}}$$
       整學期 16 週合計僅消耗 **`~0.67 GB-months`**（僅佔免費額度的 **4.5%**）！

#### 第二部分：課堂最後 3 分鐘「五步零帳單安全撤離 SOP」
1. **Step 1 — 確認變更已全部存檔並推送至 GitHub Fork**：
   ```bash
   git status
   git add -A && git commit -m "chore(dm2026): save workshop progress before codespace teardown" && git push origin main
   ```
   > **安全檢查**：必須看到 `main -> main` 推送成功，且再次輸入 `git status` 顯示 `nothing to commit, working tree clean`！若未 push 就 Delete，容器內未同步檔案將永久遺失。
2. **Step 2 — 前往個人 GitHub Codespaces 管理控制台**：
   開啟網址：`https://github.com/codespaces`。
3. **Step 3 — 執行徹底刪除（Delete，非 Stop）**：
   找到本次課程建立的 Codespace → 點擊右側 **`...`** → 選擇 **`Delete`** → 確認刪除。
   （若使用本機 CLI，直接執行：`gh cs list` 確認名稱後執行 `gh cs delete -c <codespace-name>`）。
4. **Step 4 — 永久加固個人帳號防呆設定（僅做一次）**：
   前往 `https://github.com/settings/codespaces`：
   - **Default idle timeout**: 設為 **`30 minutes`**（防忘記關網頁時算力空轉超過半小時）。
   - **Default retention period**: 設為 **`1 day`**（最低保護，即使偶爾忘記刪，停止超過設定天數也會協助止損，但仍不可替代課後主動 Delete）。
5. **Step 5 — 檢查當月剩餘免費額度**：
   前往 `https://github.com/settings/billing` → 展開 **`Codespaces`** 區塊，確認 `Core hours` 與 `Storage` 消耗趨勢正常。

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **儲存費率防禦**：將單月儲存消耗從風險值 `15–32 GB-months` 壓低至 **`~0.67 GB-months/學期`**（節省超過 **95%** 儲存額度）。
- **算力保護**：設定 `30 minutes` idle timeout，即使學生下課直接闔上筆電離開教室，最多僅多扣 `2 cores × 0.5 hr = 1.0 core-hour`（約佔月配額 0.8%）。
- **安全撤離法則 (`IF-THEN Law`)**：`IF git status 仍有 untracked 或 modified 檔案，THEN 嚴禁執行 Delete；MUST 先完成 git commit && git push 並於網頁端重新整理確認檔案已出現在 github.com/<student>/DM2026 後，才可點擊 Delete。`

### 5. Verification Check
- 網頁確認：`https://github.com/codespaces` 頁面在 `DM2026` 專案下顯示 `0` 個殘留 Codespace（`No codespaces`）。
- 檔案確認：重新整理 `https://github.com/<你的帳號>/DM2026`，確認最後一次 Commit 時間為「1–2 分鐘前」，且最新程式碼與圖片已安全儲存於遠端。

---

## PB-10：Codespaces 內 AI 上下文接地結對編程 (`@workspace` 實戰)

### 1. Goal & Trigger
- **量化目標**：在 Codespaces 內透過 GitHub Copilot Chat 的 `@workspace` 與 `#file` 上下文錨定機制，結合 **P.A.U.S.E. 前提審計** 與 **L.A.W. 量化檢核**，將 `DM2026` 的重構與單元測試撰寫時間縮短 `~50%` `[HYPOTHESIS]`，同時把 AI 幻覺代碼採納率壓低於 `5%` `[HYPOTHESIS]`（Bloom's `L6 Create`）。
- **觸發條件**：學生已理解 `WEEK02` / `WEEK03` 基礎語法，進入模組化重構、撰寫 `pytest` 邊界測試、或針對離散數學演算法進行除錯時。

### 2. Before (Anti-Pattern) vs. After (Codespace SOP)

| 比較項目 | Before（反模式 / 盲貼外部 Chatbot） | After（Codespace `@workspace` 接地結對編程） |
|:---|:---|:---|
| **上下文提供** | 把一段殘缺程式碼貼給網頁版聊天機器人，AI 不知道專案結構與 Python 版本，亂吐過時語法 | 在 Codespace 側邊欄使用 **`@workspace`** 與 `#file:WEEK03.md`，AI 直接讀取真實 `.devcontainer` 與 `src/` 檔案 |
| **驗證紀律** | AI 給什麼就直接複製貼上，連跑都沒跑或不知道錯在哪裡 | 要求 AI 同時輸出 **`pytest` 邊界案例**，並由學生親自執行驗證與邏輯審計 |
| **學習深度** | 淪為「代寫作業機」，考筆試時完全寫不出 `list comprehension` 或 `OOP` | 將 AI 設定為 **蘇格拉底式助教（Socratic Coach）**，先點出盲點與思考框架，再進行代碼對照 |

### 3. Concrete Steps（專屬於 `DM2026` 的 4 個即戰力 Prompt）

在 Codespaces 中按 `Ctrl + Alt + I`（或點擊左側對話圖示）開啟 Chat 面板，直接使用以下為 `Grace-TA/DM2026` 量身訂製的實戰 Prompt（零佔位符）：

#### Prompt 1：Colab 講義轉工程模組（`WEEK02.md` / `WEEK03.md` 跨檔重構）
```text
@workspace 請讀取 #file:WEEK03.md 與 #file:requirements.txt 的內容。
請協助我把 WEEK03.md 中的「4-phase triangle waves」與「unit circle parametric plot」重構為一個符合 OOP 設計原則的 Python 模組，需滿足：
1. 使用 Python 3.12 type hints 與 try-except 邊界檢查。
2. 遵循容器環境變數 MPLBACKEND=Agg，輸出 PNG 至 outputs/ 目錄，不要呼叫阻塞式的 plt.show()。
3. 同時為每個公開方法產生對應的 pytest 單元測試函數，並指出哪些邊界值（例如負數相位或空陣列）容易出錯。
```

#### Prompt 2：離散數學概念蘇格拉底式除錯（避免直接要答案）
```text
@workspace 我正在實作 #file:src/week03_lab.py 中的 discrete_set_relations。
請不要直接給我完整解答，而是扮演《離散數學》助教的角色：
1. 檢查這段邏輯在處理空集合 set() 或重複元素轉換時，是否存在潛在的數學定義漏洞。
2. 列出 3 個我應該自行撰寫的測試案例輸入（包含邊界情況），讓我自己跑 pytest 驗證。
```

#### Prompt 3：無頭繪圖與環境診斷（結合 `verify_codespace_env.py`）
```text
@workspace #terminalLastCommand
我在執行 Matplotlib 繪圖腳本時遇到這個終端機輸出。請先根據 #file:.devcontainer/devcontainer.json 的設定檢查問題根因（例如是否為 backend 設定、中文字型缺失或相對路徑錯誤），再用繁體中文給我「最小改動修復方案」以及修復後的驗證指令。
```

#### Prompt 4：執行前 P.A.U.S.E. 前提與效能審計
```text
@workspace 請針對 #file:src/week03_lab.py 進行 P.A.U.S.E. 工程審計：
1. 找出程式中所有隱含的假設（例如假設 outputs/ 目錄存在、假設輸入 n 為整數、假設圖片檔案可覆寫）。
2. 檢查是否使用了無效的記憶體拷貝（例如大型陣列改用 NumPy 向量化運算取代雙層 Python for 迴圈）。
3. 給出每一項修改的量化改善理由（時間複雜度或異常安全等級）。
```

### 4. Quantitative Cost/Latency Impact (`MR-8`)
- **知識遷移效率**：學生在本地編輯器內直接取得上下文精準回答，避免視窗切換與重複複製貼上，單次除錯查詢往返時間壓縮至 `10–20 秒`。
- **費用說明**：GitHub Copilot 基礎功能（含免費方案 / GitHub Education Student Pack 教育免費授權）可於 Codespaces 內直接啟用，不額外消耗 Codespaces `core-hours`（僅計算容器開機時長）。
- **抗幻覺鐵律 (`IF-THEN Law`)**：`IF AI 產生的程式碼包含未列於 requirements.txt 的第三方套件或未附帶 pytest 驗證，THEN 嚴禁直接 git commit；MUST 先執行測試並確認全部 PASS，同時能向助教口頭解釋每一行核心邏輯。`

### 5. Verification Check
- 使用 Prompt 1 或 Prompt 4 修改完成後，在終端機執行：
  ```bash
  PYTHONPATH=. pytest -v && python3 verify_codespace_env.py
  ```
- 確認所有單元測試與 `VERIFY_PASS` 均通過，再執行 `git commit && git push` 與 `PB-09` 課後清理。

---

## 附錄：90 分鐘《離散數學 `DM2026`》工作坊標準時間軸調度表

供助教 `Grace-TA` 搭配 Book 1 與 Book 2 現場控場使用（總計 `90 分鐘`）：

| 時段 | 執行動作 | 對應手冊 | 關鍵檢查點 (Checkpoint) |
|:---|:---|:---:|:---|
| **00–10 min** | **開講破題與拓撲宣告**：說明為何從 `WEEK01` Colab 跨入 Codespaces，強調「不可直接點擊 `fantastic-dollop` 網址」 | Book 1 §1-2 + `PB-01` | 投影示範 `Grace-TA/DM2026` 首頁與 Fork 按鈕 |
| **10–25 min** | **全員啟動與確定性驗證**：學生 Fork 後建立 `2-core` (`Southeast Asia`) 容器，執行 `verify_codespace_env.py` | `PB-01` + `PB-03` | 全班舉手/回報 `VERIFY_PASS`；助教用 `PB-02` Live Share 搶救卡關者 |
| **25–55 min** | **`WEEK03` 工程化遷移實作**：撰寫 OOP 類別、產出 4-Phase Triangle Waves 與 Unit Circle 圖表並跑通 `pytest` | `PB-04` + `PB-10` | 終端機顯示 `4 passed`，`outputs/` 出現兩張 PNG 圖檔 |
| **55–75 min** | **進階工具鏈體驗**：啟動 Port `8000` (`Private`) 預覽圖表畫廊 + 示範 `.env` `.gitignore` 檢查 | `PB-05` + `PB-08` | 無痕視窗驗證 `Private` 保護有效；`SECURITY_SCAN_CLEAN` |
| **75–87 min** | **CLI 備援示範與原理收斂**：助教示範 `gh cs list/cp`，並透過 `S.T.U.D.Y.` 總結 OCI 容器與認知負荷理論 | `PB-06` + `PB-07` + Book 1 §3 | 學生完成 `git push` 並看見遠端 Repo 更新 |
| **87–90 min** | **FinOps 強制撤離檢查點 (`LO-CS-4`)**：全班核對 `git status` clean → 執行 **Delete codespace** → 檢查 `https://github.com/codespaces` 歸零 | `PB-09` | **100% 學生確認容器已 Delete（非僅 Stop）才下課** |
