# Random Data Visualizer

A small Python project for generating, storing, and visualizing randomly generated time-series data through a desktop GUI.

The project was mainly built as an exercise in combining **random data generation**, **data visualization**, **file handling**, and a **PySide6 graphical interface**.

## What it does

The application generates numerical data using one of two stochastic processes:

* **Random Walk**
* **Mean-Reverting Process**

After a series is generated, it is:

1. displayed as a line chart,
2. saved automatically as a CSV file,
3. added to a list of previously generated datasets.

Saved datasets can later be loaded back into the graph or deleted from the application.

## Data generation

The generation logic is contained in `random_data.py`.

### Random Walk

The random walk starts from a chosen value and moves by either `+1` or `-1` at every step.

A **bias** controls the probability of moving upward.

For example:

* `bias = 0.5` gives equal probability to moving up or down.
* a value above `0.5` makes upward movements more likely.
* a value below `0.5` makes downward movements more likely.

The function returns two sequences:

* the step number
* the generated value at each step

### Mean-Reverting Process

The second generator uses an **Ornstein–Uhlenbeck-style mean-reverting process**.

Instead of wandering freely like a random walk, the generated values tend to move back toward a defined mean over time while still being affected by random noise.

The main user-controlled parameter is `sigma`, which determines the strength of the random variation.

Internally, the process also uses:

* `theta` — the rate of mean reversion
* `mu` — the long-term mean

These currently have default values in the generator.

## Graphical interface

The application interface is built with **PySide6**.

`visual.py` contains the main application logic and connects the GUI to the data-generation functions.

The main window contains an embedded **Matplotlib** figure used to display the currently selected or generated dataset.

A separate data-generation dialog lets the user choose between the two generation methods and enter their parameters.

When the dialog submits the parameters, the main window calls the corresponding function from `random_data.py` and updates the graph.

## Saving generated data

Every generated series is automatically written to the `Data/` directory as a CSV file.

Files use a timestamped name such as:

```text
random_walk_YYYY_MM_DD_HHMMSS.csv
```

or

```text
random_mean_reverting_YYYY_MM_DD_HHMMSS.csv
```

Each CSV contains two columns:

```text
step,value
```

This makes the generated series independent from the GUI and easy to inspect as normal tabular data.

## Loading data

Existing CSV files from the `Data/` directory are shown in the application's file list.

When a file is selected, the program reads its `step` and `value` columns and reconstructs the series.

The loaded data is then passed back to the Matplotlib canvas and plotted in the main window.

## Deleting data

Saved datasets can also be removed through the interface.

Deleting an entry removes both:

* the CSV file from the `Data/` directory
* the corresponding item from the GUI list

## Project structure

```text
Project---Random-Data-Visualizer/
│
├── Data/
│   └── Generated CSV datasets
│
├── GUI Files/
│   └── Qt Designer interface files
│
├── random_data.py
│   └── Random walk and mean-reverting data generators
│
├── visual.py
│   └── Main application logic, plotting, file handling, and GUI events
│
├── edited_frontend.py
│   └── Generated/main-window PySide6 interface code
│
├── secondary_window.py
│   └── Generated PySide6 code for the data-generation dialog
│
└── README.md
```

## Technologies used

* **Python**
* **NumPy** — numerical operations and random-number generation
* **Matplotlib** — plotting the generated series
* **PySide6 / Qt** — desktop graphical interface
* **CSV** — storage of generated datasets
* **Arrow** — timestamp generation for saved filenames

## Purpose

This is a small programming project rather than a finished application or software product.

Its purpose is to demonstrate how a Python desktop interface can connect stochastic data-generation functions with visualization and simple persistent CSV storage.
