# author: big-bacon
import turtle

r = turtle.Turtle()
sides = 9
angle = 360.0
colors = ["red", "green", "yellow", "blue"]
distances = range(20, 120)

for distance in distances:
	r.left(100)
	for c in colors:
		r.color(c)
		r.forward(distance)
		r.left(1000)
		
		r.speed(0)