# Cross_Fire_Recoil_Script


A Python automation script for simulating human-like mouse actions to control in-game recoil. It mimics the natural variability in mouse clicks and movement to enhance the realism of automated gameplay.

## Key Features

- **Natural Timing**: Generates random click and interval timings based on a normal distribution.
- **Simulated Mouse Movement**: Optionally moves the mouse downward to simulate recoil control.
- **Trigger on Side Button**: Activated by the mouse side button or Shift key for easy control.
- **Failsafe Disabled**: The script runs without interruptions from the pydirectinput failsafe.

## How to Use

1. Ensure you have `pydirectinput`, `numpy`, and `pywin32` installed.
2. Save the script as a `.py` file.
3. Execute the script and use the mouse side button or Shift key to trigger the recoil operation.

## Dependencies

- `pydirectinput`: To simulate mouse and keyboard inputs.
- `numpy`: For creating normally distributed random timings.
- `pywin32`: For accessing Windows API functions.

## Installation

Install the dependencies with pip:

```bash
pip install pydirectinput numpy pywin32
