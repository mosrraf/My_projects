#the background list that take players input:
	#in this function user enter the column number
	#if the bottom cell of the column is empty then fill above cell and so on.
import os
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
def table(player,play,t):
	n=-1
	while t[n][play-1]!=" ":#checking column's cells
		n-=1
		if n<-7:#all collumn's cells not accessible prombt for another input
			clear()
			print("this column is no more accessible")
			game_GUI(t)
			play=int(In("please enter your column:"))
			n=-1
	t[n][play-1]=player#found an accessible cell and fell it
	return t
	#in the next function we are checking for winning condition
		#this happens when:
		#one of players build a collection of blocks can reach each other whithin single step
def winning(t,player1,player2):#a periodic check by each turn 
	p1=[[i,j] for i in range(0,len(t))for j in range(0,len(t))if t[i][j]==player1]#collect player 1 plays since the start of game
	p2=[[i,j] for i in range(0,len(t))for j in range(0,len(t))if t[i][j]==player2]#collect player 2 plays since the start of game	
	# checking either one of them has won in the last turn
	if test(p1):
		return player1
	elif test(p2):
		return player2 
	else:
		return 0 
def winner(value):# checking if there is a winner or not
	if value==0:
		return True
	return False
def tie(t):# checking for draw which happens when there are no more blocks and winning condition not satisfied
	if not " " in t[0]:
		return True
def test(player):#checking winning condition
		counters=[0]
		for i in range(0,len(player)):
			counter=1
			for j in range(0,len(player)):
				xs=abs(player[i][0]-player[j][0])
				ys=abs(player[i][1]-player[j][1])
				if xs==0 and ys==0:
					continue
				if xs in [0,1]:
					if ys in [0,1]:
						counter+=1
			counters.append(counter)
		if max(counters)==7:
			return True	
def In(text,valid=[str(i) for i in range(1,8)]):# check if the entered value is within the valid values
	x=input(text)
	while x not in valid:
		print("invalid value!")
		x=input(text)
	return x
def game_GUI(t):#the structure of the game
	print(" _____________________________")
	print(" | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
	for i in range(0,len(t)):
		sum=""
		for j in range(0,len(t)):
			sum+="| "+t[i][j]+" "
		sum+="|"
		print(" ----------------------------\n",sum)
	print(" _____________________________")
def game():#single game
	players=["X","O"]
	t=[[" " for i in range(0,7)] for i in range(0,7)]
	the_winner=winning(t,players[0],players[1])
	i=0
	game_GUI(t)
	while winner(the_winner):
		i+=1
		column=int(In(f"player {i} please enter your column:"))
		t=table(players[i-1],column,t)
		clear()
		game_GUI(t)
		the_winner=winning(t,players[0],players[1])
		if tie(t):
			print("it's a tie")
			break
		if i==2:
			i=0
	if not tie(t):
		print(f"The winner is player {players.index(the_winner)+1}")	
def main():#game controller
	print("This game is a challenge to collect near 7 blocks in which there is one block \ncan reach the other blocks with a single step.\nplayers are allowed to stop each other from reaching this target.\nif one reach that target the game is over and we have a winner\nGood luck and may the odds be in yours favour.")
	answer=In("Do you want to start? \n (yes/no)\n ans: ",["yes","no"])
	while answer=="yes":
		clear()
		game()
		answer=In("Do you want to play again? \n (yes/no)\n ans: ",["yes","no"])
		clear()
	print("see you later")
main()	
input()
