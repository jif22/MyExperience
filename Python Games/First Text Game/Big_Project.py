# -*- coding: utf-8 -*-

import random as r
import pickle
from colorama import init,Fore,Style,Back

def start_ch():
	""" "инициализация", создание персонажа
		Exp-опытность, MaxHp/Hp-здоровье макс/текущее, Dmg-урон, Money-количество средств,cost-стоимость тренеровки
		raise-повышение стоимости тренеровки,Fight-количество проведенных боев,Win-количество побед
		access-доступ к бойцовскому клубу,dif-уровень сложности,def-шанс защиты,agi-шанс уворота,cri-шанс крита
	"""
	print(
	Fore.YELLOW,'Добро пожаловать',Fore.RESET,' в ',Fore.GREEN,'текстовый',
	Fore.RESET,' симулятор ',Fore.CYAN,'бойца',Fore.RESET,'.',sep=''
	)
	print()
	print(
	'Для того что бы начать ',Style.BRIGHT,'новую игру',Style.RESET_ALL,', введите "',Fore.GREEN,'N',Fore.RESET,
	'". Для того что бы ',Style.BRIGHT,'загрузить',Style.RESET_ALL,', введите "',Fore.RED,'L',Fore.RESET,'".',sep=''
	)
	x=input()
	while x!='n' and x!='N' and x!='l' and x!='L':
		print('некорректный символ')
		x=input()
	if x=='l' or x=='L':
		try:
			with open('bigProject_save','rb') as s:
				parametrs=pickle.load(s)
				Name=pickle.load(s)
			s.close()
			print('Игра успешно ',Style.BRIGHT,'восстановлена',Style.RESET_ALL,'!',sep='')
			if parametrs['access']==4:
				print()
				print(Back.GREEN,'                                      ',Back.RESET)
				print(Style.BRIGHT,Back.YELLOW,'                                        ',Style.RESET_ALL,sep='')
				print('       Вы являетесь чемпионом ',Back.MAGENTA,Style.BRIGHT,Fore.WHITE,'!!!',Style.RESET_ALL,sep='')
				print(Style.BRIGHT,Back.YELLOW,'                                        ',Style.RESET_ALL,sep='')
				print(Back.GREEN,'                                      ',Back.RESET)
			return parametrs,Name
		except:
			print(
			Style.BRIGHT,Fore.RED,'сохранение не найдено!',Style.RESET_ALL,sep=''
			)
	print(Style.BRIGHT,'Новая игра',Style.RESET_ALL)
	print(
	'Выберите уровень сложности. ',Style.BRIGHT,'Введите',Style.RESET_ALL,' "',Fore.YELLOW,'1',Fore.RESET,
	'" для нормального или "',Fore.YELLOW,'2',Fore.RESET,'" для ',
	Style.BRIGHT,Fore.BLACK,'повышенного',Style.RESET_ALL,'.',sep=''
	)
	x=input()
	while x!='1' and x!='2':
		print('некорректный символ')
		x=input()
	print('Назовите своего персонажа:')
	Name=input()
	parametrs={
	'Exp':1,'MaxHp':20.0,'Hp':20.0,'Dmg':2,'Money':15,'cost':5,'raise':5,
	'Fight':0,'Win':0,'access':0,'dif':1,'def':0.05,'agi':0.05,'cri':0.05
	}
	if x=='2':
		parametrs['dif']=1.3
	return parametrs,Name

