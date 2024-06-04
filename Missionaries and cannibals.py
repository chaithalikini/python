print("Boat can carry two people at a time")
print("If number of cannibals is greater than number of saints at any bank, it terminates")
S = int(input("Enter the total number of saints: "))
C = int(input("Enter the total number of cannibals: "))
Si = int(input("Enter the initial number of saints in the boat: "))
Ci = int(input("Enter the initial number of cannibals in the boat: "))
boat = 'A'
error_occurred = False
while (S > 0 or C > 0):
    print(f"A: {S} SAINTS, {C} CANNIBALS \nB: {Si} SAINTS, {Ci} CANNIBALS \nBoat: {boat}\n")
    if boat == 'A':
        SA = int(input("Enter the number of saints in the boat (from river bank A): "))
        CA = int(input("Enter the number of cannibals in the boat (from river bank A): "))
        if SA + CA > 2:
            print("Error: Boat can carry only two people at a time")
            error_occurred = True
            break
        if (S - SA < C - CA and S - SA > 0) or (Si + SA < Ci + CA and Si + SA > 0):
            print("Error: Number of cannibals cannot be greater than number of saints")
            error_occurred = True
            break
        S -= SA
        C -= CA
        Si += SA
        Ci += CA
        boat = 'B'
    else:
        SB = int(input("Enter the number of saints in the boat (from river bank B): "))
        CB = int(input("Enter the number of cannibals in the boat (from river bank B): "))
        if SB + CB > 2:
            print("Error: Boat can carry only two people at a time")
            error_occurred = True
            break
        if (Si - SB < Ci - CB and Si - SB > 0) or (S + SB < C + CB and S + SB > 0):
            print("Error: Number of cannibals cannot be greater than number of saints")
            error_occurred = True
            break
        S += SB
        C += CB
        Si -= SB
        Ci -= CB
        boat = 'A'
if not error_occurred:
    print(f"A: {S} SAINTS, {C} CANNIBALS \nB: {Si} SAINTS, {Ci} CANNIBALS \nBoat: {boat}\n")
    print("All saints and cannibals safely reached from river bank A to B.")