import tkinter as tk # import tkiker 
import winsound # import sound
import random # import random
# ---------------------------------------------------------------------------------------------------
# display window
root = tk.Tk() 
root.geometry("770x650")
frame = tk.Frame()
frame.master.title('Amazing game')
canvas = tk.Canvas(frame)
root.resizable(0,0)
# ---------------------------------------------------------------------------------------------------
# menubar
menubar = tk.Menu(frame)  
menubar.add_command(label="Welcome!") 
menubar.add_command(label="Quit!", command=quit) 
# display menubar
root.config(menu=menubar)
# ---------------------------------------------------------------------------------------------------
# images
myBackground=tk.PhotoImage(file='image/backg.png')
avatar = tk.PhotoImage(file='image/avatar.png')
monster = tk.PhotoImage(file='image/monster.png')
home = tk.PhotoImage(file='image/home.png')
key = tk.PhotoImage(file='image/key.png')
wall=tk.PhotoImage(file="image/wall.png")
heart_image=tk.PhotoImage(file="image/heart.png")
coin =tk.PhotoImage(file="image/coin.png")
congrats = tk.PhotoImage(file='image/congrats.png')
lostGame = tk.PhotoImage(file='image/gameover.png')
lost = tk.PhotoImage(file="image/lost.png")
start = tk.PhotoImage(file='image/start.png')
win = tk.PhotoImage(file='image/win.png')
# ---------------------------------------------------------------------------------------------------



# ---------------------------------------
# CONSTANTS
EMPTY_CELL = 0
PLAYER_CELL = 1
MONSTER_CELL = 2 
HOME_CELL = 3
KEY_CELL = 4
COIN_CELL = 5
WALL_CELL = 6
# ---------------------------------------

# ---------------------------------------
# VARIABLES
lives = 3
score = 0
levels = 1
# ---------------------------------------

# -------------------------------------------
#Boolean
hasKey = False
hasNoKey = False
end = False
isWin = False
restart = False
# -------------------------------------------

