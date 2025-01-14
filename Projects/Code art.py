import  turtle

t = turtle.Turtle()
t.goto(0,0)
#Made backround black
turtle.Screen().bgcolor("Black")

colors = ["black","white"]
#Making the colors rotate from black to white
for i in range(600) :
     t.color( colors[i % 2])
     t.forward( 20 +i)
     t.left(72)
     #made pentagon shapes


turtle.exitonclick()