import pygame
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from drop import Drop

def run_game():
	#初始化
	pygame.init()
	#设置的实例
	my_settings = Settings()
	#屏幕设置
	screen = pygame.display.set_mode(
		(my_settings.screen_width, my_settings.screen_height))
	#标题
	pygame.display.set_caption("Raining")
	#创建一个雨滴实例
	drop = Drop(my_settings, screen)
	#创建一个编组，存储雨滴
	drops = Group()
	#创建很多雨滴，并且存入编组
	gf.create_drops(my_settings, screen, drops)
	number_drops = len(drops)
	
	
	while True:
		#检查按键
		gf.check_events()
		#更新雨滴
		gf.update_drops(drops, screen)
		#添加雨滴
		if len(drops) < number_drops:
			gf.create_one(my_settings, screen, drops)
		#更新屏幕
		gf.update_screen(my_settings, screen, drop, drops)
		
run_game()
