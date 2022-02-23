import random

def mine_list_generator():
  gridList = []
  grid_num = 64
  while grid_num > 0:
    answer = random.randint(1, 10)
    if answer == 1:
      gridList.append("mine")
    else:
      gridList.append("safe")
    grid_num = grid_num - 1
  return gridList

def mine_dict(list): 
  grid_dict = {}
  grid_count = 1
  for grid_item in list:
    grid_dict[grid_count] = grid_item
    grid_count = grid_count + 1
#  print(grid_dict)
  return grid_dict

def mine_print_debug(gridDict):
  for k, v in gridDict.items():
    if v == "hit":
      pass
    if k % 8 == 0:
      print("%s \n" % (v))
    else:
        print(v, end=", ")     

def mine_print(gridDict):
  for k, v in gridDict.items():
    if type(v) == int:
      if k % 8 == 0:
        print("%s \n" % (v))
      else:
        print(v, end=" │ ")    
    elif v == "hit":
      pass
    elif k % 8 == 0:
      print("%s \n" % ("*"))
    else:
        print("*", end=" │ ")     

def bombcountfunc(bombcheck_list):
  bombcount = 0
  for item in bombcheck_list:
    if (gridDict[item] == "mine"):
      bombcount = bombcount + 1
  return bombcount
  
def topborder_checker(answer):
  bombcheck_list = []
  bombcheck_list.append(answer - 1)
  bombcheck_list.append(answer + 1)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer + 7)
  bombcheck_list.append(answer + 9)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def bottomborder_checker(answer):
  bombcheck_list = []
  bombcheck_list.append(answer - 1)
  bombcheck_list.append(answer + 1)
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 7)
  bombcheck_list.append(answer - 9)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def leftborder_checker(answer):
  bombcheck_list = []
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 7)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer + 9)
  bombcheck_list.append(answer + 1)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def rightborder_checker(answer):
  bombcheck_list = []
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 9)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer + 7)
  bombcheck_list.append(answer - 1)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount

def checker(answer):
  bombcheck_list = []
  bombcheck_list.append(answer - 1)
  bombcheck_list.append(answer + 1)
  bombcheck_list.append(answer + 8)
  bombcheck_list.append(answer - 8)
  bombcheck_list.append(answer - 7)
  bombcheck_list.append(answer + 7)
  bombcheck_list.append(answer + 9)  
  bombcheck_list.append(answer - 9)
  bombcount = bombcountfunc(bombcheck_list)
  return bombcount



def mine_checker(answer, gridDict):
  leftborder_list = [9,17,25,33,41,49]
  bombcount = 0
  topleft = 1
  topright = 8
  bottomleft = 57
  bottomright = 64
  if (answer == topleft):
    bombcheck_list = [2, 9, 10]
    bombcount = bombcountfunc(bombcheck_list)  
    gridDict[answer] = bombcount
  elif answer == bottomleft:
    bombcheck_list = [49,50,58]
    bombcount = bombcountfunc(bombcheck_list)
    gridDict[answer] = bombcount
  elif answer == topright:
    bombcheck_list = [7,15,16]
    bombcount = bombcountfunc(bombcheck_list)
    gridDict[answer] = bombcount
  elif answer == bottomright:
    bombcheck_list = [54,55,63]
    bombcount = bombcountfunc(bombcheck_list)
    gridDict[answer] = bombcount
  elif answer in leftborder_list:
    bombcount = leftborder_checker(answer)
    gridDict[answer] = bombcount
  elif (answer % 8 == 0):
    bombcount = rightborder_checker(answer)
    gridDict[answer] = bombcount
  elif (answer < 9):
    bombcount = topborder_checker(answer)
    gridDict[answer] = bombcount
  elif (answer > 56):
    bombcount = bottomborder_checker(answer)
    gridDict[answer] = bombcount
  else:
    bombcount = checker(answer)
    gridDict[answer] = bombcount
  return bombcount

def game_over(answer,gridDict):
  for k,v in gridDict.items():
    if gridDict[answer] == "mine":
     mine_print(gridDict,1)
     print("!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*! ")
     print("*!*!*!*!*! Game-Over !*!*!*!*!* ")
     print("!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*! ")
     quit()




  
gridList = mine_list_generator()
gridDict = mine_dict(gridList)



# mine_checker(row, gridDict)
#mine_print(gridDict)
#mine_print_debug(gridDict)

while True:
  mine_print(gridDict)
  #mine_print_debug(gridDict)
  print("we were tired okay?")
  row = input("A number between 1 and 64 please: ")
  game_over(int(row),gridDict)
  mine_checker(int(row), gridDict)
  
  








  
