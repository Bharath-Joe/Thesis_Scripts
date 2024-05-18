import itertools

sensor_modalities = {
    "Camera": [
        "Facial Features",
        "Eye Movement",
        "Eye Blinking",
        "Iris",
        "Retina",
        "Ear",
    ],
    "IMD/WMD": ["BioAura", "Electroencephalograph", "Electrocardiography"],
    "Accelerometer": ["Acceleration Force - Motion", "Gait", "Vibrations"],
    "Gyroscope": ["Angular Velocity - Motion", "Gait"],
    "Magnetometer": ["Magnetic Force - Motion"],
    "Microphone": ["Proximity", "Breathing Patterns", "Speech Patterns"],
    "Keyboard": ["Keystroke Dynamics", "Stylometry Dynamics"],
    "Mouse": ["Mouse Dynamics", "Stylometry Dynamics"],
    "Touch Screen": ["Touch Dynamics", "Stylometry Dynamics"],
    "Ambient Light Sensor": ["Light Conditions"],
    "Pressure Sensors": ["Seated Posture Pattern"],
}

def main(sensors):
    sensor_combinations = []
    for sensor in sensors:
        modalities = list(set(sensor_modalities.get(sensor, [])))  # Remove duplicates
        if modalities:
            sensor_combinations.append(modalities)
    combinations = list(itertools.product(*sensor_combinations))
    unique_combinations = list(set(combinations))  # Remove duplicate combinations
    print(unique_combinations)
    print(len(unique_combinations))


if __name__ == "__main__":
    main(["Camera", "Accelerometer", "Gyroscope", "Touch Screen"])


if __name__ == "__main__":
    main(["Accelerometer", "Gyroscope", "Touch Screen"])
