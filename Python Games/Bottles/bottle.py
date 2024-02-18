b1 = ['0', 'b', 'b', 'b']
b2 = ['0', '0', 'g', 'g']
b3 = ['0', '0', 'r', 'r']
b4 = ['0', 'r', 'g', 'r']
b5 = ['0', '0', 'b', 'g']
b6 = ['0', '0', 'y', 'y']
b7 = ['0', '0', 'y', 'y']
listOfSel = [b1, b2, b3, b4, b5, b6, b7]

def checkWin():
  countOfWin = 0
  for i in listOfSel:
    if (i[0] == i[1] and i[0] == i[2] and i[0] == i[3]):
      countOfWin += 1

  if countOfWin == 7:
    return True
  return False

def showButs():
  i = 0
  while i < 4:
    print(b1[i] + '  ' + b2[i] + '  ' + b3[i] + '  ' + b4[i] + '  ' + b5[i] + '  ' + b6[i] + '  ' + b7[i])
    i += 1
  print('1  ' + '2  ' + '3  ' + '4  ' + '5  ' + '6  ' + '7')

def indexFirstBut(but:list):
  q = 0
  for w in but:
    if w != '0':
      return q
    q += 1
  return -1

def indexSecondBut(but:list):
  q = 3
  while q >= 0:
    if but[q] == '0':
      return q
    q -= 1
  return -1

def change(selectedOne:int, selectedTwo:list):
  b = listOfSel[selectedOne]
  if b is selectedTwo:
    print("I can't pour it into the same bottle.")
    return
  firstElIndex = indexFirstBut(b)
  if firstElIndex == -1:
    print('First bottle is empty')
    return
  secondElIndex = indexSecondBut(selectedTwo)
  if secondElIndex == -1:
    print('Second bottle is full')
    return
  if secondElIndex == 3 or selectedTwo[secondElIndex + 1] == b[firstElIndex]:
    selectedTwo[secondElIndex] = b[firstElIndex]
    b[firstElIndex] = '0'
  else:
    print("It's not the same color")

while True: 
  showButs()
  win = checkWin()
  if win:
    print('You Win')
    break

  firstSel = input('введите с какой колбы берем: ')
  secondSel = input('введите в какую колбу наливаем: ')
  if (secondSel == "1" or
      secondSel == "2" or
      secondSel == "3" or
      secondSel == "4" or
      secondSel == "5" or
      secondSel == "6" or
      secondSel == "7"):
    sec = listOfSel[int(secondSel) - 1]
  else:
    print('incorrect second input')
    continue

  if (firstSel != '1' and firstSel != '2' and 
      firstSel != '3' and firstSel != '4' and 
      firstSel != '5' and firstSel != '6' and 
      firstSel != '7'):
    print('incorrect first input')
    continue
  
  change(int(firstSel) - 1, sec)