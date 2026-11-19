2026-11-19 14:02:00 CST

### 第一部分：三個實務技術問題的直接解答

#### 1. 如何確認 Linux 的版本（How to verify the Linux version）

在您畫面下方的 `bash` 終端機視窗（`@Grace-TA ➜ /workspaces/DM2026 (main) $`）中，輸入以下任一指令即可確認作業系統發行版與 Linux 核心（Kernel）版本：

* **查看 Linux 發行版名稱與版本號（最推薦）**：
```bash
cat /etc/os-release

```


* *預期驗證結果*：終端機會輸出 `NAME="Ubuntu"` 與 `VERSION="22.04.x LTS"` 或 `"24.04.x LTS"`（GitHub Codespaces 預設映像檔基於 Ubuntu LTS）。


* **查看 Linux Kernel 核心架構與硬體資訊**：
```bash
uname -a

```


* *預期驗證結果*：顯示完整核心版本號與處理器架構（例如 `Linux codespaces-... 6.x.x-azure #1 SMP x86_64 GNU/Linux`）。


* **確認目前分配到的硬體資源（驗證 4-core 與 16GB RAM）**：
```bash
nproc && free -h

```


* *預期驗證結果*：`nproc` 顯示 `4`（代表 4 個 vCPU），`free -h` 顯示總記憶體約為 `15Gi`～`16Gi`。



---

#### 2. GitHub Codespaces 可以取代 Google Colab 嗎？

**結論：在「一般程式開發、演算法教學（如離散數學 DM2026）、多檔案專案與軟體工程」上，Codespaces 不僅能完全取代 Google Colab，而且功能更強大；但在「需要免費 GPU 訓練深度學習模型」的場景下，兩者屬於互補關係。**

| 比較維度 | GitHub Codespaces (`4-core / 16GB RAM`) | Google Colab（免費版） | 教學與工程選型建議 |
| --- | --- | --- | --- |
| **環境架構** | 完整 Ubuntu Linux 容器 + 完整 VS Code IDE | 單一瀏覽器 Notebook 沙盒（階段性連線） | 需要寫 `.py` 模組、CLI 工具或建置網站時，選 **Codespaces** |
| **Jupyter Notebook 支援** | 原生支援（安裝 `ms-toolsai.jupyter` 擴充套件即可直接執行 `.ipynb`） | 原生支援 | Codespaces 執行 `.ipynb` 同時擁有 Git 版本比對與中斷點除錯（Debugger） |
| **硬體算力** | 4-core CPU + 16GB RAM（無免費 GPU） | 2-core CPU + ~12.7GB RAM（提供有限時數 T4 GPU） | 離散數學（`NetworkX`、`SymPy`、`Z3`）僅需 CPU，**Codespaces 速度更快且不中斷** |
| **檔案持久化與 Git** | `/workspaces/DM2026` 永久保留磁碟狀態，原生整合 Git Commit/Push | 連線逾時（閒置約 90 分鐘）後本機磁碟清空，需手動掛載 Google Drive | **Codespaces 徹底解決學生忘記存檔或版本覆蓋的問題** |

---

#### 3. 指定 Repo 為 `DM2026` 時，Linux 環境是否直接指向該資料夾？

**是的，完全正確。**
從您截圖右下角的終端機提示字元可以直接驗證：`@Grace-TA ➜ /workspaces/DM2026 (main) $`。

1. **自動掛載路徑**：當您從 `[https://github.com/Grace-TA/DM2026](https://github.com/Grace-TA/DM2026)` 啟動 Codespace（`fantastic-dollop-9rpj66gp74hxx5w`）時，系統會自動將該 Repository 完整 Clone 至容器內的 **`/workspaces/DM2026`** 目錄，並將終端機的初始工作目錄（Working Directory）與 VS Code 檔案總管根目錄鎖定在此路徑（目前裡面已有 `README.md`、`WEEK01.md`、`WEEK02.md`、`WEEK03.md`）。


