# This is a gomoku game designed by Tao Liu.
# gomoku.py
from graphics import *

class Board:
        '''This class includes almost all the interfaces (except pieces and two buttons). 
        We will use a this class a lot in our call of main function.'''


        def __init__(self):
            self.width = 1000
            self.height = 700
            self.win = GraphWin("Gomoku",self.width,self.height)
            color_of_graph = self.win.setBackground(color_rgb(233,186,63))
            self.back_home = False

        def instructions(self):
            '''This function draws the instruction interface and undraws it when getting a mouse click.'''

            text_line1 = Text(Point(450,30),"Hello friends, this is a Gomoku (Five Pieces In A Row) Game designed by Tao Liu")
            text_line2 = Text(Point(100,60),"")
            text_line3 = Text(Point(110,110),"Rules and how to play:")
            text_line4 = Text(Point(480,140),"If you connect five consecutive pieces in a row, or five consecutive pieces in a column,or five consecutive")
            text_line5 = Text(Point(490,170),"pieces in a diagnoal, you will win the game. You can make a move by clicking around the line intersections.")
            text_line6 = Text(Point(45,220),"Buttons:")
            text_line7 = Text(Point(480,250),"Undo: You can undo the move you want. However, each time you could only undo a move and you may")
            text_line8 = Text(Point(190,280),"NOT undo a move after one side wins.")
            text_line9 = Text(Point(30,330),"Quit:")
            text_line10 = Text(Point(345,360),"You can click quit if you feel a little bit tired and the window will be closed.")
            text_line11 = Text(Point(38,410),"Home:")
            text_line12 = Text(Point(300,440),"You can ALWAYS go back to this page by pressing this button.")
            text_line13 =  Text(Point(475,550),"")
            text_line14 = Text(Point(220,660),"(Click anywhere in the interface to continue)")     

            for ch in [text_line1,text_line2,text_line3,text_line4,text_line5,text_line6,text_line7,text_line8,text_line9,text_line10,text_line11, \
            text_line12,text_line13]:
                ch.setSize(15)
                ch.draw(self.win)

            text_line14.setFill("red")
            text_line14.setSize(18)
            text_line14.draw(self.win)
            
            if self.win.getMouse():
                for ch in [text_line1,text_line2,text_line3,text_line4,text_line5,text_line6,text_line7,text_line8,text_line9,text_line10,text_line11, \
            text_line12,text_line13,text_line14]:
                    ch.undraw()

        def home(self):
            '''This function draws the home button, which is always activated during the game.'''

            rec_home = Rectangle(Point(900,0),Point(1000,60))
            text_home = Text(Point(950,30),"Home")
            text_home.setTextColor("Dark Green")
            text_home.setSize(25)
            text_home.setStyle("bold italic")
            rec_home.setFill(color_rgb(224,224,224))
            rec_home.setOutline(color_rgb(224,224,224))
            self.rec_home = rec_home.draw(self.win)
            self.text_home = text_home.draw(self.win)

        def select_opponent(self):
            '''This function draws the interface of selecting the opponent'''

            ask = Text(Point(320,50),"Please select your opponent (human or computer)")
            ask.setSize(15)
            ask.setStyle("bold italic")
            ask.draw(self.win)

            computer_rectangle = Rectangle(Point(400,200),Point(600,300))
            human_rectangle = Rectangle(Point(400,400),Point(600,500))
            computer_rectangle.setFill(color_rgb(224,224,224))
            human_rectangle.setFill(color_rgb(224,224,224))
            computer_rectangle.setOutline(color_rgb(224,224,224))
            human_rectangle.setOutline(color_rgb(224,224,224))
            play_with_computer = Text(Point(500,250),"Play with computer")
            play_with_human = Text(Point(500,450), "Play with human")
            play_with_computer.setSize(17)
            play_with_human.setSize(17)
            play_with_computer.setTextColor("Red")
            play_with_human.setTextColor("Blue")
            play_with_human.setStyle("bold")
            play_with_computer.setStyle("bold")
            computer_rectangle.draw(self.win)
            human_rectangle.draw(self.win)
            play_with_computer.draw(self.win)
            play_with_human.draw(self.win)

            mouse = self.win.getMouse()
            mouse_x , mouse_y = mouse.getX(),mouse.getY()

            if 400 <= mouse_x <= 600 and 200 <= mouse_y <= 300:
                computer_rectangle.undraw()
                human_rectangle.undraw()
                play_with_human.undraw()
                play_with_computer.undraw()
                ask.undraw()
                return "play with computer"

            elif 400 <= mouse_x <= 600 and 400 <= mouse_y <= 500:
                computer_rectangle.undraw()
                human_rectangle.undraw()
                play_with_human.undraw()
                play_with_computer.undraw()
                ask.undraw()
                return "play with human"

            elif 900 <= mouse.getX() <= 1000 and 0 <= mouse.getY() <= 60:
                self.back_home = True
                computer_rectangle.undraw()
                human_rectangle.undraw()
                play_with_human.undraw()
                play_with_computer.undraw()
                ask.undraw()


            else:
                computer_rectangle.undraw()
                human_rectangle.undraw()
                play_with_human.undraw()
                play_with_computer.undraw()
                ask.undraw()
                return self.select_opponent()

        def select_first_move(self):
            '''This function prompts the user to select whether they want to move first if they play with the computer, and it also
            prompts the user to enter his/her name.'''

            ask = Text(Point(380,50),"Please enter your name and select whether you want to move first")
            ask.setSize(15)
            ask.setStyle("bold italic")
            ask.draw(self.win)

            name_rectangle = Text(Point(450,170),"Please enter your name here (max. 10 letters)")
            name_rectangle.setSize(13)
            name_rectangle.setStyle("bold")
            name_rectangle.draw(self.win)
            user_name = Entry(Point(500,200),40)
            user_name.setText("Your name")
            move_first_button = Rectangle(Point(400,250),Point(600,300))
            move_first_button.setFill(color_rgb(224,224,224))
            move_first_button.setOutline(color_rgb(224,224,224))
            move_second_button = Rectangle(Point(400,350),Point(600,400))
            move_second_button.setFill(color_rgb(224,224,224))
            move_second_button.setOutline(color_rgb(224,224,224))
            move_first_text = Text(Point(500,275),"I want to move first")
            move_first_text.setSize(13)
            move_first_text.setTextColor("Brown")
            move_first_text.setStyle("bold")
            move_second_text = Text(Point(500,375),"I want to move second")
            move_second_text.setSize(15)
            move_second_text.setTextColor("Purple")
            move_second_text.setStyle("bold")
            move_first_button.draw(self.win)
            move_second_button.draw(self.win)
            move_first_text.draw(self.win)
            move_second_text.draw(self.win)
            user_name.draw(self.win)
            mouse = self.win.getMouse()
            mouse_x,mouse_y = mouse.getX(),mouse.getY()
            self.userName = user_name.getText()

            if 400 <= mouse_x <= 600 and 250 <= mouse_y <= 300:

                user_name.undraw()
                name_rectangle.undraw()
                move_first_button.undraw()
                move_second_button.undraw()
                move_first_text.undraw()
                move_second_text.undraw()
                ask.undraw()

                return "move first"

            elif 400 <= mouse_x <= 600 and 350 <= mouse_y <= 400:

                user_name.undraw()
                name_rectangle.undraw()
                move_first_button.undraw()
                move_second_button.undraw()
                move_first_text.undraw()
                move_second_text.undraw()
                ask.undraw()


                return "move second"

            elif 900 <= mouse.getX() <= 1000 and 0 <= mouse.getY() <= 60:
                self.back_home = True
                user_name.undraw()
                name_rectangle.undraw()
                move_first_button.undraw()
                move_second_button.undraw()
                move_first_text.undraw()
                move_second_text.undraw()
                ask.undraw()

            else:
                user_name.undraw()
                name_rectangle.undraw()
                move_first_button.undraw()
                move_second_button.undraw()
                move_first_text.undraw()
                move_second_text.undraw()
                ask.undraw()
                return self.select_first_move()

        def select_difficulty(self):
            '''This function allows the user to select which difficulty of computer they want to play against, hard or easy.'''

            ask = Text(Point(220,50),"Please select the difficulty")
            ask.setSize(15)
            ask.setStyle("bold italic")
            ask.draw(self.win)

            rec_easy = Rectangle(Point(400,150),Point(600,250))
            rec_hard = Rectangle(Point(400,450),Point(600,550))
            rec_easy.setFill(color_rgb(224,224,224))
            rec_easy.setOutline(color_rgb(224,224,224))
            rec_hard.setFill(color_rgb(224,224,224))
            rec_hard.setOutline(color_rgb(224,224,224))
            rec_easy.draw(self.win)
            rec_hard.draw(self.win)

            easy = Text(Point(500,200),"Easy")
            hard = Text(Point(500,500),"Hard")

            easy.setSize(20)
            hard.setSize(20)

            easy.setTextColor("Red")
            hard.setTextColor("Brown")

            easy.setStyle("bold")
            hard.setStyle("bold")

            easy.draw(self.win)
            hard.draw(self.win)

            mouse = self.win.getMouse()
            mouse_x = mouse.getX()
            mouse_y = mouse.getY()

            if 400 <= mouse_x <= 600 and 150 <= mouse_y <= 250:
                rec_easy.undraw()
                rec_hard.undraw()
                easy.undraw()
                hard.undraw()
                ask.undraw()

                return "easy"


            elif 400 <= mouse_x <= 600 and 450 <= mouse_y <= 550:

                rec_easy.undraw()
                rec_hard.undraw()
                easy.undraw()
                hard.undraw()
                ask.undraw()

                return "hard"

            elif 900 <= mouse.getX() <= 1000 and 0 <= mouse.getY() <= 60:

                self.back_home = True
                rec_easy.undraw()
                rec_hard.undraw()
                easy.undraw()
                hard.undraw()
                ask.undraw()

            else:
                rec_easy.undraw()
                rec_hard.undraw()
                easy.undraw()
                hard.undraw()
                ask.undraw()

                return self.select_difficulty()

        def play_with_human(self):
            '''This function draws the interface if the user prompts "playing with human" when "selecting opponent"'''

            ask = Text(Point(300,50),"Please enter your name and your partner's name")
            ask.setSize(15)
            ask.setStyle("bold italic")
            ask.draw(self.win)

            name1 = Text(Point(450,150),"Please enter Player1's name here (max. 10 letters)")
            name1.setSize(15)
            name1.setStyle("bold")
            self.user_name1 = Entry(Point(500,200),40)
            self.user_name1.setText("Player 1")

            name2 = Text(Point(450,250),"Please enter Player2's name here (max. 10 letters)")
            name2.setSize(15)
            name2.setStyle("bold")
            self.user_name2 = Entry(Point(500,300),40)
            self.user_name2.setText("Player 2")

            enter_rectangle = Rectangle(Point(450,350),Point(550,450))
            enter_rectangle.setFill(color_rgb(224,224,224))
            enter_rectangle.setOutline(color_rgb(224,224,224))
            enter = Text(Point(500,400),"GO!")
            enter.setSize(30)
            enter.setStyle("bold italic")
            enter.setTextColor("Red")
            enter_rectangle.draw(self.win)
            enter.draw(self.win)

            name1.draw(self.win)
            name2.draw(self.win)
            self.user_name1.draw(self.win)
            self.user_name2.draw(self.win)

            mouse = self.win.getMouse()
            x,y = mouse.getX(),mouse.getY()

            if 450 <= mouse.getX() <= 550 and 350 <= mouse.getY() <= 450:

                name1.undraw()
                name2.undraw()
                self.user_name1.undraw()
                self.user_name2.undraw()
                ask.undraw()
                enter.undraw()
                enter_rectangle.undraw()


                return True

            elif 900 <= mouse.getX() <= 1000 and 0 <= mouse.getY() <= 60:
                self.back_home = True
                name1.undraw()
                name2.undraw()
                self.user_name1.undraw()
                self.user_name2.undraw()
                ask.undraw()
                enter.undraw()
                enter_rectangle.undraw()

            else:
                name1.undraw()
                name2.undraw()
                self.user_name1.undraw()
                self.user_name2.undraw()
                ask.undraw()
                enter.undraw()
                enter_rectangle.undraw()
                
                return self.play_with_human()

        def return_home(self):
            '''This is a Boolean function to coordinate with other functions to 
            decide whether we should return_home. Note that home Button is always on.'''

            if self.back_home == True:
                self.back_home = False
                return True
            else:
                return False                


        def draw_horizontal_line(self,interval):
            '''This function draws the horizontal line.'''

            line = Line(Point(50,50+interval),Point(650,50+interval))
            line.draw(self.win)

        def draw_vertical_line(self,interval):
            '''This function draws vertical line.'''

            line = Line(Point(50+interval,50),Point(50+interval, 650))
            line.draw(self.win)

        def draw_board_say_hi(self):
            '''This function draws the board if the user wants to play with computer and 
            the user's name will be on the interface of gomoku board.'''

            for i in range(0,650,50):
                self.draw_horizontal_line(i)
                self.draw_vertical_line(i)

            self.say_hi = Text(Point(200,25),"Hi "+ self.userName+", welcome to Gomoku!")
            self.say_hi.setSize(15)
            self.say_hi.setTextColor("blue")
            self.say_hi.setStyle("bold italic")
            self.say_hi.draw(self.win)

        def draw_board_two_player_say_hi(self):
            '''This function draws the board if the user wants to play with another user
            and their names will both appear on the interface of gomoku board.'''

            self.user_name1_string = self.user_name1.getText()
            self.user_name2_string = self.user_name2.getText()

            for i in range(0,650,50):
                self.draw_horizontal_line(i)
                self.draw_vertical_line(i)


            self.say_hi_two = Text(Point(250,25),"Hi " + self.user_name1_string + " and " + self.user_name2_string + ", welcome to Gomoku!")
            self.say_hi_two.setSize(15)
            self.say_hi_two.setTextColor("blue")
            self.say_hi_two.setStyle("bold italic")
            self.say_hi_two.draw(self.win)

        

        def getWin(self):
            '''This function gets the graphics window, which could be returned for future use.'''

            return self.win

