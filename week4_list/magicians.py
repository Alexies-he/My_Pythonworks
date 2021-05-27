magicians = ['alex','david','bob']
for magician in magicians:#遍历整个列表
    print (magician.title()+", that was a great trick!")
    print("I like your trick, "+magician.title()+"!\n")
print("Thanks, everyon. That was a great magic show!")
numbers = list(range(0, 11, 2))
for squ in numbers:
    num = squ**2
    print(num)
squares = []
for sq in range(0, 11, 2):
    squares.append(sq**2)
print(squares)
squares = [value**2 for value in range(0, 11)]
print(squares)
squares = []
for square in range(0,11):
    squares.append(square**2)
print(squares)