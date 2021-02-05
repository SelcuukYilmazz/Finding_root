import sys

del sys.argv[0]


a = int(sys.argv[0])
b = int(sys.argv[1])
c = int(sys.argv[2])


if a == 0:
    print("a can't be zero")

elif ((b**2) - 4) * a * c > 0:
   k = (-b + ((b**2)- 4 * a * c) ** 1 / 2) / (2 * a)
   l = (-b - ((b**2)- 4 * a * c) ** 1 / 2) / (2 * a)
   
   print("There are two solutions")
   print("Solution(s): ", k, l)
   
elif ((b**2) - 4) * a * c == 0:
    k = (-b + (((b**2)- 4) * a * c) ** 1 / 2) / (2 * a)
    print("There is one solution")
    print("Solution(s): ", k)
    
else:
    k = (-b + (((b**2)- 4) * a * c) ** 1 / 2) / (2 * a)
    l = (-b - (((b**2)- 4) * a * c) ** 1 / 2) / (2 * a)
    
    print("There are no real number solutions")
