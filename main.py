from numpy import *
from scipy.optimize import *
from fractions import Fraction
import math
import time

print("Ahoj! Tohle je chytrá iKalkulačka")
time.sleep(0.1)
if input("Pokud se chceš podívat na manuál, jdi na https://my-python-apps.weebly.com/manuals.html. Pro zjištění verze napište \"verze\", jinak stiskněte ENTER\n") == "verze":
    print("1.1")
time.sleep(0.1)

while True:
    choose_action = input("Vyberte si typ kalkulačky: \n 1. Kalkulačka rovnic \n 2. Kalkulačka zlomků \n 3. Kalkulačka procent \n 4. Kalkulačka alkoholu \n 5. Normální kalkulačka \n----------------------- \n")

    if choose_action == "1":
        def equationFunction(values):
            global LEFT_SIDES, RIGHT_SIDES
            x = values[0]
            if len(values) >= 2:
                y = values[1]
            if len(values) >= 3:
                z = values[2]
    
            output = []
            for i in range(len(values)):
                result = eval(LEFT_SIDES[i]) - eval(RIGHT_SIDES[i])
                output.append(result)
            return output

        numbers = ["První", "Druhá", "Třetí"]

        def round_half_up(n, decimals=0):
            multiplier = 10 ** decimals
            return math.floor(n*multiplier + 0.5) / multiplier

        while True:

            def askForEquations(amount):
                global LEFT_SIDES, RIGHT_SIDES
                for i in range(amount):
                    print("-----------------")
                    print("{} rovnice:".format(numbers[i-4+1]))
                    equation = input("Sem napište rovnici: ")
                    equation_split = equation.split("=")
                    leftSide = equation_split[0]
                    rightSide = equation_split[1]
                    LEFT_SIDES.append(leftSide)
                    RIGHT_SIDES.append(rightSide)

            LEFT_SIDES = []
            RIGHT_SIDES = []

            def squareRoot(amount):
                variables = "x", "y", "z"
                split = "x_split", "y_split", "z_split"
                for i in range(amount):
                    value_variables = roots[i]
                    variable_split = str(value_variables).split(".")
                    splited_variable = variable_split[1]
                    value_variables_rounded = round(value_variables,6)
                    value_variables_int = round(value_variables,0)
                    value_variables_rounded_split = str(value_variables_rounded).split(".")
                    value_variables_nondecimal = value_variables_rounded_split[0]
            
                    if len(splited_variable) >= 15 and value_variables_rounded != value_variables_int and round(value_variables**2) != 0:
                        value_variables_fraction = str(Fraction(value_variables).limit_denominator())
                        if i == 0:
                            print("---")
                        print(variables[i],"= odmocnina(", round(value_variables**2, 14), ") =", value_variables, "=", value_variables_fraction)
                        print("---")
                        i = i+1
                    else:
                        if i == 0:
                            print("---")
                        if round(value_variables, 13) == value_variables_rounded:
                            if value_variables_rounded == value_variables_int:
                                print(variables[i], "=", value_variables_nondecimal)
                            else:
                                print(variables[i], "=", value_variables_rounded)
                        elif round(value_variables, 13) != value_variables_rounded and value_variables != round(value_variables, 13):
                            value_variables_fraction = str(Fraction(value_variables).limit_denominator())
                            print(variables[i], "=", value_variables, "=", value_variables_fraction)
                        else:
                            print(variables[i], "=", value_variables)
                        print("---")
                        i = i+1

            def round_half_up(n, decimals=0):
                multiplier = 10 ** decimals
                return math.floor(n*multiplier + 0.5) / multiplier

            print("---------------------------------------")
            variablesAmount = int(input("Kolik proměnných rovnice má/mají (1-3)? \n"))
            if variablesAmount > 3 or variablesAmount <= 0: continue
            askForEquations(variablesAmount)

            rootsGuess = [1 for _ in range(variablesAmount)]
            roots = fsolve(equationFunction, rootsGuess)

            squareRoot(variablesAmount)

            if input("Pokud chcete vypočítat další rovnici, stiskněte ENTER. Napište \"stop\" pro ukončení kalkulačky rovnic: \n") == "stop":
                break

    if choose_action == "2":
        while True:
            def fraction_calculator():
                example = input("Sem napište příklad: ")
                solution_number = str(eval(example))
                solution_fraction = str(Fraction(solution_number).limit_denominator())
                if eval(solution_number) > 1:
                    split_solution_number = solution_number.split(".")
                    zero_point = "0."
                    number_and_fraction_nonsolve = zero_point + str(split_solution_number[1])
                    solution_fraction_2 = str(Fraction(number_and_fraction_nonsolve).limit_denominator())
                    solution_number_and_fraction = split_solution_number[0] + "+" + solution_fraction_2
                    print(example, "=", solution_fraction, "=", solution_number_and_fraction, "=", solution_number)
                else:
                    print(example, "=", solution_fraction, "=", solution_number)
            fraction_calculator()
            if input("Pokud chcete vypočítat další příklad, stiskněte ENTER. Napište \"stop\" pro ukončení kalkulačky zlomků: \n") == "stop":
                break

    if choose_action == "3":
        while True:
            def percents_calculator():
                if type_of_example == 1:
                    x = input("Kolik procent: ")
                    y = input("Z kolika: ")
                    solution_number = eval(y)/100*eval(x)
                    solution_fraction = str(Fraction(solution_number).limit_denominator())
                    print(x, "% from", y, "=", solution_number, "=", solution_fraction)
                elif type_of_example == 2:
                    x = input("Kolik je: ")
                    y = input("Z: ")
                    solution_number = 100/eval(y)*eval(x)
                    solution_fraction = str(Fraction(solution_number).limit_denominator())
                    print(x, "from", y, "=", solution_number, "%", "=", solution_fraction, "%")
                    
            type_of_example = int(input("Vyberte typ: \n 1. \"x\"% z \"y\" je: \n 2. Kolik procent je \"x\" z \"y\": \n"))
            if type_of_example > 3 or type_of_example <= 0: continue
            percents_calculator()
            if input("Pokud chcete vypočítat další příklad, stiskněte ENTER. Napište \"stop\" pro ukončení kalkulačky procent: \n") == "stop":
                break
        
    if choose_action == "4":
        while True:
            def kalkulačka_alkoholu():
                choose_action_2 = input("Vyberte si typ kalkulačky: \n 1. Kolik mám promile \n 2. Kolik můžu vypít \n-------------------- \n") 

                if choose_action_2 == "1":
                    objem = str(input("Objem vypitého alkoholu (ml): "))
                    pocent_alkoholu = str(input("Počet procent alkoholu: "))
                    váha = str(input("Kolik vážíte (kg): "))
                    pohlaví = input("Pohlaví: \n 1. Žena \n 2. Muž \n")
                    if pohlaví == "1":
                        konstanta_1 = str(0.6)
                    if pohlaví == "2":
                        konstanta_1 = 0.7
                    konstanta_2 = 0.8
                    hmotnost_mezivýpočet = str(eval(objem) * eval(pocent_alkoholu))
                    konstanta_3 = 100
                    hmotnost = str(eval(hmotnost_mezivýpočet) * eval(str(konstanta_2)) / eval(str(konstanta_3)))
                    promile_mezivýpočet = str(eval(váha) * eval(str(konstanta_1)))
                    promile = str(eval(hmotnost) / eval(promile_mezivýpočet))
                    print("\n--------")
                    print("Promile:", round(eval(promile), 2))
                    print("-------- \n")

                if choose_action_2 == "2":
                    max_promile = str(input("Maximální počet promile, kterého chci dosáhnout: "))
                    procent_alkoholu = str(input("Počet procent alkoholu: "))
                    váha = str(input("Kolik vážíte (kg): "))
                    pohlaví = input("Pohlaví: \n 1. Žena \n 2. Muž \n")
                    if pohlaví == "1":
                        konstanta_1 = 0.6
                    if pohlaví == "2":
                        konstanta_1 = 0.7
                    konstanta_2 = 0.8
                    konstanta_3 = 100
                    hmotnost_mezivýpočet = str(eval(váha) * eval(str(konstanta_1)))
                    hmotnost = str(eval(max_promile)*eval(hmotnost_mezivýpočet))
                    objem_mezivýpočet = str(eval(hmotnost) / eval(procent_alkoholu) / eval(str(konstanta_2)))
                    objem = str(eval(objem_mezivýpočet) * eval(str(konstanta_3)))
                    print("\n-------------")
                    print("Můžete vypít:", objem, "ml drinku")
                    print("------------- \n")

            kalkulačka_alkoholu()
            if input("Pokud chcete vypočítat další příklad, stiskněte ENTER. Napište \"stop\" pro ukončení kalkulačky alkoholu: \n") == "stop":
                break

    if choose_action == "5":
        while True:
            def calculator():
                example = input("Sem napište příklad: ")
                solution = str(eval(example))
                print(example, "=", solution)
            calculator()
            if input("Pokud chcete vypočítat další příklad, stiskněte ENTER. Napište \"stop\" pro ukončení kalkulačky: \n") == "stop":
                break

    if input("Pokud chcete vybrat jiný typ kalkulačky stiskněte ENTER. Napište \"stop\" pro ukončení aplikace: \n") == "stop":
            break
