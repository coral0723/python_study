#주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
#입력: 문자열 s
#출력: 회문이면 true, 아니면 false

def palindrome(s):
    #큐와 스택을 리스트로 정의
    qu=[]
    st=[]
    #1단계: 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        #해당 문자가 알파벳이면(공백, 숫자, 특수문자가 아니면)
        #큐와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

        #2단계: 큐와 스택에 들어 있는 문자를 꺼내면서 비교
        while qu:
            if qu.pop(0) != st.pop():
                return False

        return True


print(palindrome("wow"))
print(palindrome("Madam, I'm Adam."))
