def avg_marks(array):
    # scores = list(map(float, array))
    scores = [float(x) for x in array]
    return sum(scores) / len(scores)


if __name__ == "__main__":
    students = {}
    for _ in range(int(input())):
        list_input = input().split()
        students[list_input[0]] = list_input[1:]
    
    student = input()
    x = avg_marks(students[student])
    print(f"{x:.2f}")


    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

    # print("{0:.2f}".format(sum(student_marks[query_name])/3))
    