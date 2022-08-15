#그리디 알고리즘
#손님에게 거슬러줘야 할 돈이 n원일때, 줘야 할 동전의 최소 개수를 구하라. 
#거슬러줘야 할 돈 N은 항상 10의 배수이다.


n = 1260
count = 0

#큰 단위의 화폐부터
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count = count + n//coin 
    n %= coin 

print(count)


#코드의 시간 복잡도 : O(k)