def choise(parametrs):
	""" после боя или тренажерки или госпитоля
		будет задавать вопрос, куда пойти.
	"""
	print('______________________________________________________________________________')
	if parametrs['Hp']<5 and parametrs['Money']<10:
		print('У вас кончилось здоровье и денег на лечение не осталось.')
		print('                     ____',Fore.RED,'G A M E   O V E R !!!',Fore.RESET,'____',sep='')
		input()
		exit()
	if parametrs['dif']==1:
		print('Сложность: нормальная')
	else:
		print('Сложность: ',Style.BRIGHT,Fore.BLACK,'повышенная',Style.RESET_ALL,sep='')
	print(
	'Ваши параметры: ',Style.BRIGHT,Fore.YELLOW,'опытность = ', parametrs['Exp'],Style.RESET_ALL,
	'; ',Style.BRIGHT,Fore.MAGENTA,'урон = ',parametrs['Dmg'],Style.RESET_ALL,
	'; ',Style.BRIGHT,Fore.GREEN,'жизни = ',parametrs['Hp'],Style.RESET_ALL,
	'; ',Style.BRIGHT,Fore.CYAN,'средства = ',parametrs['Money'],Style.RESET_ALL,sep=''
	)
	print('Количество боев/побед = ',parametrs['Fight'],'/',parametrs['Win'])
	print('______________________________________________________________________________')
	print(
	'Куда пойти? ',Style.BRIGHT,Fore.BLUE,Name,Style.RESET_ALL,'    (для сохранения введите ',
	Style.BRIGHT,'save',Style.RESET_ALL,')',sep=''
	)
	print(
	Style.BRIGHT,'1:',Style.RESET_ALL,' Тренажерка; ',
	Style.BRIGHT,'2:',Style.RESET_ALL,' Уличные бои; ',
	Style.BRIGHT,'3:',Style.RESET_ALL,' Больница; ',
	Style.BRIGHT,'4:',Style.RESET_ALL,' Бойцовский клуб; ',
	Style.BRIGHT,'5:',Style.RESET_ALL,' Титульные бои;',sep=''
	)
	if parametrs['access']==3:
		print(
		Style.BRIGHT,Fore.RED,'6: Бой с чемпионом',Style.RESET_ALL,sep=''
		) 
	x=input()
	while x!='1' and x!='2' and x!='3' and x!='4' and x!='5' and x!='save':
		if parametrs['access']==3 and x=='6':
			break
		print('Неизвестное направление')
		x=input()
	if x=='1':
		traning(parametrs)
	elif x=='2':
		streetfight(parametrs)
	elif x=='3':
		hospital(parametrs)
	elif x=='4':
		clubfight(parametrs)
	elif x=='5':
		TitulFight(parametrs)
	elif x=='6':
		ChempFight(parametrs)
	elif x=='save':
		with open('bigProject_save','wb') as s:
			pickle.dump(parametrs,s)
			pickle.dump(Name,s)
		s.close()
		print()
		print(Style.BRIGHT,Fore.GREEN,'Игра сохранена!',Style.RESET_ALL)
	return

def traning(parametrs):
	""" тренеровка, повышение опытности за деньги
		Опытность - повышает жизни, урон, ловкость, защиту, шанс крита
	"""
	print('Ваша опытность = ',parametrs['Exp'])
	print(
	'введите "',Style.BRIGHT,Fore.GREEN,'+',Style.RESET_ALL,'" для повышения силы, или "',
	Style.BRIGHT,Fore.RED,'-',Style.RESET_ALL,'" что бы выйти с тренажерки.',sep=''
	)
	print(
	Style.BRIGHT,Fore.CYAN,'Тренеровка',Style.RESET_ALL,' вам обойдется в стоимость ',
	Style.BRIGHT,parametrs['cost'],Style.RESET_ALL,'.',sep=''
	)
	x=input()
	while x!='+' and x!='-':
		print('Некорректный символ')
		x=input()
	if x=='+' and parametrs['Money']>=parametrs['cost']:
		parametrs['Money']-=parametrs['cost']
		parametrs['Money']=int(parametrs['Money']*100)/100
		parametrs['Exp']+= 1
		parametrs['Hp']+=2
		parametrs['MaxHp']+=2
		parametrs['Dmg']+=0.5
		parametrs['def']+=0.0045
		parametrs['def']=int(parametrs['def']*10000)/10000
		parametrs['agi']+=0.0045
		parametrs['agi']=int(parametrs['agi']*10000)/10000
		parametrs['cri']+=0.0035
		parametrs['cri']=int(parametrs['cri']*10000)/10000
		parametrs['cost']+=parametrs['raise']
		parametrs['raise']+=3
	elif x=='+':
		print('Не хватает стредств')
	return

