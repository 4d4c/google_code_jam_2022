def solution(number_of_dices, dices):
    dices.sort(reverse=True)

    len_count = number_of_dices
    for len_count in range(number_of_dices, 1, -1):
        tmp_len_count = len_count
        for dice in dices:
            if tmp_len_count > dice:
                break
            tmp_len_count -= 1
        else:
            return len_count
    return len_count

def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        number_of_dices = int(input())
        dices = [int(x) for x in input().split(" ")]
        result = solution(number_of_dices, dices)

        print("Case #{}: {}".format(case_id, result))


if __name__ == '__main__':
    main()