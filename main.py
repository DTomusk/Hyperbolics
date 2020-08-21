from tkinter import *
import math 
import random

root = Tk()
canvas_width = 1600
canvas_height = 1000
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ORIGIN = [canvas_width/2, canvas_height/2]
GRID_RADIUS = 300

# you only need to points on a circle to draw an arc 
def drawArc(first, second, line):
	# if points are opposite draw a line not an arc 
	if (int(distance(first, second)) == int(2 * GRID_RADIUS)) | line:
		canvas.create_line(first[0], first[1], second[0], second[1])
	else:
		my_focus = focus(first, second)
		canvas.create_rectangle(my_focus[0]-2, my_focus[1]-2, my_focus[0]+2, my_focus[1]+2)
		canvas.create_line(my_focus[0], my_focus[1], first[0], first[1])
		canvas.create_line(my_focus[0], my_focus[1], second[0], second[1])
		radius = distance(first, my_focus)
		# at some point need to choose the right angles 
		for i in range(1024):
			x = my_focus[0] + radius * math.cos(i * math.pi / 512)
			y = my_focus[1] + radius * math.sin(i * math.pi / 512)
			# inefficient solution
			if distance((x,y), ORIGIN) < GRID_RADIUS:
				canvas.create_rectangle(x-1, y-1, x, y)
		
def drawInitial():
	x = ORIGIN[0]
	y = ORIGIN[1]
	canvas.create_oval(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_rectangle(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_line(x,y-GRID_RADIUS,x,y+GRID_RADIUS)
	canvas.create_line(x-GRID_RADIUS,y,x+GRID_RADIUS,y)

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

def getPointOnCircle(angle):
	return (GRID_RADIUS*math.cos(angle)+ORIGIN[0], GRID_RADIUS*math.sin(angle)+ORIGIN[1])

# this function is more in terms of vectors 
def alpha(point, param):
	x = point[0]
	y = point[1]

	canvas.create_rectangle(x-2, y-2, x+2, y+2)

	print("Point: " + str(x) + " " + str(y))

	a = [param * (x - ORIGIN[0]), param * (y - ORIGIN[1])]
	b = [param * (ORIGIN[1] - y), param * (x - ORIGIN[0])]

	canvas.create_line(ORIGIN[0], ORIGIN[1], ORIGIN[0] + a[0], ORIGIN[1] + a[1])
	
	modA = math.sqrt(a[0]**2 + a[1]**2)

	lam = math.sqrt((GRID_RADIUS**2 / modA**2) - 1)
	b[0] *= lam
	b[1] *= lam

	modB = math.sqrt(b[0]**2 + b[1]**2)

	alpha_x = ORIGIN[0] + a[0] + b[0]
	alpha_y = ORIGIN[1] + a[1] + b[1]

	beta_x = ORIGIN[0] + a[0] - b[0]
	beta_y = ORIGIN[1] + a[1] - b[1]

	canvas.create_line(alpha_x, alpha_y, beta_x, beta_y)
	canvas.create_line(ORIGIN[0], ORIGIN[1], alpha_x, alpha_y)
	canvas.create_line(ORIGIN[0], ORIGIN[1], beta_x, beta_y)

	mu = (GRID_RADIUS * modB) / modA**2

	gamma_x = ORIGIN[0] + mu * a[0]
	gamma_y = ORIGIN[1] + mu * a[1]

	canvas.create_line(ORIGIN[0], ORIGIN[1], gamma_x, gamma_y)
	canvas.create_line(alpha_x, alpha_y, gamma_x, gamma_y)
	canvas.create_line(beta_x, beta_y, gamma_x, gamma_y)

	# we need the choice of parameter to be such that mod gamma-alpha == mod gamma

def main():
	drawInitial()

	#for i in range(10):
	#	angle1 = random.randint(0, 64)*math.pi/32
	#	print("Angle 1: " + str(angle1))
	#	angle2 = random.randint(0, 64)*math.pi/32
	#	if angle2 == angle1:
	#		angle2 = angle1 + math.pi/64
	#	print("Angle 2: " + str(angle2))
	#	point1 = getPointOnCircle(angle1)
	#	print("Point 1: " + str(point1[0]) + ", " + str(point1[1]))
	#	point2 = getPointOnCircle(angle2)
	#	print("Point 2: " + str(point2[0]) + ", " + str(point2[1]))
	#	drawArc(point1, point2, False)

	#angle1 = 13*math.pi/8
	#angle2 = 7*math.pi/8
	#point1 = getPointOnCircle(angle1)
	#point2 = getPointOnCircle(angle2)
	#drawArc(point1, point2, False)

	#angle1 = 3*math.pi/8
	#angle2 = 9*math.pi/8
	#point1 = getPointOnCircle(angle1)
	#point2 = getPointOnCircle(angle2)
	#drawArc(point1, point2, False)

	#angle1 = 11*math.pi/8
	#angle2 = 1*math.pi/8
	#point1 = getPointOnCircle(angle1)
	#point2 = getPointOnCircle(angle2)
	#drawArc(point1, point2, False)

	#angle1 = 15*math.pi/8
	#angle2 = 5*math.pi/8
	#point1 = getPointOnCircle(angle1)
	#point2 = getPointOnCircle(angle2)
	#drawArc(point1, point2, False)

	alpha((ORIGIN[0]+50, ORIGIN[1]+50), 1.8)
	alpha((ORIGIN[0]-20, ORIGIN[1]-70), 1.5)
	
	root.mainloop()

if __name__=="__main__":
	main()