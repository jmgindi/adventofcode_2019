with open("12_02_01.txt", "r") as f:
    noun, verb = 0, 0
    answer = 19690720
    text = f.readlines()[0]
    while noun <= 99:
        while verb <= 99:
            l = [int(num) for num in text.split(",")]

            l[1], l[2] = noun, verb

            print(f"noun: {noun}\nverb: {verb}")

            position = 0

            while position < len(l):
                opcode = l[position]
                var_a = l[l[position + 1]]
                var_b = l[l[position + 2]]
                place_at = l[position + 3]
                if opcode == 1:
                    value = var_a + var_b
                    l[place_at] = value
                elif opcode == 2:
                    value = var_a * var_b
                    l[place_at] = value
                elif opcode == 99:
                    break
                else:
                    print("SOMETHING WENT WRONG, REFACTOR THE CODE!")
                    quit()

                position += 4
            
            if l[0] == answer:
                nv = noun * 100 + verb
                print(f"noun-verb combo that gives {answer} is {nv}")
                print(noun)
                print(verb)
                quit()
            verb += 1

        noun += 1
        verb = 0
