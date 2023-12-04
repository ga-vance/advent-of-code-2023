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
                for i, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[l:].startswith(val):
                        lfound = True
                        ldigit = str(i + 1)
                        break
                l += 1
            while (not rfound):
                if line[r].isdigit():
                    rfound = True
                    rdigit = line[r]
                for i, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[r:].startswith(val):
                        rfound = True
                        rdigit = str(i + 1)
                        break
                r -= 1
            total += int(ldigit + rdigit)
        print(total)
            

if __name__ == "__main__":
    main()