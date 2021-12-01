"""
Name: Matt Stewart
lab13.py

I'll admit, my brain is not here today. I know the first doesn't work, I'm just done for the day. Sorry >_>
"""

#    x = [1, 3, 4, 9, 14]
def is_in_binary(search_val, values):
    mid = values[len(values) // 2]
    while search_val != mid and len(values) != 1:
        if search_val > mid:
            values = values[:mid]
        else:
            values = values[mid+1:]
        mid = values[len(values) // 2]
    if mid == search_val:
        return True
    else:
        return False



def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def rect_sort(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    for i in range(len(areas)):
        values[i] = d[i]


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p2.getX()-p1.getX())
    h = abs(p2.getY()-p1.getY())
    return w*h


def trade_alert(filename):
    infile = open(filename, 'r')
    data = infile.read().split()
    time = 0
    for i in data:
        time += 1
        if int(i) > 830:
            print("At " + str(time) + "seconds, the volume exceeded 830!!!")
        elif int(i) > 500 and int(i) <= 830:
            print("At " + str(time) + "seconds, the volume exceeded 500.")


def main():
    #is_in_binary(search_val, values)
    #selection_sort(values)
    #rect_sort(values)
    #trade_alert("trades.txt")
    pass


main()