def streetfight(parametrs):
	""" первые самые простые бои
	"""
	if parametrs['Hp']>5:
		enemy={
		'Hp':10*parametrs['dif'],'Dmg':r.randint(1,2)*parametrs['dif'],'Money':5*parametrs['dif'],
		'UpHp':0,'UpDmg':0,'UpMoney':0,'def':0.1,'agi':0.1,'cri':0.09,'Champ':0
		}
		battleround(parametrs,enemy)
	else:
		print('Мало здоровья. Пойди подлечись.')
	return

def clubfight(parametrs):
	""" те же уличные бои только противники сильнее, награда выше
		за вход тоже надо заплатить
	"""
	if parametrs['access']==0:
		print(
		'У вас нет ',Fore.CYAN,'абонемента',Fore.RESET,' для этого клуба. Хотите купить за ',
		Fore.YELLOW,'100',Fore.RESET,'?',sep=''
		)
		print(
		'Для согласия введите "',Style.BRIGHT,Fore.GREEN,'+',Style.RESET_ALL,
		'", что бы выйти "',Style.BRIGHT,Fore.RED,'-',Style.RESET_ALL,'".',sep=''
		)
		x=input()
		while x!='+' and x!='-':
			print('Некорректный символ')
			x=input()
		if x=='+' and parametrs['Money']>=100:
			print('Вы преобрели ',Style.BRIGHT,Fore.YELLOW,'доступ',Style.RESET_ALL,' к бойцовскому клубу',sep='')
			parametrs['Money']-=100
			parametrs['access']=1
		elif x=='+':
			print('Недостаточно средств')
		return
	if parametrs['Hp']>10:
		enemy={
		'Hp':13.5*parametrs['dif'],'Dmg':3.8*parametrs['dif'],'Money':13.5*parametrs['dif'],
		'UpHp':1.5*parametrs['dif'],'UpDmg':0.2*parametrs['dif'],'UpMoney':1.5*parametrs['dif'],
		'def':0.15,'agi':0.15,'cri':0.12,'Champ':0
		}
		battleround(parametrs,enemy)
	else:
		print('Мало здоровья. Пойди подлечись.')
	return

def TitulFight(parametrs):
	""" те же уличные бои только противники сильнее, награда выше
		за вход тоже надо заплатить
	"""
	if parametrs['Exp']<30:
		print(
		'Вы еще ',Style.BRIGHT,Fore.RED,'не достаточно',Fore.CYAN,
		' известны',Style.RESET_ALL,', идите подкачайтесь!',sep=''
		)
		return
	if parametrs['access']<2:
		print(
		'Для доступа к титульным боям ',Style.BRIGHT,Fore.YELLOW,'необходимо',Style.RESET_ALL,' подкупить организатора. ',
		'Заплатить ',Fore.YELLOW,'2000',Fore.RESET,'?',sep=''
		)
		print(
		'Для согласия введите "',Style.BRIGHT,Fore.GREEN,'+',Style.RESET_ALL,
		'", что бы выйти "',Style.BRIGHT,Fore.RED,'-',Style.RESET_ALL,'".',sep=''
		)
		x=input()
		while x!='+' and x!='-':
			print('Некорректный символ')
			x=input()
		if x=='+' and parametrs['Money']>=2000:
			print('Теперь у вас есть ',Style.BRIGHT,Fore.YELLOW,'доступ',Style.RESET_ALL,' к титульным боям',sep='')
			parametrs['Money']-=2000
			parametrs['access']+=1
		elif x=='+':
			print('Недостаточно средств')
		return
	if parametrs['Hp']>30:
		enemy={
		'Hp':40*parametrs['dif'],'Dmg':6.5*parametrs['dif'],'Money':70*parametrs['dif'],
		'UpHp':3*parametrs['dif'],'UpDmg':0.35*parametrs['dif'],'UpMoney':10*parametrs['dif'],
		'def':0.18,'agi':0.18,'cri':0.16,'Champ':0
		}
		battleround(parametrs,enemy)
	else:
		print('Мало здоровья. Пойди подлечись.')
	return