2. **重要持久化邊界（Poka-Yoke 防呆提醒）**：只有存放在 **`/workspaces/DM2026`** 目錄底下的檔案會受到持久性磁碟（Persistent Volume）保護；若在 `/tmp` 或 `/home/codespace` 建立檔案，一旦執行 `Rebuild Container`，這些目錄外的檔案將會被重置清除。

---

### 第二部分：90 分鐘「GitHub Codespaces: From ZERO to HERO」工作坊完整教案

* **適用帳號**：`[https://github.com/Grace-TA](https://github.com/Grace-TA)`


* **目標儲存庫**：`[https://github.com/Grace-TA/DM2026](https://github.com/Grace-TA/DM2026)`（115學年第1學期，離散數學 Discrete Mathematics）


* **實戰執行個體**：`[https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)`（4-core • 16GB RAM • 32GB Storage）Codespaces 90-Min Workshop#### 一、 90 分鐘工作坊時程規劃表（Workshop Agenda）



| 時段 | 時間長度 | 模組主題 | 核心目標與實作對應 |
| --- | --- | --- | --- |
| **00–10 分** | 10 min | **Module 0: 破冰與架構心智圖** | 講解 5W1H 與 5-Why 分析，啟動 `Grace-TA/DM2026` 雲端環境 |
| **10–25 分** | 15 min | **Module 1: Linux 核心與終端機制霸** | 執行 **Labs 1–5**（系統探測、檔案導航、權限與管線操作） |
| **25–45 分** | 20 min | **Module 2: Python 與 Jupyter 離散數學實戰** | 執行 **Labs 6–10**（虛擬環境、`.ipynb` 互動運算、`NetworkX` 圖論視覺化） |
| **45–60 分** | 15 min | **Module 3: Git 版本控制與防呆協作流** | 執行 **Labs 11–15**（Branch 分支隔離、Commit 規範、Pull Request 合併） |
| **60–75 分** | 15 min | **Module 4: 環境即程式碼（DevContainer）** | 執行 **Labs 16–20**（編寫 `.devcontainer/devcontainer.json` 鎖定套件與擴充） |
| **75–90 分** | 15 min | **Module 5: 雲端服務轉發、AI 代理與資源回收** | 執行 **Labs 21–25**（Port Forwarding 網頁預覽、Copilot 協作、Stop 止血機制） |

---

#### 二、 Codespaces 的 5W1H 系統解析與 5-Why 根因推演

##### 1. 5W1H 系統架構分析

* **What（是什麼）**：GitHub Codespaces 是將雲端虛擬機（VM）與 Docker 容器（Development Container）深度整合至 GitHub 儲存庫的「即時雲端整合開發環境（CDE）」。
* **Why（為什麼需要）**：消除本地端作業系統差異（Windows / macOS / Linux）、套件版本衝突與硬體效能瓶頸，實現「環境即程式碼（Environment as Code）」與「零配置秒級開工」。
* **Who（誰最受益）**：授課教師（統一全班實驗環境）、修課學生（用 Chromebook 或平板也能寫大型專案）、開源貢獻者（審查 PR 無需污染本地環境）與跨機器開發者。
* **When（何時使用）**：課程實習課（如 `DM2026` 離散數學演算法實作）、黑客松（Hackathon）、技術面試、以及任何需要快速驗證新框架的時刻。
* **Where（在哪裡運行）**：運算與容器託管於 Microsoft Azure 雲端資料中心（如截圖中選定的 `Southeast Asia` 區域）；前端介面可透過瀏覽器（`[https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)`）或本機桌面版 VS Code 遠端連線。


* **How（如何運作）**：透過專案根目錄的 `.devcontainer/devcontainer.json` 定義映像檔、擴充套件與啟動腳本，由 GitHub 自動掛載 `/workspaces/<repo>` 並透過 SSH/HTTPS 加密通道串流至瀏覽器。

##### 2. 5-Why 根因推演（為何傳統程式教學必須轉向 Codespaces？）

