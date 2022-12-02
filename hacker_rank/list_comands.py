def run_command(cmd: str, args: list, list_int: list):
    match cmd:
        
        case "print":
            print(list_int)
        
        case "append":
            list_int.append(int(args[0]))
        
        case "insert":
            list_int.insert(int(args[0]), int(args[1]))
        
        case "sort":
            list_int.sort()
        
        case "reverse":
            list_int.reverse()
            
        case "pop":
            list_int.pop()

        case "remove":
            list_int.remove(int(args[0]))

        case _:
            print(f"Command invalid! {cmd}")


if __name__ == "__main__":
    n = int(input())
    list_int = []
    
    for _ in range(n):
        command, *arguments = input().split()
        run_command(command, arguments, list_int)
