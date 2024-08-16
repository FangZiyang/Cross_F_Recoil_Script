# Cross_Fire_Recoil_Script

A Python automation script designed to overcome the limitations of `pyautogui` in gaming scenarios, where traditional GUI automation tools may fail to register clicks. This script ensures mouse clicks are registered within games, providing a more reliable and human-like interaction.

## Key Features

- **Game-Compatible**: Effectively registers mouse clicks in games where `pyautogui` fails.
- **Human-like Random Click Distribution**: Simulates the natural variability in human clicking patterns for a more authentic automation experience.
- **Admin Privileges Required**: The script must be run with administrator privileges to function correctly.

## How to Use

1. Ensure you have `pydirectinput`, `numpy`, and `pywin32` installed.
2. Save the script as a `.py` file.
3. Run the script with administrator privileges and use the mouse side button or Shift key to trigger the recoil operation.

## Dependencies

- `pydirectinput`: For simulating mouse and keyboard inputs that work in games.
- `numpy`: For generating random numbers based on a normal distribution to mimic human click patterns.
- `pywin32`: For accessing Windows API functions.

## Installation

Install the dependencies with pip:

```bash
pip install pydirectinput numpy pywin32
