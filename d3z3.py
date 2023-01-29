


language = str(input("podaj jezyk (en/pl): "))
if language == "pl":
    var1 = input("podaj var1: ")
    var2 = input("podaj var2: ")
    print("And (var1 and var2):", "PRAWDA" if var1 and var2 else "FAŁSZ")
    print("Or (var1 or var2):", "PRAWDA" if var1 or var2 else "FAŁSZ")
    print("Not (not var1):", "PRAWDA" if not var1 else "FAŁSZ")
    print("Not (not var2):", "PRAWDA" if not var2 else "FAŁSZ")
    print("     Operaca logiczna:")
    print("And (var1 and var2):", var1 and var2)
    print("Or (var1 or var2):", var1 or var2)
    print("Not (not var1):", not var1)
    print("Not (not var2):", not var2)
elif language == "en":
    var1 = input("enter first var1: ")
    var2 = input("enter secound var2: ")
    print("And (var1 and var2):", "TRUE" if var1 and var2 else "FALSE")
    print("Or (var1 or var2):", "TRUE" if var1 or var2 else "FALSE")
    print("Not (not var1):", "TRUE" if not var1 else "FALSE")
    print("Not (not var2):", "TRUE" if not var2 else "FALSE")
    print("     Logic operations:")
    print("And (var1 and var2):", var1 and var2)
    print("Or (var1 or var2):", var1 or var2)
    print("Not (not var1):", not var1)
    print("Not (not var2):", not var2)

