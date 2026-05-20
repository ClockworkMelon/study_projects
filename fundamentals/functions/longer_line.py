import math as m

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = m.sqrt(x1**2 + y1**2)
    d2 = m.sqrt(x2**2 + y2**2)
    d3 = m.sqrt(x3**2 + y3**2)
    d4 = m.sqrt(x4**2 + y4**2)

    if (d1 + d2) <= (d3 + d4):
        if d3 <= d4:
            return f"({m.floor(x3)}, {m.floor(y3)})({m.floor(x4)}, {m.floor(y4)})"
        else:
            return f"({m.floor(x4)}, {m.floor(y4)})({m.floor(x3)}, {m.floor(y3)})"
    else:
        if d1 <= d2:
            return f"({m.floor(x1)}, {m.floor(y1)})({m.floor(x2)}, {m.floor(y2)})"
        else:
            return f"({m.floor(x2)}, {m.floor(y2)})({m.floor(x1)}, {m.floor(y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))