* **現象（Symptom）**：在 90 分鐘的程式或離散數學實驗課中，往往前 45 分鐘都在解決學生的環境報錯，真正寫程式的時間不到一半。
* **Why 1（為何環境會報錯？）**：因為每位學生的筆電作業系統（Windows 路徑反斜線、macOS M 系列 ARM 架構、Linux 權限）與預設 Python/GCC 版本完全不同。
* **Why 2（為何版本差異會導致程式崩潰？）**：因為套件相依性（Dependency Tree）缺乏隔離機制，全域安裝（Global `pip install`）造成不同課程的函式庫互相覆蓋。
* **Why 3（為何學生無法自行排除相依性衝突？）**：因為初學者缺乏作業系統環境變數（`PATH`）、編譯器工具鏈與虛擬環境的底層除錯知識，認知負載（Cognitive Load）瞬間超載。
* **Why 4（為何教師提供的安裝手冊（PDF/Markdown）依然無效？）**：因為靜態文件（Static Documentation）無法對抗作業系統的動態更新與環境漂移（Configuration Drift），手冊永遠落後於真實系統狀態。
* **Why 5（根因與第一性原理解法）**：**「環境不應該靠人類手動組裝，而應該作為不可變的程式碼（Immutable Infrastructure as Code）隨專案一起版本控制。」** 透過 Codespaces 與 `devcontainer.json`，將環境建置從「每位學生重複踩雷」轉化為「教師定義一次、全班確定性複製」。

---

#### 三、 Top 10 實戰作戰手冊（Top 10 Playbooks）

1. **Playbook 01｜一鍵環境啟動與區域延遲最佳化**
* 在 `[https://github.com/Grace-TA/DM2026](https://github.com/Grace-TA/DM2026)` 點擊 `Code` -> `Codespaces` -> 點擊 `...` 選擇 `New with options...`，將 **Region** 鎖定為 **`Southeast Asia`（新加坡）**，大幅降低台灣連線的終端機打字延遲。




2. **Playbook 02｜免裝 Jupyter 的 `.ipynb` 互動運算工作流**
* 在 Codespaces 內安裝官方 `Jupyter` 擴充套件後，直接建立 `week01_logic.ipynb`，即可用 4-core / 16GB RAM 執行離散數學真值表與圖論運算，完全取代 Google Colab。


3. **Playbook 03｜`devcontainer.json` 環境鎖定標準範本**
* 在 `/workspaces/DM2026/.devcontainer/devcontainer.json` 寫入預設安裝的 Python 套件（`numpy`, `networkx`, `sympy`, `matplotlib`）與 VS Code 擴充套件清單，讓每位學生開啟即用。


4. **Playbook 04｜雙向連接埠轉發（Port Forwarding）即時預覽**
* 當在終端機啟動網頁服務（如 `python -m http.server 8000` 或 `streamlit run app.py`）時，切換至下方 `連接埠 (PORTS)` 分頁，即可取得專屬 HTTPS 網址，並可將 `Visibility` 設為 `Public` 分享給全班檢視。


5. **Playbook 05｜GitHub CLI (`gh`) 終端機自動化管線**
* Codespaces 內建已驗證登入的 `gh` 工具，在終端機直接輸入 `gh pr create`、`gh issue list` 或 `gh codespace list`，無需離開鍵盤即可管理整個 Repo。


6. **Playbook 06｜功能分支隔離（Feature Branch Isolation）防呆法**
* 嚴禁直接在 `main` 分支修改講義；每位學生或每次實驗先執行 `git checkout -b lab-week01`，完成後再透過 Pull Request 合併，確保主幹永遠乾淨。


7. **Playbook 07｜AI 代理程式建置與 Copilot 雙欄協作**
* 善用畫面右側的 **Copilot 聊天視窗**，選取程式碼區塊後直接要求重構、撰寫單元測試（`pytest`）或解釋離散數學時間複雜度。




8. **Playbook 08｜機密金鑰安全注入（Codespaces Secrets）**
* 若課程需要使用 OpenAI / Gemini API Key，切勿寫死在程式碼中！應在 GitHub `Settings -> Secrets and variables -> Codespaces` 註冊，系統會自動以環境變數注入容器。


