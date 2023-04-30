#86779130 -id решения на контексте
ROWS = 4
PLAYERS = 2


def typing_trainer(keys: int, digits: str) -> int:
    dicts = {}
    for num in digits:
        dicts[num] = dicts.get(num, 0) + 1
    result = 0
    for num in dicts.values():
        if num <= keys * PLAYERS:
            result += 1
    return result

if __name__ == '__main__':
    keys = int(input())
    matrix = [i for i in range(4) for i in input().strip() if i.isdigit()]
    result = typing_trainer(keys, matrix)
    print(result)
