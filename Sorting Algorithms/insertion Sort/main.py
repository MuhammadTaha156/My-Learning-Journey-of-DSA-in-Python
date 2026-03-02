def insertion_sort(data):
    for i in range(1,len(data)):
        temp=data[i]

        j=i-1
        while j>=0 and temp<data[j]:
            data[j+1]=data[j]
            j-=1
        data[j+1]=temp

l=[12,74,33,89,23,56]
insertion_sort(l)
print(l)

        

        