9. **Playbook 09｜Prebuilds 預建置加速冷啟動**
* 在大型課程開始前 1 小時，於 Repo 設定開啟 **Codespaces Prebuilds**，讓 GitHub Actions 預先編譯好容器映像檔，學生點擊啟動時間可從 2 分鐘縮短至 15 秒內。


10. **Playbook 10｜閒置休眠與帳單止血紀律（Cost Hygiene）**
* 課程結束前 3 分鐘，全員執行 `git push` 並點擊左下角綠色狀態列 **`Codespaces: fantastic dollop`** -> 選擇 **`Stop Current Codespace`**，避免閒置期間持續消耗預算額度。





---

#### 四、 經典 25 個實作實驗室（Classic 25 Labs: Zero to Hero）

所有實驗皆預設於 **`[https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)`**（工作目錄 `/workspaces/DM2026`，帳號 `Grace-TA`） 執行。

---

##### 階段一：Linux 系統底層與 CLI 基礎（Labs 01–05）

###### Lab 01：雲端容器指紋與硬體規格驗證

* **Complete Context Prompt**：
> 「我目前在 GitHub Codespaces (`[https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)`) 的 `/workspaces/DM2026` 目錄中。請幫我寫一個名為 `check_env.sh` 的 Bash 腳本，自動輸出目前的 Linux 發行版版本、Kernel 版本、CPU 核心數、總記憶體容量，以及目前登入的使用者帳號。」


* **Complete Student Guide**：
1. 在終端機確認目前路徑位於 `/workspaces/DM2026`。


2. 執行指令檢查系統資訊：`cat /etc/os-release | grep PRETTY_NAME && nproc && free -h && whoami`。
3. **驗證標準**：終端機清晰印出 Ubuntu 版本、`4` 核心、`16Gi` 記憶體與 `codespace` 使用者名稱。



###### Lab 02：檔案系統樹狀結構探勘與持久化邊界測試

* **Complete Context Prompt**：
> 「請在 `/workspaces/DM2026` 中建立一個 `labs/lab02` 資料夾，並用指令比較 `/workspaces/DM2026` 與 `/tmp` 的磁碟掛載點（`df -h`），說明為什麼作業檔案必須存放在 `/workspaces/DM2026` 底下。」


* **Complete Student Guide**：
1. 執行 `mkdir -p labs/lab02 && df -h /workspaces/DM2026 /tmp`。
2. 觀察兩者的 `Filesystem` 與 `Mounted on` 欄位差異。
3. **驗證標準**：成功建立 `labs/lab02` 目錄，並確認 `/workspaces` 掛載於獨立的持久化磁碟區塊。



###### Lab 03：檔案權限（`chmod`）與可執行腳本建置

* **Complete Context Prompt**：
> 「請在 `labs/lab02` 內建立一個執行檔 `hello_dm.sh`，印出『歡迎來到 115-1 離散數學實驗室』與當前時間，並示範如何透過 `chmod +x` 賦予執行權限。」


* **Complete Student Guide**：
1. 執行 `echo -e '#!/bin/bash\necho "Welcome to DM2026: $(date)"' > labs/lab02/hello_dm.sh`。
2. 賦予執行權限並執行：`chmod +x labs/lab02/hello_dm.sh && ./labs/lab02/hello_dm.sh`。
3. **驗證標準**：無出現 `Permission denied` 錯誤，且正確印出系統時間。



###### Lab 04：文字管線處理（`grep` / `wc` / 重導向）分析課程大綱

* **Complete Context Prompt**：
> 「目前 `/workspaces/DM2026` 根目錄有 `README.md`、`WEEK01.md`、`WEEK02.md`、`WEEK03.md`。請給我一組 Linux 管線指令，統計所有 `.md` 檔案的總行數，並搜尋包含『離散』或『數學』的段落。」


* **Complete Student Guide**：
1. 統計行數：`wc -l *.md`。
2. 搜尋關鍵字：`grep -rn "離散\|數學" *.md`。
3. **驗證標準**：終端機列出每個 `.md` 檔的行數統計與匹配的文字行號。



