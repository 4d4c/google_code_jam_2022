def solution():
    return 0

def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        line_read = input()
        result = solution(*line_read.split(" "))

        print("Case #{}: {}".format(case_id, result))


if __name__ == '__main__':
    main()
