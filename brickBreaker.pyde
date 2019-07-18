#By Joshua Lewis
#July 17,2019
#Brick Breaker 

#Window Size
baseSize = 500

#Object Placement
ballX = 250
ballY = 435
rectX = 200
rectY = baseSize * .90
paddleLength = 20
paddleWidth = 100

#visuals
ballColor = 255

#Speed Variables
speedX =  10
speedY = 4
directionX = speedX
directionY = speedY

#Bricks
brick1 = True
brick2 = True
brick3 = True
brick4 = True
brick5 = True
brick6 = True
brick7 = True
brick8 = True
brick9 = True
brick10 = True

#Menu + Mode
Menu = True
Easy = False
Medium = False
Hard = False
Start = False
Ready = False

#Score + Scoreboard
score = 0 

def setup():
    global baseSize
    global Easy,Medium,Hard,Start,Menu,Ready
    global ballX,ballY,rectX,rectY,rectangleWidth
    global paddleLength,paddleWidth,paddlePosition
    global directionX,directionY,speedX,speedY
    global brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9,brick10
    size(baseSize,baseSize)    #Sets size to value of baseSize
    noStroke()
    background(0)

    
def draw():
    global baseSize
    global Easy,Medium,Hard,Start,Menu,Ready
    global ballX,ballY,rectX,rectY,rectangleWidth
    global paddleLength,paddleWidth,paddlePosition
    global directionX,directionY,speedX,speedY
    global brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9,brick10
    background(0)
    ballTop = ballY - 12.5
    ballBottom = ballY + 12.5
    paddleLeftCorner = rectX
    paddleRightCorner = rectX + 100
    paddleBottom = rectY + paddleLength
    r = 0
    g = 255
    b = 0
    
    easyBoxPressed = mousePressed and mouseX > 50 and mouseX < 150 and mouseY > 250 and mouseY < 300
    mediumBoxPressed = mousePressed and mouseX > 200 and mouseX < 300 and mouseY > 250 and mouseY < 300
    hardBoxPressed = mousePressed and mouseX > 350 and mouseX < 450 and mouseY > 250 and mouseY < 300
    
    #Checks to see if any box's are pressed 
    if easyBoxPressed:
        Easy = True
        Menu = False
    elif mediumBoxPressed:
        Medium = True
        Menu = False
    elif hardBoxPressed:
        Hard = True
        Menu = False
    
    #Initailize the basic conditions of the can and of the Menu
    if Menu:
        noStroke()
        Easy = False
        Medium = False
        Hard = False
        Start = False
        Ready = False
        brick1 = True
        brick2 = True
        brick3 = True
        brick4 = True
        brick5 = True
        brick6 = True
        brick7 = True
        brick8 = True
        brick9 = True
        brick10 = True
        ballX = 250
        ballY = 435
        fill(0,255,0)
        easyBox = rect(50,250,100,50)
        fill(255,255,0)
        mediumBox = rect(200,250,100,50)
        fill(255,0,0)
        hardBox = rect(350,250,100,50)
    
    #Sets the stats for the game mode selected and starts the game 
    
    if Easy and not Ready:
        speedX = 5
        speedY = 2
        Start = True
    elif Medium and not Ready:
        speedX = 10
        speedY = 4
        Start = True

    elif Hard and not Ready:
        speedX = 20
        speedY = 8
        Start = True

    #Runs the game code
    if Start:
        noStroke()
        fill(r,g,b)
        startButton = rect(237,475,25,25)
        startButtonPressed = mousePressed and mouseX >  237 and mouseX < 262 and mouseY > 475 and mouseY < 500
        
        if(brick1 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(0,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(0,0,100,50)
            
        if(brick2 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(100,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(100,0,100,50)
        
        if(brick3 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(200,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(200,0,100,50)
    
        if(brick4 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(300,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(300,0,100,50)
        
        if(brick5 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(400,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(400,0,100,50)
        
        if(brick6 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(0,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(0,50,100,50)
            
        if(brick7 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(100,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(100,50,100,50)
        
        if(brick8 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(200,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(200,50,100,50)
    
        if(brick9 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(300,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(300,50,100,50)
        
        if(brick10 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(400,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(400,50,100,50)
            
        if startButtonPressed:
            Ready = True
            Start = False
            
        ballX = 250
        ballY = 435
        rectX = 200
        rectY = baseSize * .90
            
        #Creates ball and paddle     
        stroke(0,255,0)
        fill(ballColor) 
        ball = ellipse(ballX,ballY,25,25)
        stroke(0,255,0)
        fill(255) 
        paddle = rect(rectX,rectY,paddleWidth, paddleLength)
            
    if Ready:
        Start = False
        r = 0
        g = 0
        b = 0
        
        if(brick1 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(0,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(0,0,100,50)
            
        if(brick2 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(100,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(100,0,100,50)
        
        if(brick3 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(200,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(200,0,100,50)
    
        if(brick4 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(300,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(300,0,100,50)
        
        if(brick5 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(400,0,100,50)
        else:
            stroke(0)
            fill(0)
            rect(400,0,100,50)
        
        if(brick6 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(0,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(0,50,100,50)
            
        if(brick7 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(100,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(100,50,100,50)
        
        if(brick8 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(200,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(200,50,100,50)
    
        if(brick9 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(300,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(300,50,100,50)
        
        if(brick10 == True):
            stroke(255,0,0)
            fill(255,255,255)
            rect(400,50,100,50)
        else:
            stroke(0)
            fill(0)
            rect(400,50,100,50)
        
        if(ballTop < 50 and ballX < 100 and  brick1 == True):
            brick1 = False
            directionY = + speedY
    
        
        if(ballTop < 50 and ballX > 100 and ballX < 200 and brick2 == True):
            brick2 = False
            directionY = + speedY
    
        
        if(ballTop < 50 and ballX > 200 and ballX <  300 and brick3 == True):
            brick3 = False
            directionY = + speedY
    
            
        if(ballTop < 50 and ballX > 300 and ballX <  400 and brick4 == True):
            brick4 = False
            directionY = + speedY
    
            
        if(ballTop < 50 and ballX > 400 and ballX <  500 and brick5 == True):
            brick5 = False
            directionY = + speedY
            
        if(ballTop < 100 and ballX < 100 and  brick6 == True):
            brick6 = False
            directionY = + speedY
    
        
        if(ballTop < 100 and ballX > 100 and ballX < 200 and brick7 == True):
            brick7 = False
            directionY = + speedY
    
        
        if(ballTop < 100 and ballX > 200 and ballX <  300 and brick8 == True):
            brick8 = False
            directionY = + speedY
    
            
        if(ballTop < 100 and ballX > 300 and ballX <  400 and brick9 == True):
            brick9 = False
            directionY = + speedY
    
            
        if(ballTop < 100 and ballX > 400 and ballX <  500 and brick10 == True):
            brick10 = False
            directionY = + speedY
    
        
        ballX = ballX + directionX
        ballY = ballY + directionY
        
        if (ballX >= baseSize):
            directionX =  -speedX
        elif(ballX <= 0):
            directionX = +speedX
            
        if (ballY <= 0):
            directionY = + speedY
        elif (ballY >= 500):
            directionY = - speedY
            
        if (rectX in range(-5,405)):
            rectX = mouseX - 50 
        elif(rectX < -1):
            rectX = 1
        elif(rectX > 401):
            rectX = 399
            
        if ballBottom + 2 >= rectY and ballBottom < rectY + 20  and ballX > paddleLeftCorner and ballX < paddleRightCorner: 
            directionY = - speedY
            
        #Creates ball and paddle     
        stroke(0,255,0)
        fill(ballColor) 
        ball = ellipse(ballX,ballY,25,25)
        stroke(0,255,0)
        fill(255) 
        paddle = rect(rectX,rectY,paddleWidth, paddleLength)
                    
        #If game lost restart the game to the menu
        if ballBottom > paddleBottom:   
            Menu = True
            
        #If game won restart the game to menu 
        if(not brick1 and not brick2 and not brick3 and not brick4 and not brick5 and not brick6 and not brick7 and not brick8 and not brick9 and not brick10): 
            Menu = True
    
