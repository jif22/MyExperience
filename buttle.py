b1 = ['0', 'b', 'b', 'b']
b2 = ['0', '0', 'g', 'g']
b3 = ['0', 'r', 'r', 'r']
b4 = ['0', '0', 'g', 'b']
b5 = ['0', '0', 'g', 'r']
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False

def checkWin():
  if (b1[0] == b1[1] and b1[0] == b1[2] and b1[0] == b1[3]):
    flag1 = True
  else:
    flag1 = False
  if (b2[0] == b2[1] and b2[0] == b2[2] and b2[0] == b2[3]):
    flag2 = True
  else:
    flag2 = False
  if (b3[0] == b3[1] and b3[0] == b3[2] and b3[0] == b3[3]):
    flag3 = True
  else:
    flag3 = False
  if (b4[0] == b4[1] and b4[0] == b4[2] and b4[0] == b4[3]):
    flag4 = True
  else:
    flag4 = False
  if (b5[0] == b5[1] and b5[0] == b5[2] and b5[0] == b5[3]):
    flag5 = True
  else:
    flag5 = False
  
  if (flag1 and flag2 and flag3 and flag4 and flag5):
    return True
  return False

def showButs():
  i = 0
  while i < 4:
    print(b1[i] + '  ' + b2[i] + '  ' + b3[i] + '  ' + b4[i] + '  ' + b5[i])
    i += 1
  print('1  ' + '2  ' + '3  ' + '4  ' + '5')

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

while True: 
  showButs()
  win = checkWin()
  if win:
    print('You Win')
    break

  firstSel = input('введите с какой колбы берем: ')
  secondSel = input('введите в какую колбу наливаем: ')
  if secondSel == '1':
    sec = b1
  elif secondSel == '2':
    sec = b2
  elif secondSel == '3':
    sec = b3
  elif secondSel == '4':
    sec = b4
  elif secondSel == '5':
    sec = b5
  else:
    print('incorrect second input')
    continue

  if firstSel != '1' and firstSel != '2' and firstSel != '3' and firstSel != '4' and firstSel != '5':
    print('incorrect first input')
    continue
  
# ----------------------------------
  if firstSel == '1':
    if b1 is sec:
      print("I can't pour it into the same bottle.")
      continue
    firstElIndex = indexFirstBut(b1)
    if firstElIndex == -1:
      print('First bottle is empty')
      continue
    secondElIndex = indexSecondBut(sec)
    if secondElIndex == -1:
      print('Second bottle is full')
      continue
    if secondElIndex == 3 or sec[secondElIndex + 1] == b1[firstElIndex]:
      sec[secondElIndex] = b1[firstElIndex]
      b1[firstElIndex] = '0'
    else:
      print("It's not the same color")
    

# ----------------------------------
  elif firstSel == '2':
    if b2 is sec:
      print("I can't pour it into the same bottle.")
      continue
    firstElIndex = indexFirstBut(b2)
    if firstElIndex == -1:
      print('First bottle is empty')
      continue
    secondElIndex = indexSecondBut(sec)
    if secondElIndex == -1:
      print('Second bottle is full')
      continue
    if secondElIndex == 3 or sec[secondElIndex + 1] == b2[firstElIndex]:
      sec[secondElIndex] = b2[firstElIndex]
      b2[firstElIndex] = '0'
    else:
      print("It's not the same color")

# ----------------------------------
  elif firstSel == '3':
    if b3 is sec:
      print("I can't pour it into the same bottle.")
      continue
    firstElIndex = indexFirstBut(b3)
    if firstElIndex == -1:
      print('First bottle is empty')
      continue
    secondElIndex = indexSecondBut(sec)
    if secondElIndex == -1:
      print('Second bottle is full')
      continue
    if secondElIndex == 3 or sec[secondElIndex + 1] == b3[firstElIndex]:
      sec[secondElIndex] = b3[firstElIndex]
      b3[firstElIndex] = '0'
    else:
      print("It's not the same color")

# ----------------------------------
  elif firstSel == '4':
    if b4 is sec:
      print("I can't pour it into the same bottle.")
      continue
    firstElIndex = indexFirstBut(b4)
    if firstElIndex == -1:
      print('First bottle is empty')
      continue
    secondElIndex = indexSecondBut(sec)
    if secondElIndex == -1:
      print('Second bottle is full')
      continue
    if secondElIndex == 3 or sec[secondElIndex + 1] == b4[firstElIndex]:
      sec[secondElIndex] = b4[firstElIndex]
      b4[firstElIndex] = '0'
    else:
      print("It's not the same color")

# ----------------------------------
  elif firstSel == '5':
    if b5 is sec:
      print("I can't pour it into the same bottle.")
      continue
    
    firstElIndex = indexFirstBut(b5)
    if firstElIndex == -1:
      print('First bottle is empty')
      continue
    secondElIndex = indexSecondBut(sec)
    if secondElIndex == -1:
      print('Second bottle is full')
      continue
    if secondElIndex == 3 or sec[secondElIndex + 1] == b5[firstElIndex]:
      sec[secondElIndex] = b5[firstElIndex]
      b5[firstElIndex] = '0'
    else:
      print("It's not the same color")
