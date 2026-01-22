import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.bgcolor("white")

# =====================
# FUNGSI BANGUN DATAR
# =====================
def persegi_panjang(x, y, p, l, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    for _ in range(2):
        t.forward(p)
        t.right(90)
        t.forward(l)
        t.right(90)
    t.end_fill()

def segitiga(x, y, sisi, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    for _ in range(3):
        t.forward(sisi)
        t.left(120)
    t.end_fill()

def trapesium(x, y, a, b, tng, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    t.forward(a)
    t.left(120)
    t.forward(tng)
    t.left(60)
    t.forward(b)
    t.left(60)
    t.forward(tng)
    t.left(120)
    t.end_fill()

def jajar_genjang(x, y, a, tng, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    t.forward(a)
    t.left(60)
    t.forward(tng)
    t.left(120)
    t.forward(a)
    t.left(60)
    t.forward(tng)
    t.left(120)
    t.end_fill()

def belah_ketupat(x, y, sisi, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    for _ in range(2):
        t.forward(sisi)
        t.left(60)
        t.forward(sisi)
        t.left(120)
    t.end_fill()

# =====================
# 1. BANGUN DATAR BERWARNA
# =====================
persegi_panjang(-400, 200, 150, 80, "red")
segitiga(-150, 200, 100, "yellow")
trapesium(50, 200, 120, 80, 60, "green")
jajar_genjang(230, 200, 120, 70, "blue")
belah_ketupat(400, 200, 70, "purple")

# =====================
# 2. BENDERA INDONESIA
# =====================
persegi_panjang(-200, 50, 300, 75, "red")
persegi_panjang(-200, -25, 300, 75, "white")

# =====================
# 3. FIBONACCI TREE
# =====================
t.penup()
t.goto(0, -200)
t.setheading(90)
t.pendown()
t.color("brown")

def fibonacci_tree(n, panjang):
    if n == 0:
        return
    t.forward(panjang)
    t.left(30)
    fibonacci_tree(n-1, panjang*0.7)
    t.right(60)
    fibonacci_tree(n-1, panjang*0.7)
    t.left(30)
    t.backward(panjang)

fibonacci_tree(6, 80)

# =====================
# 4. GAMBAR BEBAS (BUNGA)
# =====================
t.penup()
t.goto(300, -200)
t.setheading(0)
t.pendown()
t.color("pink")

for i in range(36):
    t.circle(60)
    t.left(10)

# =====================
# 5. LOGO SEDERHANA (SMK PRESTASI PRIMA - SIMBOL)
# =====================
t.penup()
t.goto(-450, -200)
t.pendown()
t.color("black", "orange")
t.begin_fill()
t.circle(60)
t.end_fill()

t.penup()
t.goto(-480, -210)
t.pendown()
t.color("black")
t.write("SMK\nPrestasi\nPrima", font=("Arial", 10, "bold"))

t.hideturtle()
turtle.done()