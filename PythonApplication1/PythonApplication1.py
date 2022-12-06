print("Welcome to the Basic Insurance Calculator.")
print("This Calculator has the Suggestions module installed.")

con = True
name = None
rounded_bmi = None
smoker = None

def calculator():

    print("To start, please enter name of person to be assessed. Please only use numbers for data after name.")

    name = input("Enter name: ")

    valid_age = False

    while not valid_age:
        
        try:
            age = int(input("Enter age (in years): "))
        except:
            print("Age cannot have alphabets or symbols. Please try again.")
            valid_age = False
            continue

        if age >= 0:
            valid_age = True
        else:
            print("Age cannot be a negative value. Please try again.")
            valid_age = False

    valid_sex = False

    while not valid_sex:
        sex = input("Enter biological sex - 0 if female, 1 if male: ")
        if sex == "0":
            print("Acknowledged that " + name + " is biologically a female.")
            sex = 0
            valid_sex = True
        elif sex == "1":
            print("Acknowledged that " + name + " is biologically a male.")
            sex = 1
            valid_sex = True
        else:
            print("Please only enter 0 or 1.")
            valid_sex = False

    valid_height = False

    while not valid_height:
        try:
            height = float(input("Enter height (in cm): "))
        except:
            print("Height cannot have any alphabets or symbols other than decimal point. Please try again.")
            valid_height = False
            continue

        if height > 0:
            valid_height = True
        else:
            print("Age cannot be a negative value or zero. Please try again.")
            valid_height = False

    valid_weight = False

    while not valid_weight:
        try:
            weight = float(input("Enter weight (in kg): "))
        except:
            print("Weight cannot have any alphabets or symbols other than decimal point. Please try again.")
            valid_biodata = False
            continue   

        if weight > 0:
            valid_weight = True
        else:
            print("Age cannot be a negative value or zero. Please try again.")
            valid_weight = False

    bmi = float(weight / ((height/100) ** 2))
    rounded_bmi = round(bmi, 1)
    print("BMI calculated. The BMI of " + name + " is " + str(rounded_bmi) + ".")

    valid_children = False
        
    while not valid_children:

        try:
            num_of_children = int(input("Enter number of children " + name + " has: "))
        except:
            print("Number of children cannot have alphabet or symbols, or cannot be a decimal. Please try again.")
            valid_children = False
            continue

        if num_of_children >= 0:
            valid_children = True
        else:
            print("Number of children cannot be a negative value. Please try again.")
            valid_children = False
        
    valid_smoker = False

    while not valid_smoker:
        smoker = input("Is " + name + " a smoker? 0 if no, 1 if yes: ")
        if smoker == "0":
            print("Acknowledged that " + name + " does not smoke.")
            smoker = 0
            valid_smoker = True
        elif smoker == "1":
            print("Acknowledged that " + name + " is a smoker.")
            smoker = 1
            valid_smoker = True
        else:
            print("Please only enter 0 or 1.")

    print("Data collection complete.")

    insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 *smoker - 12500
    rounded_insurance = round(insurance_cost, 2)
        
    if rounded_insurance <= 0:
        print("According to the calculator, " + name + " does not need to pay for insurance due to optimal conditions.")
    else:
        print("According to the calculator, the estimated insurance cost for " + name + " is " + str(rounded_insurance) + " dollars.")

    suggest = input("Would you like to know how to lower the cost " + name + " has to pay for insurance? Y for yes, other keys for no: ")
        
    suggest_bool = True
    if suggest == "Y" or suggest == "y":
        suggest_bool = True
    else:
        suggest_bool = False

    return name, rounded_bmi, smoker, suggest_bool

def suggestion(suggest_bool, name, rounded_bmi, smoker):
    if suggest_bool == True:
        print("Suggestions will be showed.")

        optimal_bmi = False
        optimal_smoke = False

        if rounded_bmi >= 30.0:
            print(name + " is classed as being obese. To lower insurance cost, consider losing significant amounts of weight.")
        elif rounded_bmi >= 25.0 and rounded_bmi < 30.0:
            print(name + " is classed as being overweight. To lower insurance cost, consider reducing weight to healthy levels.")
        elif rounded_bmi >= 18.5 and rounded_bmi < 25.0:
            print(name + " currently has a healthy BMI. There is no need to alter weight.")
            optimal_bmi = True
        else:
            print(name + "is underweight. Increasing weight does not further lower cost, but is important for " + name + " to remain healthy.")

        if smoker == 1:
            print("Smoking increases insurance cost. To lower cost, consider quitting.")
        else:
            print("Continue being a non-smoker to maintain insurance cost.")
            optimal_smoke = True

        if optimal_bmi == True and optimal_smoke == True:
            print(name + " currently has the optimal insurance cost.")
        else:
            print("Please refer to the previous statements to lower insurance cost.")

    elif suggest_bool == False:
        print("Suggestions will not be displayed.")

while con:
    name, rounded_bmi, smoker, suggest_bool = calculator()

    suggestion(suggest_bool, name, rounded_bmi, smoker)

    choice = str(input("Try again? Y for yes, other keys for no: "))

    if choice == "Y" or choice == "y":
        print("All data wiped - ready to calculate again.")
        con = True
    else:
        print("Thank you for using the Calculator. Shutting down.")
        con = False
