# Imtiaz Caspian
# Insertation Sort
# O(n^2)
def insertation_sort(li):
    length = len(li)
    for i in range(1, length):
        key = li[i]
        j = i - 1
        while j >= 0 and li[j] > li[j + 1]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = key

def print_li(li):
    print('<-- PRINTING THE LIST -->')
    for items in li:
        print(f'{items} ', end='')
    print()

def main():
    li = [33, 11, 22, 66, 44, 55]
    print_li(li)
    insertation_sort(li)
    print_li(li)

if __name__ == '__main__':
    main()