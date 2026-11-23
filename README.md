# Sensor Data Analysis Tool

## Project Description

This project is a Python program that simulates sensor readings, analyzes the data, and displays graphs.

The program does not require a physical sensor. It uses Python's `random` module to generate simulated sensor values.

## Features

- Generate random sensor readings.
- Choose the sensor type, number of readings, minimum value, maximum value, and alert threshold.
- Calculate statistics using NumPy.
- Display the number of readings, mean, minimum, maximum, and standard deviation.
- Identify readings above the alert threshold.
- Display a line graph with an alert threshold.
- Display a histogram.
- Save readings to a CSV file.
- Load existing readings from a CSV file.
- Handle invalid inputs and file errors.

## Requirements

- Python 3
- NumPy
- Matplotlib

## Installation

Open a terminal in the project folder and install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the program using:

```bash
python sensor_monitor.py
```

The program displays two options:

**Option 1: Generate new sensor readings**

Enter the sensor type, number of readings, minimum value, maximum value, and alert threshold.

The program generates readings, saves them to `sensor_readings.csv`, calculates statistics, and displays two graphs.

**Option 2: Load readings from CSV**

Enter the CSV filename or press Enter to use `sensor_readings.csv`.

The program loads the existing readings, asks for an alert threshold, calculates statistics, and displays the graphs without generating new data.

## Libraries Used

- **random:** Generates simulated sensor readings.
- **csv:** Saves and loads sensor readings.
- **NumPy:** Calculates statistics.
- **Matplotlib:** Creates graphs.

## Project Files

- `sensor_monitor.py`: Main Python program.
- `requirements.txt`: Required Python libraries.
- `README.md`: Project documentation.
- `sensor_readings.csv`: Saved sensor readings.

## Reproducibility

The program uses `random.seed(42)` so the same inputs produce the same random readings.

## Author

Student project for the Sensor Data Analysis Tool assignment.
