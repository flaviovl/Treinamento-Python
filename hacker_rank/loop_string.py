def mount_string(n : int) -> str:
    string = ""
    for i in range(1, n+1):
        string += str(i)
    return string


if __name__ == '__main__':
    n = int(input())

    print(mount_string(n))
