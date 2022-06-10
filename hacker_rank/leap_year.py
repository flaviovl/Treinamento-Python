# 3 condições para ano bissexto
# year % 4 == 0
# year % 100 != 0
# year % 400 == 0


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
