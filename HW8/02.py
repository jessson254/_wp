a=str(input())
b = [float (c.strip()) for c in a.split(",") if c.strip()]
f=sum(b)
print(f)
e=len(b)
print(e)
d=f/e
print(d)
