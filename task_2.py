def solution(printers):
    MAX_VALUE = 1000000

    for printer in printers:
        if sum(printer) < MAX_VALUE:
            return "IMPOSSIBLE"

    cyan = []
    magenta = []
    yellow = []
    black = []

    for printer in printers:
        cyan.append(printer[0])
        magenta.append(printer[1])
        yellow.append(printer[2])
        black.append(printer[3])


    all_mins = [min(cyan), min(magenta), min(yellow), min(black)]

    if sum(all_mins) == MAX_VALUE:
        return "{} {} {} {}".format(*all_mins)

    if sum(all_mins) < MAX_VALUE:
        return "IMPOSSIBLE"

    result = [0, 0, 0, 0]
    for index, color in enumerate(all_mins):
        result[index] = color
        if sum(result) == MAX_VALUE:
            return "{} {} {} {}".format(*result)
        if sum(result) > MAX_VALUE:
            result[index] = MAX_VALUE - sum(result[:index])
            return "{} {} {} {}".format(*result)


def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        printers = [[] for _ in range(3)]
        for i in range(3):
            printers[i] = [int(x) for x in input().split(" ")]

        result = solution(printers)

        print("Case #{}: {}".format(case_id, result))


if __name__ == '__main__':
    main()
