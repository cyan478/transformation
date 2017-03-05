from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as file:
    	l = file.readline().strip()
    	while (l != "quit" and line != ""):

    		if l == "line":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 6:
    				print "Wrong number of arguments for line"
    			else:
    				add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])

    		if l == "ident":
    			ident(transform)

    		if l == "scale":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 3:
    				print "Wrong number of arguments for scale"
    			else:
					smatrix = make_scale(args[0],args[1],args[2])
					mult_matrix(smatrix, transform)

    		if l == "move":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 3:
    				print "Wrong number of arguments for move"
    			else:
					tmatrix = make_translate(args[0],args[1],args[2])
					mult_matrix(tmatrix, transform)

    		if l == "rotate":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 2:
    				print "Wrong number of arguments for rotate"
    			else:
					if args[0] == "x":
						rmatrix = make_rotX(args[1])
						mult_matrix(rmatrix, transform)
					elif args[0] == "y":
						rmatrix = make_rotY(args[1])
						mult_matrix(rmatrix, transform)
					elif args[0] == "z":
						rmatrix = make_rotZ(args[1])		
						mult_matrix(rmatrix, transform)
					else:
						print "Wrong Axis input, not x/y/z"  
						
    		if l == "yrotate":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 1:
    				print "Wrong number of arguments for y rotate"
    			else:
					rmatrix = make_rotY(args[1])
					mult_matrix(rmatrix, transform)
    		if l == "zrotate":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 1:
    				print "Wrong number of arguments for z rotate"
    			else:
					rmatrix = make_rotZ(args[1])
					mult_matrix(rmatrix, transform) 
    		if l == "apply":
    			matrix_mult(transform, points)
    		if l == "display":
    			draw_lines(points, screen, color)
    			display(screen)
    		if l == "save":
    			l = file.readline().strip()
    			args = l.split(" ")
    			if len(args) != 1:
    				print "Wrong number of arguments for save"
    			else:
					draw_lines(points, screen, color)
					display(screen)
					save_extension(screen,args[0])
    		if l == "quit":
    			pass #already accounted for in while loop
    		l = file.readline().strip()                       		

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

