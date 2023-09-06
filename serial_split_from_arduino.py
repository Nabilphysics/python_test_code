
#!/usr/bin/env python
a = b'25,69,\r\n'
print(type(a))
b = a.decode()
print(type(b))
print(b)

c = b.split(",")
print(c)
print(type(c))
print(c[0])
print(c[1])
print(c[2])
print(c[3])

