def choose_pivot(opt, arr, start, end):
    if opt == 1:
        return start
    if opt == 2:
        return end
    if opt == 3:
        half = start + (end - start) // 2
        if arr[start] < arr[half]: #start < half
            if arr[start] < arr[end]:  #start < end
                if arr[end] < arr[half]: # start <end < half
                    return end
                else: # start <half < end
                    return half
            else:
                return start # end < start < half
        else: # half < start
            if arr[start] < arr[end]: # half < start < end
                return start
            else:
                if arr[end] < arr[half]:
                    return half
                else:
                    return end


def partition(arr, start, end, opt):
    pivot_pos = choose_pivot(opt, arr,start,end)
    arr[start], arr[pivot_pos] = arr[pivot_pos], arr[start]
    pivot = arr[start]
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return i - 1

def quicksort(arr, start, end, sum, opt):
    if end - start < 1:
        return sum
    pivot_pos = partition(arr, start, end, opt)
    sum += quicksort(arr, start, pivot_pos - 1, pivot_pos - start + 1, opt)
    sum += quicksort(arr, pivot_pos + 1, end, end - pivot_pos - 1, opt)
    return sum

with open("quicksort.txt") as f:
     content = list(map(lambda x: int(x), f.readlines()))

l1 = content[:]
l2 = content[:]
l3 = content[:]
last = len(content) - 1
output = quicksort(l1, 0, last, 0, 1)
print(l1)
print(output)

output = quicksort(l2, 0, last, 0, 2)
print(l2)
print(output)

output = quicksort(l3, 0, last, 0, 3)
print(l3)
print(output)
# print(content)

