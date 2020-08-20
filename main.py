from tkinter import *
import math 

root = Tk()
canvas_width = 1600
canvas_height = 1200
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ORIGIN = [canvas_width/2, canvas_height/2]
GRID_RADIUS = 500

# you only need to points on a circle to draw an arc 
def drawArc(first, second):
	# if points are opposite draw a line not an arc 
	if int(distance(first, second)) == int(2 * GRID_RADIUS):
		canvas.create_line(first[0], first[1], second[0], second[1])
	else:
		my_focus = focus(first, second)
		radius = distance(first, my_focus)
		# choose what to iterate over 
		if abs(first[0]-second[0]) > abs(first[1]-second[1]):
			for i in range(first[0], second[0]):
				j = math.sqrt(radius**2-(i-my_focus[0])**2)+my_focus[1]
				canvas.create_rectangle(i-1,j-1,i,j)
		else:
			for j in range(first[1], second[1]):
				print("j: " + str(j))
				print("radius: " + str(radius))
				i = math.sqrt(radius**2-(j-my_focus[1])**2)+my_focus[0]
				canvas.create_rectangle(i-1,j-1,i,j)

def focus(first, second):
	# get two lines which are normal to radii 
	# need to check for division with 0
	# normals are the gradients of the lines created by the given points and the origin
	normal_one = gradient(ORIGIN, first)
	print("First radial: " + str(normal_one))
	normal_two = gradient(ORIGIN, second)
	print("Second radial: " + str(normal_two))
	# the gradients are of the lines tangent to the circle at the points 
	gradient_one = -1/normal_one
	print("First tangent gradient: " + str(gradient_one))
	gradient_two = -1/normal_two
	print("Second tangent gradient: " + str(gradient_two))
	# I checked that this should work 
	# find the coordinates of the focus of the circle 
	x = (first[1]-(gradient_one*first[0])+(gradient_two*second[0])-second[1])/(gradient_two-gradient_one)
	print("Focus x coordinate: " + str(x))
	y = (gradient_one*(x-first[0]))+first[1]
	print("Focus y coordinate: " + str(y))
	return (x,y)

def distance(first, second):
	return math.sqrt((first[0]-second[0])**2+(first[1]-second[1])**2)

def gradient(first, second):
	# need to test if these approximations are valid 
	if first[0]-second[0] == 0:
		gradient = (first[1]-second[1])/0.0001
	else:
		gradient = (first[1]-second[1])/(first[0]-second[0])
	if gradient == 0:
		gradient = 0.00001
	return gradient

def drawInitial():
	x = ORIGIN[0]
	y = ORIGIN[1]
	canvas.create_oval(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_rectangle(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_line(x,y-GRID_RADIUS,x,y+GRID_RADIUS)
	canvas.create_line(x-GRID_RADIUS,y,x+GRID_RADIUS,y)

def main():
	drawInitial()

	drawArc((800,100),(300,600))
	
	root.mainloop()

if __name__=="__main__":
	main()