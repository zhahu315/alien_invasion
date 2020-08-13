import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_settings, screen, ship):
		# 调用super使Bullet来继承Sprite
		super().__init__()
		self.screen = screen

