# Snooker Points Tracker

Snooker Points Tracker is a project that helps you enjoy watching a snooker match by doing the maths for the remaining points on the table through the use of Computer Vision. 

If you want to install the project on your local machine, follow the instructions below.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python. 
* You have a Windows/Linux/Mac machine.

## Installation

To install, follow these steps:

Clone the repository onto your machine:

```
git clone https://github.com/SafwanSipai/snooker-points-tracker.git
```

## Using Snooker Points Tracker

To use, follow these steps:

1. Go to the root of the folder that was created when the repository was cloned.

2. Create a python virtual environment using the command: `python -m venv <env-name>`

3. Install the required libraries/dependencies: `pip install requirements.txt`

4. Activate the python environment (run the following commands in the root folder):

    | Platform | Command                |
    | :--------| :------------------------- |
    | bash/zsh | `source <env-name>/bin/activate` |
    | PowerShell | `<env-name>\Scripts\Activate.ps1` |
    | cmd.exe | `<env-name>\Scripts\activate.bat` |

5. Inside the terminal, run the command: `python app.py --video-path=<path-to-your-mp4-file>`

## In Action

![snooker-tracker-1](https://github.com/SafwanSipai/snooker-points-tracker/assets/83706912/3fb3a638-79c5-43d8-bc9a-bee6ef312a21)
![snooker-tracker-2](https://github.com/SafwanSipai/snooker-points-tracker/assets/83706912/8db52950-f23a-4e57-80ef-dc63701aae2c)

## Limitations and Future Enhancements

* Currently, the model is hard-coded to predict every 400th frame. I would like to fix this by making a prediction every time a full snooker table is detected.

* This program can only be run through the terminal as of now. My main goal is to create a browser extension that makes the prediction on a YouTube video or a live stream. (Feel free to reach out if you have worked with extensions before!)

## Acknowledgement 

* YOLOv8 - the model used to train and predict.

* [Dataset used to train the YOLOv8 model](https://universe.roboflow.com/rushi-l93yy/snookers/dataset/1)
