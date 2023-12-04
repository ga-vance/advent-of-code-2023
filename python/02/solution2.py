def main():
    with open("input.txt") as input:
        total = 0
        for game, line in enumerate(input):
            maximums = {"red": 0, "green": 0, "blue": 0}
            check = {}
            draws = line.split(":")[1].strip().split("; ")
            for draw in draws:
                colors = draw.split(', ')
                for color in colors:
                    hand = color.split()
                    check[hand[1]] = int(hand[0])
                for key in check:
                    maximums[key] = max(maximums[key], check[key])
            power = 1
            for key in maximums:
                power *= maximums[key] 
            total += power
        print(total)

if __name__ == "__main__":
    main()