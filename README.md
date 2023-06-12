# Quick start

New to whatever that is? This guide is mostly copied from the [Qt for Python](https://doc.qt.io/qtforpython-6/quickstart.html) quick start page and [Install TensorFLow 2](https://www.tensorflow.org/install).

## Requirements

Before you can install Qt for Python and TensorFlow, first you must install the following software:

- Python 3.8–3.11
- We recommend using a virtual environment, such as `venv` or `virtualenv`

You need to run one of the following 64-bit systems:

- Ubuntu 16.04 or later
- Windows 7 or later (with C++ redistributable)
- macOS 10.12.6 (Sierra) or later (no GPU support)
- WSL2 via Windows 10 19044 or higher including GPUs (Experimental)

## Installation

### Updating `pip`

TensorFlow 2 packages require a pip version >19.0 (or >20.3 for macOS).

```
pip install --upgrade pip
```

### Creating and activating an environment

Create environment (Your Python executable might be called python3):
```
python -m venv env
```
Activate the environment (Linux and macOS):
```
source env/bin/activate
```
Activate the environment (Windows):
```
env\Scripts\activate.bat
```

### Installing PySide6 and TensorFlow

Now you are ready to install the Qt for Python and TensorFlow packages using `pip`. From the terminal, run the following command for the latest version:
```
pip install pyside6 tensorflow
```

## Usage

### Running the application

```
python3 main.py
```

### Exiting the virtual environment

```
deactivate
```