def quick_sort(data):
    if len(data)<1:
        return data
    else:
        pivot=data[0]
        lesser=[x for x in data[1:] if x<=pivot]
        greater=[x for x in data[1:] if x>=pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
l=[12,5,78,43,79,43,68,68,74,23]
print(quick_sort(l))