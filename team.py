def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# 두 수 입력 받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

print("덧셈 결과: ", add(num1, num2))
print("뺄셈 결과: ", subtract(num1, num2))
print("곱셈 결과: ", multiply(num1, num2))
print("나눗셈 결과: ", divide(num1, num2))
