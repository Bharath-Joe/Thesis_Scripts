def main():
    # In this code, we assume the specific values actually apply to the system
    # In this code, the modality scores will be for a single modalality type.
    database_0 = {
        "General": [8.23, 3.17, 6.89, 2.58],
        "Specific": [7.45, 1.89, 4.76, 9.52, 2.67, 6.19],
        "Modality": {},
    }
    database_1 = {
        "General": [8.23, 3.17, 6.89, 2.58],
        "Specific": [],
        "Modality": {"f": 5.64},
    }
    database_2 = {
        "General": [4.65, 6.80, 5.22],
        "Specific": [5.12],
        "Modality": {"FF": [6.32]},
    }
    database_3 = {
        "General": [],
        "Specific": [],
        "Modality": {},
    }

    # Defined Dictionaries
    categories = ["General", "Specific", "Modality"]
    indicatorFunction = {"General": 1, "Specific": 1, "Modality": 1}
    weights = {
        "General": 0.20,
        "Specific": 0.45,
        "Modality": 0.35,
    }

    # Active Dictionary
    database = database_2

    # Weight normalization with modalities
    weight_active = 0
    # Weight normalization without modalities
    weight_active_without = 0
    # Initialize dictionary to store security scores for modalities,
    # which includes general and specific sensor vulns
    modalityScores = {}

    # Set weight_active and weight_active_without values
    # Set indicator function values
    # initialize modality score to zero
    for category in categories:
        if len(database[category]) > 0:
            if category == "Modality":
                for key in database[category]:
                    modalityScores[key] = 0
                weight_active_without -= weights[category]
            weight_active += weights[category]
            weight_active_without += weights[category]
        else:
            indicatorFunction[category] = 0
    score_without = 0
    # Calculate Score with and without individual Modalities
    for category in categories:
        if len(database[category]) == 0 or category == "Modality":
            average = 0
        else:
            average = sum(database[category]) / len(database[category])
        temp = weights[category] * average * indicatorFunction[category]
        score_without += temp  # Security score without modality vuln scores
        # Logic to handle how to calculate each modality security score
        if category == "Modality" and len(database[category]) != 0:
            for modality in database[category]:
                average = sum(database[category][modality]) / len(
                    database[category][modality]
                )
                temp = weights[category] * average * indicatorFunction[category]
                modalityScores[modality] = (temp + score_without) / weight_active
    if weight_active_without == 0:
        print("All Other Modalities Security Score: " + str(score_without))
    else:
        score_without = score_without / weight_active_without
        print("All Other Modalities Security Score: " + str(score_without))
    for modality in modalityScores:
        print(f"{modality} Modality Security Score: {modalityScores[modality]}")


if __name__ == "__main__":
    main()
