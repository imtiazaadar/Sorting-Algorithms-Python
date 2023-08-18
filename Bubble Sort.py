# Imtiaz Caspian
# Bubble Sort
# O(n^2)
def swap(li, val1, val2):
    temp = li[val1]
    li[val1] = li[val2]
    li[val2] = temp

def bubble_sort(li):
    for i in range(0, len(li) - 1):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                swap(li, j, j + 1)

def print_li(li):
    print('<-- PRINTING LIST -->')
    for items in li:
        print(f'{items} ', end='')
    print()

def main():
    li = [20, 10, 30, 40, 70, 50, 90, 80]
    print_li(li)
    bubble_sort(li)
    print_li(li)

if __name__ == '__main__':
    main()