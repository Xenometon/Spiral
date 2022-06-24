import turtle 

  #importing turtle module

colors = ['yellow', 'blue', 'green', 'purple', 'orange', 'red']     #setting the colors

t = turtle.Pen()   
turtle .shape("arrow") #setting the shape of the pen as turtle
turtle.bgcolor('black')
turtle.speed(10000)   
for x in range(250):
    t.pencolor(colors[x%6])   
    t.width(x//20)
    t.forward(x)
    t.left(50)
    
    #End
