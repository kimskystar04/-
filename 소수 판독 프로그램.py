print(" 소수인지 아닌지 알고싶은 숫자를 입력하세요 : ", end = "")
a = int(input())


# 소수의 정의 : 약수가 1과 자기 자신만 있는 숫자
isPrime = True

for i in range(2,a):
    print("dfljkdj")
    if a % i == 0:
        isPrime = False
        break


if a == 1:
    print(a,"는 소수가 아닙니")
    exit()
if isPrime :
    print(a,"는 소수입니다.")
else:
    print(a, "는 소수가 아닙니다.")
