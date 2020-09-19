def quick_sort(a):
    n=len(a)
    if n<=1:
        return a
    #기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot=a[-1]#편의상 리스트의 마지막 값을 기준 값으로 정함
    g1=[]
    g2=[]
    for i in range(0,n-1):
        if a[i]<pivot:
            g1.append(a[i])#작으면 g1에 추가
        else:
            g2.append(a[i])#크면 g2에 추가
    #각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    #기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return quick_sort(g1)+[pivot]+quick_sort(g2)

d=[6,8,3,9,10,1,2,4,7,5]
print(quick_sort(d))
            
    
