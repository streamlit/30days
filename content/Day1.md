# 設定本地開發環境

在我們真正開始建立 Streamlit 應用程式之前，我們必須先設置一個開發環境。

讓我們從安裝和設定 conda 環境開始。

## 安裝 conda

- 前往 https://docs.conda.io/en/latest/miniconda.html 安裝 conda，選擇你的作業系統（Windows、Mac 或 Linux）
- 下載並執行安裝檔來安裝 conda

## 建立一個新的 conda 環境
現在你的 conda 已經裝好了，我們可以建立一個 conda 環境來管理所有的 Python 函式庫相依。

要使用 Python 3.9 建立新環境，請輸入以下指令：
To create a new environment with Python 3.9, enter the following:
```bash
conda create -n stenv python=3.9
```

指令 `conda create -n stenv` 會建立一個 conda 環境叫做 `stenv`，然後 `python=3.9` 會使用 Python 版本 3.9 來設定 conda 環境。

## 啟動 conda 環境

要使用我們剛剛建立好的 conda 環境（叫做 `stenv`），輸入下列指令到 Command Line

```bash
conda activate stenv
```

## 安裝 Streamlit

現在終於是時候安裝 `streamlit` 套件了：
```bash
pip install streamlit
```

## 啟動 Streamlit demo 應用程式

要啟動 Streamlit demo 應用程式（Figure 1），輸入：
```bash
streamlit hello
```
