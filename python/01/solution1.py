def main():
    with open("input.txt") as input:
        total  = 0
        for line in input:
            l = 0
            r = len(line) - 2
            lfound = rfound = False
            while (not lfound):
                if line[l].isdigit():
                    lfound = True
                    ldigit = line[l]
                l += 1
            while (not rfound):
                if line[r].isdigit():
                    rfound = True
                    rdigit = line[r]
                r -= 1
            total += int(ldigit + rdigit)
        print(total)
            

if __name__ == "__main__":
    main()