class Pieces:
    '''This class includes all the drawings and movings associated with pieces.'''

    def __init__(self):
         self.radius = 15
         self.whether_quit = False
         self.radius_locate = 3
         self.whether_first_move = True

    def get_mouse_position(self):
        ''' This function gets the position of the user's mouse click'''
        self.win = Board.getWin(board)
        self.p = self.win.getMouse()

    def get_mouse_position_player2(self):
        '''This function gets the position of the second player's mouse click'''
    	self.win = Board.getWin(board)
    	self.q = self.win.getMouse()

        

        
    def human_move_piece(self):
        '''If the mouse click is in the range of the pieceboard, then the function draws the black piece on the pieceboard and stores the position information into list1'''
        self.get_mouse_position()
        
        if 45 <= self.p.getX() <= 655 and 45 <= self.p.getY() <= 655:
            self.m = int((self.p.getX()+25)/50)*50
            self.n = int((self.p.getY()+25)/50)*50
            list1_x_position = self.m/50 -1
            list1_y_position = self.n/50 -1
            if list1[list1_y_position][list1_x_position] != -1 and list1[list1_y_position][list1_x_position] != 1:
                piece.draw_piece()
            else:
                return self.human_move_piece()
        # if the player clicks undo , the function will undraw the previous step of the computer and the human. And then the position information in list1 will be erased to 0 so that these two positions become empty ones again.
        elif 750 <= self.p.getX() <= 850 and 50 <= self.p.getY() <= 100:
            human_x_undraw,human_y_undraw = piece.get_previous_position()
           # print human_x_undraw,human_y_undraw
            piece.undraw_piece(human_x_undraw,human_y_undraw)
            computer_x_undraw,computer_y_undraw = self.x_board,self.y_board
            piece.undraw_piece(computer_x_undraw,computer_y_undraw)

            list1[int(self.y_board)/50-1][int(self.x_board)/50-1] = 0
            list1[int(human_y_undraw/50-1)][int(human_x_undraw)/50-1]=0

            return self.human_move_piece()
        # if the user clicks the quit, the function will cause the game to quit
        elif 750<= self.p.getX() <= 850 and 150 <= self.p.getY() <= 200:
            self.whether_quit = True
            print "Game over. Thank you!"
            board.win.close()
        # if the user clicks home, the game will return to its original interface and a new game will start
        elif 900 <= self.p.getX() <= 1000 and 0 <= self.p.getY() <= 60:
             self.whether_quit = True
             big_rec = Rectangle(Point(0,0),Point(1000,700))
             big_rec.setFill(color_rgb(233,186,63))
             board.say_hi.undraw()
             big_rec.draw(self.win)
             main()
        # if the user doesn't click above area, the function will only recurse and wait for the next click
        else:
            return self.human_move_piece()
    
    def player1_move_piece(self):
        '''this function execute in the same way as the fucntion above. It is just this function is used for human plays against human mode'''
        self.get_mouse_position()
        if 45 <= self.p.getX() <= 655 and 45 <= self.p.getY() <= 655:
            self.m = int((self.p.getX()+25)/50)*50
            self.n = int((self.p.getY()+25)/50)*50
            list1_x_position = self.m/50 -1
            list1_y_position = self.n/50 -1
            if list1[list1_y_position][list1_x_position] != -1 and list1[list1_y_position][list1_x_position] != 1:
                piece.draw_piece()
            else:
                return self.player1_move_piece()
        elif 750 <= self.p.getX() <= 850 and 50 <= self.p.getY() <= 100:
            human_x_undraw,human_y_undraw = piece.get_previous_position()
            piece.undraw_piece(human_x_undraw,human_y_undraw)
            # the little difference from the above fucntion is that now the undo step undraws the two players' previous steps instead of the computer's move.
            human2_x_undraw,human2_y_undraw = piece.get_previous_position_player2()
            piece.undraw_piece(human2_x_undraw,human2_y_undraw)

            list1[int(human2_y_undraw)/50-1][int(human2_x_undraw)/50-1] = 0
            list1[int(human_y_undraw/50-1)][int(human_x_undraw)/50-1]=0

            return self.player1_move_piece()
        elif 750<= self.p.getX() <= 850 and 150 <= self.p.getY() <= 200:
            self.whether_quit = True
            print "Game over. Thank you!"
            board.win.close()

        elif 900 <= self.p.getX() <= 1000 and 0 <= self.p.getY() <= 60:
             self.whether_quit = True
             big_rec = Rectangle(Point(0,0),Point(1000,700))
             big_rec.setFill(color_rgb(233,186,63))
             big_rec.draw(self.win)
             board.say_hi_two.undraw()
             main()

        else:
            return self.player1_move_piece()
    
    def player2_move_piece(self):
        ''' this function does the same thing as the above function '''
        self.get_mouse_position_player2()
        if 45 <= self.q.getX() <= 655 and 45 <= self.q.getY() <= 655:
            self.j = int((self.q.getX()+25)/50)*50
            self.k = int((self.q.getY()+25)/50)*50
            list1_x_position = self.j/50 -1
            list1_y_position = self.k/50 -1
            if list1[list1_y_position][list1_x_position] != -1 and list1[list1_y_position][list1_x_position] != 1:
                piece.draw_piece_player2()
            else:
                return self.player2_move_piece()
        elif 750 <= self.q.getX() <= 850 and 50 <= self.q.getY() <= 100:
            human_x_undraw,human_y_undraw = piece.get_previous_position()
            piece.undraw_piece(human_x_undraw,human_y_undraw)
            human2_x_undraw,human2_y_undraw = piece.get_previous_position_player2()
            piece.undraw_piece(human2_x_undraw,human2_y_undraw)

            list1[int(human2_y_undraw)/50-1][int(human2_x_undraw)/50-1] = 0
            list1[int(human_y_undraw/50-1)][int(human_x_undraw)/50-1]=0

            return self.player2_move_piece()
        elif 750<= self.q.getX() <= 850 and 150 <= self.q.getY() <= 200:
            self.whether_quit = True
            print "Game over. Thank you!"
            board.win.close()

        elif 900 <= self.q.getX() <= 1000 and 0 <= self.q.getY() <= 60:
             self.whether_quit = True
             big_rec = Rectangle(Point(0,0),Point(1000,700))
             big_rec.setFill(color_rgb(233,186,63))
             big_rec.draw(self.win)
             board.say_hi_two.undraw()
             main()

        else:
            return self.player2_move_piece()
    def ifClose(self):
        ''' this function returns the condition of whether quit or not'''
        return self.whether_quit

    def computer_move_piece_easy(self):
        ''' this function is applied to easy mode, and the computer compares the relative value of offense (the largest value from list2) and the value of offense(the largest value from the list3) and makes the move.'''
        list2_local = available_place_easy(list1,list2)
        list3_local = check_black_easy(list1,list3)
        self.x_board ,self.y_board = int(choose_white_easy(list2_local,list3_local)[0]),int(choose_white_easy(list2_local,list3_local)[1])
        computer.beginning_white(self.x_board,self.y_board)
        # after computer's move, the function stores the position information of the computer to list1
        list1[int(self.y_board)/50-1][int(self.x_board)/50-1]= -1
    def computer_move_piece_hard(self):
        '''this function does the same thing as the above function and the only difference is this function is applied to hard mode.'''
    	list2_local = available_place_hard(list1,list2)
    	list3_local = check_black_hard(list1,list3)
    	self.x_board ,self.y_board = int(choose_white_hard(list2_local,list3_local)[0]),int(choose_white_hard(list2_local,list3_local)[1])
    	computer.beginning_white(self.x_board,self.y_board)
    	list1[int(self.y_board)/50-1][int(self.x_board)/50-1]= -1    


    def draw_piece(self):    
        ''' this function is used to draw the black pieces'''
        circle1 = Circle(Point(self.m,self.n),self.radius)
        circle1.setFill("black")

        self.circle_locate_black = Circle(Point(self.m,self.n),self.radius_locate)
        self.circle_locate_black.setFill("white")
        self.circle_locate_black.setOutline("white")
        
        if 45 <= self.p.getX() <= 655 and 45 <= self.p.getY() <= 655:
            circle1.draw(self.win)
            self.circle_locate_black.draw(self.win)

            list1[self.n/50-1][self.m/50-1] = 1

    def draw_piece_player2(self):
        ''' this function is used to draw white piece for player2 in the human plays against human mode'''
    	circle2 = Circle(Point(self.j,self.k),self.radius)
    	circle2.setFill("white")
        circle2.setOutline("white")
        self.circle_locate_white = Circle(Point(self.j,self.k),self.radius_locate)
        self.circle_locate_white.setFill("dark green")
        self.circle_locate_white.setOutline("dark green")

    	if 45 <= self.p.getX() <= 655 and 45 <= self.p.getY() <= 655:
            circle2.draw(self.win)
            self.circle_locate_white.draw(self.win)

            list1[self.k/50-1][self.j/50-1] = -1

    def undraw_locate_white(self):
        '''this function undraws the white piece'''
        if self.whether_first_move:
            self.whether_first_move = False

        else:
            self.circle_locate_white.undraw()

    def undraw_locate_black(self):
        ''' this function undraws the black piece'''

        self.circle_locate_black.undraw()

    def get_previous_position(self):
        '''this function returns the position of the player's previous move's piece's centerpoint'''

        return self.m, self.n
    def get_previous_position_player2(self):
        '''this function returns the position of the player2's previous move's piece's centerpoint'''
    	return self.j , self.k


    
    def undraw_piece(self,x,y):
        '''this function undraws the pieces'''

        self.undraw_rectangle = Rectangle(Point(x-15,y-15),Point(x+15,y+15))
        self.undraw_rectangle.setFill(color_rgb(233,186,63))
        self.undraw_rectangle.setOutline(color_rgb(233,186,63))
        self.undraw_rectangle.draw(self.win)

        self.undraw_line_x = Line(Point(x-15,y),Point(x+15,y))
        self.undraw_line_y = Line(Point(x,y-15),Point(x,y+15))

        self.undraw_line_x.draw(self.win)
        self.undraw_line_y.draw(self.win)

