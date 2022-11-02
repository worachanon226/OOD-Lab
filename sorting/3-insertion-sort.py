def insertion(arr, l):
    if l <= 1:
        return
    insertion(arr, l - 1)
    end = arr[l - 1]
    
    i = l - 2
    while(i >= 0 and arr[i] > end):

        arr[i+1] = arr[i]
        i = i - 1

    arr[i + 1] = end
    if len(arr[l:]) == 0:
        print(f'insert {end} at index {i+1} : {arr[:l]}\nsorted')
    else:
        print(f'insert {end} at index {i+1} : {arr[:l]} {arr[l:]}')
    return arr

inp = [int(i) for i in input("Enter Input : ").split()]
print(insertion(inp,len(inp)))