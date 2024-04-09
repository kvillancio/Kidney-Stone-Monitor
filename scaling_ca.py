def scaling_Ca():
    option = "y"
    while option.lower() == "y":
        sex = input("Enter your sex (male or female): ")
        weight = float(input("Enter your weight (kg): "))
        print(" ")
        if sex == "male":
            Ca = (0.3119) / (0.05 * weight * 0.0205)
            if Ca<250:
                print(f"Your urine Ca^(2+) concentration is {Ca}. It is within the NORMAL range!")
            else:
                print(f"Your urine Ca^(2+) concentration is {Ca}. It is too HIGH!")
        elif sex == "female":
            Ca = (0.2495) / (0.05 * weight * 0.0205)
            if Ca<200:
                print(f"Your urine Ca^(2+) concentration is {round(Ca, 2)}. It is within the NORMAL range!")
            else:
                print(f"Your urine Ca^(2+) concentration is {round(Ca, 2)}. It is too HIGH!")
        print(" ")
        option = input("Would you like to recalaculate your Ca^(2+) concentration and re-enter your information? \nIf yes, please enter y. If not, please enter n.\nKeep in mind, this new value will replace your old one. \nWould you like to continue?")

scaling_Ca()
