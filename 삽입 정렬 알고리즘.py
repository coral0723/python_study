d=[2,4,5,1,3]

#리스트 r에서 v가 들어가야할 위치를 돌려주는 함수
def find_ins_idx(r,v):
    #이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    for i in range(0,len(r)):
        #v값보다 i번 위치에 있는 자료값이 크면
        #v가 그 값보다 앞에 위치해야 정렬 순서가 유지됨
        if v<r[i]:
            return i
        #적절한 위치를 못찾았을 땐
        #v가 모든 자료보다 크다는 뜻이므로 맨뒤에 위치
    return len(r)

def ins_sort(a):
    result=[]
    while a:
        value=a.pop(0)#기존 리스트에서 한 개를 꺼냄
        ins_idx=find_ins_idx(result,value)#꺼낸 값이 들어갈 적절한 위치 찾기
        result.insert(ins_idx,value)#찾은 위치에 값 삽입

    return result


print(ins_sort(d))
