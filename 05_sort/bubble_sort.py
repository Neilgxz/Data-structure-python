def bubble_sort(alist):
    count = len(alist) - 1
    while count > 0:
        lastexchangeindex = 0
        for i in range(count):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                lastexchangeindex = i
        count = lastexchangeindex

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)