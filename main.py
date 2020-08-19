from tkinter import *
import math 

root = Tk()
canvas_width = 1600
canvas_height = 1200
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ORIGIN = [canvas_width/2, canvas_height/2]
GRID_RADIUS = 500

def calc(angle):
	x = math.cos(angle)
	print(x)
	y = math.sin(angle)
	print(y)
	gradient = y/x 
	print(gradient)
	normal = -1/gradient
	print(normal)
	focus = x - (y/normal)
	print(focus)
	return (x, y, focus)

def convertToScreen(x, y, focus):
	c_focus = (focus * GRID_RADIUS) + ORIGIN[0]
	print(c_focus)
	c_y = int((y * GRID_RADIUS) + ORIGIN[1])
	print(c_y)
	c_x = int((x * GRID_RADIUS) + ORIGIN[0])
	print(c_x)
	arc_radius = math.sqrt((c_y-ORIGIN[1])**2 + (c_x-c_focus)**2)
	return (c_x, c_y, c_focus, arc_radius)

def drawArc(angle):

	(x, y, focus) = calc(angle)

	(c_x, c_y, c_focus, arc_radius) = convertToScreen(x, y, focus)

	for j in range(2*int(ORIGIN[1])-c_y,c_y):
		if angle > math.pi/2:
			i = math.sqrt(arc_radius**2-(j-ORIGIN[1])**2)+c_focus
		else:
			i = -math.sqrt(arc_radius**2-(j-ORIGIN[1])**2)+c_focus
		canvas.create_rectangle(i-1,j-1,i,j)

def drawInitial():
	x = ORIGIN[0]
	y = ORIGIN[1]
	canvas.create_oval(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_rectangle(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_line(x,y-GRID_RADIUS,x,y+GRID_RADIUS)
	canvas.create_line(x-GRID_RADIUS,y,x+GRID_RADIUS,y)

def main():
	drawInitial()
	
	for x in range(1, 32):
		if x % 16 != 0:
			drawArc(x*math.pi/32)
	
	root.mainloop()

if __name__=="__main__":
	main()