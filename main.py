def validate(obj):
	"""
	validate argument is object .
	The function returns True if anyone wins and returns False if anyone no one wins
	"""
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
	player1_char="X"
	player2_char="O"
	                
	def __init__(self,player1,player2):
		self.p1=player1.upper()
		self.p2=player2.upper()
		
	@property
	def show_board(self):
		"""
		Show the board
		"""
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
		 """
		 pos ==> int
		 letter ==> str
		 first check if the position is valide if  the position is valide then place the letter and return True but if the position is worng return False
		 """
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
		 return True     
		 
	"""
   player1_play() and player2_play() are same . They both are player and controler of human user
   """  		  				  		
	def player1_play(self):
	   	print(self.show_board)
	   	player1=int(input(" {0} Enter your position you has {1}: ".format(self.p1,self.player1_char)))
	   	
	   	if(player1>0):
	   		if(self.change_position(player1,self.player1_char)==False):
	   			self.player1_play()
	   		else:
	   			self.log.append(self.p1)
	   			
	   	
    				    	
	def player2_play(self):
	   	print(self.show_board)
	   	player2=int(input(" {0} Enter your position you has {1}: ".format(self.p2,self.player2_char)))
	   	
	   	if(player2>0):
	   		if(self.change_position(player2,self.player2_char)==False):
	   			self.player2_play()
	   		else:
	   		    self.log.append(self.p2)
    				    			
	def run(self):
		"""
		This run() method starts the game and decide if anyone is the winner
		"""
		while True:
			
			if(validate(self)):
				break
			self.player1_play()
			if(validate(self)):
				break					
			self.player2_play()
			if(validate(self)):
				break	
							
		print(self.show_board)							
		print("Winner is "+self.log[-1])
			
	

		
#Lets play

game=TicTicTac(input("X ===> "),input("O ===> "))
game.run()