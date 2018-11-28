import pygame
import pyganim
import Meteors_setting as setting
import Meteors_game_objects as objects

# init
pygame.init()

# var
clock = pygame.time.Clock()
score = 0

# wind
pygame.display.set_caption('GeekGame')
sc = pygame.display.set_mode(setting.SIZE)

explosition_animation = pyganim.PygAnimation([
	('images/bam_{}.png'.format(i), 50) for i in range(1, 8)
], loop=False)

# Game objects
player = objects.Player()
background = objects.Background()

# Groups
all_objects = pygame.sprite.Group()
plasmoid_group = pygame.sprite.Group()
meteo_group = pygame.sprite.Group()
mini_meteo_group = pygame.sprite.Group()

explosions = []

# add in group
all_objects.add(background)
all_objects.add(player)
plasmoid_group.add(objects.Plasmoid(player.rect.midtop))

text_Algerian_font = pygame.font.Font('fonts/Algerian.ttf', 30)

while True:
	# First step
	clock.tick(setting.FPS)
	sc.fill(setting.WHITE)

	# Create new objects
	objects.Meteorites.create_meteo(clock, meteo_group)
	objects.Plasmoid.create_plasmoid(clock, plasmoid_group, player.rect.midtop)

	# Update places
	all_objects.update()
	plasmoid_group.update(player.rect.midtop)
	meteo_group.update()
	mini_meteo_group.update()

	# Draw in surface
	all_objects.draw(sc)
	plasmoid_group.draw(sc)
	meteo_group.draw(sc)
	mini_meteo_group.draw(sc)

	if pygame.sprite.spritecollide(player, mini_meteo_group, True):
		player.health -= 1

	if pygame.sprite.spritecollide(player, meteo_group, True):
		player.health = 0

	text_Algerian_text = text_Algerian_font.render('score: {}|{}'.format(score, player.health), 1, (255, 0, 0))
	text_Algerian_place = text_Algerian_text.get_rect(bottomright=(setting.WIDTH, setting.HEIGHT))
	sc.blit(text_Algerian_text, text_Algerian_place)

	meteo_and_plasmoid_collided = pygame.sprite.groupcollide(plasmoid_group, meteo_group, True, True)
	mini_meteo_and_plasmoid_collided = pygame.sprite.groupcollide(plasmoid_group, mini_meteo_group, True, True)

	for collided in meteo_and_plasmoid_collided:
		explosion = explosition_animation.getCopy()
		explosion.play()
		explosions.append((explosion, (collided.rect.center)))

	for explosion, position in explosions:
		if explosion.isFinished():
			explosions.remove((explosion, position))
		else:
			x, y = position
			explosion.blit(sc, (x-40, y-40))

	if meteo_and_plasmoid_collided:
		score += 1
		for collided in meteo_and_plasmoid_collided:
			position_mini = collided.rect.center
		for number in range(1, 4):
			objects.MiniMeteorites.create_meteo(mini_meteo_group, position_mini)

	if mini_meteo_and_plasmoid_collided:
		score += 1

	pygame.display.update()

	# End
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	if pygame.sprite.spritecollide(player, meteo_group, True) or player.health == 0:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()