def sum(a,b,c):
  return a+b+c

def printboard():
  zero = 'X' if Xstate[0] else('O' if Zstate[0] else 0)
  one = 'X' if Xstate[1] else('O' if Zstate[1] else 1)
  two = 'X' if Xstate[2] else('O' if Zstate[2] else 2)
  three = 'X' if Xstate[3] else('O' if Zstate[3] else 3)
  four = 'X' if Xstate[4] else('O' if Zstate[4] else 4)
  five = 'X' if Xstate[5] else('O' if Zstate[5] else 5)
  six = 'X' if Xstate[6] else('O' if Zstate[6] else 6)
  seven = 'X' if Xstate[7] else('O' if Zstate[7] else 7)
  eight = 'X' if Xstate[8] else('O' if Zstate[8] else 8)
  print(f" {zero}  |  {one}  |  {two}  ")
  print("----|-----|-----")
  print(f" {three}  |  {four}  |  {five}  ")
  print("----|-----|-----")
  print(f" {six}  |  {seven}  |  {eight}  ")

def checkwin(Xstate,Zstate):
  wincondition=[[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for win in wincondition:
    if(sum(Xstate[win[0]],Xstate[win[1]],Xstate[win[2]])==3):
      print("X won")
      return 1

    if(sum(Xstate[win[0]],Xstate[win[1]],Xstate[win[2]])==3):
      print("O won")
      return 0
  return -1

 

Xstate = [0,0,0,0,0,0,0,0,0]
Zstate = [0,0,0,0,0,0,0,0,0]
turn = 1

while(True):
  printboard()
  if(turn == 1):
    print("X's Turn")
    val=int(input("Enter the position you want to place X: "))
    Xstate[val]=1
    
  if(turn == 0):
    print("O's Turn")
    val = int(input("Enter the position you want to place O: "))
    Zstate[val]=1
  turn = 1 - turn
  winner = checkwin(Xstate,Zstate)
    
  if(winner != -1):
    
    print("Match Over")
    break
      