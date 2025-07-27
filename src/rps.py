from tkinter import *
from PIL import ImageTk, Image
from typing import get_type_hints
import random
# main window object
root = Tk()

def ExitAppRPS():
        root.destroy()

    # Title of GUI window
root.title('RPS')

# Size of window
root.geometry('800x680')

# Creating canvas
canvas = Canvas(root, width=800, height=680)
canvas.grid(row=0, column=0)

# Creating labels on GUI window
l1 = Label(root, text='Player', font=('Algerian', 25))
l2 = Label(root, text='Computer', font=('Algerian', 25))
l3 = Label(root, text='Vs', font=('Algerian', 40))

# Placing all the labels on window
l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

# Default image
img_p = Image.open("assets/images/default.png")
img_p = img_p.resize((300, 300))

# Flipping image from left to right
img_c = img_p

# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

# Rock image
rock_p = Image.open('assets/images/rock.jpeg')
rock_p = rock_p.resize((300, 300))

# Flipping image from left to right
rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

# Paper image
paper_p = Image.open('assets/images/paper.jpeg')
paper_p = paper_p.resize((300, 300))

# Flipping image from left to right
paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

# Scissor image
scissor_p = Image.open('assets/images/scissor.jpeg')
scissor_p = scissor_p.resize((300, 300))

# Flipping image from left to right
scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

# Selection image
img_s = Image.open("assets/images/Selection.jpg")
img_s = img_s.resize((300, 130))
img_s = ImageTk.PhotoImage(img_s)

# Putting image on canvas on specific coordinates
canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
canvas.create_image(0, 400, anchor=NW, image=img_s)
canvas.create_image(500, 400, anchor=NW, image=img_s)

coscore=0
score=0
# game function
def game(player):
	canvas.delete('score')
	canvas.delete('coscore')
	global score
	global coscore
	select = [1, 2, 3]
	
	# Randomly selects option for computer
	computer = random.choice(select)

	# Setting image for player on canvas
	if player == 1:
	
		# Puts rock image on canvas
		canvas.create_image(0, 100, anchor=NW, image=rock_p)
	elif player == 2:
		
		# Puts paper image on canvas
		canvas.create_image(0, 100, anchor=NW, image=paper_p)
	else:
		
		# Puts scissor image on canvas
		canvas.create_image(0, 100, anchor=NW, image=scissor_p)

	# Setting image for computer on canvas
	if computer == 1:
		
		# Puts rock image on canvas
		canvas.create_image(500, 100, anchor=NW, image=rock_c)
	elif computer == 2:
		
		# Puts paper image on canvas
		canvas.create_image(500, 100, anchor=NW, image=paper_c)
	else:
		
		# Puts scissor image on canvas
		canvas.create_image(500, 100, anchor=NW, image=scissor_c)

	# Obtaining result by comparison
	if player == computer: # Case of DRAW
		canvas.delete('result')
		res = 'Draw'
		score+=0
		coscore+=0
		
	# Case of player's win
	elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
		canvas.delete('result')
		res = 'You won'
		score += 1
		coscore+=0
	
	# Case of computer's win
	else:
		canvas.delete('result')
		res = 'Computer won'
		score += 0
		coscore = coscore + 1

	# Putting result on canvas
	canvas.create_text(200, 640, text='Result:- ' + res,fill="black", font=('Algerian', 25), tag='result')
	canvas.create_text(590, 640, text='Score:- ' + str(score),fill="black", font=('Algerian', 25), tag='score')
	canvas.create_text(590, 600, text='Computer Score:- ' + str(coscore),fill="black", font=('Algerian', 25), tag='coscore')
	
score=score
coscore=coscore
# Function for clear button
def clear():

	# Removes result from canvas
	canvas.delete('result')
	canvas.delete('score')
	canvas.delete('coscore')
	# Puts default image on canvas
	canvas.create_image(0, 100, anchor=NW, image=img_p)
	canvas.create_image(500, 100, anchor=NW, image=img_c)


# Button for selecting rock
rock_b = Button(root, text=' Play Rock', command=lambda: game(1))
rock_b.place(x=30, y=550)

# Button for selecting paper
paper_b = Button(root, text='Play Paper', command=lambda: game(2))
paper_b.place(x=123, y=550)

# Button for selecting scissor
scissor_b = Button(root, text='Play Scissor', command=lambda: game(3))
scissor_b.place(x=215, y=550)

# Button for clear
clear_b = Button(root, text='CLEAR', font=('Times', 10, 'bold'),width=10, command=clear).place(x=370, y=28)
Qu = Button(root, text='Quit', font=('Times', 10, 'bold'),width=10, command=ExitAppRPS).place(x=370, y=200)

#sc=Label(root, text=('Score:- ' + str(score)), font=('Algerian', 25))
#sc.place(x=500,y=600)
root.mainloop()
score=score
coscore=coscore