# Imtiaz Caspian
# Quick Sort
# O (nlogn)
def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp

def partition(li, low, high):
    i = low - 1
    pivot = li[high]
    for j in range(high):
        if li[j] < pivot:
            i += 1
            swap(li, i, j)
    swap(li, i + 1, high)
    return i + 1

def quick_sort(li, low, high):
    if low < high:
        part = partition(li, low, high)
        print(f'PART = {part}')
        quick_sort(li, low, part - 1)
        quick_sort(li, part + 1, high)

def print_li(li):
    print('<-- PRINTING ITEMS -->')
    for items in li:
        print(f'{items} ', end='')
    print()
if __name__ == '__main__':
    li = [55, 45, 65, 75, 222, 122]
    print_li(li)
    quick_sort(li, 0, len(li) - 1)
    print_li(li)