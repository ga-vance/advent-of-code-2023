def main():
    with open("input.txt") as input:
        total = 0
        for line in input:
            matches = 0
            nums = line.split(":")[1].strip().split("|")
            numsWin = nums[0].split()
            numsHave = nums[1].split()
            for num in numsHave:
               if num in numsWin:
                    matches += 1
            if matches > 0:
                total += 2 ** (matches - 1)
        print(total)
        
if __name__ == "__main__":
    main()