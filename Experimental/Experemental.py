import pygame
import random as r
import pickle
from colorama import init, Fore, Style, Back

pygame.init()
init()
clock = pygame.time.Clock()
FPS = 60
sc = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Fighting')
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (100, 100, 100)
Green = (0, 255, 0)
SoftGray = (150, 150, 150)
Red = (255, 0, 0)
DarkRed = (150, 0, 0)
Yellow = (255, 255, 0)
color_welcome = (35, 165, 210)
Red_Dmg = (255, 30, 150)
Gray_Exp = (200, 200, 200)
Green_Hp = (50, 255, 50)
Sky_Money = (50, 255, 255)

health_full = False
save =False
saved = False
not_save = False
health = False
Exit = False
health_info = False
not_enough_money = False
Trainig = False
Trainig_info = False
win = False
titulaccess = False
champ = False
Q = False

volume = 0.6
timer = 0

try:
	Name_file = open('name')
	Name = Name_file.readline()
	Name_file.close()
except:
	Name = 'Gamer'

music = ['music/skorpion.ogg', 'music/12-TheBank&RiverKombat.ogg', 'music/21-TheBridge&KhansKave.ogg',
		 'music/03-BankRobbery(Stages1-1&1-3).ogg', 'music/03-MarbleZone.ogg', 'music/05-PuppyLove.ogg',
		 'music/06-Drive-In.ogg', 'music/06-StageHoldup(Stage2).ogg', 'music/11-HighlandHighschool.ogg',
		 'music/16-PanicPuppetZoneAct2.ogg', 'music/26-WeBCars.ogg', 'music/05-BretHart.ogg', 'music/08-Stage4-1.ogg',
		 'music/13-FriendLikeMe.ogg', 'music/36-FinalBossIntro.ogg']

def main():

	sc.fill(Gray)

	pygame.display.update()

	sound1 = pygame.mixer.Sound('sound\hit-01.wav')
	sound2 = pygame.mixer.Sound('sound\punch.wav')

	l = 0

	while l < 300:

		clock.tick(FPS)
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

		l += 1

		if l == 50:
			wel_f_font = pygame.font.SysFont('Arial Black', 70)
			wel_f_text = wel_f_font.render('Добро пожаловать', 1, color_welcome)
			wel_f_place = wel_f_text.get_rect(topleft=(250, 230))
			sc.blit(wel_f_text, wel_f_place)
			sound1.play()

			pygame.display.update()

		if l == 100:
			wel_s_font = pygame.font.SysFont('Haettenschweiler', 80)
			wel_s_text = wel_s_font.render('В', 1, Yellow)
			wel_s_place = wel_s_text.get_rect(topleft=(600, 370))
			sc.blit(wel_s_text, wel_s_place)
			sound1.play()

			pygame.display.update()

		if l == 150:
			wel_t_font = pygame.font.SysFont('Arial Black', 70)
			wel_t_text = wel_t_font.render('Симулятор бойца', 1, Red)
			wel_t_place = wel_t_text.get_rect(topleft=(270, 480))

			main_fon_image = pygame.image.load('images/main_fon.png')
			main_fon_rect = main_fon_image.get_rect(topleft=(0, 0))
			sc.blit(main_fon_image, main_fon_rect)
			sc.blit(wel_t_text, wel_t_place)
			sc.blit(wel_s_text, wel_s_place)
			sc.blit(wel_f_text, wel_f_place)
			sound2.play()

			pygame.display.update()

	parametrs = new_load()
	while parametrs == {}:
		parametrs = new_load()
	return parametrs


def new_load():

	sound1 = pygame.mixer.Sound('sound/01040.ogg')
	sound2 = pygame.mixer.Sound('sound/09470.ogg')
	sound3 = pygame.mixer.Sound('sound/09155.ogg')
	sound4 = pygame.mixer.Sound('sound/09430.ogg')
	pygame.mixer.music.load('music/38-Continue.ogg')
	pygame.mixer.music.set_volume(volume)
	sound2.play()
	pygame.time.delay(100)
	pygame.mixer.music.play(-1)

	while True:

		clock.tick(FPS)
		sc.fill(White)

		new_game_image = pygame.image.load('images/New_game.png')
		new_game_rect = new_game_image.get_rect(topleft=(400, 150))
		sc.blit(new_game_image, new_game_rect)

		load_image = pygame.image.load('images/Load.png')
		load_rect = load_image.get_rect(topleft=(400, 400))
		sc.blit(load_image, load_rect)

		if pygame.mouse.get_focused:
			mouse = pygame.mouse.get_pos()
			rect_M = pygame.Rect((mouse[0]-1, mouse[1]-1), (2, 2))
			surf_M = pygame.Surface((2, 2))
			surf_M.set_alpha(0)
			sc.blit(surf_M, rect_M)

		if new_game_rect.contains(rect_M):
			new_game_fon_image = pygame.image.load('images/New_game_fon.png')
			new_game_fon_rect = new_game_fon_image.get_rect(topleft=(400, 150))
			new_gamer_image = pygame.image.load('images/newbie.jpg')
			new_gamer_rect = new_gamer_image.get_rect(topleft=(50, 80))
			sc.blit(new_game_fon_image, new_game_fon_rect)
			sc.blit(new_game_image, new_game_rect)
			sc.blit(new_gamer_image, new_gamer_rect)
		if load_rect.contains(rect_M):
			load_fon_image = pygame.image.load('images/Load_fon.png')
			load_fon_rect = load_fon_image.get_rect(topleft=(400, 400))
			load_gamer_image = pygame.image.load('images/master.jpg')
			load_gamer_rect = load_gamer_image.get_rect(topleft=(900, 325))
			sc.blit(load_fon_image, load_fon_rect)
			sc.blit(load_image, load_rect)
			sc.blit(load_gamer_image, load_gamer_rect)

		pygame.display.update()

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

			if i.type == pygame.MOUSEBUTTONUP and new_game_rect.contains(rect_M):

				pygame.mixer.music.stop()

				sound1.play()

				l = 0

				while l < 25:

					clock.tick(FPS)
					l += 1
					for i in pygame.event.get():
						if i.type == pygame.QUIT:
							exit()

				pygame.mixer.music.load('music/skorpion.ogg')
				pygame.mixer.music.play()

				parametrs = {
					'Exp': 1, 'MaxHp': 20.0, 'Hp': 20.0, 'Dmg': 2, 'Money': 15, 'cost': 5, 'raise': 5,
					'Fight': 0, 'Win': 0, 'access': 0, 'dif': 1, 'def': 0.05, 'agi': 0.05, 'cri': 0.05
				}

				while True:

					clock.tick(FPS)

					if pygame.mouse.get_focused:
						mouse = pygame.mouse.get_pos()
						rect_M = pygame.Rect((mouse[0] - 1, mouse[1] - 1), (2, 2))
						surf_M = pygame.Surface((2, 2))
						surf_M.set_alpha(0)
						sc.blit(surf_M, rect_M)

					sc.fill(White)

					dif_info_font = pygame.font.SysFont('Haettenschweiler', 70)
					dif_info_text = dif_info_font.render('Выберите уровень сложности', 1, Green)
					dif_info_place = dif_info_text.get_rect(center=(600, 300))
					sc.blit(dif_info_text, dif_info_place)

					dif_norm_font = pygame.font.SysFont('Haettenschweiler', 40)
					dif_norm_text = dif_norm_font.render('нормальная', 1, SoftGray)
					dif_norm_place = dif_norm_text.get_rect(center=(450, 460))
					sc.blit(dif_norm_text, dif_norm_place)

					dif_high_font = pygame.font.SysFont('Haettenschweiler', 40)
					dif_high_text = dif_high_font.render('повышенная', 1, Gray)
					dif_high_place = dif_high_text.get_rect(center=(750, 460))
					sc.blit(dif_high_text, dif_high_place)

					if dif_norm_place.contains(rect_M):

						pygame.draw.rect(sc, Red, (337, 420, 225, 90), 4)
						pygame.draw.rect(sc, Red, (658, 435, 185, 60), 4)

					elif dif_high_place.contains(rect_M):

						pygame.draw.rect(sc, Red, (637, 420, 225, 90), 4)
						pygame.draw.rect(sc, Red, (358, 435, 185, 60), 4)

					else:
						pygame.draw.rect(sc, Red, (358, 435, 185, 60), 4)
						pygame.draw.rect(sc, Red, (658, 435, 185, 60), 4)

					pygame.display.update()

					for i in pygame.event.get():
						if i.type == pygame.QUIT:
							exit()
						if i.type == pygame.MOUSEBUTTONUP and dif_high_place.contains(rect_M):
							parametrs['dif'] = 1.3

							pygame.mixer.music.set_volume(0.2)

							sound1.play()
							sound1.play()
							pygame.time.delay(300)
							sound3.play()
							sound3.play()

							l = 0

							dif_info_h = 298
							dif_norm_h = 458
							dif_high_h = 458

							while l < 130:

								if l < 50 and dif_info_h > 300:
									sc.fill(White)
									dif_info_place = dif_info_text.get_rect(center=(600, dif_info_h))
									dif_norm_place = dif_norm_text.get_rect(center=(450, dif_norm_h))
									dif_high_place = dif_high_text.get_rect(center=(750, dif_high_h))
									sc.blit(dif_info_text, dif_info_place)
									sc.blit(dif_norm_text, dif_norm_place)
									sc.blit(dif_high_text, dif_high_place)
									pygame.draw.rect(sc, Red, (637, 422, 225, 90), 4)
									pygame.draw.rect(sc, Red, (358, 437, 185, 60), 4)
									dif_info_h = 298
									dif_norm_h = 458
									dif_high_h = 458
									pygame.display.update()
								elif l < 50 and dif_info_h < 300:
									sc.fill(White)
									dif_info_place = dif_info_text.get_rect(center=(600, dif_info_h))
									dif_norm_place = dif_norm_text.get_rect(center=(450, dif_norm_h))
									dif_high_place = dif_high_text.get_rect(center=(750, dif_high_h))
									sc.blit(dif_info_text, dif_info_place)
									sc.blit(dif_norm_text, dif_norm_place)
									sc.blit(dif_high_text, dif_high_place)
									pygame.draw.rect(sc, Red, (637, 418, 225, 90), 4)
									pygame.draw.rect(sc, Red, (358, 433, 185, 60), 4)
									dif_info_h = 302
									dif_norm_h = 462
									dif_high_h = 462
									pygame.display.update()

								clock.tick(FPS)
								l += 1
								for i in pygame.event.get():
									if i.type == pygame.QUIT:
										exit()
							pygame.mixer.music.set_volume(volume)
							return parametrs
						elif i.type == pygame.MOUSEBUTTONUP and dif_norm_place.contains(rect_M):

							pygame.mixer.music.set_volume(0.2)

							sound1.play()
							sound1.play()
							pygame.time.delay(300)
							sound3.play()
							sound3.play()

							l = 0

							dif_info_h = 298
							dif_norm_h = 458
							dif_high_h = 458

							while l < 130:

								if l < 50 and dif_info_h > 300:
									sc.fill(White)
									dif_info_place = dif_info_text.get_rect(center=(600, dif_info_h))
									dif_norm_place = dif_norm_text.get_rect(center=(450, dif_norm_h))
									dif_high_place = dif_high_text.get_rect(center=(750, dif_high_h))
									sc.blit(dif_info_text, dif_info_place)
									sc.blit(dif_norm_text, dif_norm_place)
									sc.blit(dif_high_text, dif_high_place)
									pygame.draw.rect(sc, Red, (337, 422, 225, 90), 4)
									pygame.draw.rect(sc, Red, (658, 437, 185, 60), 4)
									dif_info_h = 298
									dif_norm_h = 458
									dif_high_h = 458
									pygame.display.update()
								elif l < 50 and dif_info_h < 300:
									sc.fill(White)
									dif_info_place = dif_info_text.get_rect(center=(600, dif_info_h))
									dif_norm_place = dif_norm_text.get_rect(center=(450, dif_norm_h))
									dif_high_place = dif_high_text.get_rect(center=(750, dif_high_h))
									sc.blit(dif_info_text, dif_info_place)
									sc.blit(dif_norm_text, dif_norm_place)
									sc.blit(dif_high_text, dif_high_place)
									pygame.draw.rect(sc, Red, (337, 418, 225, 90), 4)
									pygame.draw.rect(sc, Red, (658, 433, 185, 60), 4)
									dif_info_h = 302
									dif_norm_h = 462
									dif_high_h = 462
									pygame.display.update()

								clock.tick(FPS)
								l += 1
								for i in pygame.event.get():
									if i.type == pygame.QUIT:
										exit()
							pygame.mixer.music.set_volume(volume)
							return parametrs

			elif i.type == pygame.MOUSEBUTTONUP and load_rect.contains(rect_M):



				try:
					with open('experemental_save', 'rb') as s:
						parametrs = pickle.load(s)
					s.close()

					pygame.mixer.music.stop()

					sound1.play()

					l = 0

					while l < 25:

						clock.tick(FPS)
						l += 1
						for i in pygame.event.get():
							if i.type == pygame.QUIT:
								exit()

					pygame.mixer.music.load('music/skorpion.ogg')
					pygame.mixer.music.play()

					sc.fill(White)

					load_font = pygame.font.SysFont('Arial Black', 52)
					load_text = load_font.render('Игра успешно восстановлена', 1, Green)
					load_place = load_text.get_rect(center=(600, 350))
					sc.blit(load_text, load_place)
					pygame.draw.line(sc, Green, [160, 400], [1042, 400], 5)

					pygame.display.update()

					l = 0

					while l < 100:

						clock.tick(FPS)
						l += 1
						for i in pygame.event.get():
							if i.type == pygame.QUIT:
								exit()

					return parametrs

				except:

					l = 0

					while l < 25:

						clock.tick(FPS)
						l += 1
						for i in pygame.event.get():
							if i.type == pygame.QUIT:
								exit()

					sound4.play()

					sc.fill(White)

					load_error_font = pygame.font.SysFont('Arial Black', 52)
					load_error_text = load_error_font.render('Не удалось восстановить игру', 1, Red)
					load_error_place = load_error_text.get_rect(center=(600, 350))
					sc.blit(load_error_text, load_error_place)
					pygame.draw.line(sc, Red, [150, 400], [1050, 400], 5)

					pygame.display.update()

					while l < 100:

						clock.tick(FPS)
						l += 1
						for i in pygame.event.get():
							if i.type == pygame.QUIT:
								exit()

					parametrs = {}

					return parametrs


