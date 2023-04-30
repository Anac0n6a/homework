ROWS = 4
PLAYERS = 2


def typing_trainer(k, digits) -> int:
    dicts = {}
    for num in digits:
        dicts[num] = dicts.get(num, 0) + 1
    result = 0
    for num in dicts.values():
        if num <= k * PLAYERS:
            result += 1
    return result


def read_input():
    digits = ''
    k = int(input())
    for _ in range(ROWS):
        for c in input():
            if c.isdigit():
                digits += c
    return k, digits


def main():
    k, digits = read_input()
    result = typing_trainer(k, digits)
    print(result)


if __name__ == '__main__':
    main()
