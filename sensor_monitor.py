import random
import csv
import numpy as np
import matplotlib.pyplot as plt


# Generate simulated sensor readings
def generate_readings(number_of_readings, min_value, max_value):
    random.seed(42)

    readings = []

    for i in range(number_of_readings):
        value = random.uniform(min_value, max_value)
        readings.append(value)

    return readings


# Calculate and display statistics
def calculate_statistics(readings, alert_threshold):
    data = np.array(readings)

    print("\n===== SENSOR STATISTICS =====")
    print("Number of readings:", len(data))
    print("Mean:", round(np.mean(data), 2))
    print("Minimum:", round(np.min(data), 2))
    print("Maximum:", round(np.max(data), 2))
    print("Standard Deviation:", round(np.std(data), 2))

    above_threshold = data[data > alert_threshold]

    print("Readings above threshold:", len(above_threshold))
    print("Alert readings:", np.round(above_threshold, 2))


# Find readings above the alert threshold
def find_outliers(readings, alert_threshold):
    return [reading for reading in readings if reading > alert_threshold]


# Create a line graph
def plot_readings(readings, alert_threshold):
    plt.figure()

    sample_numbers = range(1, len(readings) + 1)

    plt.plot(
        sample_numbers,
        readings,
        marker="o",
        color="blue",
        label="Sensor Readings"
    )

    plt.axhline(
        y=alert_threshold,
        color="red",
        linestyle="--",
        label="Alert Threshold"
    )

    plt.title("Sensor Readings Over Time")
    plt.xlabel("Sample Number")
    plt.ylabel("Sensor Value")
    plt.legend()
    plt.grid(True)
    plt.show()


# Create a histogram
def plot_histogram(readings):
    plt.figure()

    plt.hist(
        readings,
        bins=5,
        color="skyblue",
        edgecolor="black"
    )

    plt.title("Sensor Readings Distribution")
    plt.xlabel("Sensor Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


# Get and validate user input
def get_user_input():
    sensor_type = input("Enter sensor type: ").strip()

    if not sensor_type:
        raise ValueError("Sensor type cannot be empty.")

    number_of_readings = int(input("Enter number of readings: "))
    min_value = float(input("Enter minimum value: "))
    max_value = float(input("Enter maximum value: "))
    alert_threshold = float(input("Enter alert threshold: "))

    if number_of_readings <= 0:
        raise ValueError("Number of readings must be greater than zero.")

    if not np.isfinite([min_value, max_value, alert_threshold]).all():
        raise ValueError("Sensor values must be finite numbers.")

    if min_value >= max_value:
        raise ValueError("Minimum value must be smaller than maximum value.")

    return (
        sensor_type,
        number_of_readings,
        min_value,
        max_value,
        alert_threshold
    )


# Save readings to CSV
def save_readings(readings, filename="sensor_readings.csv"):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["sample", "reading"])

            for i, reading in enumerate(readings, start=1):
                writer.writerow([i, reading])

        print("\nSensor readings saved to", filename)
        return True

    except OSError as error:
        print("Error saving CSV file:", error)
        return False


# Load readings from CSV
def load_readings(filename="sensor_readings.csv"):
    readings = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None or "reading" not in reader.fieldnames:
                raise ValueError("CSV file must contain a 'reading' column.")

            for row in reader:
                value = float(row["reading"])

                if not np.isfinite(value):
                    raise ValueError("CSV contains a non-finite sensor value.")

                readings.append(value)

        if not readings:
            raise ValueError("CSV file contains no readings.")

        print("\nSensor readings loaded from", filename)
        return readings

    except (OSError, ValueError, TypeError, csv.Error) as error:
        print("Error loading CSV file:", error)
        return None


# Analyze and visualize readings
def analyze_and_plot(readings, alert_threshold):
    print("\nSensor Readings:")

    for reading in readings:
        print(round(reading, 2))

    calculate_statistics(readings, alert_threshold)

    outliers = find_outliers(readings, alert_threshold)
    print("Outliers:", [round(value, 2) for value in outliers])

    plot_readings(readings, alert_threshold)
    plot_histogram(readings)


# Main program
def main():
    print("Welcome to Sensor Data Analysis Tool!")
    print("1. Generate new sensor readings")
    print("2. Load readings from CSV")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        try:
            (
                sensor_type,
                number_of_readings,
                min_value,
                max_value,
                alert_threshold
            ) = get_user_input()

            print("\nSensor Information:")
            print("Sensor Type:", sensor_type)
            print("Number of Readings:", number_of_readings)
            print("Minimum Value:", min_value)
            print("Maximum Value:", max_value)
            print("Alert Threshold:", alert_threshold)

            readings = generate_readings(
                number_of_readings,
                min_value,
                max_value
            )

            save_readings(readings)

            analyze_and_plot(readings, alert_threshold)

        except ValueError as error:
            print("Invalid input:", error)

    elif choice == "2":
        filename = input(
            "Enter CSV filename (press Enter for sensor_readings.csv): "
        ).strip()

        if not filename:
            filename = "sensor_readings.csv"

        readings = load_readings(filename)

        if readings is not None:
            try:
                alert_threshold = float(input("Enter alert threshold: "))

                if not np.isfinite(alert_threshold):
                    raise ValueError("Alert threshold must be a finite number.")

                analyze_and_plot(readings, alert_threshold)

            except ValueError as error:
                print("Invalid input:", error)

    else:
        print("Invalid choice! Please enter 1 or 2.")


# Start the program
if __name__ == "__main__":
    main()