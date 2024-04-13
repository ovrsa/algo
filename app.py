from algo import sort

arr = [64, 34, 25, 12, 22, 11, 90]


def app(arr):
    sorted_arr = sort.gnome_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]
    

if __name__ == '__main__':
    app(arr)