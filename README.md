# Multi-Criteria Decision Analysis (MCDA) Script

## Overview

This Python script performs a Multi-Criteria Decision Analysis (MCDA) using the PROMETHEE II method. The analysis ranks various biometric modalities based on specific criteria (security, privacy, usability, and performance) with predefined weights. This particular script is tailored for a use case involving biometric modalities and their performance scores derived from specific sensors.

## Use Case

The script is designed to analyze and rank alternatives based on performance data provided in an input text file (`MCDA_alternatives.txt`). Each alternative represents a combination of biometric modalities, and their performance is evaluated against four criteria:
1. Security
2. Privacy
3. Usability
4. Performance

The weights assigned to these criteria are:
- Security: 0.20
- Privacy: 0.40
- Usability: 0.15
- Performance: 0.25

These weights and criteria reflect the specific priorities and requirements of the given use case.

## Requirements

- Python 3.x
- NumPy library

To install NumPy, you can use the following command:

pip install numpy

## Files
- MCDA_alternatives.txt: This file contains the alternatives and their performance scores.
- MCDA.py: The main Python script to perform the MCDA analysis.

## MCDA_alternatives.txt Format
The input file should have the following format:
<performance_score> <modality_1> <modality_2> ... <modality_n>

Example:
5 Facial_Features Iris
2 Eye_Blinking Keystroke_Dynamics
...

## Modifying the Script
### Updating Alternatives and Performance Scores
To use this script with different alternatives and performance scores, update the MCDA_alternatives.txt file with the new data. Ensure the format matches the example provided above.

### Adjusting Criteria Weights
To adjust the weights of the criteria, modify the criteria_weights dictionary in the script

## Running the Script
1. Place the MCDA_alternatives.txt file in the same directory as the script.
2. Execute the script: python3 MCDA.py

## Output
The script will print the ordered ranking of alternatives based on their net outranking flows. The output includes:

- Hardware input details.
- Weight inputs details.
- Ranked list of alternatives with their corresponding net outranking flows.

## Conclusion
This MCDA script is flexible and can be adapted to different use cases by modifying the input file and adjusting the weights. It provides a systematic way to evaluate and rank alternatives based on multiple criteria, ensuring informed decision-making.
