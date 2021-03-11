str1="ahmed"
print(str1*3)
str1="""
name: ahmed elkady
age : 21
job : back end developer  & have abackground flutter
"""
print(str1)

#   Conversions
msg_str='20'
xint=int(msg_str)
print(xint+5)

xflo=float(msg_str)
print(xflo)

#   More convenient way
x,y,z=input().split()
print(x,y,int(z)+6)

# Let’s read 4 integers:
a, b, c, d = map(int, input().split())

# Let’s read 5 floats
a, b, c, d, e = map(float, input('Enter 5 numbers: ').split())



