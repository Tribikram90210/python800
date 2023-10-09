import random
random.seed(0)
signal = [random.randint(1,25) for i in range(10)]
print(signal)

# lamda function is used with map() and filter()
# syntax: lambda argument :Expression
odd =filter(lambda x:x %2==1,signal)
even = filter(lambda x:x%2 == 0 ,signal)
print(f'The odd numbers are:{list(odd)}')
print(f'The even numbers are :{list(even)}')
squares = map(lambda x:x**2,signal)
print('the squares are:',list(squares))
# lambda is a funtion without name