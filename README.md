# Controlling Game Through Hand Gestures

## Project Overview
An interactive system that allows players to control a browser/desktop game using hand gestures detected from a webcam. The project demonstrates real-time hand-pose detection, gesture recognition, and mapping gestures to in-game actions.

## Features
- Real-time hand detection and landmark tracking
- Custom gesture recognition (e.g., open palm = jump, fist = shoot, swipe = move)
- Low-latency mapping of gestures to keyboard/game controls
- Configurable gesture-to-action mappings
- Demo game integration (example: simple endless runner / canvas game)

## Tech Stack
- Language: Python / JavaScript (choose one or both)
- Libraries: MediaPipe (or OpenCV + pre-trained model), TensorFlow (optional), PyAutoGUI or keyboard JS bindings
- Frontend (if browser game): HTML5 Canvas / Phaser.js
- Tools: WebCam, Git, GitHub


# ✋ Hand Gesture Control for Subway Surfers

This project allows you to control the classic endless runner game **Subway Surfers** using simple hand gestures captured via a webcam. Navigate the game's lanes (left, right, jump, and duck) without ever touching the keyboard!

## 🌟 Features

* **Real-time Hand Detection:** Uses your webcam and computer vision to detect the position of your hand.
* **Gesture-to-Key Mapping:** Translates hand movements (moving hand left, right, up, down) into corresponding keyboard inputs (Left Arrow, Right Arrow, Up Arrow/Space, Down Arrow) for seamless gameplay.
* **Game Compatibility:** Specifically tested and configured to control the PC version of **Subway Surfers**.

## ⚙️ Installation

### Prerequisites

You need **Python 3.x** installed on your system.

### 1. Clone the Repository

Open your terminal or command prompt and clone the project:

```bash
git clone [https://github.com/Harshithab14/Hand-Gestures.git](https://github.com/Harshithab14/Hand-Gestures.git)
cd Hand-Gestures

## Install Dependencies
This project relies on OpenCV for image processing and the pyautogui library for simulating keyboard presses.

```Bash

python main_gesture_controller.py


🎮 How to Run
Start the Game: Launch Subway Surfers on your PC and make sure the game window is active.
Run the Script: Execute the main Python script from your terminal.
```Bash

python main_gesture_controller.py

(Note: Replace main_gesture_controller.py with the actual name of your primary Python script.)
Calibrate: The script will open your webcam feed. Center your hand in the frame.

###Play! Use the following gestures to control the surfer:
ActionHand         Gesture
Move Left          Move your hand quickly to the left
Move Right         Move your hand quickly to the right
Jump               Move your hand quickly upwards
Duck/Roll          Move your hand quickly downwards


🧑‍💻 ContributingContributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
1)Fork the Project
2)Create your Feature Branch (git checkout -b feature/AmazingFeature)
3)Commit your Changes (git commit -m 'Add some AmazingFeature')
4)Push to the Branch (git push origin feature/AmazingFeature)
5)Open a Pull Request


📄 LicenseDistributed under the MIT License. See LICENSE for more information.
***

## 🌐 GitHub Setup Commands

Here are the commands you'll use to initialize your project locally and push it to a new GitHub repository:

```bash
# 1. Initialize a new Git repository in your project folder
git init

# 2. Add all your project files to the staging area
git add .

# 3. Commit the initial set of files
git commit -m "Initial commit of Python Gesture Controller for Subway Surfers"

# 4. (On GitHub) Create a new empty repository named 'SubwaySurfers-GestureControl'

# 5. Link your local repository to the new remote GitHub repository
#    (Replace 'your-username' with your actual GitHub username)
git remote add origin https://github.com/your-username/SubwaySurfers-GestureControl.git

# 6. Push your committed files to the remote repository
git push -u origin main
