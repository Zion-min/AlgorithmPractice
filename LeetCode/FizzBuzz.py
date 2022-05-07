def fizzBuzz(self, n: int) -> List[str]:

    answer = []

    for i in range(1,n+1):
        #파이썬에는 &&연산자가 없다..
        if i%3==0 and i%5==0:
            answer.append("FizzBuzz")
        elif i%3==0:
            answer.append("Fizz")
        elif i%5==0:
            answer.append("Buzz")
        #else뒤에 : 자꾸 빼먹지마
        else:
            answer.append(str(i))

    return answer
        
