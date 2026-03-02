def insertion_sort(data):
    for i in range(1,len(data)):
        temp=data[i]

        j=i-1
        while j>=0 and temp<data[j]:
            data[j+1]=data[j]
            j-=1
        data[j+1]=temp


list=[25,11,37,73,77,33,41]
insertion_sort(list)
print(list)



