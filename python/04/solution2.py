def main():
    input = open("input.txt").read().splitlines()
    total = [1] * len(input)
    for i, line in enumerate(input):
        matches = 0
        nums = line.split(":")[1].strip().split("|")
        numsWin = nums[0].split()
        numsHave = nums[1].split()
        for num in numsHave:
            if num in numsWin:
                matches += 1
        for j in range(1, matches + 1):
            total[i + j] += 1 * total[i]

            
    print(sum(total))

if __name__ == "__main__":
    main()