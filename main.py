from tkinter import *
import math 

root = Tk()
canvas_width = 1600
canvas_height = 1200
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

ORIGIN = [canvas_width/2, canvas_height/2]
GRID_RADIUS = 500

def drawArc(angle):
	# pretend we have a unit circle and then convert to coordinates 
	x = math.cos(angle)
	print("x: " + str(x))
	y = math.sin(angle)
	print("y: " + str(y))
	gradient = y/x 
	print("Gradient: " + str(gradient))
	normal = -1/gradient
	print("Normal: " + str(normal))
	focus = x - (y/normal)
	print("Focus: " + str(focus))

	# now convert to coordinates 
	# everything is scaled up by a factor of grid_radius 
	c_focus = (focus * GRID_RADIUS) + ORIGIN[0]
	c_y = int((y * GRID_RADIUS) + ORIGIN[1])
	c_x = int((x * GRID_RADIUS) + ORIGIN[0])

	print("Corrected y: " + str(c_y))
	print("Corrected focus: " + str(c_focus))
	print("Screen y: " + str(ORIGIN[1]))
	print("Opposite y: " + str((2*ORIGIN[1])-c_y))
	arc_radius = math.sqrt((c_y-ORIGIN[1])**2 + (c_x-c_focus)**2)

	for j in range(2*int(ORIGIN[1])-c_y,c_y):
		i = math.sqrt(arc_radius**2-(j-ORIGIN[1])**2)+c_focus
		#print(str(i) + ", " + str(j))
		canvas.create_rectangle(i-1,j-1,i,j)

def main():
	x = ORIGIN[0]
	y = ORIGIN[1]
	canvas.create_oval(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_rectangle(x-GRID_RADIUS,y-GRID_RADIUS,x+GRID_RADIUS,y+GRID_RADIUS)
	canvas.create_line(x,y-GRID_RADIUS,x,y+GRID_RADIUS)
	canvas.create_line(x-GRID_RADIUS,y,x+GRID_RADIUS,y)
	for x in range(17,32):
		if x % 16 != 0:
			drawArc(x*math.pi/32)
	root.mainloop()

if __name__=="__main__":
	main()