###### Lab 05：環境變數（Environment Variables）與別名（Alias）客製化

* **Complete Context Prompt**：
> 「請教我如何在 Codespaces 的 `~/.bashrc` 中設定自訂別名 `alias dm='cd /workspaces/DM2026 && git status'`，並立即生效。」


* **Complete Student Guide**：
1. 執行 `echo "alias dm='cd /workspaces/DM2026 && git status'" >> ~/.bashrc && source ~/.bashrc`。
2. 切換到根目錄 `cd /` 後，直接輸入 `dm` 測試。
3. **驗證標準**：輸入 `dm` 後瞬間跳回 `/workspaces/DM2026` 並顯示 Git 狀態。



---

##### 階段二：Python、Jupyter 與離散數學工具鏈（Labs 06–10）

###### Lab 06：Python 虛擬環境（`venv`）隔離與套件管理

* **Complete Context Prompt**：
> 「在 `/workspaces/DM2026` 中，請幫我建立一個獨立的 Python 虛擬環境 `.venv`，啟動它，並安裝離散數學常用的 `numpy`、`sympy`、`networkx` 與 `matplotlib`，最後匯出 `requirements.txt`。」


* **Complete Student Guide**：
1. 建立並啟動環境：`python3 -m venv .venv && source .venv/bin/activate`。
2. 安裝套件並鎖定版本：`pip install numpy sympy networkx matplotlib && pip freeze > requirements.txt`。
3. **驗證標準**：提示字元前方出現 `(.venv)`，且根目錄產生 `requirements.txt`。



###### Lab 07：在 Codespaces 中啟動互動式 Jupyter Notebook（取代 Colab）

* **Complete Context Prompt**：
> 「請在 `labs/lab07_logic.ipynb` 建立一個 Jupyter Notebook，用 Python 撰寫命題邏輯（Propositional Logic）真值表生成器，驗證笛摩根定律 $\neg(P \land Q) \equiv \neg P \lor \neg Q$。」


* **Complete Student Guide**：
1. 在左側擴充套件面板確認已安裝 `Jupyter`（`ms-toolsai.jupyter`），並於 `labs/` 建立 `lab07_logic.ipynb`。
2. 選擇右上角 Kernel 為 `.venv (Python 3.x)`，執行布林代數真值表驗證程式。
3. **驗證標準**：儲存格成功輸出 4 種真值組合且所有列驗證為 `True`。



###### Lab 08：集合論（Set Theory）與冪集合（Power Set）演算法實作

* **Complete Context Prompt**：
> 「請使用 Python 標準庫 `itertools` 在 `labs/lab08_sets.py` 實作集合的聯集、交集、差集、對稱差集以及冪集合（Power Set）計算，並驗證集合大小為 $n$ 時冪集合元素個數為 $2^n$。」


* **Complete Student Guide**：
1. 建立並執行腳本：`python labs/lab08_sets.py`。
2. 修改輸入集合元素個數從 3 增至 5，觀察輸出長度變化。
3. **驗證標準**：當輸入集合有 5 個元素時，輸出清單長度精確等於 `32`。



###### Lab 09：圖論（Graph Theory）最短路徑與視覺化匯出

* **Complete Context Prompt**：
> 「請使用 `networkx` 與 `matplotlib` 在 `labs/lab09_graph.py` 建立一個包含 6 個節點的加權無向圖，計算節點 A 到 F 的 Dijkstra 最短路徑，並將圖形儲存為 `labs/shortest_path.png` 供我在 VS Code 直接預覽。」


* **Complete Student Guide**：
1. 執行腳本：`python labs/lab09_graph.py`。
2. 在左側檔案總管直接點擊 `labs/shortest_path.png`。
3. **驗證標準**：終端機印出最短路徑節點序列與總權重，且編輯器分頁直接渲染出清晰的圖論節點圖。



###### Lab 10：使用 `pytest` 進行離散數學演算法自動化單元測試

