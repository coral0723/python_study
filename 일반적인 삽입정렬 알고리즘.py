d=[2,4,5,1,3]

def ins_sort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
    #j를 i 바로 왼쪽에 저장
        j=i-1
        #리스트의 j번에 위치한 값과 key를 비교해 key의 적절한 위치를 찾음
        while j>=0 and a[j]>key:
            a[j+1]=a[j]#삽입할 공간이 생기도록 값을 오른쪽으로 이동
            j-=1
        a[j+1]=key#찾은 삽입 위치에 key값을 저장

ins_sort(d)
print(d)
