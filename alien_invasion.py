import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
	# 初始化游戏创建一个屏幕
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	# 开始主循环
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullet(bullets)

		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
