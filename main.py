def validate(obj):
	b=obj.board
	u=0
	for i in range(len(b)):
		
		if(b[i][0]==b[i][1]==b[i][2]):
			return True
			
		if(b[0][u]==b[1][u]==b[2][u]):
			return True
		u+=1
			
	if((b[0][0]==b[1][1]==b[2][2]) or (b[0][2]==b[1][1]==b[2][0])):
		return True
		
	return False
	
class TicTicTac:
	board=[ ["1","2","3"],["4","5","6"],["7","8","9"]]	                
	log=[]
	                
	def __init__(self,player1,player2):
		self.p1=player1
		self.p2=player2
		
	@property
	def show_board(self):
		divider="-----------------"
		text="" 
		text+="{0}\n".format(divider)
		line=""
		for i in self.board:
			for j in i:
				line+=(" | {0} ".format(j))
			text+=(line+" | \n")
			text+="{0}\n".format(divider)
			line=""
		return text
		
	def change_position(self,pos,letter):
		 
		 total=self.board[0]+self.board[1]+self.board[2]
		 
		 if(str(pos) not in total ):
		 	
		 	print("Try again lol")
		 	
		 	return False
		 
		 if(pos==1):
		 	self.board[0][0]=letter
		 if(pos==2):
		    self.board[0][1]=letter
		 if(pos==3):
		    self.board[0][2]=letter
		 if(pos==4):
		    self.board[1][0]=letter
		 if(pos==5):
		   	self.board[1][1]=letter
		 if(pos==6):
     		  self.board[1][2]=letter
		 if(pos==7):
		    self.board[2][0]=letter
		 if(pos==8):
		   	self.board[2][1]=letter
		 if(pos==9):
     		  self.board[2][2]=letter
     		  		
	def player1_play(self):
	   	print(self.show_board)
	   	player1=int(input(" {0} Enter your position you has X: ".format(self.p1)))
	   	
	   	if(player1>0):
	   		self.log.append(self.p1)
	   		if(self.change_position(player1,"X")==False):
	   			self.player1_play()
	   			
	   	
    				    	
	def player2_play(self):
	   	print(self.show_board)
	   	player2=int(input(" {0} Enter your position you has O: ".format(self.p2)))
	   	
	   	if(player2>0):
	   		self.log.append(self.p2)
	   		if(self.change_position(player2,"X")==False):
	   			self.player2_play()
    				    			
	def run(self):
		while True:
			if(validate(self)):
				break			
			self.player1_play()
			self.player2_play()

									
		print("Winner in "+self.log[-1])
			
	

		

game=TicTicTac(input("X ===> "),input("O ===> "))
game.run()