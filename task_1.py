from ossaudiodev import control_labels


def solution(rows, columns):
    card = ""

    for row_count in range(0, int(rows) * 2 + 1):
        for col_count in range(0, int(columns) * 2 + 1):
            if row_count < 2 and col_count < 2:
                card += "."
                continue

            if col_count % 2 == 0:
                if row_count % 2 == 0:
                    card += "+"
                else:
                    card += "|"
            else:
                if row_count % 2 == 0:
                    card += "-"
                else:
                    card += "."

        card += "\n"

    return card

def main():
    number_of_test_cases = int(input())

    for case_id in range(1, number_of_test_cases + 1):
        line_read = input()
        result = solution(*line_read.split(" "))

        print("Case #{}:\n{}".format(case_id, result.strip()))


if __name__ == '__main__':
    main()
