import numpy as np

criteria_weights = {
    "security": 0.20,
    "privacy": 0.40,
    "usability": 0.15,
    "performance": 0.25,
}


def main():

    analysis_scores = {
        "Facial_Features": [5.627, 9, 4.12],
        "Blurry_Facial_Features": [5.254, 1, 4.12],
        "Eye_Movement": [5.254, 3, 4.12],
        "Eye_Blinking": [5.254, 2, 4.12],
        "Iris": [5.254, 8, 4.12],
        "Ear": [5.254, 7, 4.12],
        "Retina": [5.254, 8, 4.12],
        "Keystroke_Dynamics": [5.738, 6, 1],
        "Stylometry_Dynamics": [5.738, 5, 1],
    }

    # Step 1: Parse the text file
    file_path = "MCDA_alternatives.txt"
    with open(file_path, "r") as file:
        text_data = file.read()

    alternatives_performance, alternatives = setAlternatives(text_data)
    (
        security_scores,
        privacy_scores,
        usability_scores,
        performance_scores,
    ) = createMatrix(alternatives_performance, analysis_scores)

    normalized_security_scores = non_beneficial_normalize(security_scores)
    normalized_privacy_scores = non_beneficial_normalize(privacy_scores)
    normalized_usability_scores = non_beneficial_normalize(usability_scores)
    normalized_performance_scores = non_beneficial_normalize(performance_scores)

    matrix = pariwiseComparisons(
        normalized_security_scores,
        normalized_privacy_scores,
        normalized_usability_scores,
        normalized_performance_scores,
    )

    leaving_flows, entering_flows = calculate_flows(matrix)
    net_flows = calculate_net_flows(leaving_flows, entering_flows)
    ordered_net_flows = dict(
        sorted(net_flows.items(), key=lambda item: item[1], reverse=True)
    )
    print("Hardware Input: Mac G5 webcam & Acer Wireless Keyboard SK-9662")
    print("Weight Inputs:" + str(criteria_weights))
    for key in ordered_net_flows:
        print(key, alternatives[key-1], ordered_net_flows[key])


def setAlternatives(text_data):
    alternatives_performance = {}
    alternatives = []
    for line in text_data.strip().split("\n"):
        score, *modalities = line.split()
        performance_score = float(score)
        modalities = tuple(set(modalities))
        alternatives.append(modalities)
        alternatives_performance[modalities] = performance_score
    return alternatives_performance, alternatives


def createMatrix(alternatives, analysis_scores):
    security_scores = []
    privacy_scores = []
    usability_scores = []
    performance_scores = []
    for modalities, performance_score in alternatives.items():
        max_security = max(analysis_scores[modality][0] for modality in modalities)
        max_privacy = max(analysis_scores[modality][1] for modality in modalities)
        max_usability = max(analysis_scores[modality][2] for modality in modalities)
        security_scores.append(max_security)
        privacy_scores.append(max_privacy)
        usability_scores.append(max_usability)
        performance_scores.append(performance_score)
    return (
        security_scores,
        privacy_scores,
        usability_scores,
        performance_scores,
    )


def non_beneficial_normalize(scores):
    new_scores_list = []
    minimum = min(scores)
    maximum = max(scores)
    for score in scores:
        new_scores_list.append((maximum - score) / (maximum - minimum))
    return new_scores_list


def beneficial_normalize(scores):
    new_scores_list = []
    minimum = min(scores)
    maximum = max(scores)
    for score in scores:
        new_scores_list.append((score - minimum) / (maximum - minimum))
    return new_scores_list


def calculate_difference(value1, value2):
    return max(0, value1 - value2)


def pariwiseComparisons(
    security_values, privacy_values, usability_values, performance_values
):
    matrix = np.full((11, 11), 0.0)
    for i in range(len(security_values)):
        for j in range(len(security_values)):
            if i != j:
                security_difference = calculate_difference(
                    security_values[i], security_values[j]
                )
                privacy_difference = calculate_difference(
                    privacy_values[i], privacy_values[j]
                )
                usability_difference = calculate_difference(
                    usability_values[i], usability_values[j]
                )
                performance_difference = calculate_difference(
                    performance_values[i], performance_values[j]
                )
                aggregated_value = (
                    security_difference * criteria_weights["security"]
                    + privacy_difference * criteria_weights["privacy"]
                    + usability_difference * criteria_weights["usability"]
                    + performance_difference * criteria_weights["performance"]
                )
                # print(
                #     "A" + str(i + 1) + "-" "A" + str(j + 1),
                #     security_difference * criteria_weights["security"],
                #     privacy_difference * criteria_weights["privacy"],
                #     usability_difference * criteria_weights["usability"],
                #     performance_difference * criteria_weights["performance"],
                #     aggregated_value,
                # )
                
                matrix[i, j] = aggregated_value
        # print()
    np.set_printoptions(precision=4)
    matrix_str = np.array2string(matrix, precision=4, max_line_width=np.inf)

    # print(matrix_str)
    return matrix


def calculate_flows(matrix):
    row_sums = np.sum(matrix, axis=1)
    col_sums = np.sum(matrix, axis=0)
    leaving_flows = row_sums / (matrix.shape[1] - 1)
    entering_flows = col_sums / (matrix.shape[0] - 1)
    # print("Leaving Flow:", leaving_flows)
    # print("Entering Flow:", entering_flows)
    return leaving_flows, entering_flows


def calculate_net_flows(leaving, entering):
    net_outranking_flows = {}
    for i in range(len(leaving)):
        net_outranking_flows[i + 1] = leaving[i] - entering[i]
    # print(net_outranking_flows)
    return net_outranking_flows


if __name__ == "__main__":
    main()
