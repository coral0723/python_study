#입력:리스트a
#출력:없음(입력으로 주어진 a가 정렬됨)

def find(a):
    n=len(a)
    for i in range(0,n-1):
        min_idx=i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]

d=[3,4,2,1,5]
find(d)
print(d)
