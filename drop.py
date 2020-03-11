import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
		"""表示雨滴的类"""
		def __init__(self, my_settings, screen):
			"""初始化雨滴"""
			super().__init__()
			self.screen = screen
			self.my_settings = my_settings
			#加载外星人图像
			self.image = pygame.image.load('images/drop.png')
			self.rect = self.image.get_rect()
			#雨滴的初始位置
			self.rect.x = 0
			self.rect.y = 0
			#存储雨滴的准确位置
			self.y = float(self.rect.y)									#这个self.y 可存小数
			
		def blitme(self):
			"""在指定位置上画雨滴"""					#画单个帮助理解，画很多的时候用.draw(screen)
			self.screen.blit(self.image, self.rect)
			
		def shower(self):
			"""下雨啦"""
			self.y += self.my_settings.drops_speed_factor  
			self.rect.y = self.y
