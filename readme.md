# Mouse Click Counter
## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example](#example)

## Introduction

This project counts the number of left mouse clicks and displays the count on a Busy Tag device. Each left click updates an image with the current count, which is saved to the Busy Tag device's drive.

## Project Purpose

The main goal of this project is to:
	
- Count the number of left mouse clicks.

- Generate an image displaying the current click count.

- Update the image on the Busy Tag device each time the count changes.


## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.6 or higher
- `Pillow` (PIL Fork) - Python Imaging Library
- `pynput` - A library to monitor and control input devices
- A Busy Tag device connected to your computer.

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```
   git clone https://github.com/busy-tag/Mouse_Click_Counter.git
2. Navigate to the cloned repository:

	```
	cd Mouse_Click_Counter
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install Pillow pynput
	```

4. Ensure the default font file `MontserratBlack-3zOvZ.ttf` is in the project directory.

## Configuration

The script provides several customizable parameters:
 
• **Drive Letter:** Prompted input for the drive letter where the Busy Tag device is located (e.g., `D`).

• **Text Content:** Displays the current click count.

• **Font Size and Colors:** Predefined but can be modified in the script. The font size adjusts dynamically based on the number of clicks.


## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python main.py
```
2. **Provide Drive Letter:**
   
    The script will prompt you to enter the drive letter assigned to the Busy Tag device. Enter the letter (e.g., `D`) and press Enter.
         
3. **Script Operation:**

	The script will start counting the left mouse clicks.
	
	Each left click updates the image `click_count.png` with the current click count and saves it to the specified drive.
	
4. **Output:**
	
	The generated image will be saved in the specified directory (e.g., D:) and will be updated with each left click.
	
### Example

After running the script, you should see output similar to this in your terminal:
```
Please enter the drive letter assigned to Busy Tag device (e.g., D): D
Left click counter started. Press 'Ctrl+C' to stop.
Left click count: 1
Left click count: 2
Left click count: 3
Left click count: 4
Left click count: 5
```

An image (e.g., click_count.png) will be saved in the specified directory (e.g., D:), displaying the current click count.
Sample:

<img src="/click_count_sample.png" alt="Sample Moon Phase Image" width="300" height="330"/>

### Troubleshooting ###

If you encounter any issues, ensure:

All Python packages are installed correctly.

The font file (`MontserratBlack-3zOvZ.ttf`) is present in the project directory.

The drive letter is correct and the Busy Tag device is connected.

For any additional help, please open an issue in the repository or contact the maintainer.
