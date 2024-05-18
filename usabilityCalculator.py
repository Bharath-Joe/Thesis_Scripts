def main():
    options = {
        "S": 1.0,
        "M": 1.5,
        "D": 3.0,
        "E": 5.0,
    }
    factors = ["D", "S", "S", "M", "S"]
    factor_num = []
    for factor in factors:
        factor_num.append(options[factor])
    maximum = max(factor_num)
    length = len(factors)
    total = sum(factor_num)
    if length == 1:
        score = maximum
    else:
        score = maximum + ((total-maximum) / (length - 1))
    print("Usability Score: " + str(score))

if __name__ == "__main__":
    main()