def get_coffee_type_size():
    time = 0
    dic1 = {'Put Water':15, 'Add Sugar':15, 'Mix Well':20, 'Add Coffee':2, 'Add Milk':4}
    dic2 = {'Put Water':20, 'Add Sugar':20, 'Mix Well':25, 'Add Coffee':15, 'Add Milk':0}
    type = input("Enter the type of coffee (B for Black and W for White): ")

    size = input("Is the cup size double? (Y/N): ")
    full_foam = input("Enter in full foam White coffee OR Black coffee: ")
    manual = input("Is the coffee manual? (Y/N): ")

    print("--------------------------------------")

    print(f"Operation\t\t\t\t{full_foam}")

    print("--------------------------------------")

    if type == "W":
        if size == "Y":
            for key, value in dic1.items():
                print(key, "\t\t\t\t", value * 1.5, "minutes")
                time = time+value*1.5
                if manual == "Y":
                    input()
        else:
            for key, value in dic1.items():
                print(key, "\t\t\t\t", value * 1.5, "minutes")
                time = time + value
                if manual == "Y":
                    input()
    elif type == "B":
        if size == "Y":
            for key, value in dic2.items():
                print(key, "\t\t\t\t", value * 1.5, "minutes")
                time = time+value*1.5
                if manual == "Y":
                    input()
        else:
            for key, value in dic2.items():
                print(key, "\t\t\t\t", value, "minutes")
                time = time + value
                if manual == "Y":
                    input()
    else:
        print("Invalid Input")

    print("--------------------------------------")

    print("Hurrah! Your coffee is ready in ",time,"minutes")

get_coffee_type_size()