* **Complete Context Prompt**：
> 「請在 `labs/test_discrete.py` 為最大公因數（Euclidean Algorithm）與費氏數列（Fibonacci）撰寫 5 組 `pytest` 單元測試（包含邊界條件 0 與負數），並教我執行測試。」


* **Complete Student Guide**：
1. 安裝並執行測試：`pip install pytest && pytest -v labs/test_discrete.py`。
2. 故意修改一項斷言（Assert）觀察紅字錯誤報告後再改回。
3. **驗證標準**：終端機顯示 `5 passed` 綠字報告。



---

##### 階段三：Git 版本控制與團隊協作流（Labs 11–15）

###### Lab 11：設定 `.gitignore` 防止虛擬環境污染儲存庫

* **Complete Context Prompt**：
> 「請幫我為 `Grace-TA/DM2026` 產生一份標準 Python + VS Code 的 `.gitignore` 檔案，確保剛才建立的 `.venv/` 與 `__pycache__/` 不會被推送到 GitHub。」


* **Complete Student Guide**：
1. 建立 `.gitignore` 並加入 `.venv/`、`__pycache__/`、`*.pyc`、`.ipynb_checkpoints/`。
2. 執行 `git status` 檢查未追蹤檔案清單。
3. **驗證標準**：`.venv/` 資料夾完全從 `git status` 的 Untracked files 中消失。



###### Lab 12：功能分支隔離開發（Feature Branch Workflow）

* **Complete Context Prompt**：
> 「請引導我從 `main` 分支切出一個名為 `feat/week04-combinatorics` 的新分支，新增 `WEEK04.md` 排列組合講義大綱，並完成本地端 Commit。」


* **Complete Student Guide**：
1. 執行 `git checkout -b feat/week04-combinatorics`。
2. 建立 `WEEK04.md` 並執行 `git add WEEK04.md && git commit -m "docs: add WEEK04 combinatorics outline"`。
3. **驗證標準**：終端機提示字元括號內的分支名稱從 `(main)` 變更為 `(feat/week04-combinatorics)`。



###### Lab 13：透過 GitHub CLI (`gh`) 一鍵發起 Pull Request

* **Complete Context Prompt**：
> 「請教我如何在 Codespaces 終端機內使用 `gh` 指令，將 `feat/week04-combinatorics` 推送到 `[https://github.com/Grace-TA/DM2026](https://github.com/Grace-TA/DM2026)` 並直接建立 Pull Request。」


* **Complete Student Guide**：
1. 推送分支：`git push -u origin feat/week04-combinatorics`。
2. 建立 PR：`gh pr create --title "Add WEEK04 Combinatorics" --body "Completed in Codespaces Lab 13"`。
3. **驗證標準**：終端機回傳新建立的 GitHub Pull Request 網址（`[https://github.com/Grace-TA/DM2026/pull/](https://github.com/Grace-TA/DM2026/pull/)...`）。



###### Lab 14：合併衝突（Merge Conflict）模擬與視覺化三方合併

* **Complete Context Prompt**：
> 「請教我在 VS Code 介面中如何模擬並解決 `README.md` 的 Git 合併衝突（Merge Conflict），使用內建的 Merge Editor 選擇保留雙方變更。」


* **Complete Student Guide**：
1. 在不同分支修改 `README.md` 同一行文字並嘗試執行 `git merge`。
2. 點擊 VS Code 編輯器下方的 **`在合併編輯器中解析 (Resolve in Merge Editor)`** 勾選變更並完成合併。
3. **驗證標準**：衝突標記（`<<<<<<<`、`=======`、`>>>>>>>`）完全消除，完成合併提交。



###### Lab 15：時光倒流救星——`git reflog` 與 `git reset` 誤刪救援

* **Complete Context Prompt**：
> 「假設我不小心執行了 `git reset --hard HEAD~1` 刪除了最新的 Commit，請示範如何利用 `git reflog` 找回遺失的提交雜湊值（Commit Hash）並完整復原。」