def choise(parametrs):

	global timer, health_full, saved, not_save, save, health_info, titulaccess, champ, volume, Q

	sound1 = pygame.mixer.Sound('sound/01090.ogg')
	sound2 = pygame.mixer.Sound('sound/09415.ogg')
	sound3 = pygame.mixer.Sound('sound/09430.ogg')
	sound4 = pygame.mixer.Sound('sound/09155.ogg')
	sound5 = pygame.mixer.Sound('sound/09440.ogg')
	sound6 = pygame.mixer.Sound('sound/09460.ogg')

	streetfight_activ = True
	training_activ = False
	hospital_activ = False
	clubfight_activ = False
	titulfight_activ = False
	chempfight_activ = False

	if parametrs['Hp'] < 5 and parametrs['Money'] < 10:
		pygame.mixer.music.stop()
		pygame.time.delay(100)
		sound4.play()

		sc.fill(White)
		game_over_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 40)
		game_over_text = game_over_font.render('Ваши дни сочтены. вам нечем платить за лечение', 1, Black)
		game_over_place = game_over_text.get_rect(center=(600, 400))
		sc.blit(game_over_text, game_over_place)
		pygame.display.update()

		l = 0

		while l < 500:

			clock.tick(FPS)
			l += 1
			for i in pygame.event.get():
				if i.type == pygame.QUIT:
					exit()
			if l == 150:
				sound6.play()
			if l == 300:
				sound5.play()
		exit()

	if parametrs['Exp'] > 59 and parametrs['access'] == 2:
		parametrs['access'] += 1
		champ = True
		health_full = False
		saved = False
		not_save = False
		health_info = False
		titulaccess = False

	ava = pygame.image.load('images/ava.jpg')
	ava_rect = ava.get_rect(topleft=(900, 0))

	dif_im = pygame.image.load('images/difficult.png')
	dif_im_rect = dif_im.get_rect(topleft=(900, 200))

	label_gamer = pygame.image.load('images/gamer.png')

	label_streetfight = pygame.image.load('images/label.png')
	label_training = pygame.image.load('images/label.png')
	label_hospital = pygame.image.load('images/label.png')
	label_clubfight = pygame.image.load('images/label.png')
	label_titulfight = pygame.image.load('images/label.png')
	if parametrs['access'] == 3:
		label_chempfight = pygame.image.load('images/label.png')

	dif_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 28)
	dif_text = dif_font.render('Сложность: {}'.format('нормальная' if parametrs['dif'] == 1 else 'повышенная'), 1, Red)
	dif_text_place = dif_text.get_rect(topleft=(918, 215))

	par_name_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 30)
	par_name_text = par_name_font.render('Ваши параметры:', 1, Yellow)
	par_text_place = par_name_text.get_rect(topleft=(928, 310))

	par_exp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_exp_text = par_exp_font.render('Опытность       =  {}'.format(parametrs['Exp']), 1, Gray_Exp)
	par_exp_place = par_exp_text.get_rect(topleft=(928, 360))

	par_dmg_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_dmg_text = par_dmg_font.render('Урон                    =  {}'.format(parametrs['Dmg']), 1, Red_Dmg)
	par_dmg_place = par_dmg_text.get_rect(topleft=(928, 390))

	par_hp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_hp_text = par_hp_font.render('Жизни                =  {}'.format(parametrs['Hp']), 1, Green_Hp)
	par_hp_place = par_hp_text.get_rect(topleft=(928, 420))

	par_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_money_text = par_money_font.render('Средства          =  {}'.format(parametrs['Money']), 1, Sky_Money)
	par_money_place = par_money_text.get_rect(topleft=(928, 450))

	par_stats_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_stats_text = par_stats_font.render('боев/побед    =  {}/{}'.format(parametrs['Fight'],
																		   parametrs['Win']), 1, Black)
	par_stats_place = par_stats_text.get_rect(topleft=(928, 480))

	Q_image = pygame.image.load('images/Q.png')
	Q_rect = Q_image.get_rect(center=(870, 30))

	while True:

		if pygame.mixer.music.get_busy():
			pass
		else:
			pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
			pygame.mixer.music.play()

		sc.fill(White)

		pygame.draw.line(sc, Gray, [900, 0], [900, 800], 3)
		pygame.draw.line(sc, Gray, [900, 200], [1200, 200], 3)

		main_image = pygame.image.load('images/city.jpg')
		main_rect = main_image.get_rect(topleft=(0, 0))

		info_im = pygame.image.load('images/info.png')
		info_im_rect = info_im.get_rect(topleft=(900, 280))

		save_button_font = pygame.font.SysFont('Algerian', 84)
		save_button_text = save_button_font.render('SAVE', 1, color_welcome)
		save_button_place = save_button_text.get_rect(center=(1050, 730))

		pygame.draw.rect(main_image, White, (200, 730, 500, 50))

		label_streetfight_rect = label_streetfight.get_rect(center=(395, 160))
		label_training_rect = label_training.get_rect(center=(520, 240))
		label_hospital_rect = label_hospital.get_rect(center=(560, 450))
		label_clubfight_rect = label_clubfight.get_rect(center=(365, 480))
		label_titulfight_rect = label_titulfight.get_rect(center=(250, 380))
		if parametrs['access'] == 3:
			label_chempfight_rect = label_chempfight.get_rect(center=(450, 340))

		if streetfight_activ:
			label_streetfight_rect = label_streetfight.get_rect(center=(395, 155))
			label_gamer_rect = label_gamer.get_rect(center=(357, 155))
			main_image.blit(label_gamer, label_gamer_rect)

			info_streetfight_font = pygame.font.SysFont('Arial Black', 30)
			info_streetfight_text = info_streetfight_font.render('Уличные бои', 1, Red)
			info_streetfight_place = info_streetfight_text.get_rect(center=(450, 755))
			main_image.blit(info_streetfight_text, info_streetfight_place)

		if training_activ:
			label_training_rect = label_training.get_rect(center=(520, 235))
			label_gamer_rect = label_gamer.get_rect(center=(482, 235))
			main_image.blit(label_gamer, label_gamer_rect)

			info_training_font = pygame.font.SysFont('Arial Black', 30)
			info_training_text = info_training_font.render('Тренажерка', 1, Red)
			info_training_place = info_training_text.get_rect(center=(450, 755))
			main_image.blit(info_training_text, info_training_place)

		if hospital_activ:
			label_hospital_rect = label_hospital.get_rect(center=(560, 445))
			label_gamer_rect = label_gamer.get_rect(center=(522, 445))
			main_image.blit(label_gamer, label_gamer_rect)

			info_hospital_font = pygame.font.SysFont('Arial Black', 30)
			info_hospital_text = info_hospital_font.render('Больница', 1, Red)
			info_hospital_place = info_hospital_text.get_rect(center=(450, 755))
			main_image.blit(info_hospital_text, info_hospital_place)

		if clubfight_activ:
			label_clubfight_rect = label_clubfight.get_rect(center=(365, 475))
			label_gamer_rect = label_gamer.get_rect(center=(327, 475))
			main_image.blit(label_gamer, label_gamer_rect)

			info_clubfight_font = pygame.font.SysFont('Arial Black', 30)
			info_clubfight_text = info_clubfight_font.render('Бойцовский клуб', 1, Red)
			info_clubfight_place = info_clubfight_text.get_rect(center=(450, 755))
			main_image.blit(info_clubfight_text, info_clubfight_place)

		if titulfight_activ:
			label_titulfight_rect = label_titulfight.get_rect(center=(250, 375))
			label_gamer_rect = label_gamer.get_rect(center=(212, 375))
			main_image.blit(label_gamer, label_gamer_rect)

			info_titulfight_font = pygame.font.SysFont('Arial Black', 30)
			info_titulfight_text = info_titulfight_font.render('Титульные бои', 1, Red)
			info_titulfight_place = info_titulfight_text.get_rect(center=(450, 755))
			main_image.blit(info_titulfight_text, info_titulfight_place)

		if chempfight_activ:
			label_chempfight_rect = label_chempfight.get_rect(center=(450, 335))
			label_gamer_rect = label_gamer.get_rect(center=(412, 335))
			main_image.blit(label_gamer, label_gamer_rect)

			info_chempfight_font = pygame.font.SysFont('Arial Black', 30)
			info_chempfight_text = info_chempfight_font.render('Чемпионский бой', 1, Red)
			info_chempfight_place = info_chempfight_text.get_rect(center=(450, 755))
			main_image.blit(info_chempfight_text, info_chempfight_place)

		if health_full:
			pygame.draw.rect(main_image, White, (200, 20, 500, 50))
			full_health_font = pygame.font.SysFont('Arial Black', 30)
			full_health_text = full_health_font.render('Вы полностью здоровы', 1, Green)
			full_health_place = full_health_text.get_rect(center=(450, 40))
			main_image.blit(full_health_text, full_health_place)
			timer += 1
			if timer == 60:
				timer = 0
				health_full = False

		if saved:
			pygame.draw.rect(main_image, White, (200, 20, 500, 50))
			save_font = pygame.font.SysFont('Arial Black', 30)
			save_text = save_font.render('Игра успешно сохранена', 1, Green)
			save_place = save_text.get_rect(center=(450, 40))
			main_image.blit(save_text, save_place)
			timer += 1
			if timer == 60:
				timer = 0
				saved = False

		if not_save:
			pygame.draw.rect(main_image, White, (200, 20, 500, 50))
			save_error_font = pygame.font.SysFont('Arial Black', 30)
			save_error_text = save_error_font.render('Игра не сохранена', 1, Red)
			save_error_place = save_error_text.get_rect(center=(450, 40))
			main_image.blit(save_error_text, save_error_place)
			timer += 1
			if timer == 60:
				timer = 0
				not_save = False

		if health_info:
			pygame.draw.rect(main_image, White, (200, 20, 500, 50))
			health_font = pygame.font.SysFont('Arial Black', 30)
			health_text = health_font.render('пойди подлечись', 1, Red)
			health_place = health_text.get_rect(center=(450, 40))
			main_image.blit(health_text, health_place)
			timer += 1
			if timer > 60:
				timer = 0
				health_info = False

		if titulaccess:
			pygame.draw.rect(main_image, White, (200, 20, 500, 50))
			titulaccess_font = pygame.font.SysFont('Arial Black', 30)
			titulaccess_text = titulaccess_font.render('пойди еще подкачайся', 1, Red)
			titulaccess_place = titulaccess_text.get_rect(center=(450, 40))
			main_image.blit(titulaccess_text, titulaccess_place)
			timer += 1
			if timer > 60:
				timer = 0
				titulaccess = False

		if champ:
			pygame.draw.rect(main_image, White, (20, 20, 860, 50))
			champ_font = pygame.font.SysFont('Arial Black', 30)
			champ_text = champ_font.render('Вам бросил вызов чемпион, попытайте удачу', 1, Red)
			champ_place = champ_text.get_rect(center=(450, 40))
			main_image.blit(champ_text, champ_place)
			timer += 1
			if timer > 300:
				timer = 0
				champ = False

		if save:
			save_button_font = pygame.font.SysFont('Algerian', 90)
			save_button_text = save_button_font.render('SAVE', 1, color_welcome)
			save_button_place = save_button_text.get_rect(center=(1050, 730))

		if Q:
			Q_text_image = pygame.image.load('images/Q_text.png')
			Q_text_rect = Q_text_image.get_rect(topright=(843, 8))
			main_image.blit(Q_text_image, Q_text_rect)

		if pygame.mouse.get_focused:
			mouse = pygame.mouse.get_pos()
			rect_m = pygame.Rect((mouse[0] - 1, mouse[1] - 1), (2, 2))
			surf_m = pygame.Surface((2, 2))
			surf_m.set_alpha(0)
			sc.blit(surf_m, rect_m)

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			if save_button_place.contains(rect_m):
				save = True
			else:
				save = False

			if Q_rect.contains(rect_m):
				Q = True
			else:
				Q = False

			if i.type == pygame.KEYUP:
				if i.key == pygame.K_RIGHT:
					pygame.mixer.music.stop()
					pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
					pygame.mixer.music.play()
				if i.key == pygame.K_UP:
					pygame.mixer.music.unpause()
					volume += 0.2
					if volume > 1:
						volume = 1
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_DOWN:
					volume -= 0.2
					if volume < 0:
						volume = 0
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_LEFT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.pause()

			if i.type == pygame.MOUSEBUTTONUP and save_button_place.contains(rect_m):
				try:
					with open('experemental_save', 'wb') as s:
						pickle.dump(parametrs, s)
					s.close()
					saved = True
					health_full = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					timer = 0
					sound2.play()

				except:
					not_save = True
					saved = False
					health_full = False
					health_info = False
					titulaccess = False
					champ = False
					timer = 0
					sound3.play()

			if label_streetfight_rect.contains(rect_m):

				streetfight_activ = True
				training_activ = False
				hospital_activ = False
				clubfight_activ = False
				titulfight_activ = False
				chempfight_activ = False

			elif label_training_rect.contains(rect_m):

				streetfight_activ = False
				training_activ = True
				hospital_activ = False
				clubfight_activ = False
				titulfight_activ = False
				chempfight_activ = False

			elif label_hospital_rect.contains(rect_m):

				streetfight_activ = False
				training_activ = False
				hospital_activ = True
				clubfight_activ = False
				titulfight_activ = False
				chempfight_activ = False

			elif label_clubfight_rect.contains(rect_m):

				streetfight_activ = False
				training_activ = False
				hospital_activ = False
				clubfight_activ = True
				titulfight_activ = False
				chempfight_activ = False

			elif label_titulfight_rect.contains(rect_m):

				streetfight_activ = False
				training_activ = False
				hospital_activ = False
				clubfight_activ = False
				titulfight_activ = True
				chempfight_activ = False

			elif parametrs['access'] == 3 and label_chempfight_rect.contains(rect_m):

				streetfight_activ = False
				training_activ = False
				hospital_activ = False
				clubfight_activ = False
				titulfight_activ = False
				chempfight_activ = True

			if i.type == pygame.MOUSEBUTTONUP and label_training_rect.contains(rect_m):
				health_full = False
				saved = False
				not_save = False
				health_info = False
				titulaccess = False
				champ = False
				sound1.play()
				training(parametrs)
				return

			elif i.type == pygame.MOUSEBUTTONUP and label_hospital_rect.contains(rect_m):

				if parametrs['Hp'] < parametrs['MaxHp']:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					sound1.play()
					hospital(parametrs)
				else:
					health_full = True
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False

				return

			elif i.type == pygame.MOUSEBUTTONUP and label_streetfight_rect.contains(rect_m):
				if parametrs['Hp'] > 5:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					if parametrs['dif'] == 1:
						enemy = {
							'Hp': 8 * parametrs['dif'], 'Dmg': r.randint(1, 2) * parametrs['dif'],
							'Money': 15 * parametrs['dif'],
							'UpHp': 0, 'UpDmg': 0, 'UpMoney': 0, 'def': 0.1, 'agi': 0.1, 'cri': 0.09, 'Champ': 0
						}
					if parametrs['dif'] == 1.3:
						enemy = {
							'Hp': 10 * parametrs['dif'], 'Dmg': r.randint(1, 2) * parametrs['dif'],
							'Money': 5 * parametrs['dif'],
							'UpHp': 0, 'UpDmg': 0, 'UpMoney': 0, 'def': 0.1, 'agi': 0.1, 'cri': 0.09, 'Champ': 0
						}
					sound1.play()
					battleround(parametrs, enemy)
				else:
					health_info = True
					health_full = False
					saved = False
					not_save = False
					titulaccess = False
					champ = False
				return

			elif i.type == pygame.MOUSEBUTTONUP and label_clubfight_rect.contains(rect_m):
				if parametrs['access'] == 0:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					club = 'club'
					sound1.play()
					access(parametrs, club)
				elif parametrs['Hp'] > 10:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					if parametrs['dif'] == 1:
						enemy = {
							'Hp': 10.5 * parametrs['dif'], 'Dmg': 3.8 * parametrs['dif'], 'Money': 40.5 * parametrs['dif'],
							'UpHp': 1.1 * parametrs['dif'], 'UpDmg': 0.2 * parametrs['dif'],
							'UpMoney': 4.5 * parametrs['dif'],
							'def': 0.15, 'agi': 0.15, 'cri': 0.12, 'Champ': 0
						}
					if parametrs['dif'] == 1.3:
						enemy = {
							'Hp': 13.5 * parametrs['dif'], 'Dmg': 3.8 * parametrs['dif'], 'Money': 13.5 * parametrs['dif'],
							'UpHp': 1.5 * parametrs['dif'], 'UpDmg': 0.2 * parametrs['dif'],
							'UpMoney': 1.5 * parametrs['dif'],
							'def': 0.15, 'agi': 0.15, 'cri': 0.12, 'Champ': 0
						}
					sound1.play()
					battleround(parametrs, enemy)
				else:
					health_info = True
					health_full = False
					saved = False
					not_save = False
					titulaccess = False
					champ = False
				return

			elif i.type == pygame.MOUSEBUTTONUP and label_titulfight_rect.contains(rect_m):
				if parametrs['Exp'] < 30:
					titulaccess = True
					health_full = False
					saved = False
					not_save = False
					health_info = False
					champ = False
				elif parametrs['access'] == 1:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					club = 'titul'
					sound1.play()
					access(parametrs, club)
				elif parametrs['Hp'] > 30 and parametrs['access'] > 1:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					if parametrs['dif'] == 1:
						enemy = {
							'Hp': 35 * parametrs['dif'], 'Dmg': 6.5 * parametrs['dif'], 'Money': 210 * parametrs['dif'],
							'UpHp': 2 * parametrs['dif'], 'UpDmg': 0.35 * parametrs['dif'],
							'UpMoney': 30 * parametrs['dif'],
							'def': 0.18, 'agi': 0.18, 'cri': 0.16, 'Champ': 0
						}
					if parametrs['dif'] == 1.3:
						enemy = {
							'Hp': 40 * parametrs['dif'], 'Dmg': 6.5 * parametrs['dif'], 'Money': 70 * parametrs['dif'],
							'UpHp': 3 * parametrs['dif'], 'UpDmg': 0.35 * parametrs['dif'],
							'UpMoney': 10 * parametrs['dif'],
							'def': 0.18, 'agi': 0.18, 'cri': 0.16, 'Champ': 0
						}
					sound1.play()
					battleround(parametrs, enemy)
				else:
					health_info = True
					health_full = False
					saved = False
					not_save = False
					titulaccess = False
					champ = False
				return

			elif i.type == pygame.MOUSEBUTTONUP and parametrs['access'] == 3 and label_chempfight_rect.contains(rect_m):
				if parametrs['Hp'] > 5:
					health_full = False
					saved = False
					not_save = False
					health_info = False
					titulaccess = False
					champ = False
					if parametrs['dif'] == 1:
						enemy = {
							'Hp': 300 * parametrs['dif'], 'Dmg': 30 * parametrs['dif'], 'Money': 300000 * parametrs['dif'],
							'UpHp': 0 * parametrs['dif'], 'UpDmg': 0 * parametrs['dif'], 'UpMoney': 0 * parametrs['dif'],
							'def': 0.22, 'agi': 0.22, 'cri': 0.25, 'Champ': 1
						}
					if parametrs['dif'] == 1.3:
						enemy = {
							'Hp': 400 * parametrs['dif'], 'Dmg': 30 * parametrs['dif'],
							'Money': 100000 * parametrs['dif'],
							'UpHp': 0 * parametrs['dif'], 'UpDmg': 0 * parametrs['dif'],
							'UpMoney': 0 * parametrs['dif'],
							'def': 0.22, 'agi': 0.22, 'cri': 0.25, 'Champ': 1
						}
					sound1.play()
					battleround(parametrs, enemy)
				else:
					health_info = True
					health_full = False
					saved = False
					not_save = False
					titulaccess = False
					champ = False
				return

		main_image.blit(label_streetfight, label_streetfight_rect)
		main_image.blit(label_training, label_training_rect)
		main_image.blit(label_hospital, label_hospital_rect)
		main_image.blit(label_clubfight, label_clubfight_rect)
		main_image.blit(label_titulfight, label_titulfight_rect)
		if parametrs['access'] == 3:
			main_image.blit(label_chempfight, label_chempfight_rect)

		sc.blit(main_image, main_rect)
		sc.blit(ava, ava_rect)

		sc.blit(dif_im, dif_im_rect)
		sc.blit(dif_text, dif_text_place)

		sc.blit(info_im, info_im_rect)
		sc.blit(par_name_text, par_text_place)
		sc.blit(par_exp_text, par_exp_place)
		sc.blit(par_dmg_text, par_dmg_place)
		sc.blit(par_hp_text, par_hp_place)
		sc.blit(par_money_text, par_money_place)
		sc.blit(par_stats_text, par_stats_place)
		sc.blit(save_button_text, save_button_place)
		sc.blit(Q_image, Q_rect)

		pygame.display.update()
		clock.tick(FPS)