# levels ------------------------------------------------------ 
gridLevel1 = [
    [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,6 ,5 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,6 ,6 ,6 ,5 ,5 ,5, 5, 6, 5, 0 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5, 6 ],
    [6 ,5 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,0 ,0 ,0 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,6 ,6 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,4 ,1 ,3 ,6 ,6 ,6 ,6 ,5 ,2 ,5 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,0 ,0 ,0 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,0 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ],
    [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
]
gridLevel2  = [
    [6 ,6 ,6 ,6 ,0 ,0 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,6 ,5 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,6 ,6 ,6 ,5 ,5 ,5, 5, 6, 5, 0 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5, 6 ],
    [6 ,5 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,4 ,0 ,3 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,6 ,6 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,0 ,1 ,0 ,6 ,6 ,6 ,6 ,5 ,2 ,5 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,0 ,0 ,0 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ],
    [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
]
# ---------------------------------------------------------------------------------------------------
# drawing

def slide1():
    canvas.create_image(380,320,image=start)
slide1()

if levels == 1:
        grid = gridLevel1
if levels == 2:
        grid = gridLevel2

def drawGrid():
    global end,lives,restart,grid,levels
    canvas.delete('all')
    canvas.create_image(380,320, image=myBackground)
    canvas.create_text(330,30,text='Lives: ',font=('share',18,'bold'),fill='white')
    # -------------------------------------------- draw heart -------------------------------------------
    if lives == 3:
        heart1 = canvas.create_image(380,30,image=heart_image)
        heart2 = canvas.create_image(420,30,image=heart_image)
        heart3 = canvas.create_image(460,30,image=heart_image)
    elif lives == 2:
        heart1 = canvas.create_image(380,30,image=heart_image)
        heart2 = canvas.create_image(420,30,image=heart_image)
    elif lives == 1:
        heart1 = canvas.create_image(380,30,image=heart_image)
    # -------------------------------------------- draw heart -------------------------------------------
    # -------------------------------------------- levels -----------------------------------------------
    # -------------------------------------------- levels -----------------------------------------------
    canvas.create_text(620,30,text='Levels: ' + str(levels),font=('Arial',18,'bold'),fill='white') # show level
    canvas.create_text(150,30,text='Score: ' + str(score),font=('Arial',18,'bold'),fill='white') # show score
    # -------------------------------------------- display message ---------------------------------------
    if hasNoKey:
        textKey = canvas.create_text(380,70,text='You has no key, you need to find key!',font=('Arial',18,'bold'),fill='white') 
    if hasKey and not hasNoKey:
        textKey = canvas.create_text(380,70,text='You has key, you can go home now!',font=('Arial',18,'bold'),fill='white')
    if hasNoKey and hasKey:
        canvas.itemconfig(textKey,text='You has key, you can go home now!')
    if hasKey:
        textKey = canvas.create_text(380,70,text='You has key, you can go home now!',font=('Arial',18,'bold'),fill='white')
    # -------------------------------------------- display message ---------------------------------------

    # ------------------------------------------ end game ------------------------------------------------
    if end:
        getStatus()
    # ------------------------------------------ end game ------------------------------------------------

    # ------------------------------------------ restart game ------------------------------------------------
    if restart and not end:
        restartGame()
    x=10
    y=100
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == EMPTY_CELL:
                canvas.create_rectangle(x,y,x+30,y+30,fill='',outline='')
            elif grid[row][col] == PLAYER_CELL:
                canvas.create_image(x+15,y+15,image = avatar,anchor='center')   
            elif grid[row][col] == MONSTER_CELL:
                canvas.create_image(x+15,y+15,image = monster,anchor='center')      
            elif grid[row][col] == HOME_CELL:
                canvas.create_image(x+15,y+15,image = home,anchor='center')
            elif grid[row][col] == KEY_CELL:
                canvas.create_image(x+15,y+15,image = key,anchor='center')  
            elif grid[row][col] == COIN_CELL:
                canvas.create_image(x+15,y+15,image = coin,anchor='center') 
            elif grid[row][col]== WALL_CELL:
                canvas.create_image(x+15,y+15,image= wall,anchor='center')           
            x+=30
        x=10
        y+=30
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# move monster
def getMonster(grid):
    indexEnemy = []
    for row in range (len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == MONSTER_CELL:
                indexEnemy.append([row, col])
    return indexEnemy

def moveInGrid(grid,monsterY,monsterX):
    moveMonster = []
    if (grid[monsterY][monsterX-1] == COIN_CELL or grid[monsterY][monsterX-1] == EMPTY_CELL or grid[monsterY][monsterX-1] == PLAYER_CELL) and grid[monsterY][monsterX-1] != WALL_CELL:
        moveMonster.append('left')
    if (grid[monsterY][monsterX+1] == COIN_CELL or grid[monsterY][monsterX+1] == EMPTY_CELL or grid[monsterY][monsterX+1] == PLAYER_CELL) and grid[monsterY][monsterX+1] != WALL_CELL :
        moveMonster.append('right')
    if (grid[monsterY-1][monsterX] == COIN_CELL or grid[monsterY-1][monsterX] == EMPTY_CELL or grid[monsterY-1][monsterX] == PLAYER_CELL) and grid[monsterY-1][monsterX] != WALL_CELL:
        moveMonster.append('up')
    if (grid[monsterY+1][monsterX] == COIN_CELL or grid[monsterY+1][monsterX] == EMPTY_CELL or grid[monsterY+1][monsterX] == PLAYER_CELL) and grid[monsterY+1][monsterX] != WALL_CELL :
        moveMonster.append('down')
    return moveMonster

def monsterCanMove():
    global grid,lives,end,restart
    if lives <= 0:
        end = True
    indexEmeny = getMonster(grid)
    for move in indexEmeny:
        monsterY = move[0]
        monsterX = move[1]
        postionToGo = moveInGrid(grid,monsterY,monsterX)
        if len(postionToGo) > 0:
            moveMonster = random.choice(postionToGo)
            if moveMonster == 'left':
                if grid[monsterY][monsterX-1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX-1] = MONSTER_CELL
                if grid[monsterY][monsterX-1] == COIN_CELL:
                    grid[monsterY][monsterX] = COIN_CELL
                    grid[monsterY][monsterX-1] = MONSTER_CELL
                elif grid[monsterY][monsterX-1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX-1] = MONSTER_CELL
                elif grid[monsterY][monsterX-1] == PLAYER_CELL and lives >= 0:
                    lostLife(monsterY,monsterX-1)
                    restart = True
            if moveMonster == 'right':
                if grid[monsterY][monsterX+1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                if grid[monsterY][monsterX+1] == COIN_CELL:
                    grid[monsterY][monsterX] = COIN_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                elif grid[monsterY][monsterX+1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                elif grid[monsterY][monsterX+1] == PLAYER_CELL and lives >= 0:
                    lostLife(monsterY,monsterX+1)
                    restart = True
            if moveMonster == 'up':
                if grid[monsterY-1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                if grid[monsterY-1][monsterX] == COIN_CELL:
                    grid[monsterY][monsterX] = COIN_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                elif grid[monsterY-1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                elif grid[monsterY-1][monsterX] == PLAYER_CELL and lives >= 0:
                    lostLife(monsterY-1,monsterX)
                    restart = True

            if moveMonster == 'down':
                if grid[monsterY+1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                if grid[monsterY+1][monsterX] == COIN_CELL:
                    grid[monsterY][monsterX] = COIN_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                elif grid[monsterY+1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                elif grid[monsterY+1][monsterX] == PLAYER_CELL and lives >= 0:
                    lostLife(monsterY+1,monsterX)
                    restart = True

    drawGrid()
    canvas.after(500,monsterCanMove)
canvas.after(500,monsterCanMove)
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# move player

def getPlayerY():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                index = row
    return index

def getPlayerX():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                index = col
    return index

def move(moveX, moveY) :
    global lives,score,hasNoKey,hasKey,end,isWin,restart,levels
    playerX = getPlayerX()
    playerY = getPlayerY()
    newPlayerX = playerX + moveX
    newPlayerY = playerY + moveY 
    if grid[newPlayerY][newPlayerX] != WALL_CELL :
        if grid[newPlayerY][newPlayerX] == COIN_CELL: # count score
                score += 10 
                # winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
        if grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = MONSTER_CELL
                restart = True
        if moveX == 1 and moveY == 0: # move right -------------------------------------------------------------  
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True  
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True 
                isWin = True  
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                hasNoKey = True
                grid[newPlayerY][newPlayerX] = HOME_CELL
                grid[playerY][playerX] = PLAYER_CELL               
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                lostLife(playerY,playerX)
            elif newPlayerX < len(grid[0]):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
                
        if moveX == -1 and moveY == 0: # move left -------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True  
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True 
                isWin = True  
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                hasNoKey = True
                grid[newPlayerY][newPlayerX] = HOME_CELL
                grid[playerY][playerX] = PLAYER_CELL               
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                lostLife(playerY,playerX)
            elif newPlayerX < len(grid[0]):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL

        if moveX == 0 and moveY == 1: # move down --------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True  
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True 
                isWin = True  
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                hasNoKey = True
                grid[newPlayerY][newPlayerX] = HOME_CELL
                grid[playerY][playerX] = PLAYER_CELL               
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                lostLife(playerY,playerX)
            elif newPlayerX < len(grid[0]):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
        if moveX == 0 and moveY == -1: # move up --------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True  
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True 
                isWin = True  
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                hasNoKey = True
                grid[newPlayerY][newPlayerX] = HOME_CELL
                grid[playerY][playerX] = PLAYER_CELL               
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                lostLife(playerY,playerX)
            elif newPlayerX < len(grid[0]):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
    drawGrid()
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# restart game
def restartGame():
    global restart,hasNoKey,hasKey
    if lives >= 0:
        grid[9][12]=PLAYER_CELL
        restart = False
    drawGrid()
# ---------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------
# end game
def getStatus():
    global grid,score,levels
    grid=[]
    canvas.create_image(380,320, image=myBackground)
    if end and not isWin:
        canvas.create_image(380,440, image=lostGame)  
        canvas.create_text(380,520,text='Your score is : ' + str(score) + ' points' ,font=('Arial',30))
        canvas.create_image(380,250,image=lost)
    elif end and isWin:
        canvas.create_image(380,410, image=congrats)
        canvas.create_text(380,480,text='Your score is : ' + str(score) + ' points',font=('Arial',30))
        canvas.create_image(380,230,image=win)
        if levels <= 3:
            canvas.create_rectangle(290,510,470,550,fill='red',tags='next')
            canvas.create_text(380,530,text='Next game',font=('Arial',24),tags='next')



def next(event):
    global lives,score,hasKey,hasNoKey,end,isWin,levels,grid
    lives = 3
    score = 0
    hasKey = False
    hasNoKey = False
    end = False
    isWin = False
    levels += 1
    if levels == 2:
        grid =   [
        [6 ,6 ,6 ,6 ,0 ,0 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,6 ,5 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,6 ,6 ,6 ,5 ,5 ,5, 5, 6, 5, 0 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5, 6 ],
        [6 ,5 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,4 ,0 ,3 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,6 ,6 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,0 ,1 ,0 ,6 ,6 ,6 ,6 ,5 ,2 ,5 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,0 ,0 ,0 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,5 ,6 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ],
        [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ]]
    if levels == 3:
        grid =   [
        [6 ,6 ,6 ,6 ,0 ,0 ,0 ,0 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,6 ,5 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,6 ,6 ,6 ,5 ,5 ,5, 5, 6, 5, 0 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5, 6 ],
        [6 ,5 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,4 ,0 ,3 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,6 ,6 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,0 ,1 ,0 ,6 ,6 ,6 ,6 ,5 ,2 ,5 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,0 ,0 ,0 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,5 ,6 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,6 ],
        [6 ,5 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,5 ,5 ,6 ],
        [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ],
        [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ]]

    drawGrid()
drawGrid()

# ------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# lost lives
def lostLife(positionY,positionX):
    global lives
    lives -= 1
    grid[positionY][positionX] = EMPTY_CELL
    grid[9][12] = PLAYER_CELL
# ---------------------------------------------------------------------------------------------------

# --------------------------------------------------------
# MOVE PLAYER
def move_right(event):
    move(1,0)
def move_left(event):
    move(-1,0)
def move_down(event):
    move(0,1)
def move_up(event):
    move(0,-1)
# --------------------------------------------------------

# ---------------------------------------------------------------------------------------
# click on key board
root.bind('<Left>',move_left) #### keyboard
root.bind('<Right>',move_right) #### keyboard
root.bind('<Down>',move_down) #### keyboard
root.bind('<Up>',move_up) #### keyboard
# ---------------------------------------------------------------------------------------
canvas.tag_bind('next','<Button-1>',next)
# ---------------------------------------------------------------------------------------
# display all
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
# ---------------------------------------------------------------------------------------