* **Complete Student Guide**：
1. 執行 `git reflog` 檢視操作歷史紀錄。
2. 找到被重置前的 Commit ID，執行 `git reset --hard <commit_hash>`。
3. **驗證標準**：執行 `git log -n 2` 確認原本遺失的 Commit 紀錄與檔案完整重現。



---

##### 階段四：環境即程式碼（DevContainer 客製化，Labs 16–20）

###### Lab 16：建立專案專屬 `.devcontainer/devcontainer.json`

* **Complete Context Prompt**：
> 「請為 `Grace-TA/DM2026` 設計一份 `.devcontainer/devcontainer.json`，基於官方 Python 3.12 映像檔，並在容器建立時自動預裝 `ms-python.python`、`ms-toolsai.jupyter` 與 `GitHub.copilot` 擴充套件。」


* **Complete Student Guide**：
1. 建立目錄與檔案：`mkdir -p .devcontainer && touch .devcontainer/devcontainer.json`。
2. 填入 JSON 組態並儲存（注意合法 JSON 語法）。
3. **驗證標準**：按下 `Ctrl+Shift+P`（Mac 為 `Cmd+Shift+P`），搜尋 `Dev Containers` 時可識別到設定檔無語法紅線報錯。



###### Lab 17：設定 `postCreateCommand` 自動化環境初始化

* **Complete Context Prompt**：
> 「請在 `.devcontainer/devcontainer.json` 中加入 `postCreateCommand`，讓未來任何修課學生開啟 `DM2026` 的 Codespace 時，系統自動執行 `pip install -r requirements.txt`。」


* **Complete Student Guide**：
1. 在 `devcontainer.json` 新增 `"postCreateCommand": "pip install --user -r requirements.txt"`。
2. 透過指令面板測試或檢視語法驗證。
3. **驗證標準**：確認 JSON 結構包含 `postCreateCommand` 鍵值且與 `requirements.txt` 路徑對應正確。



###### Lab 18：容器重建（Rebuild Container）與持久性驗證

* **Complete Context Prompt**：
> 「我剛修改完 `.devcontainer/devcontainer.json`，請引導我執行 `Codespaces: Rebuild Container`，並說明重建過程中 `/workspaces/DM2026` 內的檔案會發生什麼事。」


* **Complete Student Guide**：
1. 按下 `F1` 或 `Ctrl+Shift+P`，輸入並執行 **`Codespaces: Rebuild Container`**。
2. 等待約 1～2 分鐘容器重新連線後，檢查 `ls -la /workspaces/DM2026`。
3. **驗證標準**：專案程式碼與講義完全保留，且預定義的擴充套件已自動載入。



###### Lab 19：客製化終端機歡迎橫幅（MOTD）與快捷指令

* **Complete Context Prompt**：
> 「請在 `.devcontainer/` 內建立一個 `welcome.sh`，在學生每次開啟終端機時自動顯示『DM2026 離散數學雲端實驗室已就緒』與 Git 分支提示。」


* **Complete Student Guide**：
1. 建立 `.devcontainer/welcome.sh` 並在 `devcontainer.json` 的 `postAttachCommand` 掛載執行。
2. 開啟新的終端機分頁（點擊終端機右上角 `+` 號）。
3. **驗證標準**：新終端機啟動第一行即顯示客製化的課程歡迎訊息。



###### Lab 20：設定預設連接埠屬性（`portsAttributes`）

* **Complete Context Prompt**：
> 「請在 `devcontainer.json` 中設定 `portsAttributes`，將 Port `8501`（Streamlit 應用程式）預設標記為 `DM2026 Interactive App` 並設定自動在瀏覽器分頁開啟通知。」


* **Complete Student Guide**：
1. 在 `devcontainer.json` 加入 `"portsAttributes": { "8501": { "label": "DM2026 Interactive App", "onAutoForward": "notify" } }`。
2. **驗證標準**：後續啟動 8501 埠服務時，`連接埠 (PORTS)` 面板自動顯示自訂標籤名稱。



---

##### 階段五：雲端網頁部署、AI 代理與資源管控（Labs 21–25）

