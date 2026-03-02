def quick_sort(data):
    if len(data) <=1:
        return data
    else:
        pivot=data[0]
        lesser=[x for x in data[1:] if x<=pivot]
        greater=[x for x in data[1:] if x>=pivot]

        return quick_sort(lesser)+[pivot]+quick_sort(greater)






l=[53,11,72,68,41,25,18,37,44,80]
print(quick_sort(l))