def hospital(parametrs):

	global health, Exit, health_info, timer, not_enough_money, health_full, volume

	sound1 = pygame.mixer.Sound('sound/01085.ogg')
	sound2 = pygame.mixer.Sound('sound/01095.ogg')

	ava = pygame.image.load('images/ava.jpg')
	ava_rect = ava.get_rect(topleft=(900, 0))

	dif_im = pygame.image.load('images/difficult.png')
	dif_im_rect = dif_im.get_rect(topleft=(900, 200))

	info_im = pygame.image.load('images/info.png')
	info_im_rect = info_im.get_rect(topleft=(900, 280))

	dif_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 28)
	dif_text = dif_font.render('Сложность: {}'.format('нормальная' if parametrs['dif'] == 1 else 'повышенная'), 1,
							   Red)
	dif_text_place = dif_text.get_rect(topleft=(918, 215))

	par_name_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 30)
	par_name_text = par_name_font.render('Ваши параметры:', 1, Yellow)
	par_text_place = par_name_text.get_rect(topleft=(928, 310))

	par_exp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_exp_text = par_exp_font.render('Опытность       =  {}'.format(parametrs['Exp']), 1, Gray_Exp)
	par_exp_place = par_exp_text.get_rect(topleft=(928, 360))

	par_dmg_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_dmg_text = par_dmg_font.render('Урон                    =  {}'.format(parametrs['Dmg']), 1, Red_Dmg)
	par_dmg_place = par_dmg_text.get_rect(topleft=(928, 390))

	par_stats_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_stats_text = par_stats_font.render('боев/побед    =  {}/{}'.format(parametrs['Fight'],
																		   parametrs['Win']), 1, Black)
	par_stats_place = par_stats_text.get_rect(topleft=(928, 480))

	while True:

		if pygame.mixer.music.get_busy():
			pass
		else:
			pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
			pygame.mixer.music.play()

		sc.fill(White)

		hospital_image = pygame.image.load('images/hospital.jpg')
		hospital_rect = hospital_image.get_rect(topleft=(0, 0))

		pygame.draw.rect(hospital_image, White, (170, 730, 560, 50))

		info_health_font = pygame.font.SysFont('Arial Black', 30)
		info_health_text = info_health_font.render('стоимость лечения 10', 1, SoftGray)
		info_health_place = info_health_text.get_rect(center=(450, 755))
		hospital_image.blit(info_health_text, info_health_place)

		par_hp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_hp_text = par_hp_font.render('Жизни                =  {}'.format(parametrs['Hp']), 1, Green_Hp)
		par_hp_place = par_hp_text.get_rect(topleft=(928, 420))

		par_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_money_text = par_money_font.render('Средства          =  {}'.format(parametrs['Money']), 1, Sky_Money)
		par_money_place = par_money_text.get_rect(topleft=(928, 450))

		exit_button_font = pygame.font.SysFont('Comic Sans MS', 76)
		exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
		exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		health_button_font = pygame.font.SysFont('Comic Sans MS', 52)
		health_button_text = health_button_font.render('лечиться', 1, Green)
		health_button_place = health_button_text.get_rect(center=(1050, 630))

		if Exit:
			exit_button_font = pygame.font.SysFont('Comic Sans MS', 80)
			exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
			exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		if health:
			health_button_font = pygame.font.SysFont('Comic Sans MS', 56)
			health_button_text = health_button_font.render('лечиться', 1, Green)
			health_button_place = health_button_text.get_rect(center=(1050, 630))

		if pygame.mouse.get_focused:
			mouse = pygame.mouse.get_pos()
			rect_m = pygame.Rect((mouse[0] - 1, mouse[1] - 1), (2, 2))
			surf_m = pygame.Surface((2, 2))
			surf_m.set_alpha(0)
			sc.blit(surf_m, rect_m)

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

			if i.type == pygame.KEYUP:
				if i.key == pygame.K_RIGHT:
					pygame.mixer.music.stop()
					pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
					pygame.mixer.music.play()
				if i.key == pygame.K_UP:
					pygame.mixer.music.unpause()
					volume += 0.2
					if volume > 1:
						volume = 1
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_DOWN:
					volume -= 0.2
					if volume < 0:
						volume = 0
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_LEFT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.pause()

			if health_button_place.contains(rect_m):
				health = True
			else:
				health = False

			if exit_button_place.contains(rect_m):
				Exit = True
			else:
				Exit = False

			if i.type == pygame.MOUSEBUTTONUP and exit_button_place.contains(rect_m):
				health_info = False
				not_enough_money = False
				sound1.play()
				return

			if i.type == pygame.MOUSEBUTTONUP and health_button_place.contains(rect_m):
				if parametrs['Money'] >= 10 and parametrs['Hp'] < parametrs['MaxHp']:
					sound2.play()
					parametrs['Hp'] += 30
					parametrs['Hp'] = int(parametrs['Hp'] * 100) / 100
					parametrs['Money'] -= 10
					parametrs['Money'] = int(parametrs['Money'] * 100) / 100
					if parametrs['Hp'] >= parametrs['MaxHp']:
						parametrs['Hp'] = parametrs['MaxHp']
					health_info = True
					not_enough_money = False
					health_full = False

				elif parametrs['Hp'] < parametrs['MaxHp'] and parametrs['Money'] < 10:
					not_enough_money = True
					health_info = False
					health_full = False

				elif parametrs['Hp'] == parametrs['MaxHp']:
					health_full = True
					health_info = False
					not_enough_money = False

		if health_info:
			pygame.draw.rect(hospital_image, White, (200, 20, 500, 50))
			health_font = pygame.font.SysFont('Arial Black', 30)
			health_text = health_font.render('восстановлено 30 hp', 1, Green)
			health_place = health_text.get_rect(center=(450, 40))
			hospital_image.blit(health_text, health_place)
			timer += 1
			if timer > 60:
				timer = 0
				health_info = False

		if not_enough_money:
			pygame.draw.rect(hospital_image, White, (200, 20, 500, 50))
			health_font = pygame.font.SysFont('Arial Black', 30)
			health_text = health_font.render('не достаточно средств', 1, Red)
			health_place = health_text.get_rect(center=(450, 40))
			hospital_image.blit(health_text, health_place)
			timer += 1
			if timer > 60:
				timer = 0
				not_enough_money = False

		if health_full:
			pygame.draw.rect(hospital_image, White, (200, 20, 500, 50))
			full_health_font = pygame.font.SysFont('Arial Black', 30)
			full_health_text = full_health_font.render('Вы полностью здоровы', 1, Green)
			full_health_place = full_health_text.get_rect(center=(450, 40))
			hospital_image.blit(full_health_text, full_health_place)
			timer += 1
			if timer > 60:
				timer = 0
				health_full = False

		sc.blit(hospital_image, hospital_rect)
		sc.blit(ava, ava_rect)
		sc.blit(dif_im, dif_im_rect)
		sc.blit(info_im, info_im_rect)

		sc.blit(dif_text, dif_text_place)
		sc.blit(par_name_text, par_text_place)
		sc.blit(par_exp_text, par_exp_place)
		sc.blit(par_dmg_text, par_dmg_place)
		sc.blit(par_hp_text, par_hp_place)
		sc.blit(par_money_text, par_money_place)
		sc.blit(par_stats_text, par_stats_place)

		sc.blit(exit_button_text, exit_button_place)
		sc.blit(health_button_text, health_button_place)

		pygame.display.update()

		clock.tick(FPS)


