def pH_calcium_values(pH_location, calcium_location):
    if pH_location == 0:
        pH = 5.0
    elif pH_location == 1:
        pH = 6.0
    elif pH_location == 2:
        pH = 6.5
    elif pH_location == 3:
        pH = 7.0
    elif pH_location == 4:
        pH = 7.5
    elif pH_location == 5:
        pH = 8.0
    elif pH_location == 6:
        pH = 8.5

    if pH_location==6:
        print("Your urine pH value is " + str(pH) + " or higher")
    elif pH_location==0:
         print("Your urine pH value is " + str(pH) + " or lower")
    else:
        print("Your urine pH value is " + str(pH))
    if pH < 6:
        print("Your pH is low.")
    else: 
        print("Your pH is normal.")
    
    if calcium_location == 0:
        ca = 0.1
    elif calcium_location == 1:
        ca = 2.5
    elif calcium_location == 2:
        ca = 5.0
    elif calcium_location == 3:
        ca = 7.5
    elif calcium_location == 4:
        ca = 10


    #get reference number from scaling function
    Ca_ref=scaling_Ca();
    
    print("Your urine calcium value is " + str(ca))
    if ca < Ca_ref:
        print("Your calcium is normal.")
    elif ca > Ca_ref:
        print("Your calcium is high.")


    return pH, ca

def scaling_Ca():
        sex = input("Enter your sex (male or female): ")
        weight = float(input("Enter your weight (kg): "))
        if sex == "male":
            Ca_ref = (0.3119) / (0.05 * weight * 0.0205)
        elif sex == "female":
            Ca_ref = (0.2495) / (0.05 * weight * 0.0205)
        print(Ca_ref)
        return Ca_ref
