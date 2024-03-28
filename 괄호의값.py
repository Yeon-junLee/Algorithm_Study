import sys
N = sys.stdin.readline()
st = []
sum = 0
num = 1
# 분배법칙을 이용
# EX : (()[[]])
# 계산 : 2x(2+3x3)=22
# 분배법칙을 보면 (2x2) + (2x3x3) 로 계산됨
for i in range(len(N) - 1):
    if N[i] =='(':
        # ( 가 오면 현재 계산중인 num에 2를 곱해줌
        num *= 2
        st.append(N[i])
    elif N[i] == '[':
        # [ 가 오면 현재 계산중인 num에 2를 곱해줌
        num *= 3
        st.append(N[i])        
    elif N[i] == ')':
        # ) 가 오면
        if len(st) == 0 or st[-1] != '(':
            # 스택이 비어있거나 스택의 최근 문자가 ( 가 아니면 괄호 오류이므로 sum = 0으로 만들고 반복문 탈출
            sum = 0
            break
        if N[i - 1] == '(':
            # 이전 차례의 문자가 ( 라면 곱셈을 닫는 것이므로 sum에 num을 더한 뒤, 2로 나눠줌
            sum += num
        num //= 2
        st.pop()
    else: # N[i] == ']'
        # ) 가 오면
        if len(st) == 0 or st[-1] != '[':
            # 스택이 비어있거나 스택의 최근 문자가 [ 가 아니면 괄호 오류이므로 sum = 0으로 만들고 반복문 탈출
            sum = 0
            break
        if N[i - 1] == '[':
            # 이전 차례의 문자가 [ 라면 곱셈을 닫는 것이므로 sum에 num을 더한 뒤, 3으로 나눠줌
            sum += num
        num //= 3
        st.pop()

# 제대로 된 괄호인지 확인
if len(st) == 0:
    print(sum)
else:
    print(0)