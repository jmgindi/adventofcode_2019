def find_intersections(grid):
    intersections = []
    for row_f in range(len(grid)):
        for col_f in range(len(grid[0])):
            if "ab" in grid[row_f][col_f]:
                intersections.append((row_f, col_f))
    return intersections

def expand_grid(grid, direction):
    if direction == "U":
        grid.insert(0, ["" for i in grid[0]])

    if direction == "D":
        grid.append(["" for i in grid[0]])

    if direction == "L":
        for row_f in grid:
            row_f.insert(0, "")

    if direction == "R":
        for row_f in grid:
            row_f.append("")

def build_instruction(instruction, grid, letter, row, col):
    direction = instruction[0]
    dis = int("".join(instruction[1:]))
    for i in range(dis):
        if direction == "U":
            row -= 1
            if row >= 0:
                grid[row][col] += letter
            else:
                expand_grid(grid, direction)
                row = 0
                grid[row][col] += letter
        if direction == "D":
            row += 1
            if row < len(grid):
                grid[row][col] += letter
            else:
                expand_grid(grid, direction)
                row = len(grid) - 1
                grid[row][col] += letter
        if direction == "L":
            col -= 1
            if col >= 0:
                grid[row][col] += letter
            else:
                expand_grid(grid, direction)
                col = 0
                grid[row][col] += letter
        if direction == "R":
            col += 1
            if col < len(grid[row]):
                grid[row][col] += letter
            else:
                expand_grid(grid, direction)
                col = len(grid[row]) - 1
                grid[row][col] += letter

    return row, col

def build_wire(wire, grid, letter):
    row, col = 0, 0

    ## find center point
    for row_f in grid:
        if "x" in row_f:
            for num in row_f:
                if num == "x":
                    break
                else:
                    col += 1
            break
        else:
            row += 1

    ## build instructions
    for instruction in wire:
        row, col = build_instruction(instruction, grid, letter, row, col)


if __name__ == "__main__":
    grid = [["" for i in range(10001)] for j in range(10001)]
    grid[5001][5001] = "x"

    with open("12_03_01.txt", "r") as f:
        wire_a, wire_b = f.readline().split(","), f.readline().split(",")

        print(f"wire a is: {wire_a}")
        build_wire(wire_a, grid, "a")
        print(f"wire a complete:\n\t{wire_a}")

        print(f"wire b is: {wire_b}")
        build_wire(wire_b, grid, "b")
        print(f"wire b complete:\n\t{wire_b}")

        intersections = find_intersections(grid)

        ## find center point
        row, col = 0, 0
        for row_f in grid:
            if "x" in row_f:
                for num in row_f:
                    if num == "x":
                        break
                    else:
                        col += 1
                break
            else:
                row += 1

        man_dists = []

        for intset in intersections:
            r = abs(row - intset[0])
            c = abs(col - intset[1])
            d = r + c
            man_dists.append(d)
        
        man_dists.sort()

        print(f"the closest intersection to the center is {man_dists[0]}")
