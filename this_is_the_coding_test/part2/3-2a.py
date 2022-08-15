#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort # 입력받은 수를 정렬하기
first = data[n - 1] #첫번째로 큰 수
second = data[n - 2] #두번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: #m이 0이면 break
            break
        result += first
        print(result)
        m -= 1 #더할 때마다 1씩 빼기
    if m == 0: #m이 0이면 break
        print(result)
        break
    result += second # 두번째로 큰 수를 더하기
    print(result)
    m -= 1 #더할 때마다 1씩 빼기

print(result) #최종답안출력