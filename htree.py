from drawingpanel import *
panel = DrawingPanel(500,500)
canvas = panel.canvas


def drawH(size,x,y):
	canvas.create_line(x-size/2,y,x+size/2,y,fill="red")
	canvas.create_line(x-size/2,y-size/2,x-size/2,y+size/2,fill="red")
	canvas.create_line(x+size/2,y-size/2,x+size/2,y+size/2,fill="red")

def htree(n):
	draw_htree_rec_helper(n,200,250,250)


def draw_htree_rec_helper(n,size,x,y):
	if n==1:
		# draw a single H
		drawH(size,x,y)
		return None

	drawH(size,x,y)
	draw_htree_rec_helper(n-1,size/2,x-size/2,y-size/2)
	draw_htree_rec_helper(n-1,size/2,x+size/2,y-size/2)
	draw_htree_rec_helper(n-1,size/2,x-size/2,y+size/2)
	draw_htree_rec_helper(n-1,size/2,x+size/2,y+size/2)





def main():
	#n = int(input("input an integer"))
	panel.set_background("white")

	htree(5)


main()

