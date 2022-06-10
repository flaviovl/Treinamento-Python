def sorted_grade(array: list):
    records_sorted = sorted(array, key=lambda x: (x[1], x[0]))

    last_grade = records_sorted[0]

    for n, x in enumerate(records_sorted[1:], start=1):
        if x[1] != last_grade[1]:
            return records_sorted[n:]
        else:
            last_grade = records_sorted[n]


if __name__ == '__main__':
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    # primeiro input() = é o do for _ in range(int(input()))
    # segundo input()  = é o primeiro da lista -> [input(), float(input())]
    # terceiro input() = é o segundo da lista  -> [input(), float(input())]
    records = [[input(), float(input())] for _ in range(int(input()))]
    
    records_sorted = sorted_grade(records)
    
    next_name = records_sorted[0][0]
    next_grade = records_sorted[0][1]
    
    print(next_name)
    for name, grade in records_sorted[1:]:
        if grade == next_grade:
            print(name)
