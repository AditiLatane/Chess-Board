import turtle as t

t.color("black")
t.pensize(5)
t.speed(100)
t.shape("turtle")
t.penup()
t.goto(-100,200)
t.pendown()
t.write("__CHESS BOARD__", font=("Verdana", 15, "normal"))

t.penup()
t.goto(-120,-120)
t.pendown()

for i in range(4):
    t.forward(240)
    t.left(90)
    
for i in range(4):
    t.forward(30)
    t.left(90)
    t.forward(240)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(240)
    t.left(90)
for i in range(4):
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(240)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(240)
    
print(t.position())
    
t.penup()
t.goto(-120,-120)
t.pendown()

t.fillcolor("black")
x=-120
y=-120
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            t.penup()
            t.goto(x+(i*30) , y+(j*30))
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                 t.forward(30)
                 t.left(90)
            t.end_fill()