def training(parametrs):

	global Exit, timer, not_enough_money, Trainig, Trainig_info, volume

	sound1 = pygame.mixer.Sound('sound/01085.ogg')
	sound2 = pygame.mixer.Sound('sound/01095.ogg')

	ava = pygame.image.load('images/ava.jpg')
	ava_rect = ava.get_rect(topleft=(900, 0))

	dif_im = pygame.image.load('images/difficult.png')
	dif_im_rect = dif_im.get_rect(topleft=(900, 200))

	info_im = pygame.image.load('images/info.png')
	info_im_rect = info_im.get_rect(topleft=(900, 280))

	dif_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 28)
	dif_text = dif_font.render('Сложность: {}'.format('нормальная' if parametrs['dif'] == 1 else 'повышенная'), 1,
							   Red)
	dif_text_place = dif_text.get_rect(topleft=(918, 215))

	par_name_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 30)
	par_name_text = par_name_font.render('Ваши параметры:', 1, Yellow)
	par_text_place = par_name_text.get_rect(topleft=(928, 310))

	par_stats_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_stats_text = par_stats_font.render('боев/побед    =  {}/{}'.format(parametrs['Fight'],
																		   parametrs['Win']), 1, Black)
	par_stats_place = par_stats_text.get_rect(topleft=(928, 480))

	while True:

		if pygame.mixer.music.get_busy():
			pass
		else:
			pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
			pygame.mixer.music.play()

		sc.fill(White)

		sport_image = pygame.image.load('images/sport.jpg')
		sport_rect = sport_image.get_rect(topleft=(0, 0))

		if parametrs['cost'] > 1000000:
			pygame.draw.rect(sport_image, White, (140, 730, 620, 50))
		else:
			pygame.draw.rect(sport_image, White, (170, 730, 560, 50))

		info_training_font = pygame.font.SysFont('Arial Black', 30)
		info_training_text = info_training_font.render('стоимость тренеровки {}'.format(parametrs['cost']), 1, SoftGray)
		info_training_place = info_training_text.get_rect(center=(450, 755))
		sport_image.blit(info_training_text, info_training_place)

		par_exp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_exp_text = par_exp_font.render('Опытность       =  {}'.format(parametrs['Exp']), 1, Gray_Exp)
		par_exp_place = par_exp_text.get_rect(topleft=(928, 360))

		par_hp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_hp_text = par_hp_font.render('Жизни                =  {}'.format(parametrs['Hp']), 1, Green_Hp)
		par_hp_place = par_hp_text.get_rect(topleft=(928, 420))

		par_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_money_text = par_money_font.render('Средства          =  {}'.format(parametrs['Money']), 1, Sky_Money)
		par_money_place = par_money_text.get_rect(topleft=(928, 450))

		par_dmg_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_dmg_text = par_dmg_font.render('Урон                    =  {}'.format(parametrs['Dmg']), 1, Red_Dmg)
		par_dmg_place = par_dmg_text.get_rect(topleft=(928, 390))

		exit_button_font = pygame.font.SysFont('Comic Sans MS', 76)
		exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
		exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		sport_button_font = pygame.font.SysFont('Comic Sans MS', 54)
		sport_button_text = sport_button_font.render('качаться', 1, Red)
		sport_button_place = sport_button_text.get_rect(center=(1050, 630))

		if Exit:
			exit_button_font = pygame.font.SysFont('Comic Sans MS', 80)
			exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
			exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		if Trainig:
			sport_button_font = pygame.font.SysFont('Comic Sans MS', 58)
			sport_button_text = sport_button_font.render('качаться', 1, Red)
			sport_button_place = sport_button_text.get_rect(center=(1050, 630))

		if pygame.mouse.get_focused:
			mouse = pygame.mouse.get_pos()
			rect_m = pygame.Rect((mouse[0] - 1, mouse[1] - 1), (2, 2))
			surf_m = pygame.Surface((2, 2))
			surf_m.set_alpha(0)
			sc.blit(surf_m, rect_m)

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

			if i.type == pygame.KEYUP:
				if i.key == pygame.K_RIGHT:
					pygame.mixer.music.stop()
					pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
					pygame.mixer.music.play()
				if i.key == pygame.K_UP:
					pygame.mixer.music.unpause()
					volume += 0.2
					if volume > 1:
						volume = 1
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_DOWN:
					volume -= 0.2
					if volume < 0:
						volume = 0
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_LEFT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.pause()

			if sport_button_place.contains(rect_m):
				Trainig = True
			else:
				Trainig = False

			if exit_button_place.contains(rect_m):
				Exit = True
			else:
				Exit = False

			if i.type == pygame.MOUSEBUTTONUP and exit_button_place.contains(rect_m):
				not_enough_money = False
				Trainig_info = False
				sound1.play()
				return

			if i.type == pygame.MOUSEBUTTONUP and sport_button_place.contains(rect_m):
				if parametrs['Money'] >= parametrs['cost']:
					sound2.play()
					parametrs['Money'] -= parametrs['cost']
					parametrs['Money'] = int(parametrs['Money'] * 100) / 100
					parametrs['Exp'] += 1
					parametrs['Hp'] += 2
					parametrs['MaxHp'] += 2
					parametrs['Dmg'] += 0.5
					parametrs['def'] += 0.0045
					parametrs['def'] = int(parametrs['def'] * 10000) / 10000
					parametrs['agi'] += 0.0045
					parametrs['agi'] = int(parametrs['agi'] * 10000) / 10000
					parametrs['cri'] += 0.0035
					parametrs['cri'] = int(parametrs['cri'] * 10000) / 10000
					parametrs['cost'] += parametrs['raise']
					if parametrs['dif'] == 1:
						parametrs['raise'] += 2
					if parametrs['dif'] == 1.3:
						parametrs['raise'] += 3
					Trainig_info = True
					not_enough_money = False

				elif parametrs['Money'] < parametrs['cost']:
					not_enough_money = True
					Trainig_info = False


		if Trainig_info:
			pygame.draw.rect(sport_image, White, (200, 20, 500, 50))
			trainig_font = pygame.font.SysFont('Arial Black', 30)
			trainig_text = trainig_font.render('вы стали еще сильнее', 1, Green)
			trainig_place = trainig_text.get_rect(center=(450, 40))
			sport_image.blit(trainig_text, trainig_place)
			timer += 1
			if timer > 60:
				timer = 0
				Trainig_info = False

		if not_enough_money:
			pygame.draw.rect(sport_image, White, (200, 20, 500, 50))
			trainig_font = pygame.font.SysFont('Arial Black', 30)
			trainig_text = trainig_font.render('не достаточно средств', 1, Red)
			trainig_place = trainig_text.get_rect(center=(450, 40))
			sport_image.blit(trainig_text, trainig_place)
			timer += 1
			if timer > 60:
				timer = 0
				not_enough_money = False

		sc.blit(sport_image, sport_rect)
		sc.blit(ava, ava_rect)
		sc.blit(dif_im, dif_im_rect)
		sc.blit(info_im, info_im_rect)

		sc.blit(dif_text, dif_text_place)
		sc.blit(par_name_text, par_text_place)
		sc.blit(par_exp_text, par_exp_place)
		sc.blit(par_dmg_text, par_dmg_place)
		sc.blit(par_hp_text, par_hp_place)
		sc.blit(par_money_text, par_money_place)
		sc.blit(par_stats_text, par_stats_place)

		sc.blit(exit_button_text, exit_button_place)
		sc.blit(sport_button_text, sport_button_place)

		pygame.display.update()

		clock.tick(FPS)


