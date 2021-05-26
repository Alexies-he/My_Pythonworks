number = ['1', '2','3']
print("The first number is ",number[0])
number = ['1', '2','3']
print("The last number is ",number[-2])
number = ['1', '2','3']
number[0] = '-1'
print("The number changed is ",number[0])
print(number)
number = ['1', '2','3']
number.append(-1)
print("The number appended is ",number[-1])
number = ['1', '2','3']
number.insert(0, -1)
print("The insert is ",number[0])
number = [1, 2, 3]
number.remove(2)
print("The number is ",number[1])
cars = ["porche","bmw","audi"]
cars.sort(reverse=True)
print(cars[0],cars[1],cars[2])
cars = ["porche","bmw","audi"]
print(sorted(cars, reverse=False))
print(cars[0],cars[1],cars[2])
print(len(cars))