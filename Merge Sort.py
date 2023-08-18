# Imtiaz Caspian
# Merge Sort
# O (nlogn)
def merge(li, left, mid, right):
    size_1 = mid - left + 1
    size_2 = right - mid
    li1 = [0] * size_1
    li2 = [0] * size_2
    for index in range(size_1):
        li1[index] = li[index + left]
    for index in range(size_2):
        li2[index] = li[index + mid + 1]
    ind1, ind2, k = 0, 0, left
    while ind1 < size_1 and ind2 < size_2:
        if li1[ind1] <= li2[ind2]:
            li[k] = li1[ind1]
            k += 1
            ind1 += 1
        else:
            li[k] = li2[ind2]
            k += 1
            ind2 += 1
    while ind1 < size_1:
        li[k] = li1[ind1]
        k += 1
        ind1 += 1
    while ind2 < size_2:
        li[k] = li2[ind2]
        k += 1
        ind2 += 1

def divide(li, left, right):
    if left < right:
        mid = left + (right - left) // 2
        divide(li, left, mid)
        divide(li, mid + 1, right)
        merge(li, left, mid, right)

def print_list(li):
    print('<-- PRINTING THE LIST -->')
    for items in li:
        print(f'{items} ', end='')
    print()

if __name__ == '__main__':
    li = [45, 25, 55, 65, 15, 105, 95]
    print_list(li)
    divide(li, 0, len(li) - 1)
    print_list(li)