def access(parametrs, club):

	buy = False
	bought = False

	global Exit, timer, not_enough_money, volume

	sound1 = pygame.mixer.Sound('sound/09415.ogg')
	sound2 = pygame.mixer.Sound('sound/01085.ogg')

	ava = pygame.image.load('images/ava.jpg')
	ava_rect = ava.get_rect(topleft=(900, 0))

	dif_im = pygame.image.load('images/difficult.png')
	dif_im_rect = dif_im.get_rect(topleft=(900, 200))

	info_im = pygame.image.load('images/info.png')
	info_im_rect = info_im.get_rect(topleft=(900, 280))

	dif_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 28)
	dif_text = dif_font.render('Сложность: {}'.format('нормальная' if parametrs['dif'] == 1 else 'повышенная'), 1,
							   Red)
	dif_text_place = dif_text.get_rect(topleft=(918, 215))

	par_name_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 30)
	par_name_text = par_name_font.render('Ваши параметры:', 1, Yellow)
	par_text_place = par_name_text.get_rect(topleft=(928, 310))

	par_exp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_exp_text = par_exp_font.render('Опытность       =  {}'.format(parametrs['Exp']), 1, Gray_Exp)
	par_exp_place = par_exp_text.get_rect(topleft=(928, 360))

	par_dmg_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_dmg_text = par_dmg_font.render('Урон                    =  {}'.format(parametrs['Dmg']), 1, Red_Dmg)
	par_dmg_place = par_dmg_text.get_rect(topleft=(928, 390))

	par_hp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_hp_text = par_hp_font.render('Жизни                =  {}'.format(parametrs['Hp']), 1, Green_Hp)
	par_hp_place = par_hp_text.get_rect(topleft=(928, 420))

	par_stats_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_stats_text = par_stats_font.render('боев/побед    =  {}/{}'.format(parametrs['Fight'],
																		   parametrs['Win']), 1, Black)
	par_stats_place = par_stats_text.get_rect(topleft=(928, 480))

	while True:

		if pygame.mixer.music.get_busy():
			pass
		else:
			pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
			pygame.mixer.music.play()

		sc.fill(White)

		if club == 'club':
			clubcontrol_image = pygame.image.load('images/clubcontrol.jpg')
			clubcontrol_rect = clubcontrol_image.get_rect(topleft=(0, 0))
		elif club == 'titul':
			clubcontrol_image = pygame.image.load('images/titulcontrol.jpg')
			clubcontrol_rect = clubcontrol_image.get_rect(topleft=(0, 0))

		par_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
		par_money_text = par_money_font.render('Средства          =  {}'.format(parametrs['Money']), 1, Sky_Money)
		par_money_place = par_money_text.get_rect(topleft=(928, 450))

		if club == 'club':
			abon_font = pygame.font.SysFont('Arial Black', 30)
			abon_text = abon_font.render('стоимость абонемента 100', 1, DarkRed)
			abon_place = abon_text.get_rect(center=(450, 755))
		elif club == 'titul':
			abon_font = pygame.font.SysFont('Arial Black', 30)
			abon_text = abon_font.render('стоимость абонемента 2000', 1, DarkRed)
			abon_place = abon_text.get_rect(center=(450, 755))

		exit_button_font = pygame.font.SysFont('Comic Sans MS', 76)
		exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
		exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		buy_font = pygame.font.SysFont('Comic Sans MS', 52)
		buy_text = buy_font.render('купить', 1, Yellow)
		buy_place = buy_text.get_rect(center=(1050, 630))

		if Exit:
			exit_button_font = pygame.font.SysFont('Comic Sans MS', 80)
			exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
			exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		if buy:
			buy_font = pygame.font.SysFont('Comic Sans MS', 56)
			buy_text = buy_font.render('купить', 1, Yellow)
			buy_place = buy_text.get_rect(center=(1050, 630))

		if pygame.mouse.get_focused:
			mouse = pygame.mouse.get_pos()
			rect_m = pygame.Rect((mouse[0] - 1, mouse[1] - 1), (2, 2))
			surf_m = pygame.Surface((2, 2))
			surf_m.set_alpha(0)
			sc.blit(surf_m, rect_m)

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

			if i.type == pygame.KEYUP:
				if i.key == pygame.K_RIGHT:
					pygame.mixer.music.stop()
					pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
					pygame.mixer.music.play()
				if i.key == pygame.K_UP:
					pygame.mixer.music.unpause()
					volume += 0.2
					if volume > 1:
						volume = 1
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_DOWN:
					volume -= 0.2
					if volume < 0:
						volume = 0
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_LEFT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.pause()

			if buy_place.contains(rect_m):
				buy = True
			else:
				buy = False

			if exit_button_place.contains(rect_m):
				Exit = True
			else:
				Exit = False

			if i.type == pygame.MOUSEBUTTONUP and exit_button_place.contains(rect_m):
				bought = False
				not_enough_money = False
				sound2.play()
				return

			if i.type == pygame.MOUSEBUTTONUP and buy_place.contains(rect_m):
				if club == 'club':
					if parametrs['access'] == 0 and parametrs['Money'] >= 100:
						sound1.play()
						parametrs['Money'] -= 100
						parametrs['Money'] = int(parametrs['Money'] * 100) / 100
						parametrs['access'] += 1
						bought = True
						not_enough_money = False

					elif parametrs['access'] == 0 and parametrs['Money'] < 100:
						not_enough_money = True
						bought = False

					else:
						bought = True
						not_enough_money = False

				elif club == 'titul':
					if parametrs['access'] == 1 and parametrs['Money'] >= 2000:
						sound1.play()
						parametrs['Money'] -= 2000
						parametrs['Money'] = int(parametrs['Money'] * 100) / 100
						parametrs['access'] += 1
						bought = True
						not_enough_money = False

					elif parametrs['access'] == 1 and parametrs['Money'] < 2000:
						not_enough_money = True
						bought = False

					else:
						bought = True
						not_enough_money = False

		if bought:
			pygame.draw.rect(clubcontrol_image, White, (200, 20, 500, 50))
			bought_font = pygame.font.SysFont('Arial Black', 30)
			bought_text = bought_font.render('абонемент куплен', 1, Green)
			bought_place = bought_text.get_rect(center=(450, 40))
			clubcontrol_image.blit(bought_text, bought_place)
			timer += 1
			if timer > 60:
				timer = 0
				bought = False

		if not_enough_money:
			pygame.draw.rect(clubcontrol_image, White, (200, 20, 500, 50))
			bought_font = pygame.font.SysFont('Arial Black', 30)
			bought_text = bought_font.render('не достаточно средств', 1, Red)
			bought_place = bought_text.get_rect(center=(450, 40))
			clubcontrol_image.blit(bought_text, bought_place)
			timer += 1
			if timer > 60:
				timer = 0
				not_enough_money = False

		sc.blit(clubcontrol_image, clubcontrol_rect)
		sc.blit(ava, ava_rect)
		sc.blit(dif_im, dif_im_rect)
		sc.blit(info_im, info_im_rect)

		sc.blit(dif_text, dif_text_place)
		sc.blit(par_name_text, par_text_place)
		sc.blit(par_exp_text, par_exp_place)
		sc.blit(par_dmg_text, par_dmg_place)
		sc.blit(par_hp_text, par_hp_place)
		sc.blit(par_money_text, par_money_place)
		sc.blit(par_stats_text, par_stats_place)

		sc.blit(exit_button_text, exit_button_place)
		sc.blit(buy_text, buy_place)
		pygame.draw.rect(sc, White, (170, 730, 560, 50))
		sc.blit(abon_text, abon_place)

		pygame.display.update()
		clock.tick(FPS)