###### Lab 21：建置並公開預覽離散數學互動式 Web App（Port Forwarding）

* **Complete Context Prompt**：
> 「請用 `streamlit` 在 `labs/app_dm2026.py` 寫一個互動式『二進位與十六進位轉換暨布林邏輯計算器』，並教我透過 Codespaces Port Forwarding 產生公開預覽網址。」


* **Complete Student Guide**：
1. 安裝並啟動：`pip install streamlit && streamlit run labs/app_dm2026.py`。
2. 在下方 `連接埠 (PORTS)` 分頁找到 `8501`，右鍵將 `Port Visibility` 改為 `Public`，點擊地球圖示開啟網頁。
3. **驗證標準**：外部瀏覽器成功開啟互動式網頁介面並可即時滑動計算。



###### Lab 22：使用 GitHub Actions 建置自動化作業批改（CI Autograding）

* **Complete Context Prompt**：
> 「請為 `Grace-TA/DM2026` 建立 `.github/workflows/ci_test.yml`，設定每次學生 Push 程式碼或發起 PR 時，自動在雲端執行 `pytest` 驗證離散數學作業。」


* **Complete Student Guide**：
1. 建立 `.github/workflows/ci_test.yml` 並推送至 GitHub。
2. 前往 `[https://github.com/Grace-TA/DM2026/actions](https://github.com/Grace-TA/DM2026/actions)` 檢視工作流程執行狀態。
3. **驗證標準**：Actions 頁面顯示綠色勾勾（`All checks have passed`）。



###### Lab 23：利用 Copilot Agent 批次重構與文件自動化

* **Complete Context Prompt**：
> 「請在右側 Copilot 聊天視窗中，針對 `labs/lab09_graph.py` 要求 AI 補齊完整的 Google Style Docstrings、Type Hints（型別註記），並產生時間複雜度 Big-O 分析註解。」


* **Complete Student Guide**：
1. 全選 `labs/lab09_graph.py` 程式碼，在右側 Copilot 視窗輸入指令並點擊套用（Apply in Editor）。
2. 使用 VS Code 內建的 Diff 檢視器逐行審查變更。
3. **驗證標準**：程式碼具備完整型別註記（如 `def find_path(graph: nx.Graph, start: str, end: str) -> list[str]:`）且可無誤執行。



###### Lab 24：跨裝置無縫切換——從瀏覽器連線至本機桌面版 VS Code

* **Complete Context Prompt**：
> 「請說明如何從目前的瀏覽器分頁（`[https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/](https://fantastic-dollop-9rpj66gp74hxx5w.github.dev/)`），一鍵切換到我電腦本機安裝的桌面版 VS Code 繼續操作同一個雲端容器。」


* **Complete Student Guide**：
1. 點擊瀏覽器視窗左上角三條橫線選單 -> 選擇 **`在 VS Code 桌面版中開啟 (Open in VS Code Desktop)`**。
2. 允許瀏覽器喚起本機 VS Code 並自動安裝 `GitHub Codespaces` 延伸模組。
3. **驗證標準**：本機桌面版 VS Code 左下角顯示 `Codespaces: fantastic dollop`，且終端機路徑與檔案狀態完全同步。



###### Lab 25：工作坊收尾——環境清理、Push 備份與停止運算計費

* **Complete Context Prompt**：
> 「工作坊即將結束，請給我一組最終檢查清單與指令，確保我在 `/workspaces/DM2026` 的所有實驗成果都已推送到 `Grace-TA/DM2026`，並安全停止 `fantastic-dollop-9rpj66gp74hxx5w` 停止計費。」


* **Complete Student Guide**：
1. 執行最終同步：`git status && git add . && git commit -m "chore: complete 90-min codespaces workshop" && git push`。
2. 點擊編輯器左下角綠色按鈕 **`Codespaces: fantastic dollop`**，選擇 **`Stop Current Codespace`**。


3. **驗證標準**：瀏覽器顯示「Your codespace is stopped」，確認 `Grace-TA` 組織停止計算 Core-hours 運算費用。
