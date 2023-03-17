# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    i = int(n / 2)
    while(i >= 0):
        left_child = i * 2 + 1
        right_child = i * 2 + 2
        minimum = i

        if left_child <= n - 1 and data[left_child] < data[minimum]:
            minimum = left_child

        if right_child <= n - 1 and data[right_child] < data[minimum]:
            minimum = right_child

        if minimum != i:
            data[i], data[minimum] = data[minimum], data[i]
            swaps.append((i, minimum))
            i = minimum
        else:
            i = i - 1

    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard

    FI = input()
    if "I" in FI:
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in FI:
        test = input()
        test_file = "test/" + test
        with open(test_file) as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    if len(swaps) < 4 * n:
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()