def battleround(parametrs, enemy):

	global win, Exit, volume

	sound1 = pygame.mixer.Sound('sound/09145.ogg')
	sound2 = pygame.mixer.Sound('sound/01085.ogg')
	sound3 = pygame.mixer.Sound('sound/09475.ogg')
	sound4 = pygame.mixer.Sound('sound/09150.ogg')
	sound5 = pygame.mixer.Sound('sound/09015.ogg')
	sound6 = pygame.mixer.Sound('sound/00069.ogg')

	money = 0

	for i in range(1, 11):
		backup = dict.copy(enemy)
		enemy['Hp'] += (enemy['UpHp']*i)
		enemy['Hp'] = int(enemy['Hp']*100)/100
		enemy['Dmg'] += (enemy['UpDmg']*i)
		enemy['Dmg'] = int(enemy['Dmg']*100)/100
		enemy['Money'] += (enemy['UpMoney']*i)
		enemy['Money'] = int(enemy['Money']*100)/100
		print('___________')
		if enemy['Champ'] != 1:  # Для всех боев кроме финального
			print('Раунд ', i, '/ 10')
		else:
			print('Бой за титул чемпиона')
		print('Ваши параметры:  урон = {}; жизни = {};'.format(parametrs['Dmg'], parametrs['Hp']))
		print('Параметры противника:  урон = {}; жизни = {};'.format(enemy['Dmg'], enemy['Hp']))
		print('_____________________________________________________')
		H1 = parametrs['MaxHp']
		H2 = enemy['Hp']
		parametrs['Fight'] += 1
		while parametrs['Hp'] > 0 and enemy['Hp'] > 0:
			x = r.randint(0, 1)
			d = r.random()
			d = int(d * 10000) / 10000
			a = r.random()
			a = int(a * 10000) / 10000
			c = r.random()
			c = int(c * 10000) / 10000
			if x == 0:  # Удар игрока
				if d < enemy['def']:  # Проверка на блок
					if c < (parametrs['cri']*3):
						punch = parametrs['Dmg'] + parametrs['Dmg'] * parametrs['cri']
						punch = int(punch * 100) / 100
						enemy['Hp'] -= punch
						enemy['Hp'] = int(enemy['Hp']*100) / 100
						print(
						'Противник пытается защититься но ', Fore.YELLOW, Name, Fore.RESET, ' с ', Fore.RED, 'яростью',
						Fore.RESET,	' в глазах пробивает блок ', Fore.RED,punch,Fore.RESET, '| ',
						enemy['Hp'] if enemy['Hp'] >= 0 else 0, '/', H2, sep=''
						)
					else:
						print(
						'Противник ', Fore.GREEN, 'блокирует', Fore.RESET, ' успешно удар. ', Fore.GREEN, '0',
						Fore.RESET, '| ', enemy['Hp'] if enemy['Hp'] >= 0 else 0, '/', H2, sep=''
						)
					continue
				if a < enemy['agi']:  # Провка на уворот
					if c < (parametrs['cri']*3):
						enemy['Hp'] -= parametrs['Dmg']
						enemy['Hp'] = int(enemy['Hp']*100) / 100
						print(
						'Противник пытаясь ', Style.BRIGHT, 'увернуться', Style.RESET_ALL, ', споткнулся и упал. ',
						Style.BRIGHT, parametrs['Dmg'], Style.RESET_ALL, '| ', enemy['Hp'] if enemy['Hp'] >= 0 else 0,
						'/', H2, sep=''
						)
					else:
						print(
						'Противник успешно ', Fore.CYAN, 'уворачивается', Fore.RESET, ' от удара. ', Fore.CYAN, '0',
						Fore.RESET,	'| ', enemy['Hp'] if enemy['Hp'] >= 0 else 0, '/', H2, sep=''
						)
					continue
				if c < parametrs['cri']:  # Проверка на крит
					punch = parametrs['Dmg'] + parametrs['Dmg'] * parametrs['cri']
					punch = int(punch*100) / 100
					enemy['Hp'] -= punch
					enemy['Hp'] = int(enemy['Hp']*100) / 100
					print(
					Fore.YELLOW, Name, Fore.RESET, ' с криком ', Fore.RED, 'втаскивает',Fore.RESET, ' противнику ',
					Fore.RED, punch, Fore.RESET, '| ', enemy['Hp'] if enemy['Hp'] >= 0 else 0, '/', H2, sep=''
					)
					continue

				enemy['Hp'] -= parametrs['Dmg']
				enemy['Hp'] = int(enemy['Hp']*100) / 100
				print(
				Fore.YELLOW, Name, Fore.RESET, ' наносит урон противнику ', parametrs['Dmg'],
				'| ', enemy['Hp'] if enemy['Hp'] >= 0 else 0, '/', H2, sep=''
				)

			else:  # Удар противника
				if d < parametrs['def']:  # Проверка на блок
					if c < (enemy['cri']*3):
						punch = enemy['Dmg'] + enemy['Dmg'] * enemy['cri']
						punch = int(punch*100) / 100
						parametrs['Hp'] -= punch
						parametrs['Hp'] = int(parametrs['Hp']*100) / 100
						print(
						Fore.YELLOW, Name, Fore.RESET, ' подумал о ', Fore.RED, 'блоке', Fore.RESET,
						', но было уже поздно ', Fore.RED, punch, Fore.RESET, '| ',
						parametrs['Hp'] if parametrs['Hp'] >= 0 else 0, '/', H1, sep=''
						)
					else:
						print(
						'Богоподобно ', Fore.YELLOW, Name, Fore.RESET, ' ', Fore.GREEN, 'блокирует', Fore.RESET,
						' удар ', Fore.GREEN, '0', Fore.RESET, '| ',
						parametrs['Hp'] if parametrs['Hp'] >= 0 else 0, '/', H1, sep=''
						)
					continue
				if a < parametrs['agi']:  # Провка на уворот
					if c < (enemy['cri']*3):
						parametrs['Hp'] -= enemy['Dmg']
						parametrs['Hp'] = int(parametrs['Hp']*100) / 100
						print(
						Style.BRIGHT, 'Прыжок', Style.RESET_ALL, ' в сторону ', Fore.YELLOW, Name, Fore.RESET,
						' не увенчался успехом ', Style.BRIGHT, enemy['Dmg'], Style.RESET_ALL, '| ',
						parametrs['Hp'] if parametrs['Hp'] >= 0 else 0, '/', H1, sep=''
						)
					else:
						print(
						'Как смерч ', Fore.YELLOW, Name, Fore.RESET, ' ', Fore.CYAN, 'увернулся', Fore.RESET,
						' от удара ', Fore.CYAN, '0', Fore.RESET, '| ',
						parametrs['Hp'] if parametrs['Hp'] >= 0 else 0, '/', H1, sep=''
						)
					continue
				if c < enemy['cri']:  # Проверка на крит
					punch = enemy['Dmg'] + enemy['Dmg'] * enemy['cri']
					punch = int(punch*100) / 100
					parametrs['Hp'] -= punch
					parametrs['Hp'] = int(parametrs['Hp']*100) / 100
					print(
					'Противник ', Fore.RED, 'размашистым', Fore.RESET, ' ударом встречает ',
					Fore.YELLOW, Name, Fore.RESET, ' ',	Fore.RED, punch, Fore.RESET, '| ',
					parametrs['Hp'] if parametrs['Hp'] >= 0 else 0, '/', H1, sep=''
					)
					continue

				parametrs['Hp'] -= enemy['Dmg']
				parametrs['Hp'] = int(parametrs['Hp']*1000) / 1000
				print(
				'Противник наносит урон ', enemy['Dmg'], '| ',
				parametrs['Hp'] if parametrs['Hp'] >= 0 else 0, '/', H1, sep=''
				)

		if parametrs['Hp'] < 1:
			print('___________')
			print('Вы проиграли')
			parametrs['Hp'] = 0
			win = False
			victory = i - 1
			if enemy['Champ'] == 1:
				sound3.play()
			break
		else:
			if enemy['Champ'] != 1 and i == 10:
				sound1.play()
			print('___________')
			print('Вы выйграли. Награда за победу:', enemy['Money'])
			parametrs['Money'] += enemy['Money']
			parametrs['Money'] = int(parametrs['Money']*100) / 100
			parametrs['Win'] += 1
			if enemy['Champ'] == 1:  # Для финального боя
				parametrs['access'] += 1
				print()
				print(Back.GREEN, '                                                   ', Back.RESET)
				print(Style.BRIGHT, Back.YELLOW, '                                                     ',
					  Style.RESET_ALL, sep='')
				print('         Вы только что победили чемпиона')
				print('Данный титул теперь закреплен за Вами. Поздравляем', Back.MAGENTA, Style.BRIGHT, Fore.WHITE,
					  '!!!', Style.RESET_ALL, sep='')
				print(Style.BRIGHT, Back.YELLOW, '                                                     ',
					  Style.RESET_ALL, sep='')
				print(Back.GREEN, '                                                   ', Back.RESET)
				print()
				win = True
				victory = i
				money += enemy['Money']
				money = int(money * 100) / 100
				break
			if i == 10:
				win = True
				victory = i
			money += enemy['Money']
			money = int(money * 100) / 100
			enemy = dict.copy(backup)

	random_fon_defeat = [pygame.image.load('images/defeat.jpg'), pygame.image.load('images/defeat2.jpg'),
						 pygame.image.load('images/defeat3.jpg')]
	random_fon_victory = [pygame.image.load('images/victory.jpg'), pygame.image.load('images/win.jpg')]

	if win:
		victory_fon = random_fon_victory[0]
	else:
		victory_fon = random_fon_defeat[r.randint(0, 2)]
	victory_rect = victory_fon.get_rect(topleft=(0, 0))

	ava = pygame.image.load('images/ava.jpg')
	ava_rect = ava.get_rect(topleft=(900, 0))

	dif_im = pygame.image.load('images/difficult.png')
	dif_im_rect = dif_im.get_rect(topleft=(900, 200))

	dif_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 28)
	dif_text = dif_font.render('Сложность: {}'.format('нормальная' if parametrs['dif'] == 1 else 'повышенная'), 1, Red)
	dif_text_place = dif_text.get_rect(topleft=(918, 215))

	par_name_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 30)
	par_name_text = par_name_font.render('Ваши параметры:', 1, Yellow)
	par_text_place = par_name_text.get_rect(topleft=(928, 310))

	par_exp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_exp_text = par_exp_font.render('Опытность       =  {}'.format(parametrs['Exp']), 1, Gray_Exp)
	par_exp_place = par_exp_text.get_rect(topleft=(928, 360))

	par_dmg_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_dmg_text = par_dmg_font.render('Урон                    =  {}'.format(parametrs['Dmg']), 1, Red_Dmg)
	par_dmg_place = par_dmg_text.get_rect(topleft=(928, 390))

	par_hp_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_hp_text = par_hp_font.render('Жизни                =  {}'.format(parametrs['Hp']), 1, Green_Hp)
	par_hp_place = par_hp_text.get_rect(topleft=(928, 420))

	par_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_money_text = par_money_font.render('Средства          =  {}'.format(parametrs['Money']), 1, Sky_Money)
	par_money_place = par_money_text.get_rect(topleft=(928, 450))

	par_stats_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 24)
	par_stats_text = par_stats_font.render('боев/побед    =  {}/{}'.format(parametrs['Fight'],
																		   parametrs['Win']), 1, Black)
	par_stats_place = par_stats_text.get_rect(topleft=(928, 480))

	victory_text_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 52)
	victory_text_text = victory_text_font.render('выйграно боев - {}'.format(victory), 1, DarkRed)
	victory_text_place = victory_text_text.get_rect(center=(450, 150))

	victory_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 52)
	victory_money_text = victory_money_font.render('заработано - {}'.format(money), 1, Green)
	victory_money_place = victory_money_text.get_rect(center=(450, 220))

	victory_info_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 30)
	victory_info_text = victory_info_font.render('log боя во втором окне', 1, Yellow)
	victory_info_place = victory_info_text.get_rect(center=(440, 760))

	sc.blit(victory_fon, victory_rect)
	sc.blit(ava, ava_rect)
	sc.blit(dif_im, dif_im_rect)
	sc.blit(dif_text, dif_text_place)
	sc.blit(victory_text_text, victory_text_place)
	sc.blit(victory_money_text, victory_money_place)
	sc.blit(victory_info_text, victory_info_place)

	pygame.display.update()

	if enemy['Champ'] == 1 and win:

		sc.fill(Black)
		pygame.display.update()
		l = 0
		pygame.mixer.music.stop()
		sound4.play()
		while l < 850:
			for i in pygame.event.get():
				if i.type == pygame.QUIT:
					exit()
			l += 1
			clock.tick(FPS)
			if l == 100:
				sound5.play()
				victory_fon = random_fon_victory[1]
				victory_rect = victory_fon.get_rect(topleft=(0, 0))

				sc.blit(victory_fon, victory_rect)

				pygame.display.update()

			if l == 180:
				sound6.play()
				victory_win = pygame.image.load('images/win_text.jpg')
				victory_win.set_colorkey(Black)
				victory_win_rect = victory_win.get_rect(center=(600, 771))

				victory_money_font = pygame.font.SysFont('Franklin Gothic Medium Cond', 42)
				victory_money_text = victory_money_font.render('заработано - {}'.format(money), 1, Green)
				victory_money_place = victory_money_text.get_rect(center=(595, 60))

				sc.blit(victory_win, victory_win_rect)
				sc.blit(victory_money_text, victory_money_place)

				pygame.display.update()
		return

	while True:

		if pygame.mixer.music.get_busy():
			pass
		else:
			pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
			pygame.mixer.music.play()

		info_im = pygame.image.load('images/info.png')
		info_im_rect = info_im.get_rect(topleft=(900, 280))

		exit_button_font = pygame.font.SysFont('Comic Sans MS', 76)
		exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
		exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		if Exit:
			exit_button_font = pygame.font.SysFont('Comic Sans MS', 80)
			exit_button_text = exit_button_font.render('выйти', 1, color_welcome)
			exit_button_place = exit_button_text.get_rect(center=(1050, 730))

		if pygame.mouse.get_focused:
			mouse = pygame.mouse.get_pos()
			rect_m = pygame.Rect((mouse[0] - 1, mouse[1] - 1), (2, 2))
			surf_m = pygame.Surface((2, 2))
			surf_m.set_alpha(0)
			sc.blit(surf_m, rect_m)

		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()

			if i.type == pygame.KEYUP:
				if i.key == pygame.K_RIGHT:
					pygame.mixer.music.stop()
					pygame.mixer.music.load(music[r.randint(0, len(music) - 1)])
					pygame.mixer.music.play()
				if i.key == pygame.K_UP:
					pygame.mixer.music.unpause()
					volume += 0.2
					if volume > 1:
						volume = 1
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_DOWN:
					volume -= 0.2
					if volume < 0:
						volume = 0
					pygame.mixer.music.set_volume(volume)
				if i.key == pygame.K_LEFT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.pause()

			if exit_button_place.contains(rect_m):
				Exit = True
			else:
				Exit = False

			if i.type == pygame.MOUSEBUTTONUP and exit_button_place.contains(rect_m):
				sound2.play()
				return

		sc.blit(info_im, info_im_rect)
		sc.blit(par_name_text, par_text_place)
		sc.blit(par_exp_text, par_exp_place)
		sc.blit(par_dmg_text, par_dmg_place)
		sc.blit(par_hp_text, par_hp_place)
		sc.blit(par_money_text, par_money_place)
		sc.blit(par_stats_text, par_stats_place)

		sc.blit(exit_button_text, exit_button_place)

		pygame.display.update(info_im_rect)

		clock.tick(FPS)


if __name__ == "__main__":
	parametrs = main()
	while True:
		choise(parametrs)