def battleround(parametrs,enemy):
	""" 10 раундовые бои
	"""
	for i in range (1,11):
		backup=dict.copy(enemy)
		enemy['Hp']+=(enemy['UpHp']*i)
		enemy['Hp']=int(enemy['Hp']*100)/100
		enemy['Dmg']+=(enemy['UpDmg']*i)
		enemy['Dmg']=int(enemy['Dmg']*100)/100
		enemy['Money']+=(enemy['UpMoney']*i)
		enemy['Money']=int(enemy['Money']*100)/100
		print('___________')
		if enemy['Champ']!=1: # Для всех боев кроме финального
			print('Раунд ',i,'/ 10')
		print('Ваши параметры:  ','урон = ',parametrs['Dmg'],'; ','жизни = ',parametrs['Hp'],';',sep='')
		print('Параметры противника:  ','урон = ',enemy['Dmg'],'; ','жизни = ',enemy['Hp'],';',sep='')
		print('_____________________________________________________')
		H1=parametrs['MaxHp']
		H2=enemy['Hp']
		parametrs['Fight']+=1
		while parametrs['Hp']>0 and enemy['Hp']>0:
			x=r.randint(0,1)
			d=r.random()
			d=int(d*10000)/10000
			a=r.random()
			a=int(a*10000)/10000
			c=r.random()
			c=int(c*10000)/10000
			if x==0: # Удар игрока
				if d<enemy['def']: # Проверка на блок
					if c<(parametrs['cri']*3):
						punch=parametrs['Dmg']+parametrs['Dmg']*parametrs['cri']
						punch=int(punch*100)/100
						enemy['Hp']-=punch
						enemy['Hp']=int(enemy['Hp']*100)/100
						print(
						'Противник пытается защититься но ',Fore.YELLOW,Name,Fore.RESET,' с ',Fore.RED,'яростью',Fore.RESET,
						' в глазах пробивает блок ',Fore.RED,punch,Fore.RESET,'| ',enemy['Hp'] if enemy['Hp']>=0 else 0,'/',H2,sep=''
						)
					else:
						print(
						'Противник ',Fore.GREEN,'блокирует',Fore.RESET,' успешно удар. ',Fore.GREEN,'0',Fore.RESET,
						'| ',enemy['Hp'] if enemy['Hp']>=0 else 0,'/',H2,sep=''
						)
					continue
				if a<enemy['agi']: # Провка на уворот
					if c<(parametrs['cri']*3):
						enemy['Hp']-=parametrs['Dmg']
						enemy['Hp']=int(enemy['Hp']*100)/100
						print(
						'Противник пытаясь ',Style.BRIGHT,'увернуться',Style.RESET_ALL,', споткнулся и упал. ',
						Style.BRIGHT,parametrs['Dmg'],Style.RESET_ALL,'| ',enemy['Hp'] if enemy['Hp']>=0 else 0,'/',H2,sep=''
						)
					else:
						print(
						'Противник успешно ',Fore.CYAN,'уворачивается',Fore.RESET,' от удара. ',Fore.CYAN,'0',Fore.RESET,
						'| ',enemy['Hp'] if enemy['Hp']>=0 else 0,'/',H2,sep=''
						)
					continue
				if c<parametrs['cri']: # Проверка на крит
					punch=parametrs['Dmg']+parametrs['Dmg']*parametrs['cri']
					punch=int(punch*100)/100
					enemy['Hp']-=punch
					enemy['Hp']=int(enemy['Hp']*100)/100
					print(
					Fore.YELLOW,Name,Fore.RESET,' с криком ',Fore.RED,'втаскивает',Fore.RESET,' противнику ',Fore.RED,punch,Fore.RESET,
					'| ',enemy['Hp'] if enemy['Hp']>=0 else 0,'/',H2,sep=''
					)
					continue

				enemy['Hp']-=parametrs['Dmg']
				enemy['Hp']=int(enemy['Hp']*100)/100
				print(
				Fore.YELLOW,Name,Fore.RESET,' наносит урон противнику ',parametrs['Dmg'],
				'| ',enemy['Hp'] if enemy['Hp']>=0 else 0,'/',H2,sep=''
				)

			else: # Удар противника
				if d<parametrs['def']: # Проверка на блок
					if c<(enemy['cri']*3):
						punch=enemy['Dmg']+enemy['Dmg']*enemy['cri']
						punch=int(punch*100)/100
						parametrs['Hp']-=punch
						parametrs['Hp']=int(parametrs['Hp']*100)/100
						print(
						Fore.YELLOW,Name,Fore.RESET,' подумал о ',Fore.RED,'блоке',Fore.RESET,', но было уже поздно ',
						Fore.RED,punch,Fore.RESET,'| ',parametrs['Hp'] if parametrs['Hp']>=0 else 0,'/',H1,sep=''
						)
					else:
						print(
						'Богоподобно ',Fore.YELLOW,Name,Fore.RESET,' ',Fore.GREEN,'блокирует',Fore.RESET,' удар ',
						Fore.GREEN,'0',Fore.RESET,'| ',parametrs['Hp'] if parametrs['Hp']>=0 else 0,'/',H1,sep=''
						)
					continue
				if a<parametrs['agi']: # Провка на уворот
					if c<(enemy['cri']*3):
						parametrs['Hp']-=enemy['Dmg']
						parametrs['Hp']=int(parametrs['Hp']*100)/100
						print(
						Style.BRIGHT,'Прыжок',Style.RESET_ALL,' в сторону ',Fore.YELLOW,Name,Fore.RESET,' не увенчался успехом ',
						Style.BRIGHT,enemy['Dmg'],Style.RESET_ALL,'| ',parametrs['Hp'] if parametrs['Hp']>=0 else 0,'/',H1,sep=''
						)
					else:
						print(
						'Как смерч ',Fore.YELLOW,Name,Fore.RESET,' ',Fore.CYAN,'увернулся',Fore.RESET,' от удара ',
						Fore.CYAN,'0',Fore.RESET,'| ',parametrs['Hp'] if parametrs['Hp']>=0 else 0,'/',H1,sep=''
						)
					continue
				if c<enemy['cri']: # Проверка на крит
					punch=enemy['Dmg']+enemy['Dmg']*enemy['cri']
					punch=int(punch*100)/100
					parametrs['Hp']-=punch
					parametrs['Hp']=int(parametrs['Hp']*100)/100
					print(
					'Противник ',Fore.RED,'размашистым',Fore.RESET,' ударом встречает ',Fore.YELLOW,Name,Fore.RESET,' ',
					Fore.RED,punch,Fore.RESET,'| ',parametrs['Hp'] if parametrs['Hp']>=0 else 0,'/',H1,sep=''
					)
					continue

				parametrs['Hp']-=enemy['Dmg']
				parametrs['Hp']=int(parametrs['Hp']*1000)/1000
				print(
				'Противник наносит урон ',enemy['Dmg'],'| ',parametrs['Hp'] if parametrs['Hp']>=0 else 0,'/',H1,sep=''
				)

		if parametrs['Hp']<1:
			print('___________')
			print('Вы проиграли')
			parametrs['Hp']=0
			return
		else:
			print('___________')
			print('Вы выйграли. Награда за победу:',enemy['Money'])
			parametrs['Money']+=enemy['Money']
			parametrs['Money']=int(parametrs['Money']*100)/100
			parametrs['Win']+=1
			if enemy['Champ']==1: # Для финального боя
				parametrs['access']+=1
				print()
				print(Back.GREEN,'                                                   ',Back.RESET)
				print(Style.BRIGHT,Back.YELLOW,'                                                     ',Style.RESET_ALL,sep='')
				print('         Вы только что победили чемпиона')
				print('Данный титул теперь закреплен за Вами. Поздравляем',Back.MAGENTA,Style.BRIGHT,Fore.WHITE,'!!!',Style.RESET_ALL,sep='')
				print(Style.BRIGHT,Back.YELLOW,'                                                     ',Style.RESET_ALL,sep='')
				print(Back.GREEN,'                                                   ',Back.RESET)
				print()
				return
			enemy=dict.copy(backup)
	return

