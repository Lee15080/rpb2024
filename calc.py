def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    divide_result = divide(x, y)
    if divide_result is not None:
        print("%d / %d = %0.3f" % (x, y, divide_result))
    
    
def add(a, b):
    return a + b
    
    
# TODO: divide() 함수 정의
def divide(x, y):
    # 0으로 나누는 경우 에러 처리
    if y == 0:
        print("Error: cannot divide by zero.")
        return
    else:
        # 나눗셈 결과를 소수점 셋째 자리까지 출력
        result = round(x / y, 3)
        return result

if __name__ == "__main__":
    main()
