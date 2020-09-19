def quick_sort_sub(a,start,end):
    if end-start<=0:
        return
    #기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    #[기준 값보다 작은 값들,기준 값,기준 값보다 큰 값들]
    pivot=a[end]#편의상 리스트이 마지막값을 기준값으로 정함
    i=start
    for j in range(start,end):
        if a[j]<=pivot:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[i],a[end]=a[end],a[i]
    #재귀호출 부분
    quick_sort_sub(a,start,i-1)
    quick_sort_sub(a,i+1,end)

def quick_sort(a):
    quick_sort_sub(a,0,len(a)-1)

d=[6,8,3,9,10,1,2,4,7,5]
quick_sort(d)
print(d)
    
