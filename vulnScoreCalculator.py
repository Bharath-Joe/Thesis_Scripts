import inquirer


def main():
    impact = calculateImpact()
    exploitability = calculateExploitability()
    print("Impact Score: " + str(round(impact, 2)))
    print("Exploitability Score: " + str(round(exploitability, 2)))
    print("Vulnerability Score: " + str(round(impact + exploitability, 2)))


def calculateExploitability():
    constant = 6.3053
    type_metric_values = {
        "Network": 0.85,
        "Adjacent": 0.62,
        "Local Software": 0.585,
        "Local Hardware": 0.55,
        "Physical": 0.20,
    }
    complexity_metric_values = {"Low": 0.77, "Medium": 0.605, "High": 0.44}
    questions = [
        inquirer.List(
            "type",
            message="What is the type of the vulnerability?",
            choices=["Network", "Adjacent", "Local Hardware", "Local Software", "Physical"],
        ),
        inquirer.List(
            "complexity",
            message="What is the complexity of the vulnerability?",
            choices=["Low", "Medium", "High"],
        ),
    ]
    answers = inquirer.prompt(questions)
    exploitability = (
        constant
        * type_metric_values[answers["type"]]
        * complexity_metric_values[answers["complexity"]]
    )
    return exploitability


def calculateImpact():
    constant = 6.42
    metric_values = {"None": 0, "Low": 0.22, "Medium": 0.39, "High": 0.56}
    questions = [
        inquirer.List(
            "Impact_C",
            message="What is the confidentiality impact?",
            choices=["None", "Low", "Medium", "High"],
        ),
        inquirer.List(
            "Impact_I",
            message="What is the integrity impact?",
            choices=["None", "Low", "Medium", "High"],
        ),
        inquirer.List(
            "Impact_A",
            message="What is the availability impact?",
            choices=["None", "Low", "Medium", "High"],
        ),
    ]
    answers = inquirer.prompt(questions)
    impact = constant * (
        1
        - (
            (1 - metric_values[answers["Impact_C"]])
            * (1 - metric_values[answers["Impact_I"]])
            * (1 - metric_values[answers["Impact_A"]])
        )
    )
    return impact


if __name__ == "__main__":
    main()
