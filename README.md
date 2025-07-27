# Python Mini-Games Collection

A collection of classic mini-games developed using Python's standard **tkinter** library. This project serves as a demonstration of various game mechanics and tkinter GUI programming, offering a fun and interactive experience for users.

-----

## ✨ Features

  * **Multiple Games**: Includes a variety of popular mini-games such as **Bounce Ball**, **2048**, **Rock Paper Scissors**, **Tic-Tac-Toe**, and a simple **Spinner** animation.
  * **Tkinter GUI**: All games are built with the **tkinter** library, providing a native graphical user interface.
  * **Modular Design**: The codebase is structured into separate files for each game, promoting readability, maintainability, and ease of adding new games.
  * **Simple Controls**: Each game features intuitive and easy-to-learn controls.
  * **Score Tracking**: Real-time score display is implemented for applicable games.

-----

## 🚀 How to Run

Follow these steps to get the game collection up and running on your local machine.

### Prerequisites

  * **Python 3.x**: If you don't have Python installed, download it from [python.org](https://www.python.org/). **tkinter** is usually included with standard Python installations.

### Installation

No external `pip` installations are typically required for tkinter applications. Just ensure you have Python 3.x installed.

### File Structure

Ensure you have the following file structure in your project folder:

```
Your_Project_Folder/
├── MAINFRAME.py
├── MAIN.py
├── Game248.py
├── rps.py
├── tic_tac_toe.py
├── game.py
├── fs.py
├── PYTHONCSProject.py
├── Logo.jpg
├── default.png
└── README.md
```

### Run the Game

Navigate to your project directory in your terminal or command prompt and run the `MAINFRAME.py` file:

```sh
python MAINFRAME.py
```

-----

## 🎮 Controls

### Main Menu

Use the buttons to select and launch different games.

### Bounce Ball Game

  * **Spacebar**: Pause the game.
  * **Enter**: Restart the game (after a "Game Over").
  * (Paddle movement controls are not explicitly defined, but typically involve Arrow Keys or W/S keys.)

### 2048 Game

  * **Arrow Keys** (Up, Down, Left, Right): Move tiles on the board.

### Rock Paper Scissors

  * **Buttons**: Click the "Play Rock", "Play Paper", or "Play Scissor" buttons to make your choice.
  * **Clear Button**: Clear the current game result.
  * **Quit Button**: Exit the game.

### Tic-Tac-Toe

  * **Mouse Clicks**: Click on the squares to place your marker.
  * **Buttons**: Select game mode (Player vs Computer, Player vs Player) and rematch/main menu options.

### Spinner

  * **Spacebar**: "Flick" the spinner to increase its rotation speed.

-----

## 🧑‍💻 Project Structure

  * `MAIN.py`: Acts as a central game console, containing functions to launch the Bounce Ball game (`BB()`) and Rock Paper Scissors (`Rp()`). It also manages overall score display.
  * `Game248.py`: Implements the core logic and GUI for the 2048 game.
  * `rps.py`: Contains the logic and GUI for the Rock Paper Scissors game.
  * `tic_tac_toe.py`: Implements the Tic-Tac-Toe game with options for Player vs Computer and Player vs Player modes.
  * `game.py`: Contains classes and logic specifically for the Bounce Ball game, utilized by `MAIN.py`.
  * `fs.py`: A simple Python script demonstrating a spinner animation using the **turtle** graphics module.
  * `PYTHONCSProject.py`: Appears to be another, possibly earlier, implementation of the 2048 game, similar to `Game248.py`.
  * `Logo.jpg`, `default.png`: Image assets used within the `MAIN.py` and `rps.py` games respectively.
