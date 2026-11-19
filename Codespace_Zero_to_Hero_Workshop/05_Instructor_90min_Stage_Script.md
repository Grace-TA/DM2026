# 🎬 DM2026 — 講師／Grace-TA 90 分鐘逐分鐘舞台劇本與突發急救手冊

> **適用場域**：90 分鐘高密度實戰工作坊（推薦教室投影 1920×1080 雙視窗：左窗瀏覽器顯示 `Grace-TA/DM2026`，右窗顯示講師專屬 4-Core Codespace [`https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/`](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)）  
> **控場節拍器**：嚴格執行 **6 ×（10 分鐘講師示範 + 5 分鐘學生破關）** 心流循環  
> **黃金鐵律**：絕不讓學生點進 `fantastic-dollop` 私有 URL；下課最後 3 分鐘全班必須一起執行 **Delete Codespace 歸零儀式**！

---

## 🎯 一、 課前 T-15 分鐘講師預檢清單（Pre-Flight Checklist）

| 檢查項 | 操作動作 | 預期驗證結果 | 若失敗之處置 |
|:---:|:---|:---|:---|
| **1** | 確認 [`Grace-TA/DM2026`](https://github.com/Grace-TA/DM2026) 已包含 `.devcontainer/devcontainer.json` 與 `scripts/verify_codespace_env.py` | 倉庫根目錄可見 `.devcontainer` 資料夾 | 立即從本包 `devcontainer_starter/` 貼上並 `git push` |
| **2** | 預先喚醒講師機 `https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/` | VS Code Web 開啟，左下角顯示 `Codespaces: fantastic-dollop` | 若停機逾時，等待 ~35 秒自動啟動 |
| **3** | 在講師機 Terminal 執行 `cat /etc/os-release`、`ll /workspaces` 與 `nproc && free -h` | 顯示 `Ubuntu 24.04.5 LTS`、`/workspaces/DM2026` 目錄、`4` CPUs 與 `~16 GiB` RAM | 確認選用機器規格是否為 4-core |
| **4** | 開啟教室計時器（每 10 分鐘／5 分鐘響鈴切換）＋白板寫下短網址 `github.com/Grace-TA/DM2026` | 全班看得到 Fork 目標網址 | 確認教室 Wi-Fi 能正常連上 `github.com` 與 `*.github.dev` |

---

## ⏱️ 二、 00:00 – 90:00 逐分鐘舞台劇本（Minute-by-Minute Stage Script）

### 🔥 Cycle 1（00:00–00:15）：破冰揭秘與雲端貨櫃覺醒（Lab 01 & Lab 02）

- **00:00–00:03｜【震撼開場：Codespaces 可以取代 Google Colab 嗎？】**
  - **講師畫面**：同時開啟 `Grace-TA/DM2026` 的 `README.md`（顯示 *Oscar Levin 3rd Edition* 封面）與 `fantastic-dollop-9rpj66gp74hxx5w.github.dev`。
  - **講台口令**：
    > 「各位同學好！在我們《離散數學 `DM2026`》（Oscar Levin 3rd Ed.）的前三週，大家已經在 Google Colab 裡學了 `calendar`、字串清洗與 Matplotlib 三角波。今天一開始我先回答大家最關心的問題：**Codespaces 可以取代 Colab 嗎？結論是：在『一般程式開發、離散數學演算法教學（如 `NetworkX`、`SymPy`、`Z3` 僅需 CPU）、多檔案專案與軟體工程』上，Codespaces 不僅完全取代 Colab，而且功能更強大！只有在『需要免費 T4 GPU 訓練深度學習』時，兩者才是互補關係。**」
- **00:03–00:07｜【揭秘 `fantastic-dollop` 4-Core 主機、Ubuntu 24.04.5 LTS 與持久磁碟邊界】**
  - **講師畫面**：在講師機 Terminal 依序執行 `cat /etc/os-release`、`ll /workspaces` 與 `nproc && free -h`；接著指向 `/workspaces/DM2026` 強調持久化邊界。
  - **講台口令**：
    > 「看我的終端機！這台 `fantastic-dollop` 跑的是真實的 **`Ubuntu 24.04.5 LTS (Noble Numbat)`**，分配到 **`4-core` CPU 與 `16GB` RAM**！你們看 `/workspaces` 裡面有 `.codespaces/`、`.oryx/` 和 `DM2026/`——**請記住這條死命令：只有存放在 `/workspaces/DM2026` 底下的檔案才會受到持久性磁碟（Persistent Volume）保護！** 而且這個 `fantastic-dollop` 網址綁定老師帳號，你們點會 404；請改用 **Fork + `2-core`**（每月 120 core-hrs = **60 小時免費**），並記得：**Stop 不停算硬碟錢，Delete 才歸零！**」
- **00:07–00:10｜【Live Demo：30 秒 Fork + 啟動 2-Core Codespace】**
  - **講師畫面**：切到測試學生帳號示範點擊 `Grace-TA/DM2026` 右上角 **Fork** $\rightarrow$ 綠色 **Code** 按鈕 $\rightarrow$ **Codespaces** 分頁 $\rightarrow$ 點選 `...` $\rightarrow$ **New with options...** $\rightarrow$ 確認 **Region = Southeast Asia**、**Machine type = 2-core** $\rightarrow$ **Create codespace**。
- **00:10–00:15｜【⚡ 學員 5 分鐘破關：Lab 01 + Lab 02】**
  - **螢幕任務指令**：「1. Fork `Grace-TA/DM2026`；2. 開啟個人 `2-core` Codespace；3. 按 `` Ctrl + ` `` 開終端機，執行 `nproc && free -h && df -h /`，舉手回報看見 `2` 核心！」
  - **TA 巡場重點**：立刻抓出還沒登入 GitHub 或忘記按 Fork 直接在原庫開 Codespace 的學生（原庫通常無權限開在學生帳號下或會被擋）。

---

### ⚙️ Cycle 2（00:15–00:30）：雲端終端機與免密 Git 閉環（Lab 03, 04, 06）

- **00:15–00:25｜【講師示範：為什麼 Codespace 裡 `git push` 不用輸入密碼？】**
  - **講師畫面**：在 `fantastic-dollop` 執行 `git remote -v` 與 `git config --list | grep credential`，展示 GitHub 內建的 Token Credential Proxy，接著建立 `feat/demo-dm2026` 分支、寫入 `hello_dm2026.py` 並一鍵 `git commit && git push`。
  - **講台口令**：
    > 「以前在 Windows 終端機打 `git push` 會跳出帳號密碼視窗卡死一小時；但在 Codespaces 裡，這台容器跟你的 GitHub 帳號之間有安全代理隧道。你只要專心在邏輯與離散數學，**3 行指令完成雲端存檔**！」
- **00:25–00:30｜【⚡ 學員 5 分鐘破關：Lab 03 + Lab 04 + Lab 06】**
  - **螢幕任務指令**：「1. 執行 `git checkout -b feat/my-dm2026`；2. 建立 `hello_dm2026.py` 印出學號與當前系統時間；3. 執行 `git add . && git commit -m "feat: hello codespace" && git push -u origin feat/my-dm2026`，重整你的 GitHub Fork 網頁確認看見綠色 Commit！」

---

### 🏗️ Cycle 3（00:30–00:45）：Infrastructure-as-Code 與 DevContainer（Lab 07 & Lab 08）

- **00:30–00:40｜【講師示範：`/study5` 核心洞見 — 把「環境說明書」變成「可執行法律」】**
  - **講師畫面**：打開 `.devcontainer/devcontainer.json`，逐行高亮 `"image"`、`"customizations.vscode.extensions"`、`"postCreateCommand"`；接著執行 `python3 scripts/verify_codespace_env.py` 輸出全綠 JSON。
  - **講台口令**：
    > 「過去助教發一份 Word 檔教你『請先裝 Python 3.12、再裝 numpy 2.0、再裝 Jupyter』，永遠有 30% 的人裝錯。這叫**自然語言許願**。在工程世界，我們用 `.devcontainer/devcontainer.json` 把『作業系統、Python 版本、VS Code 套件、開機自動安裝指令』寫成一份 JSON 契約。只要這個檔案在倉庫裡，**世界另一端的教授打開你的 Repo，環境跟你一模一樣，100% 確定性重現！**」
- **00:40–00:45｜【⚡ 學員 5 分鐘破關：Lab 07 + Lab 08】**
  - **螢幕任務指令**：「1. 打開 `.devcontainer/devcontainer.json` 閱讀 4 個關鍵欄位；2. 執行 `python3 scripts/verify_codespace_env.py` 確認 `numpy`、`matplotlib`、`pytest` 全數就緒；3. （進階可選）在設定檔加入一個個人喜愛的擴充套件或設定並存檔。」

---

### 🌐 Cycle 4（00:45–01:00）：Port Forwarding 與雲端服務隧道（Lab 09 & Lab 11）

- **00:45–00:55｜【講師示範：把黑漆漆的 Linux 容器變成全世界都能看的網頁！】**
  - **講師畫面**：在 `fantastic-dollop` 建立一個簡短的 `index.html`（或開啟專案網頁），執行 `python3 -m http.server 8000`，點擊右下角彈出的 `Open in Browser` 提示，展示 **Ports** 頁籤裡的 `Private` vs `Public` 可見度切換。
  - **講台口令**：
    > 「以前你們在本機跑 `localhost:8000`，同學在對面電腦是看不見的。現在看 Codespaces 下方的 **Ports** 分頁：GitHub 幫你架了一條加密的 HTTPS 反向代理網址！預設是 `Private`（只有你自己登入 GitHub 看得到）；點右鍵切換成 `Public`，連你手機掃 QR Code 都能當場看到你寫的離散數學互動網頁！」
- **00:55–01:00｜【⚡ 學員 5 分鐘破關：Lab 09（+ 瀏覽 Lab 11 `gh cs`）】**
  - **螢幕任務指令**：「1. 建立簡單 `demo.html` 並執行 `python3 -m http.server 8000`；2. 在 **Ports** 面板找到 `8000`，點選地球/瀏覽器圖示預覽；3. 測試將 Visibility 暫時改為 `Public` 並貼網址給鄰座同學互看，看完記得關掉 `Ctrl+C`！」

---

### 🧮 Cycle 5（01:00–01:15）：`DM2026` 離散數學 Colab 遷移實戰（Lab 15, 16, 22）

- **01:00–01:10｜【講師示範：把 `WEEK02` 邏輯判斷與 `WEEK03` Matplotlib 搬進雲端貨櫃】**
  - **講師畫面**：在 `fantastic-dollop` 建立 `week03_wave.py`，復現 `DM2026/WEEK03.md` 的「4 條不同相位差三角波 + 等比例單位圓」，執行 `python3 week03_wave.py` 後直接在 VS Code Web 右側打開生成的 PNG 圖片，對照 Jupyter `.ipynb` 雙核運行。
  - **講台口令**：
    > 「還記得 `WEEK03.md` 裡的 4 條 $\pi$ 相位差三角波與單位圓嗎？在無螢幕的 Linux 雲端容器裡，沒有視窗跳出來怎麼看圖？祕訣就是 `plt.savefig('unit_circle.png', dpi=150)`！存檔瞬間，VS Code 左側一點就直接在瀏覽器高畫質預覽，而且還能用 `git` 記錄每一次圖表的演化！」
- **01:10–01:15｜【⚡ 學員 5 分鐘破關：Lab 15 + Lab 16 + Lab 22】**
  - **螢幕任務指令**：「1. 用老師提供的 `Lab 16` Context Prompt 修復 `DM2026` 縮排錯誤並印出 $(P \rightarrow Q)$ 真值表；2. 執行 `Lab 22` 腳本產出 `triangle_waves.png` 與 `unit_circle.png`，在編輯器中點擊預覽！」

---

### 🏆 Cycle 6（01:15–01:30）：Hero 檢驗閘門、PR 提交與 FinOps 歸零儀式（Lab 24, 27, 28）

- **01:15–01:24｜【講師示範：`pytest` 自動批改 + Pull Request + 最關鍵的 Delete 儀式】**
  - **講師畫面**：先跑一次 `pytest` 全綠，接著切到 `github.com/codespaces` 儀表板，指著 **Active vs Stopped** 與 **32 GB Storage** 清楚解釋計費差異。
  - **講台口令**：
    > 「看清楚最後這張儀表板！假設我們班有 40 個人，每人開一台 `32 GB` 的 Codespace，如果下課你只按 **Stop Codespace**，算力確實不扣錢了，但那顆 `32 GB` 的硬碟會每天佔用你的空間額度——你免費額度只有 **15 GB-months**，撐不到月底就爆了！正確 SOP 永遠是：**先 `git commit && git push` 把程式存回 GitHub 雲端倉庫 $\rightarrow$ 再打開 `github.com/codespaces` 按下 `Delete`！** 貨櫃拆掉回收，但藍圖永遠安全留在倉庫裡！」
- **01:24–01:30｜【⚡ 全班同步閉關儀式：Lab 28（Commit $\rightarrow$ Push $\rightarrow$ PR $\rightarrow$ Delete）】**
  - **螢幕任務指令**：「1. 執行 `git status` 確認今天所有檔案已 `add / commit / push` 到你的 Fork；2. 到 GitHub 網頁點 `Contribute -> Open pull request`（或確認線上看得到你的檔案）；3. 開啟 `https://github.com/codespaces`，點選右側 `...` $\rightarrow$ **Delete**，向 TA 舉手展示畫面已清空（$0.00 安全通關）！」

---

## 🚨 三、 課堂 10 大突發狀況急救 SOP（Troubleshooting Runbook）

| # | 現場突發狀況 | 發生徵兆 | 30 秒標準排除 SOP |
|:---:|:---|:---|:---|
| **1** | **學生點老師的 `fantastic-dollop` 連結進不去** | 瀏覽器顯示 `404 Not Found` 或 `You do not have access` | **正常安全機制！** 立即引導學生改點 `Grace-TA/DM2026` 右上角 **Fork**，再從**自己帳號的 Fork** 按 `Code -> Codespaces -> Create codespace`。 |
| **2** | **學生開錯成 4-Core 或忘記看地區** | Terminal 顯示 `4` CPUs 或延遲很高 | 若尚未寫程式：立刻關閉並 Delete 重建選 `2-core` + `Southeast Asia`；若已寫程式：下課務必準時 Delete，本次 90 分鐘僅耗 `4 × 1.5 = 6` core-hrs（仍遠低於 120 免費上限）。 |
| **3** | **未先 Fork 直接按 `Code` 找不到綠鈕** | 學生帳號對原庫無權限或未顯示選項 | 確認已登入 GitHub 帳號，先按右上角 **Fork**，確認網址列已變成 `github.com/<學生帳號>/DM2026`。 |
| **4** | **Codespace 建置卡在 `Installing extensions` 超過 3 分鐘** | 畫面一直轉圈顯示 Setting up container | 告訴學生在「Waiting for container」期間**不用等擴充套件**，可先打開 Terminal；或按 `F1` $\rightarrow$ `Codespaces: View Creation Log` 確認是否卡在 `pip install`。 |
| **5** | **`matplotlib` 執行後報錯無 GUI 顯示** | `UserWarning: FigureCanvasAgg is non-interactive` | 這是正常行為！雲端 Linux 無實體螢幕，將程式碼開頭加上 `import matplotlib; matplotlib.use('Agg')` 並用 `plt.savefig('out.png')` 存檔即可點擊預覽。 |
| **6** | **Port 8000 開啟顯示 `502 Bad Gateway`** | 轉發網址打開出現 502 | 學生忘記在 Terminal 執行 `python3 -m http.server 8000`，或按了 `Ctrl+C` 中止了伺服器。重新啟動 server 並確認 Ports 頁籤顯示綠燈 `Running`。 |
| **7** | **同學互開 Port 8000 網址跳出 404/登入要求** | 鄰座同學開網址被要求登入或被擋 | GitHub Codespaces Port 預設是 **Private**！在 Ports 頁籤針對 `8000` 按右鍵 $\rightarrow$ `Port Visibility` $\rightarrow$ 改為 **`Public`**。 |
| **8** | **`git push` 出現 `rejected - non-fast-forward`** | 在網頁版改過檔案又在雲端改同一支檔案 | 執行 `git pull --rebase origin feat/my-dm2026` 合併遠端變更後再 `git push`。 |
| **9** | **學生誤刪重要設定檔或把容器玩壞** | 終端機無法執行 `python3` 或檔案錯亂 | 先用 `git status` / `git checkout -- <file>` 救回；若系統環境全毀，按 `F1` $\rightarrow$ `Codespaces: Rebuild Container`（保留 `/workspaces` 程式同時重置系統）。 |
| **10** | **教室網路封鎖 `*.github.dev` WebSocket** | 編輯器一直顯示 `Reconnecting...` | 切換手機熱點，或使用備援方案：改開本機/教室 VS Code 安裝 `GitHub Codespaces` Extension 透過本地端遠端連線，或暫時啟用教師機 **VS Code Live Share**。 |
