with open("12_02_01.txt", "r") as f:
    text = f.readlines()[0]
    l = [int(num) for num in text.split(",")]

    print(f"before restoration:\n\n{l}")

    l[1], l[2] = 12, 2

    print(f"after restoration:\n\n{l}")

    position = 0

    while position < len(l):
        print(f"position is {position}")
        opcode = l[position]
        var_a = l[l[position + 1]]
        var_b = l[l[position + 2]]
        place_at = l[position + 3]
        if opcode == 1:
            print(f"adding {var_a} + {var_b}")
            value = var_a + var_b
            print(f"placing {value} at position {place_at}")
            l[place_at] = value
        elif opcode == 2:
            print(f"multiplying {var_a} * {var_b}")
            value = var_a * var_b
            print(f"placing {value} at position {place_at}")
            l[place_at] = value
        elif opcode == 99:
            print("opcode is 99, exiting...")
            break
        else:
            print("SOMETHING WENT WRONG, REFACTOR THE CODE!")
            quit()

        print(l)

        position += 4

    
    print(l[0])