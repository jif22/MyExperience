import random
from colorama import Fore, Style, Back, init

b1 = ['[' + Fore.BLUE + 'b' + Style.RESET_ALL + ']', '[' + Fore.BLUE + 'b' + Style.RESET_ALL + ']', '[' + Fore.BLUE + 'b' + Style.RESET_ALL + ']', '[' + Fore.BLUE + 'b' + Style.RESET_ALL + ']']
b2 = ['[' + Fore.GREEN + 'g' + Style.RESET_ALL + ']', '[' + Fore.GREEN + 'g' + Style.RESET_ALL + ']', '[' + Fore.GREEN + 'g' + Style.RESET_ALL + ']', '[' + Fore.GREEN + 'g' + Style.RESET_ALL + ']']
b3 = ['[' + Fore.RED + 'r' + Style.RESET_ALL + ']', '[' + Fore.RED + 'r' + Style.RESET_ALL + ']', '[' + Fore.RED + 'r' + Style.RESET_ALL + ']', '[' + Fore.RED + 'r' + Style.RESET_ALL + ']']
b4 = ['[' + Fore.WHITE + 'w' + Style.RESET_ALL + ']', '[' + Fore.WHITE + 'w' + Style.RESET_ALL + ']', '[' + Fore.WHITE + 'w' + Style.RESET_ALL + ']', '[' + Fore.WHITE + 'w' + Style.RESET_ALL + ']']
b5 = ['[' + Fore.LIGHTBLACK_EX + 'a' + Style.RESET_ALL + ']', '[' + Fore.LIGHTBLACK_EX + 'a' + Style.RESET_ALL + ']', '[' + Fore.LIGHTBLACK_EX + 'a' + Style.RESET_ALL + ']', '[' + Fore.LIGHTBLACK_EX + 'a' + Style.RESET_ALL + ']']
b6 = ['[' + Fore.CYAN + 'c' + Style.RESET_ALL + ']', '[' + Fore.CYAN + 'c' + Style.RESET_ALL + ']', '[' + Fore.CYAN + 'c' + Style.RESET_ALL + ']', '[' + Fore.CYAN + 'c' + Style.RESET_ALL + ']']
b7 = ['[' + Fore.YELLOW + 'y' + Style.RESET_ALL + ']', '[' + Fore.YELLOW + 'y' + Style.RESET_ALL + ']', '[' + Fore.YELLOW + 'y' + Style.RESET_ALL + ']', '[' + Fore.YELLOW + 'y' + Style.RESET_ALL + ']']
b8 = ['[' + Fore.MAGENTA + 'm' + Style.RESET_ALL + ']', '[' + Fore.MAGENTA + 'm' + Style.RESET_ALL + ']', '[' + Fore.MAGENTA + 'm' + Style.RESET_ALL + ']', '[' + Fore.MAGENTA + 'm' + Style.RESET_ALL + ']']
b9 = ['[ ]', '[ ]', '[ ]', '[ ]']
b10 = ['[ ]', '[ ]', '[ ]', '[ ]']
listOfSel = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]

def checkWin():
  countOfWin = 0
  for i in listOfSel:
    if (i[0] == i[1] and i[0] == i[2] and i[0] == i[3]):
      countOfWin += 1

  if countOfWin == 10:
    return True
  return False

def showButs():
  i = 0
  while i < 4:
    print(b1[i] + '  ' + b2[i] + '  ' + b3[i] + '  ' + b4[i] + '  ' + b5[i] + '  ' + 
          b6[i] + '  ' + b7[i] + '  ' + b8[i] + '  ' + b9[i] + '  ' + b10[i])
    i += 1
  print(' 1   ' + ' 2   ' + ' 3   ' + ' 4   ' + ' 5   ' + ' 6   ' + ' 7   ' + ' 8   ' + ' 9   ' + ' 10')

def indexFirstBut(but:list):
  q = 0
  for w in but:
    if w != '[ ]':
      return q
    q += 1
  return -1

