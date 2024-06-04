 a = int(input("Enter Jug A Capacity: "))
    b = int(input("Enter Jug B Capacity: "))
    ai = int(input("Initially Water in Jug A: "))
    bi = int(input("Initially Water in Jug B: "))
    af = int(input("Final State of Jug A: "))
    bf = int(input("Final State of Jug B: "))
    print("List Of Operations You can Do:\n")
    print("1. Fill Jug A Completely")
    print("2. Fill Jug B Completely")
    print("3. Empty Jug A Completely")
    print("4. Empty Jug B Completely")
    print("5. Pour Jug A to Jug B")
    print("6. Pour Jug B to Jug A")
    while (ai != af or bi != bf):
        op = int(input("Enter the Operation: "))
        if (op == 1):
            ai = a
        elif (op == 2):
            bi = b
        elif (op == 3):
            ai = 0
        elif (op == 4):
            bi = 0
        elif (op == 5):
            t = min(ai, b - bi)
            ai -= t
            bi += t
        elif (op == 6):
            t = min(bi, a - ai)
            bi -= t
            ai += t
        else:
            print("Invalid input")
        print(f"Jug A: {ai} Litre, Jug B: {bi} Litre")