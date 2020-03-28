X = int(input())
five_hundred = int(X / 500)
five = int((X - five_hundred * 500) / 5)
print(int(five_hundred * 1000 + five * 5))