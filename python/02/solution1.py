def main():
    with open("input.txt") as input:
        total = 0
        maximums = {"red": 12, "green": 13, "blue": 14}
        for game, line in enumerate(input):
            check = {}
            foundOver = False
            draws = line.split(":")[1].strip().split("; ")
            for draw in draws:
                colors = draw.split(', ')
                for color in colors:
                    hand = color.split()
                    check[hand[1]] = int(hand[0])
                for key in check:
                    if check[key] > maximums[key]:
                        foundOver = True
            if foundOver:
                continue                
            total += game + 1
        print(total)

if __name__ == "__main__":
    main()