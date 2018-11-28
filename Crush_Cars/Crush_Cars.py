from random import randint
import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60
freq = 280
Score = 0
speedy = 1

W = 800
H = 400
WHITE = (255, 255, 255)

def main():

	global speedy, freq, Score

	pygame.time.set_timer(pygame.USEREVENT, freq)

	CARS = ('image/car1.png', 'image/car2.png', 'image/car3.png')
	CARS_SURF = []  # для хранения готовых машин-поверхностей

	# надо установить видео режим до вызова image.load()
	sc = pygame.display.set_mode((W, H))
	pygame.display.set_caption('Superhighway')
	sc.fill(WHITE)

	pygame.mouse.set_pos(W//2, H//2)

	font_start = pygame.font.SysFont('Arial Black', 50)
	text_start = font_start.render('Press a button mouse', 1, (255, 0, 0))
	place_start = text_start.get_rect(center=(400, 200))
	sc.blit(text_start, place_start)

	pygame.display.update()
	flag = True
	while flag:
		clock.tick(5)
		for i in pygame.event.get():
			if i.type == pygame.MOUSEBUTTONUP:
				flag = False
			if i.type == pygame.QUIT:
				exit()

	sc.fill(WHITE)
	pygame.mouse.set_visible(False)

	pygame.mixer.music.load('music/8bit_muzyka.mp3')
	pygame.mixer.music.play(-1)

	my_car_surf = pygame.image.load('image/car.png').convert_alpha()
	my_car_surf.set_colorkey(WHITE)
	width = my_car_surf.get_width()//1.25
	height = my_car_surf.get_height()//1.25
	my_car_surf = pygame.transform.scale(my_car_surf, (int(width), int(height)))

	for i in range(len(CARS)):
		CARS_SURF.append(pygame.image.load(CARS[i]).convert_alpha())

	class Car(pygame.sprite.Sprite):
		def __init__(self, x, surf, group):
			pygame.sprite.Sprite.__init__(self)
			self.image = surf
			self.rect = self.image.get_rect(center=(x, 0))
			self.add(group)  # добавляем в группу
			global speedy
			self.speed = randint(1, speedy)  # у машин будет разная скорость

		def update(self):
			if self.rect.y < H:
				self.rect.y += self.speed
			else:
				# теперь не перебрасываем вверх,
				# а удаляем из всех групп
				self.kill()
				global Score
				Score+=1

	class MyCar(pygame.sprite.Sprite):
		def __init__(self, my_car_surf, group):
			pygame.sprite.Sprite.__init__(self)
			self.image = my_car_surf
			self.rect = self.image.get_rect(center=(0, 0))
			self.add(group)
		def update(self):
			mouse = pygame.mouse.get_pos()
			my_cary.rect.x = mouse[0] - my_car_surf.get_width() // 2
			my_cary.rect.y = mouse[1] - my_car_surf.get_height() // 2

	cars = pygame.sprite.Group()
	my_car = pygame.sprite.Group()

	# добавляем первую машину, которая появляется сразу
	Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
	my_cary = MyCar(my_car_surf, my_car)

	font_Ddif = pygame.font.SysFont('Arial Black', 20)
	text_Ddif = font_Ddif.render('click for increase', 1, (255, 0, 0))
	place_Ddif = text_Ddif.get_rect(center=(700, 360))
	sc.blit(text_Ddif, place_Ddif)

	font_dif = pygame.font.SysFont('Arial Black', 20)
	text_dif = font_dif.render('difficult: {}'.format(speedy), 1, (255, 0, 0))
	place_dif = text_dif.get_rect(center=(725, 380))
	sc.blit(text_dif, place_dif)

	font_Sc = pygame.font.SysFont('Arial Black', 20)
	text_Sc = font_Sc.render('Score: {}'.format(Score), 1, (205, 205, 0))
	place_Sc = text_Sc.get_rect(center=(50, 380))
	sc.blit(text_Sc, place_Sc)

	while 1:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			if pygame.sprite.spritecollideany(my_cary, cars):
				sound = pygame.mixer.Sound('sound/crush_car.wav')
				sound.play()
				font_crush = pygame.font.SysFont('Arial Black', 50)
				text_crush = font_crush.render('Crush', 1, (255, 0, 0))
				place_crush = text_crush.get_rect(center=(400, 200))
				sc.blit(text_crush, place_crush)
				font_again = pygame.font.SysFont('Arial Black', 20)
				text_again = font_again.render('Again?', 1, (255, 127, 0))
				place_again = text_again.get_rect(center=(400, 250))
				sc.blit(text_again, place_again)
				pygame.display.update()
				pygame.mouse.set_visible(True)
				pygame.mixer.music.pause()
				while 2:
					clock.tick(5)
					for i in pygame.event.get():
						if i.type == pygame.QUIT:
							exit()
						if i.type == pygame.MOUSEBUTTONUP:
							speedy = 1
							Score = 0
							freq = 280
							return
			elif i.type == pygame.USEREVENT:
				Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
			if i.type == pygame.MOUSEBUTTONUP:
				speedy += 1
				freq -= 20
				if freq == 60:
					freq = 100
				if speedy == 11:
					speedy = 10
				text_dif = font_dif.render('difficult: {}'.format(speedy), 1, (255, 0, 0))
				pygame.time.set_timer(pygame.USEREVENT, freq)

		sc.fill(WHITE)

		cars.draw(sc)
		my_car.draw(sc)
		text_Sc = font_Sc.render('Score: {}'.format(Score), 1, (205, 205, 0))
		sc.blit(text_dif, place_dif)
		sc.blit(text_Sc, place_Sc)
		sc.blit(text_Ddif, place_Ddif)

		if pygame.mouse.get_focused():
			my_cary.update()
		else:
			my_cary.rect.x = 400
			my_cary.rect.y = 200

		cars.update()
		pygame.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	while 3:
		main()