def indexSecondBut(but:list):
  q = 3
  while q >= 0:
    if but[q] == '[ ]':
      return q
    q -= 1
  return -1

def change(selectedOne:int, selectedTwo:list):
  b = listOfSel[selectedOne]
  if b is selectedTwo:
    print(Style.BRIGHT + Fore.RED + "I can't pour it into the same bottle." + Style.RESET_ALL)
    return
  firstElIndex = indexFirstBut(b)
  if firstElIndex == -1:
    print(Style.BRIGHT + Fore.RED + 'First bottle is empty' + Style.RESET_ALL)
    return
  secondElIndex = indexSecondBut(selectedTwo)
  if secondElIndex == -1:
    print(Style.BRIGHT + Fore.RED + 'Second bottle is full' + Style.RESET_ALL)
    return
  if secondElIndex == 3 or selectedTwo[secondElIndex + 1] == b[firstElIndex]:
    selectedTwo[secondElIndex] = b[firstElIndex]
    b[firstElIndex] = '[ ]'
  else:
    print(Style.BRIGHT + Fore.RED + "It's not the same color" + Style.RESET_ALL)

def newGame():
  # Количество запутанности в начале игры.
  flag = True
  while flag:

    countOfChange = input('Введите уровень сложности от 1 до 5: ')
    if countOfChange == '1':
      countOfChange = int(countOfChange) * 10
      flag = False
    elif countOfChange == '2':
      countOfChange = int(countOfChange) * 20
      flag = False
    elif countOfChange == '3':
      countOfChange = int(countOfChange) * 30
      flag = False
    elif countOfChange == '4':
      countOfChange = int(countOfChange) * 35
      flag = False
    elif countOfChange == '5':
      countOfChange = int(countOfChange) * 40
      flag = False
    else:
      print('Некорректный ввод') 
  
  while countOfChange > 0:
    flag = True
    while flag:
      randButOne = random.choice(listOfSel)
      if randButOne[3] != '[ ]':
        flag = False
    numForOne = 0
    for i in randButOne:
      if i != '[ ]':
        tempEl = i
        break
      numForOne += 1
    flag = True
    while flag:
      randButTwo = random.choice(listOfSel)
      if randButOne is not randButTwo:
        if randButTwo[0] == '[ ]':
          flag = False
    f = 3
    while f >= 0:
      if randButTwo[f] == '[ ]':
        randButTwo[f] = tempEl
        randButOne[numForOne] = '[ ]'
        break
      f -= 1
    countOfChange -= 1

# Здесь начинается программа
init()
newGame()
while True: 
  showButs()
  win = checkWin()
  if win:
    print()
    print(Back.WHITE + '                                               ' + Back.RESET)
    print(Back.BLUE +  '                    You Win                    ' + Back.RESET)
    print(Back.RED +   '                                               ' + Back.RESET)
    print()
    break

  firstSel = input('введите с какой колбы берем: ')
  secondSel = input('введите в какую колбу наливаем: ')
  if (secondSel == "1" or
      secondSel == "2" or
      secondSel == "3" or
      secondSel == "4" or
      secondSel == "5" or
      secondSel == "6" or
      secondSel == "7" or
      secondSel == "8" or
      secondSel == "9" or
      secondSel == "10"):
    sec = listOfSel[int(secondSel) - 1]
  else:
    print(Style.BRIGHT + Fore.RED + 'incorrect second input' + Style.RESET_ALL)
    continue

  if (firstSel != '1' and firstSel != '2' and 
      firstSel != '3' and firstSel != '4' and 
      firstSel != '5' and firstSel != '6' and 
      firstSel != '7' and firstSel != '8' and 
      firstSel != '9' and firstSel != '10'):
    print(Style.BRIGHT + Fore.RED + 'incorrect first input' + Style.RESET_ALL)
    continue
  
  change(int(firstSel) - 1, sec)
input('Нажмите "Enter" для завершения программы')