def Champ(parametrs):
	""" Ожидает когда игрок достигнет определенного уровня
		и дает доступ к последнему бою
	"""
	if parametrs['Exp']>59 and parametrs['access']==2:
		parametrs['access']+=1
		print()
		print(Back.RED,'                                                   ',Back.RESET)
		print(Back.WHITE,'                                                   ',Back.RESET)
		print(Back.GREEN,'                                                   ',Back.RESET)
		print(Back.MAGENTA,'                                                   ',Back.RESET)
		print(
		Style.BRIGHT,Fore.MAGENTA,'Вас',Fore.YELLOW,' заметил',Fore.CYAN,' нынешний',
		Fore.GREEN,' чемпион',Style.NORMAL,Fore.YELLOW,' и ',Style.BRIGHT,Fore.WHITE,'вызывает',
		Fore.BLUE,' вас',Fore.BLACK,' на',Fore.RED,' бой',Style.RESET_ALL,
		Back.WHITE,Fore.BLACK,'!!!',Style.RESET_ALL,sep=''
		)
		print(Back.MAGENTA,'                                                   ',Back.RESET)
		print(Back.GREEN,'                                                   ',Back.RESET)
		print(Back.WHITE,'                                                   ',Back.RESET)
		print(Back.RED,'                                                   ',Back.RESET)
		print()
	return

