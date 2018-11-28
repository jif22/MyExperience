import pygame
import Meteors_setting as setting
from random import randint

class Background(pygame.sprite.Sprite):
	def __init__(self):
		super(Background, self).__init__()

		self.image = pygame.image.load('images/sky_stars.png')
		self.rect = self.image.get_rect()

		self.rect.bottom = setting.HEIGHT

	def update(self):
		self.rect.bottom += 1

		if self.rect.bottom >= setting.HEIGHT * 3:
			self.rect.bottom = setting.HEIGHT


class Player(pygame.sprite.Sprite):
	__x = setting.WIDTH / 2
	__y = setting.HEIGHT - 64
	health = 3

	def __init__(self):
		super(Player, self).__init__()

		self.image = pygame.image.load('images/shuttle.png')
		self.image_width = self.image.get_width() / 2
		self.image_height = self.image.get_height() / 2
		self.rect = self.image.get_rect(center=(self.__x, self.__y))

	def update(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.__x -= setting.SPEED_MOVE
			if self.__x < 0 + self.image_width/2:
				self.__x += setting.SPEED_MOVE
			self.rect = self.image.get_rect(center=(self.__x, self.__y))
		if keys[pygame.K_RIGHT]:
			self.__x += setting.SPEED_MOVE
			if self.__x > setting.WIDTH-self.image_width/2:
				self.__x -= setting.SPEED_MOVE
			self.rect = self.image.get_rect(center=(self.__x, self.__y))
		if keys[pygame.K_UP]:
			self.__y -= setting.SPEED_MOVE
			if self.__y < 0 + self.image_height:
				self.__y += setting.SPEED_MOVE
			self.rect = self.image.get_rect(center=(self.__x, self.__y))
		if keys[pygame.K_DOWN]:
			self.__y += setting.SPEED_MOVE
			if self.__y > setting.HEIGHT-self.image_height/2:
				self.__y -= setting.SPEED_MOVE
			self.rect = self.image.get_rect(center=(self.__x, self.__y))


class Meteorites(pygame.sprite.Sprite):
	cooldown = 1000
	current_cooldown = 0
	speed = 6
	images_meteo = ['images/meteorite_1.png', 'images/meteorite_2.png', 'images/meteorite_3.png']

	def __init__(self):
		super(Meteorites, self).__init__()

		self.image = pygame.image.load(self.images_meteo[randint(0, 2)])
		width = self.image.get_width() // 0.7
		height = self.image.get_height() // 0.7
		self.image = pygame.transform.scale(self.image, (int(width), int(height)))
		self.rect = self.image.get_rect()

		self.rect.midtop = (randint(0, setting.WIDTH), 0-self.image.get_height())

	def update(self):
		self.rect.move_ip((0, self.speed))

	@staticmethod
	def create_meteo(clock, meteo_group):
		if Meteorites.current_cooldown <= 0:
			meteo_group.add(Meteorites())
			Meteorites.current_cooldown = Meteorites.cooldown
		else:
			Meteorites.current_cooldown -= clock.get_time()

		for meteo in list(meteo_group):
			if meteo.rect.top >= setting.HEIGHT:
				Meteorites.remove(meteo)

class MiniMeteorites(pygame.sprite.Sprite):
	speed = 3
	images_mini_meteo = ['images/part_meteo_1.png', 'images/part_meteo_2.png', 'images/part_meteo_3.png']

	def __init__(self, position):
		super(MiniMeteorites, self).__init__()

		self.image = pygame.image.load(self.images_mini_meteo[randint(0, 2)])
		self.rect = self.image.get_rect()
		x, y = position
		self.rect.midtop = (x-0-randint(-80, 80), y-40-randint(-40, 80))

	def update(self):
		self.rect.move_ip((0, self.speed))

	@staticmethod
	def create_meteo(mini_meteo_group, position):
		mini_meteo_group.add(MiniMeteorites(position))

		for meteo in list(mini_meteo_group):
			if meteo.rect.top >= setting.HEIGHT:
				MiniMeteorites.remove(meteo)



class Plasmoid(pygame.sprite.Sprite):
	speed = -10
	cooldown = 100
	current_cooldown = 0

	def __init__(self, position):
		super(Plasmoid, self).__init__()

		self.image = pygame.image.load('images/plasmoid.png')
		self.rect = self.image.get_rect()

		self.rect.midbottom = position

	def update(self, position):
		self.rect.move_ip((0, self.speed))


	@staticmethod
	def create_plasmoid(clock, plasmoid_group, position):
		if Plasmoid.current_cooldown <= 0:
			plasmoid_group.add(Plasmoid(position))
			Plasmoid.current_cooldown = Plasmoid.cooldown
		else:
			Plasmoid.current_cooldown -= clock.get_time()

		for plasm in list(plasmoid_group):
			if plasm.rect.bottom <= 0:
				plasmoid_group.remove(plasm)
