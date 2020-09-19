#최댓값 구하기
#입력:숫자가 n개 들어있는 리스트
#출력:숫자 n개중 최댓값


v=[17,92,9,77,54]

def find_max(a,n):
    if n==1:
        return a[0]
    max_n_1=find_max(a,n-1)
    if max_n_1>a[n-1]:
        return max_n_1
    else:
        return a[n-1]

print(find_max(v,len(v)))
    
    