def ChempFight(parametrs):
	""" Последний финальный бой
	"""
	if parametrs['Hp']>5:
		enemy={
		'Hp':400*parametrs['dif'],'Dmg':30*parametrs['dif'],'Money':100000*parametrs['dif'],
		'UpHp':0*parametrs['dif'],'UpDmg':0*parametrs['dif'],'UpMoney':0*parametrs['dif'],
		'def':0.22,'agi':0.22,'cri':0.25,'Champ':1
		}
		battleround(parametrs,enemy)
	else:
		print('Мало здоровья. Пойди подлечись.')
	return

def hospital(parametrs):
	""" восстановление Hp за Money
	"""
	if parametrs['Hp']<parametrs['MaxHp']:
		print(
		'Хотите подлечиться ',Style.BRIGHT,Fore.GREEN,'+30',Style.RESET_ALL,
		'? к оплате ',Fore.YELLOW,'10',Fore.RESET,' за штуку.',sep=''
		)
		print(
		'введите "',Style.BRIGHT,Fore.GREEN,'+',Style.RESET_ALL,'" если согласны, "',
		Style.BRIGHT,Fore.RED,'-',Style.RESET_ALL,'" что бы выйти.',sep=''
		)
		x=input()
		while x!='+' and x!='-':
			print('некорректный символ')
			x=input()
		if x=='-':
			return
		print('Какое количество приобрести?: ')
		flag=True
		while flag:
			try:
				y=int(input())
				flag=False
			except:
				print('некорректный символ')
		for i in range (y):
			if parametrs['Money']>=10 and parametrs['Hp']<parametrs['MaxHp']:
				parametrs['Hp']+=30
				parametrs['Hp']=int(parametrs['Hp']*100)/100
				parametrs['Money']-=10
				parametrs['Money']=int(parametrs['Money']*100)/100
				print(Fore.GREEN,'Восстановлено ',Style.BRIGHT,Fore.YELLOW,'30',Style.RESET_ALL,' едениц жизни',sep='')
				if parametrs['Hp']>=parametrs['MaxHp']:
					parametrs['Hp']=parametrs['MaxHp']
					return
			else:
				print('не хватает средств')
				return
	else:
		print('Вы здоровы')
	return

init()
parametrs,Name=start_ch()
while True:
	choise(parametrs)
	Champ(parametrs)