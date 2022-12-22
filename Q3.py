a=list(map(int,input("Enter Number:").split()))

b=[]
for y in a:
    x=(y,y*y)
    b.append(x)

print("Square of Given Numbers is:")
print(b)