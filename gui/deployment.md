# Scientific Calculator Deployment Guide

## Project Overview

This project is a Python-based Scientific Calculator built using:

* Python
* Tkinter
* PyInstaller

The calculator supports:

* Basic arithmetic operations
* Scientific operations
* Trigonometric functions
* Logarithmic functions
* Hyperbolic functions
* Responsive GUI
* Keyboard support

---

# Folder Structure

```text
SciCal/
│
├── cli/
│   └── main.py
│
├── gui/
│   ├── gui.py
│   ├── basicop.py
│   ├── scientificop.py
│   ├── utils.py
│   ├── history.py
│   ├── build/
│   ├── dist/
│   └── gui.spec
│
└── README.md
```

---

# Requirements

Install Python:

* Python 3.11 or above recommended

Install PyInstaller:

```bash
pip install pyinstaller
```

---

# Running the GUI Calculator

Open terminal inside the `gui` folder and run:

```bash
python gui.py
```

---

# Creating Executable (.exe)

Open terminal inside the `gui` folder.

Run:

```bash
pyinstaller --onefile --windowed gui.py
```

---

# Build Output

After successful build:

```text
gui/
│
├── build/
├── dist/
│   └── gui.exe
```

The executable file will be available inside:

```text
dist/gui.exe
```

---

# Important Notes

## If PermissionError Occurs

Close:

* gui.exe
* python.exe
* pythonw.exe

from Task Manager before rebuilding.

---

## If Import Errors Occur

Ensure all required files are inside the same folder as `gui.py`:

* basicop.py
* scientificop.py
* utils.py
* history.py

---

# Features Implemented

* Fullscreen responsive GUI
* Scientific operations
* Colored operator buttons
* Keyboard input support
* Error handling
* Backspace support
* Clear screen functionality

---

# Future Improvements

Possible future features:

* Calculation history
* Themes
* Graph plotting
* Memory functions
* Expression parser
* CustomTkinter UI
* Unit converter

---

# Author

Rasshi Ashish Srivastav

B.Tech Information Technology
Madan Mohan Malaviya University of Technology
