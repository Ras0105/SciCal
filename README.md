# Scientific Calculator

A fully functional Scientific Calculator built using Python and Tkinter with support for both basic and advanced scientific operations.

---

# Features

## Basic Operations

* Addition
* Subtraction
* Multiplication
* Division
* Modulus
* Floor Division
* Power

---

## Scientific Operations

* Square Root
* Cube Root
* Square
* Cube

---

## Trigonometric Functions

* sin()
* cos()
* tan()
* cosec()
* sec()
* cot()

---

## Logarithmic Functions

* ln()
* log10()
* exp()

---

## Hyperbolic Functions

* sinh()
* cosh()
* tanh()

---

## Utility Functions

* factorial()
* absolute()
* ceil()
* floor()

---

# GUI Features

* Fullscreen responsive interface
* Keyboard input support
* Colored operator buttons
* Backspace support
* Clear screen functionality
* Error handling

---

# Technologies Used

* Python
* Tkinter
* PyInstaller

---

# Project Structure

```text id="5xvb7m"
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
├── README.md
└── deployment.md
```

---

# Running the Project

## Run GUI Version

Open terminal inside the `gui` folder:

```bash id="6c7kvt"
python gui.py
```

---

## Run CLI Version

Open terminal inside the `cli` folder:

```bash id="7ytn5r"
python main.py
```

---

# Building Executable

Install PyInstaller:

```bash id="r2xw5v"
pip install pyinstaller
```

Build executable:

```powershell id="2b9zpn"
& "C:\Users\smt29\AppData\Local\Python\pythoncore-3.14-64\Scripts\pyinstaller.exe" --onefile --windowed gui.py
```

---

# Output Executable

```text id="8rv3wu"
gui/dist/gui.exe
```

---

# Screenshots

Add screenshots of:

* Main calculator UI
* Scientific operations
* Responsive layout

---

# Future Improvements

* Themes
* History panel
* Graph plotting
* Memory functions
* Unit converter
* CustomTkinter UI

---

# Author

## Rasshi Ashish Srivastav

B.Tech Information Technology
Madan Mohan Malaviya University of Technology

GitHub:
https://github.com/Ras0105
LinkedIn:
https://www.linkedin.com/in/rasshi-ashish-srivastav/