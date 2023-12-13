def main():
    with open('input.txt') as input:
        steps, _, *rest = input.read().splitlines()
    map = {}
    for line in rest:
        node, neighbors = line.split(" = ")
        map[node] = neighbors[1:-1].split(", ")
    numSteps = 0
    currNode = "AAA"
    while currNode != "ZZZ":
        nextStep = steps[numSteps % len(steps)]
        numSteps += 1
        currNode = map[currNode][0 if nextStep == "L" else 1]
    print(numSteps)

if __name__ == '__main__':
    main()