class Button:
    '''Draws the undo button and quit button. Home button is drawn in Board class.'''

    def __init__(self):
        self.win = Board.getWin(board)
        self.half_width = 50
        self.half_height = 25
        self.center1 = Point(800,75)
        self.center2 = Point(800,175)
        
    def draw_rect(self):
        '''this function draws the buttons on the screen'''    
        self.rect1 = Rectangle(Point(750,50),Point(850,100))
        self.rect2 = Rectangle(Point(750,150),Point(850,200))
        
        self.rect1.setFill(color_rgb(255,255,204))
        self.rect2.setFill(color_rgb(255,255,204))
        self.rect1.setOutline(color_rgb(255,255,204))
        self.rect2.setOutline(color_rgb(255,255,204))

        self.rect1.draw(self.win)
        self.rect2.draw(self.win)

        self.label1 = Text(self.center1,"UNDO")
        self.label2 = Text(self.center2,"QUIT")
        self.label1.setSize(15)
        self.label2.setSize(15)
        self.label1.setTextColor("Brown")
        self.label2.setTextColor("Brown")
        self.label1.setStyle("bold")
        self.label2.setStyle("bold")

        self.label1.draw(self.win)
        self.label2.draw(self.win)

class Computer:
    '''This class draws the decision made by computer.'''

    def __init__(self):
        self.win = Board.getWin(board)
        self.whether_human_first_move = True
        self.computer_first_move = True

    def beginning_white(self,xPoistion,yPosition):
        ''' this function is used to draw white piece'''
        whiteCircle = Circle(Point(xPoistion,yPosition),15)
        whiteCircle.setFill("white")
        whiteCircle.setOutline("white")
        whiteCircle.draw(self.win)

        self.circle_locate_computer = Circle(Point(xPoistion,yPosition),3)
        self.circle_locate_computer.setFill("dark green")
        self.circle_locate_computer.setOutline("dark green")
        self.circle_locate_computer.draw(self.win)

    def undraw_locate(self):
        '''determine whether it is first move for human and undraw the location marks '''
        if self.whether_human_first_move == True:
            self.whether_human_first_move = False

        else:

            self.circle_locate_computer.undraw()

