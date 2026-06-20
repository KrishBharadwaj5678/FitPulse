[English](README.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

# 🏋️‍♂️ FitPulse

**FitPulse** は、コンピュータビジョンを活用してリアルタイムで腕立て伏せを検出し、回数をカウントし、トレーニングペースを追跡し、ワークアウト履歴をExcelに保存し、パフォーマンスグラフを生成するAI搭載のフィットネストラッキングアプリケーションです。

![FitPulseDemo](https://github.com/KrishBharadwaj5678/FitPulse/raw/main/FitPulseDemo.gif)

## 🚀 機能

| 機能               | 説明                    |
| ---------------- | --------------------- |
| 🎯 リアルタイム腕立て伏せ検出 | ポーズ推定を使用して腕立て伏せの動きを検出 |
| 🔢 自動回数カウント      | 完了した腕立て伏せを正確にカウント     |
| ⏱️ トレーニングペース追跡   | 各腕立て伏せにかかった時間を計測      |
| ⚠️ 姿勢警告システム      | 体の姿勢が正しくない場合に通知       |
| 📈 進捗バー          | トレーニング目標に対する進捗を表示     |
| 🔊 音声フィードバック     | 回数完了ごとに効果音を再生         |
| 📄 Excelデータ記録    | トレーニング履歴を自動保存         |
| 📊 パフォーマンスグラフ    | セッション後に分析グラフを表示       |
| 📷 ライブカメラ追跡      | Webカメラを使用してリアルタイム分析   |
| 📹 動画ファイル対応      | 録画済み動画からトレーニングを分析     |
| 🖼️ PNGグラフ出力     | グラフを画像ファイルとして保存       |
| 🎨 シンプルなUI       | 使いやすく分かりやすいインターフェース   |

---

## 🛠 技術スタック

| 技術                       | 用途              |
| ------------------------ | --------------- |
| 🐍 Python                | メインプログラミング言語    |
| 🤖 Ultralytics YOLO Pose | 人体ポーズ検出モデル      |
| 🎥 OpenCV                | 動画処理およびUI表示     |
| 🔢 NumPy                 | 角度計算および配列操作     |
| 🔊 Pygame                | 音声フィードバックシステム   |
| 📄 OpenPyXL              | Excelファイルの作成と更新 |
| 📊 Matplotlib            | グラフ生成と可視化       |

---

## ⚙️ インストール

### 1️⃣ リポジトリをクローン

```bash id="h8r3ka"
git clone https://github.com/KrishBharadwaj5678/FitPulse.git
```

### 2️⃣ プロジェクトディレクトリへ移動

```bash id="q4m7xp"
cd FitPulse
```

### 3️⃣ 依存関係をインストール

```bash id="n2v8zd"
pip install -r requirements.txt
```

## 4️⃣ アプリを実行

### 📹 動画解析モード

```bash id="t9k1wb"
python main.py
```

#### または

### 📷 ライブカメラモード

```bash id="c5x7lm"
python liveTracking.py
```
