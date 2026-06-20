[English](README.md) | [Português](README.pt.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

# 🏋️‍♂️ FitPulse 

FitPulse is an AI-powered fitness tracking application that uses computer vision to detect push-ups in real time, count repetitions, track workout pace, save workout history to Excel, and generate performance graphs.

![FitPulseDemo](https://github.com/KrishBharadwaj5678/FitPulse/raw/main/FitPulseDemo.gif)

## 🚀 Features

|      Feature                     |  Description                                 |
| ------------------------------ | ---------------------------------------------- |
| 🎯 Real-time Push-up Detection | Detects push-up movement using pose estimation |
| 🔢 Automatic Rep Counting      | Counts completed push-ups accurately           |
| ⏱️ Workout Pace Tracking       | Measures time taken for each push-up           |
| ⚠️ Posture Warning System      | Alerts user when body alignment is incorrect   |
| 📈 Progress Bar                | Shows progress toward workout goal             |
| 🔊 Audio Feedback              | Plays sound on every completed rep             |
| 📄 Excel Data Logging          | Saves workout session history automatically    |
| 📊 Performance Graphs          | Displays workout analytics after session       |
| 📷 Live Camera Tracking        | Track workouts directly using webcam           |
| 📹 Video File Support          | Analyze workouts from recorded video           |
| 🖼️ PNG Graph Export           | Saves graphs as image files                    |
| 🎨 Clean UI                    | Simple and user-friendly interface             |

---

## 🛠 Tech Stack

|  Technology              |   Purpose                              |
| ------------------------ | --------------------------------------- |
| 🐍 Python                | Core programming language               |
| 🤖 Ultralytics YOLO Pose | Human pose detection model              |
| 🎥 OpenCV                | Video processing and UI display         |
| 🔢 NumPy                 | Angle calculations and array operations |
| 🔊 Pygame                | Audio feedback system                   |
| 📄 OpenPyXL              | Excel file creation and updates         |
| 📊 Matplotlib            | Graph generation and visualization      |

---


## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/KrishBharadwaj5678/FitPulse.git
```

### 2️⃣ Navigate to project directory

```bash
cd FitPulse
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the App

### 📹 Video Tracking Mode

```bash
python main.py
```

#### OR

### 📷 Live Camera Mode

```bash
python liveTracking.py
```
