def main():
    total = 0
    schematic = open("input.txt").read().splitlines()
    for i, row in enumerate(schematic):
        for j, char in enumerate(row):
            if char != "*":
                continue
            coords = set()

            for r in [i - 1, i, i + 1]:
                for c in [j - 1, j, j + 1]:
                    if r < 0 or r >= len(schematic) or c < 0 or c >= len(schematic[r]) or not schematic[r][c].isdigit():
                        continue
                    while c > 0 and schematic[r][c - 1].isdigit():
                        c -= 1
                    coords.add((r,c))
            if len(coords) != 2:
                continue

            nums = []
            
            for r, c in coords:
                num = ""
                while c < len(schematic[r]) and schematic[r][c].isdigit():
                    num += schematic[r][c]
                    c += 1
                nums.append(int(num))
            total += nums[0] * nums[1]
    print(total)

if __name__ == "__main__":
    main()