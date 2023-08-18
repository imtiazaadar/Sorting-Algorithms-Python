# Imtiaz Caspian
# Heap Sort
# O(nlogn)
import heapq
def heap_sort(li):
    heapq.heapify(li)
    result = []
    while li:
        result.append(heapq.heappop(li))

def print_li(li):
    print('<<-- PRINTING THE LIST -->>')
    for items in li:
        print(f'{items} ', end='')
    print()

def main():
    li = [44, 11, 22, 99, 88, 66, 77, 122, 111]
    print_li(li)
    heap_sort(li)
    print_li(li)