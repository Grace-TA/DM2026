# 🪪 DM2026 — 學生案頭速查卡、28 Labs 破關護照與 L.A.W. 評量規準

> **設計定位**：可雙面列印為 A4 案頭實戰速查卡（Quick Reference），並作為 90 分鐘課堂＋課後 1 週自主破關的**官方認證護照**。  
> **目標倉庫**：[`Grace-TA/DM2026`](https://github.com/Grace-TA/DM2026) $\rightarrow$ 你的個人 Fork：`https://github.com/<你的帳號>/DM2026`

---

## ⚡ 一、 黃金生存五守則（開機前先讀 30 秒！）

1. **絕對不要點老師的 `fantastic-dollop` 連結**：那是 `Grace-TA` 老師的私有實例，你會看到 404！請永遠先 **Fork `Grace-TA/DM2026`**，再從**你自己的 Fork** 開啟 Codespace。
2. **選 `2-core` + `Southeast Asia`**：個人 GitHub Free 帳號每月免費 **120 core-hours** + **15 GB-months**。選 `2-core` 可免費跑滿 **60 小時**，千萬別手滑開 `8-core`！
3. **只把檔案放在 `/workspaces/DM2026` 底下**：Linux 容器預設起點在 `/workspaces`（內有 `.codespaces/`、`.oryx/`、`DM2026/`），**只有 `/workspaces/DM2026` 底下受持久性磁碟（Persistent Volume）保護**；寫在 `/tmp` 或 `~/` 會在 Rebuild 時清空！
4. **Commit & Push 是唯一真存檔**：Codespace 只是臨時租來的雲端貨櫃，**寫完程式不 `git push`，刪掉容器就會永遠消失**！
5. **Stop 不算結束，Delete 才歸零儲存費**：`32 GB` 虛擬硬碟只要還存在，關機照樣吃掉你每月的 `15 GB-months` 儲存配額！**下課前最後 3 分鐘，推完程式立刻去 `github.com/codespaces` 按 `Delete`！**

---

## ⌨️ 二、 雲端 VS Code Web 與 Terminal 必備指令速查表

### 1. VS Code Web 快捷鍵（Windows / macOS）
| 功能 | Windows / Linux | macOS | 使用時機 |
|:---|:---|:---|:---|
| **開啟／隱藏終端機** | `` Ctrl + ` `` | `` Cmd + ` `` | 隨時切進 Linux 命令列 |
| **萬能指令面板（Command Palette）** | `F1` 或 `Ctrl + Shift + P` | `F1` 或 `Cmd + Shift + P` | 找 `Rebuild Container`、`Codespaces` 設定 |
| **快速搜尋開啟檔案** | `Ctrl + P` | `Cmd + P` | 一秒打開 `WEEK03.md` 或 `.devcontainer` |
| **儲存目前檔案** | `Ctrl + S` | `Cmd + S` | 執行 Python 或 `git commit` 前必按 |
| **開啟 Copilot Chat** | `Ctrl + Alt + I` | `Ctrl + Cmd + I` | 貼入本教材每題的 **Complete Context Prompt** |

### 2. Git 免密閉環四連擊 & Linux 環境體檢
```bash
# [環境體檢] 確認 Ubuntu 24.04.5 LTS、核心數、記憶體、/workspaces/DM2026 目錄與 Python 版本
cat /etc/os-release | grep PRETTY_NAME && nproc && free -h && ls -la /workspaces && python3 --version

# [建立分支] 永遠在自己的實驗分支工作
git checkout -b feat/my-dm2026

# [存檔三部曲] 寫完程式一定要推回你的 GitHub Fork
git status
git add .
git commit -m "feat: complete DM2026 lab"
git push -u origin feat/my-dm2026
```

### 3. GitHub CLI (`gh codespace`) 遙控軍火庫
| 指令 | 說明 |
|:---|:---|
| `gh codespace list`（縮寫 `gh cs list`） | 列出你名下所有運行中與已停止的 Codespace |
| `gh cs ports -c <name>` | 查看目前轉發中的 Port 與狀態 |
| `gh cs ssh -c <name>` | 從本機終端機直接 SSH 連進雲端容器 |
| `gh cs stop -c <name>` | 停止運算（停算核時，**但磁碟仍計費！**） |
| `gh cs delete -c <name>` | 徹底刪除容器（**儲存計費歸零！**） |

---

## 🔄 三、 Google Colab vs. GitHub Codespaces 遷移速對卡

| 你的舊習慣（Colab） | 升級後的高手做法（Codespaces） |
|:---|:---|
| 把所有程式碼塞進同一個 `.ipynb` 檔案 | 拆分為 `discrete_toolkit/` 多支 `.py` 模組＋`tests/` 自動化測試 |
| 每次重開都要重跑 `!pip install ...` | 寫進 `.devcontainer/devcontainer.json`，全班永遠預裝完畢 |
| 程式跑不動只會截圖問助教 | 下中斷點按 `F5` 使用 **Debugger** 單步透視變數與記憶體 |
| 跑完 `plt.show()` 右鍵下載圖片交作業 | 改用 `plt.savefig("out.png", dpi=150)` 存檔並 `git push` 永久留痕 |
| 下載 `.ipynb` 再手動上傳繳交平台 | 直接從 Fork 發起 **Pull Request** 至 `Grace-TA/DM2026` |

---

## 🎫 四、 28 題 Classic Labs 破關護照（Student Passport）

> **規則**：課堂 90 分鐘內完成標註 **🔥 課堂必修** 的 12 題；課後 1 週內自由挑戰其餘 16 題並提交 PR。

| 題號 | Lab 名稱 | 類型 | 難度 | 關聯技能 / DM2026 | 通關打勾 |
|:---:|:---|:---:|:---:|:---|:---:|
| `01` | Fork `DM2026` 與啟動 2-Core Codespace | 🔥 必修 | ★☆☆ | Fork / Free Tier | ☐ |
| `02` | 容器硬體探針（2-Core vs 4-Core 驗證） | 🔥 必修 | ★☆☆ | `nproc`, `free -h`, `df -h` | ☐ |
| `03` | 雲端 Terminal 與 Python/Git 健檢 | 🔥 必修 | ★☆☆ | `python3`, `git remote` | ☐ |
| `04` | 建立 `feat/` 分支與首支 Python 腳本 | 🔥 必修 | ★☆☆ | Git Branch / Python | ☐ |
| `05` | `.vscode/settings.json` 與擴充套件漫遊 | 🚀 進階 | ★★☆ | Settings Sync | ☐ |
| `06` | 免密 Git 閉環（`add -> commit -> push`） | 🔥 必修 | ★☆☆ | OAuth Credential Proxy | ☐ |
| `07` | 解剖與撰寫 `.devcontainer/devcontainer.json` | 🔥 必修 | ★★☆ | IaC / Docker Image | ☐ |
| `08` | `Rebuild Container` 與環境閘門驗證 | 🔥 必修 | ★★☆ | `verify_codespace_env.py` | ☐ |
| `09` | HTTP Server 與 Port Forwarding 公私切換 | 🔥 必修 | ★★☆ | Port 8000 Tunnel | ☐ |
| `10` | 雲地雙向檔案上傳與下載 | 🚀 進階 | ★★☆ | Explorer Drag & Drop | ☐ |
| `11` | `gh codespace` CLI 遠端遙控術 | 🚀 進階 | ★★☆ | `gh cs list/stop/ports` | ☐ |
| `12` | Secrets 注入與 `.gitignore` 防洩漏測試 | 🚀 進階 | ★★☆ | DevSecOps Hygiene | ☐ |
| `13` | FinOps 配額精算（Stop vs Delete 實測） | 🚀 進階 | ★★☆ | 120 core-hrs / 15 GB-mo | ☐ |
| `14` | 容器毀損急救與 Live Share 救援演練 | 🚀 進階 | ★★★ | `git diff` / Rebuild | ☐ |
| `15` | `WEEK01` Colab 遷移至 Jupyter Notebook | 🔥 必修 | ★☆☆ | `.ipynb` Kernel | ☐ |
| `16` | `WEEK02` 1135 縮排修復與命題真值表 CLI | 🔥 必修 | ★★☆ | Logic / Truth Table | ☐ |
| `17` | `WEEK02` 1160/1171 字串清洗與 `enumerate` | 🚀 進階 | ★★☆ | Data Cleaning | ☐ |
| `18` | `WEEK02` 1175 9×9 乘法表與斷點 Debugger | 🚀 進階 | ★★☆ | VS Code Debugger | ☐ |
| `19` | `WEEK03` 集合運算與冪集（Power Set）生成器 | 🚀 進階 | ★★☆ | Set Comprehension | ☐ |
| `20` | `WEEK03` Dict + `try-except` 關係性質檢測器 | 🚀 進階 | ★★☆ | Reflexive/Symmetric/Transitive | ☐ |
| `21` | `WEEK03` 升級多檔案 OOP `discrete_toolkit/` | 🚀 進階 | ★★★ | Python Package Architecture | ☐ |
| `22` | `WEEK03` Matplotlib 4 相位三角波與單位圓存圖 | 🔥 必修 | ★★☆ | `Agg` + `plt.savefig` | ☐ |
| `23` | Port 8080 互動式集合溫氏圖網頁站 | 🚀 Hero | ★★★ | HTML/SVG + Port Forward | ☐ |
| `24` | `pytest` 神經符號自動化作業批改閘門 | 🚀 Hero | ★★★ | Unit Testing (`pytest`) | ☐ |
| `25` | 客製化 `DM2026` Dockerfile 與 Prebuild 加速 | 🚀 Hero | ★★★ | Custom Image Caching | ☐ |
| `26` | Copilot Chat `@workspace` 除錯與複雜度優化 | 🚀 Hero | ★★☆ | AI Pair Programming | ☐ |
| `27` | Fork $\rightarrow$ Pull Request 至 `Grace-TA/DM2026` | 🚀 Hero | ★★★ | Open-Source Collaboration | ☐ |
| `28` | **終極閉環**：DM2026 雲端實驗室＋Delete 歸零 | 🔥 必修 | ★★★ | Commit $\rightarrow$ Push $\rightarrow$ Delete | ☐ |

---

## 📊 五、 L.A.W. 四維量化評量規準（Evaluation Rubric）

| 評量維度 | 權重 | Bloom's 層級 | 優秀（90–100 分） | 合格（70–89 分） | 待補強（< 70 分） |
|:---|:---:|:---:|:---|:---|:---|
| **1. 雲端容器建立與 Git 閉環** | **25%** | L3 Apply | 成功 Fork、獨立開 2-core、建新分支並有 ≥2 次乾淨 commit push 紀錄 | 成功開啟並完成至少 1 次 push，但直接推向 `main` | 誤連教師 URL 或未 push 導致成果遺失 |
| **2. IaC 環境配方與端口服務** | **25%** | L4 Analyze | `verify_codespace_env.py` 全綠通過，且成功示範 Port 8000/8080 HTTPS 預覽 | 跑通預覽但無法解釋 `devcontainer.json` 欄位作用 | 環境報錯未排除或未測試 Port Forwarding |
| **3. `DM2026` 離散數學遷移品質** | **30%** | L5–L6 Evaluate/Create | 完成真值表、Matplotlib 雙圖輸出，並跑通 `pytest` 單元測試或 OOP 模組 | 完成基本 Notebook 執行與圖表存檔，但缺乏測試驗證 | 仍停留在無驗證手動複製貼上階段 |
| **4. FinOps 配額與資安紀律** | **20%** | L5 Evaluate | 倉庫零明文密鑰、Port 示範後回復 Private、**課後確實 Delete 歸零儲存費** | 完成關閉但僅按 Stop 忘記 Delete（仍佔 32GB 配額） | 洩漏測試 Token 或放任容器持續掛機燒光核時 |
