def find_max_recursive(l):
    if len(l) == 1:
        return l[-1]
    
    max_v = find_max_recursive(l[1:])

    if l[0] > max_v:
        return l[0]
    else:
        return max_v
    
def find_max_iterative(l):
    max_v = 0
    for i in l:
        if i == l[0]:
            max_v = i
        else:
            if max_v < i:
                max_v = i
    return max_v


if __name__ == "__main__":
    l = list(map(int, input("리스트 입력 : ex 1,2,3 => ").split(",")))
    print(find_max_recursive(l))
    print(find_max_iterative(l))