class CheckFive:
    '''This class checks whether any side wins.'''
    

    def __init__(self):

        self.win = Board.getWin(board)
        self.choose = Text(Point(825,550),"You can either quit or home.")
        self.choose.setSize(20)
        self.choose.setStyle("bold")
        self.choose.setTextColor("Dark Green")

    def check_computer(self,list1):
        ''' this function check if there are already five pieces in a line(the winning condition) of either white or black pieces'''


        self.win_the_game = Text(Point(820,500),"Uh..you beat me.")
        self.lose_the_game = Text(Point(820,500),"Haha, you lose.")
        self.win_the_game.setSize(20)
        self.lose_the_game.setSize(20)
        self.win_the_game.setStyle("bold")
        self.lose_the_game.setStyle("bold")
        self.win_the_game.setTextColor("Dark Green")
        self.lose_the_game.setTextColor("Red")

        for row in range( len(list1) ):
            for col in range( len(list1)-4 ):
                if (list1[row][col] == list1[row][col+1] == list1[row][col+2] == list1[row][col+3] == list1[row][col+4]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.win_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.lose_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        

        for col in range( len(list1) ):
            for row in range( len(list1)-4 ):
                if (list1[row][col] == list1[row+1][col] == list1[row+2][col] == list1[row+3][col] == list1[row+4][col]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.win_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.lose_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        

        for row in range( 4,len(list1)):
            for col in range( 0,len(list1)-4 ):
                if (list1[row][col] == list1[row-1][col+1] == list1[row-2][col+2] == list1[row-3][col+3] == list1[row-4][col+4]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.win_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.lose_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        
                
        for row in range( 0,len(list1)-4):
            for col in range( 0,len(list1)-4):
                if (list1[row][col] == list1[row+1][col+1] == list1[row+2][col+2] == list1[row+3][col+3] == list1[row+4][col+4]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.win_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.lose_the_game.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        return False

    def after_game_computer(self):
        '''this function enables you to either quit or go to home after each human's move against computer.'''

        if piece.whether_quit == False:
            mouse = self.win.getMouse()
            mouse_x,mouse_y = mouse.getX(),mouse.getY()

            if 900 <= mouse_x <= 1000 and 0 <= mouse_y <= 60:
                piece.whether_quit = True
                big_rec = Rectangle(Point(0,0),Point(1000,700))
                big_rec.setFill(color_rgb(233,186,63))
                board.say_hi.undraw()
                big_rec.draw(self.win)
                main()

            elif 750 <= mouse_x <= 850 and 150 <= mouse_y <= 200:
                piece.whether_quit = True
                self.win.close()

            else:
                return self.after_game_computer()

    def check_two_human(self,list1):
        ''' this function checks which side of the two human players wins the game(forming five pieces in a line)'''
        user_name1 = board.user_name1_string
        user_name2 = board.user_name2_string

        self.black_win = Text(Point(825,450),user_name1+ " VICTORY!") 
        self.white_win = Text(Point(825,450),user_name2+ " VICTORY!")      
        self.white_win.setSize(20)
        self.black_win.setSize(20)
        self.white_win.setStyle("bold")
        self.black_win.setStyle("bold")
        self.white_win.setTextColor("Dark Green")
        self.black_win.setTextColor("Dark Green")

        for row in range( len(list1) ):
            for col in range( len(list1)-4 ):
                if (list1[row][col] == list1[row][col+1] == list1[row][col+2] == list1[row][col+3] == list1[row][col+4]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.black_win.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.white_win.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        

        for col in range( len(list1) ):
            for row in range( len(list1)-4 ):
                if (list1[row][col] == list1[row+1][col] == list1[row+2][col] == list1[row+3][col] == list1[row+4][col]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.black_win.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.white_win.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        

        for row in range( 4,len(list1)):
            for col in range( 0,len(list1)-4 ):
                if (list1[row][col] == list1[row-1][col+1] == list1[row-2][col+2] == list1[row-3][col+3] == list1[row-4][col+4]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.black_win.draw(self.win)
                        self.choose.draw(self.win)
                    else:
                        self.white_win.draw(self.win)
                        self.choose.draw(self.win)
                    return True
        
                
        for row in range( 0,len(list1)-4):
            for col in range( 0,len(list1)-4):
                if (list1[row][col] == list1[row+1][col+1] == list1[row+2][col+2] == list1[row+3][col+3] == list1[row+4][col+4]) and list1[row][col] != 0:
                    if list1[row][col]== 1:
                        self.black_win.draw(self.win)
                    else:
                        self.white_win.draw(self.win)
                    return True
        return False

    def after_game_human(self):
        ''' this function enables you to either quit or go to home after each move's aganst the other human player'''

        if piece.whether_quit == False:
            mouse = self.win.getMouse()
            mouse_x,mouse_y = mouse.getX(),mouse.getY()

            if 900 <= mouse_x <= 1000 and 0 <= mouse_y <= 60:
                piece.whether_quit = True
                big_rec = Rectangle(Point(0,0),Point(1000,700))
                big_rec.setFill(color_rgb(233,186,63))
                board.say_hi_two.undraw()
                big_rec.draw(self.win)
                main()

            elif 750 <= mouse_x <= 850 and 150 <= mouse_y <= 200:
                piece.whether_quit = True
                self.win.close()

            else:
                return self.after_game_computer()

# list1 stores the position information of each side. in the human vs computer game mode, 0 represents no piece is at the current spot and 1 represents human's move and -1 represent computer's move. 
# in the human vs human game mode,  0 represents the empty space and 1 represent the player1's move and -1 represent player2's move.
list1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# list2 stores the evaluation of the each empty position's relative value of worthiness of offense at current spot, and the spot with the highest value has the first priority of computer's move to attack.
list2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# list3 stores the evaluation of each empty position's value of worthiness of defense at current spot, and the spot with the highest value has the first priority for the computer to defend.
list3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def available_place_easy(list1,list2):
    ''' this function is used to evaluate each empty position's relative value of worthiness of making a attack for computer at the current spot'''
    for row in range(len(list1)):
        for column in range(len(list1)):
            # only if the empty spot(where the value in list1 is 0) is qualified to be evaluate .
            if list1[row][column] == 0:
                column_left = column
                column_right = column
                row_up = row
                row_down = row

                count_of_right = 0
                count_of_left = 0
                count_of_up = 0
                count_of_down = 0

                
                # this part of the function is used to check how many continuous white pieces that could be formed in a horizontal line when the computer moves a piece at the current position
                continue_search = True
                while column_left > 0 and continue_search:
                    if list1[row][column_left-1] == -1:
                        count_of_left += 1
                        column_left = column_left - 1
                    else:
                        continue_search = False
                continue_search = True
                while column_right < len(list1)-1 and continue_search:
                    if list1[row][column_right+1] == -1:
                        count_of_right += 1
                        column_right = column_right + 1
                    else:
                        continue_search = False
                # this part of the function is used to check how many continuous white pieces that could be formed in a vertical line when the computer moves a piece at the current position       
                continue_search = True
                while (row_up > 0) and continue_search:
                    if list1[row_up-1][column] == -1:
                        count_of_up += 1
                        row_up = row_up - 1
                        
                    else:
                        continue_search = False
                continue_search = True
                while (row_down < len(list1) -1) and continue_search:
                    if list1[row_down+1][column] == -1:
                        count_of_down += 1 
                        row_down = row_down + 1
                        
                    else:
                        continue_search = False
                
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                count_of_northeast_up = 0
                count_of_southwest_down = 0
                count_of_northwest_up = 0
                count_of_southeast_down = 0
                continue_search = True
                #  this part of the function is used to check how many continuous white pieces that could be formed in the northwest direction when the computer moves a piece at the current position
                while row_up > 0 and column_left > 0 and continue_search:
                    if list1[row_up - 1][column_left - 1] == -1:
                        count_of_northwest_up += 1
                        row_up = row_up - 1
                        column_left = column_left - 1
                        
                    else:
                        continue_search = False
                continue_search = True
                while row_down <len(list1)-1 and column_right < len(list1) - 1 and continue_search:
                    if list1[row_down + 1][column_right + 1] == -1:
                        count_of_southeast_down += 1
                        row_down += 1
                        column_right += 1
                        
                    else:
                        continue_search = False

                continue_search = True
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                # this part of the function is used to check how many continuous white pieces that could be formed in the northeast direction when the computer moves a piece at the current position
                while row_down < len(list1)-1 and column_left > 0 and continue_search:
                    if list1[row_down + 1][column_left - 1] == -1:
                        count_of_southwest_down += 1
                        row_down += 1
                        column_left = column_left - 1
                    else:
                        continue_search = False
                continue_search = True

                while row_up > 0 and column_right < len(list1)-1 and continue_search:
                    if list1[row_up - 1][column_right +1] == -1:
                        count_of_northeast_up += 1
                        row_up = row_up - 1
                        column_right += 1
                    else:
                        continue_search = False

                total_count_horizontal = count_of_left + count_of_right + 1
                total_count_vertical = count_of_up + count_of_down + 1
                total_count_northwest = count_of_northwest_up + count_of_southeast_down + 1
                total_count_northeast = count_of_northeast_up + count_of_southwest_down + 1
                total_value = 0
                value = 0
                # each length are assigned a different value and then we sum up the total value from all the four directions 
                for i in [total_count_horizontal,total_count_vertical,total_count_northwest,total_count_northeast]:
                    if i == 1:
                        value = 2
                    elif i == 2:
                        value = 20
                    elif i == 3:
                        value = 550
                    elif i == 4:
                        value = 2000
                    elif i == 5:
                        value = 20000
                    total_value = total_value + value
                list2[row][column] = total_value
            else:
                # place that is already not empty will not will assigned a value.
                list2[row][column] = None
    return list2

def available_place_hard(list1,list2):
    '''this fucntion evaluates each position's value basically as the above function does with a little difference of counting'''
    for row in range(len(list1)):
        for column in range(len(list1)):
            if list1[row][column] == 0:
                column_left = column
                column_right = column
                row_up = row
                row_down = row

                count_of_right = 0
                count_of_left = 0
                count_of_up = 0
                count_of_down = 0
                

                
                continue_search = True

                # now different from the above function, we also count if there are blocks by the humna's pieces at the end of the continous white pieces in the horizontal direction.
                empty_horizontal = 0
                while column_left > 0 and continue_search:
                    if list1[row][column_left-1] == -1:
                        count_of_left += 1
                        column_left = column_left - 1
                    elif list1[row][column_left-1] == 0:
                        empty_horizontal = 1
                        continue_search = False

                    else:
                        continue_search = False
                continue_search = True
                while column_right < len(list1)-1 and continue_search:
                    if list1[row][column_right+1] == -1:
                        count_of_right += 1
                        column_right = column_right + 1
                    elif list1[row][column_right+1] == 0:
                        empty_horizontal += 1
                        continue_search = False
                    else:
                        continue_search = False
                continue_search = True
                # now different from the above function, we also count if there are blocks by the humna's pieces at the end of the continous white pieces in the vertical direction.
                empty_vertical = 0
                while (row_up > 0) and continue_search:
                    if list1[row_up-1][column] == -1:
                        count_of_up += 1
                        row_up = row_up - 1
                    elif list1[row_up-1][column] == 0:
                        empty_vertical = 1
                        continue_search = False
                        
                    else:
                        continue_search = False
                continue_search = True
                while (row_down < len(list1) -1) and continue_search:
                    if list1[row_down+1][column] == -1:
                        count_of_down += 1 
                        row_down = row_down + 1
                    elif list1[row_down+1][column] == 0:
                        empty_vertical += 1
                        continue_search = False  
                        
                    else:
                        continue_search = False
                
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                count_of_northeast_up = 0
                count_of_southwest_down = 0
                count_of_northwest_up = 0
                count_of_southeast_down = 0
                continue_search = True
                # now different from the above function, we also count if there are blocks by the humna's pieces at the end of the continous white pieces in the northwest direction.
                empty_northwest = 0
                while row_up > 0 and column_left > 0 and continue_search:
                    if list1[row_up - 1][column_left - 1] == -1:
                        count_of_northwest_up += 1
                        row_up = row_up - 1
                        column_left = column_left - 1
                    elif list1[row_up - 1][column_left - 1] == 0:
                        empty_northwest = 1
                        continue_search = False
                        
                    else:
                        continue_search = False
                continue_search = True
                while row_down <len(list1)-1 and column_right < len(list1) - 1 and continue_search:
                    if list1[row_down + 1][column_right + 1] == -1:
                        count_of_southeast_down += 1
                        row_down += 1
                        column_right += 1
                    elif list1[row_down + 1][column_right + 1] == 0:
                        empty_northwest += 1
                        continue_search = False
                        
                    else:
                        continue_search = False
                continue_search = True
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                # now different from the above function, we also count if there are blocks by the humna's pieces at the end of the continous white pieces in the northeast direction.
                empty_northeast = 0
                while row_down < len(list1)-1 and column_left > 0 and continue_search:
                    if list1[row_down + 1][column_left - 1] == -1:
                        count_of_southwest_down += 1
                        row_down += 1
                        column_left = column_left - 1
                    elif list1[row_down + 1][column_left - 1] == 0:
                        empty_northeast = 1
                        continue_search = False
                    else:
                        continue_search = False
                continue_search = True
                while row_up > 0 and column_right < len(list1)-1 and continue_search:
                    if list1[row_up - 1][column_right +1] == -1:
                        count_of_northeast_up += 1
                        row_up = row_up - 1
                        column_right += 1
                    elif list1[row_up - 1][column_right +1] == 0:
                        empty_northeast += 1
                        continue_search = False
                    else:
                        continue_search = False

                total_count_horizontal = count_of_left + count_of_right + 1
                total_count_vertical = count_of_up + count_of_down + 1
                total_count_northwest = count_of_northwest_up + count_of_southeast_down + 1
                total_count_northeast = count_of_northeast_up + count_of_southwest_down + 1
                
                value = 0
                # now in order to evaluate each position, we need to consider both the length and the number of blocks at the end of the continuous white piece(0,1,2)
                for i in [[total_count_horizontal,empty_horizontal],[total_count_vertical,empty_vertical],[total_count_northwest,empty_northwest],[total_count_northeast,empty_northeast]]:
                    if i[0] == 5: # the position that will form 5 pieces is given the highest priority, A.
                        value += 100000#["A"]
                    elif i[0] == 4 and i[1] == 2:
                        value += 70000#["B"] the position that will form 4 pieces without blocks is given the highest priority, B.
                    elif i[0] == 4 and i[1] == 1:
                        value += 20000#["C"] the position that will form 4 pieces with one end blocked is given the second highest priority, B.
                    elif i[0] == 4 and i[1] == 0:
                        value += 1000#["E"] the position that will form 4 pieces with two end blocked is given the  priority E.
                    elif i[0] == 3 and i[1] == 2:
                        value += 20000#["C"]the position that will form 3 pieces without  blocks is given the  priority C.
                    elif i[0] == 3 and i[1] == 1:
                        value += 5000#["D"]the position that will form 3pieces with one end blocked is given the  priority D.
                    elif i[0] == 3 and i[1] == 0:
                        value += 500#["E"]the position that will form 3 pieces with two end blocked is given the  priority E.
                    elif i[0] == 2 and i[1] == 2:
                        value += 5000#["D"]the position that will form 2 pieces without blocks is given the  priority D.
                    elif i[0] == 2 and i[1] == 1:
                        value += 500#["E"] the position that will form 2 pieces with one end blocked is given the  priority E.
                    elif i[0] == 1 :
                        value += 100#["F"]the position that will form 1 piece is given the  priority F.
                list2[row][column] = value
            else:
                list2[row][column] = None

    return list2

def check_black_easy(list1,list3):
    ''' this function is used to evaluate each empty position's relative value of worthiness of making a defense for computer at the current spot and it works in the same way as the available_place_easy function'''
    for row in range(len(list1)):
        for column in range(len(list1)):
            if list1[row][column] == 0:
                column_left = column
                column_right = column
                row_up = row
                row_down = row

                count_of_right = 0
                count_of_left = 0
                count_of_up = 0
                count_of_down = 0
                count_of_northeast_up = 0
                count_of_southwest_down = 0
                count_of_northwest_up = 0
                count_of_southeast_down = 0

                
                continue_search = True

                

                while column_left > 0 and continue_search:
                    if list1[row][column_left-1] == 1:
                        count_of_left += 1
                        column_left = column_left - 1
                    else:
                        continue_search = False
                continue_search = True
                while column_right < len(list1)-1 and continue_search:
                    if list1[row][column_right+1] == 1:
                        count_of_right += 1
                        column_right = column_right + 1
                    else:
                        continue_search = False
                continue_search = True
                while (row_up > 0) and continue_search:
                    if list1[row_up-1][column] == 1:
                        count_of_up += 1
                        row_up = row_up - 1
                        
                    else:
                        continue_search = False
                continue_search = True
                while (row_down < len(list1) -1) and continue_search:
                    if list1[row_down+1][column] == 1:
                        count_of_down += 1 
                        row_down = row_down + 1
                        
                    else:
                        continue_search = False
                
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                continue_search = True
                while row_up > 0 and column_left > 0 and continue_search:
                    if list1[row_up - 1][column_left - 1] == 1:
                        count_of_northwest_up += 1
                        row_up = row_up - 1
                        column_left = column_left - 1
                        
                    else:
                        continue_search = False
                continue_search = True
                while row_down <len(list1)-1 and column_right < len(list1) - 1 and continue_search:
                    if list1[row_down + 1][column_right + 1] == 1:
                        count_of_southeast_down += 1
                        row_down += 1
                        column_right += 1
                        
                    else:
                        continue_search = False
                continue_search = True
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                while row_down < len(list1)-1 and column_left > 0 and continue_search:
                    if list1[row_down + 1][column_left - 1] == 1:
                        count_of_southwest_down += 1
                        row_down += 1
                        column_left = column_left - 1
                    else:
                        continue_search = False
                continue_search = True
                while row_up > 0 and column_right < len(list1)-1 and continue_search:
                    if list1[row_up - 1][column_right +1] == 1:
                        count_of_northeast_up += 1
                        row_up = row_up - 1
                        column_right += 1
                    else:
                        continue_search = False

                total_count_horizontal = count_of_left + count_of_right + 1
                total_count_vertical = count_of_up + count_of_down + 1
                total_count_northwest = count_of_northwest_up + count_of_southeast_down + 1
                total_count_northeast = count_of_northeast_up + count_of_southwest_down + 1
                total_value = 0
                value = 0
                for i in [total_count_horizontal,total_count_vertical,total_count_northwest,total_count_northeast]:
                    if i == 1:
                        value = 1
                    elif i == 2:
                        value = 10
                    elif i == 3:
                        value = 80
                    elif i == 4:
                        value = 1500
                    elif i == 5:
                        value = 8000
                    total_value = total_value + value
                list3[row][column] = total_value
            else:
                list3[row][column] = None

    return list3

def check_black_hard(list1,list3):
    ''' this function is used to evaluate each empty position's relative value of worthiness of making a defense for computer at the current spot and it works in the same way as the available_place_hard function'''
    for row in range(len(list1)):
        for column in range(len(list1)):
            if list1[row][column] == 0:
                column_left = column
                column_right = column
                row_up = row
                row_down = row

                count_of_right = 0
                count_of_left = 0
                count_of_up = 0
                count_of_down = 0
                

                
                continue_search = True

                
                empty_horizontal = 0
                while column_left > 0 and continue_search:
                    if list1[row][column_left-1] == 1:
                        count_of_left += 1
                        column_left = column_left - 1
                    elif list1[row][column_left-1] == 0:
                        empty_horizontal = 1
                        continue_search = False

                    else:
                        continue_search = False
                continue_search = True
                while column_right < len(list1)-1 and continue_search:
                    if list1[row][column_right+1] == 1:
                        count_of_right += 1
                        column_right = column_right + 1
                    elif list1[row][column_right+1] == 0:
                        empty_horizontal += 1
                        continue_search = False
                    else:
                        continue_search = False
                continue_search = True
                empty_vertical = 0
                while (row_up > 0) and continue_search:
                    if list1[row_up-1][column] == 1:
                        count_of_up += 1
                        row_up = row_up - 1
                    elif list1[row_up-1][column] == 0:
                        empty_vertical = 1
                        continue_search = False
                        
                    else:
                        continue_search = False
                continue_search = True
                while (row_down < len(list1) -1) and continue_search:
                    if list1[row_down+1][column] == 1:
                        count_of_down += 1 
                        row_down = row_down + 1
                    elif list1[row_down+1][column] == 0:
                        empty_vertical += 1
                        continue_search = False  
                        
                    else:
                        continue_search = False
                
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                count_of_northeast_up = 0
                count_of_southwest_down = 0
                count_of_northwest_up = 0
                count_of_southeast_down = 0
                continue_search = True
                empty_northwest = 0
                while row_up > 0 and column_left > 0 and continue_search:
                    if list1[row_up - 1][column_left - 1] == 1:
                        count_of_northwest_up += 1
                        row_up = row_up - 1
                        column_left = column_left - 1
                    elif list1[row_up - 1][column_left - 1] == 0:
                        empty_northwest = 1
                        continue_search = False
                        
                    else:
                        continue_search = False
                continue_search = True
                while row_down <len(list1)-1 and column_right < len(list1) - 1 and continue_search:
                    if list1[row_down + 1][column_right + 1] == 1:
                        count_of_southeast_down += 1
                        row_down += 1
                        column_right += 1
                    elif list1[row_down + 1][column_right + 1] == 0:
                        empty_northwest += 1
                        continue_search = False
                        
                    else:
                        continue_search = False
                continue_search = True
                column_left = column
                column_right = column
                row_up = row
                row_down = row
                empty_northeast = 0
                while row_down < len(list1)-1 and column_left > 0 and continue_search:
                    if list1[row_down + 1][column_left - 1] == 1:
                        count_of_southwest_down += 1
                        row_down += 1
                        column_left = column_left - 1
                    elif list1[row_down + 1][column_left - 1] == 0:
                        empty_northeast = 1
                        continue_search = False
                    else:
                        continue_search = False
                continue_search = True
                while row_up > 0 and column_right < len(list1)-1 and continue_search:
                    if list1[row_up - 1][column_right +1] == 1:
                        count_of_northeast_up += 1
                        row_up = row_up - 1
                        column_right += 1
                    elif list1[row_up - 1][column_right +1] == 0:
                        empty_northeast += 1
                        continue_search = False
                    else:
                        continue_search = False

                total_count_horizontal = count_of_left + count_of_right + 1
                total_count_vertical = count_of_up + count_of_down + 1
                total_count_northwest = count_of_northwest_up + count_of_southeast_down + 1
                total_count_northeast = count_of_northeast_up + count_of_southwest_down + 1
                
                value = 0

                for i in [[total_count_horizontal,empty_horizontal],[total_count_vertical,empty_vertical],[total_count_northwest,empty_northwest],[total_count_northeast,empty_northeast]]:
                    if i[0] == 5:
                        value += 80000#["A"]
                    elif i[0] == 4 and i[1] == 2:
                        value += 45000#["B"]
                    elif i[0] == 4 and i[1] == 1:
                        value += 16000#["C"]
                    elif i[0] == 4 and i[1] == 0:
                        value += 800#["E"]
                    elif i[0] == 3 and i[1] == 2:
                        value += 16000#["C"]
                    elif i[0] == 3 and i[1] == 1:
                        value += 4000#["D"]
                    elif i[0] == 3 and i[1] == 0:
                        value += 400#["E"]
                    elif i[0] == 2 and i[1] == 2:
                        value += 4000#["D"]
                    elif i[0] == 2 and i[1] == 1:
                        value += 400#["E"]
                    elif i[0] == 1 :
                        value += 80#["F"]
                list3[row][column] = value
            else:
                list3[row][column] = None

    return list3

def choose_white_easy(list2,list3):
    ''' this function is used to easy mode and compares the highest value from list2(offense value ) and the highest value from list3( defense value) and see what computer should do. If offense value is higher, then the computer will attack and if not, it will defend.'''
    max_value = 0
    list_white = [0,0]
    for row in range(len(list2)):
        for col in range(len(list2)):
            if available_place_easy(list1,list2)[row][col] > max_value and available_place_easy(list1,list2)[row][col] != None :
                max_value = available_place_easy(list1,list2)[row][col]
                list_white[0],list_white[1] = (col+1)*50, (row+1)*50
    max_value_black = 0
    list_black = [0,0]
    for row in range(len(list3)):
        for col in range(len(list3)):
            if check_black_easy(list1,list3)[row][col] > max_value_black and check_black_easy(list1,list3)[row][col] != None:
                max_value_black = check_black_easy(list1,list3)[row][col]
                list_black[0], list_black[1] = (col+1)*50, (row+1)*50

    if max_value > max_value_black:
        return list_white
    else:
        return list_black

def choose_white_hard(list2,list3):
    '''this function is used to easy mode and compares the highest value from list2(offense value ) and the highest value from list3( defense value) and see what computer should do. If offense value is higher, then the computer will attack and if not, it will defend.'''
    max_value = 0
    list_white = [0,0]
    for row in range(len(list2)):
        for col in range(len(list2)):
            if available_place_hard(list1,list2)[row][col] > max_value and available_place_hard(list1,list2)[row][col] != None :
                max_value = available_place_hard(list1,list2)[row][col]
                list_white[0],list_white[1] = (col+1)*50, (row+1)*50
    max_value_black = 0
    list_black = [0,0]
    for row in range(len(list3)):
        for col in range(len(list3)):
            if check_black_hard(list1,list3)[row][col] > max_value_black and check_black_hard(list1,list3)[row][col] != None:
                max_value_black = check_black_hard(list1,list3)[row][col]
                list_black[0], list_black[1] = (col+1)*50, (row+1)*50
    #print max_value
    #print max_value_black
    if max_value > max_value_black:
        return list_white
    else:
        return list_black

def simplePlay__computerFirst(piece,list1,list2,list3):
    '''This function runs the simple level and the user wants computer move first.'''
    
    computer.beginning_white(350,350)                           #computer always play in the center.
    list1[6][6] = -1
    piece.whether_quit = False                                  #Accordingly, the whether_quit has to be False and 
    computer.whether_human_first_move = False                   #human_first_move has to be False

    while not piece.ifClose() and piece.whether_quit ==  False:

        if not check_five.check_computer(list1):
            piece.human_move_piece()                            #each time when human moves a piece, the "locate" for computer's previous move
            computer.undraw_locate()                            #has to disappear
            if not check_five.check_computer(list1) and not piece.ifClose():
                piece.computer_move_piece_easy()                #Simliarly, each time when computer moves a piece, the "locate" for human's previous
                piece.undraw_locate_black()                     #move has to disappear.

            else:
                check_five.after_game_computer()

        else:
            check_five.after_game_computer()

def simplePlay_humanFirst(piece,list1,list2,list3):
    '''This function runs the simple level and the user wants to move first when playing with computer.'''

    piece.whether_quit = False                                  #computer.whether_human_first_move is by default True. (see class Computer __init__)

    while not piece.ifClose() and piece.whether_quit ==  False:

        if not check_five.check_computer(list1):
            piece.human_move_piece()
            computer.undraw_locate()
            if not check_five.check_computer(list1) and not piece.ifClose():
                piece.computer_move_piece_easy()
                piece.undraw_locate_black()

            else:
                check_five.after_game_computer()

        else:
            check_five.after_game_computer()

def hardPlay_computerFirst(piece,list1,list2,list3):
    '''This function runs the hard level and the user wants computer to move first.'''

    computer.beginning_white(350,350)
    list1[6][6] = -1
    piece.whether_quit = False
    computer.whether_human_first_move = False

    while not piece.ifClose() and piece.whether_quit ==  False:

        if not check_five.check_computer(list1):
            piece.human_move_piece()
            computer.undraw_locate()
            if not check_five.check_computer(list1) and not piece.ifClose():
                piece.computer_move_piece_easy()
                piece.undraw_locate_black()

            else:
                check_five.after_game_computer()

        else:
            check_five.after_game_computer()

def hardPlay_humanFirst(piece,list1,list2,list3):
    '''This function runs the hard level and the user wants to move first when playing with computer.'''

    piece.whether_quit = False

    while not piece.ifClose() and piece.whether_quit ==  False:

        if not check_five.check_computer(list1):
            piece.human_move_piece()
            computer.undraw_locate()
            if not check_five.check_computer(list1) and not piece.ifClose():
                piece.computer_move_piece_easy()
                piece.undraw_locate_black()

            else:
                check_five.after_game_computer()

        else:
            check_five.after_game_computer()

def play_with_human(piece,list1):
    '''This function runs when two users are playing with each other.'''

    piece.whether_quit = False

    while not piece.ifClose() and piece.whether_quit ==  False:
        if not check_five.check_two_human(list1):
            piece.player1_move_piece()
            piece.undraw_locate_white()
            if not check_five.check_two_human(list1) and not piece.ifClose():
                piece.player2_move_piece()
                piece.undraw_locate_black()

            else:
                check_five.after_game_human()

        else:
            check_five.after_game_human()
            

board = Board()
computer = Computer()
button = Button()
piece = Pieces()
check_five = CheckFive()

def main():
    '''This function includes all the inmportant functions that are needed to run the program and the main function is
    always running unless you press quit or directly close the window.'''

    for row in range(len(list1)):   #Every time we return to the main() means that we are returning to home, so we need to clean list1.
        for column in range(len(list1)):             
            list1[row][column] = 0
    board.home()
    board.instructions()

    if board.select_opponent() == "play with computer":     #We write in "if,elif,else" format in main() blocks to make sure the user could get to the
        if board.select_first_move() == "move second":      #next interface they want to arrive only with ONE mouse click!
            if board.select_difficulty() == "easy":         #(Please note that in each interface function, we need to get a mouse, so we have to 
                                                            #write a specific board.return_home function, which will not get mouse,
                board.draw_board_say_hi()                   #but return true or false depending on the mouse position getting in the interface.
                button.draw_rect()                          #This kind of format ensures that every useful mouse click in the interface will do something.
                simplePlay__computerFirst(piece, list1,list2,list3)

            elif board.return_home():

                return main()                               #return main() helps the user go back to the instruction page as he/she clicks home.

            else:
                board.draw_board_say_hi()
                button.draw_rect()
                hardPlay_computerFirst(piece,list1,list2,list3)                                  
               

        elif board.return_home():

            return main()

        else:
            if board.select_difficulty() == "easy": 
                board.draw_board_say_hi()                
                button.draw_rect()
                simplePlay_humanFirst(piece,list1,list2,list3)

            elif board.return_home():

                return main()

            else:
                board.draw_board_say_hi()
                button.draw_rect()
                hardPlay_humanFirst(piece,list1,list2,list3)

    elif board.return_home():

        return main()

    else:
        if board.play_with_human():
            board.draw_board_two_player_say_hi()
            button.draw_rect()
            play_with_human(piece,list1)                 
            

        elif board.return_home():

            return main()


if __name__ == "__main__":
    main()
