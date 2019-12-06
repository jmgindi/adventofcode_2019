if __name__ == "__main__":
    with open("12_04_01.txt", "r") as f:
        rng = f.readline().split("-")

        pwds = []

        for pwd in range(int(rng[0]), int(rng[1])):
            lpwd = [char for char in str(pwd)]

            for num in lpwd:
                num = int(num)

            flag = 1
            
            for i in range(1, len(lpwd)):
                if lpwd[i] > lpwd[i - 1]:
                    pass
                elif lpwd[i] == lpwd[i - 1]:
                    flag = 2
                else:
                    flag = 0
                    break

            if flag == 2:
                pwds.append("".join(lpwd))

        print(pwds)
        print(len(pwds))