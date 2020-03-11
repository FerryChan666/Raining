import pygame
import sys
from drop import Drop

def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
def update_screen(my_settings, screen, drop, drops):
	#每次循环都重绘屏幕
	screen.fill(my_settings.bg_color)
	#画编组里头的很多雨滴
	drops.draw(screen)
	#更新雨滴
	fall_down(my_settings, drops)
	#让最新绘制的屏幕可见
	pygame.display.flip()

def get_number_drops_x(my_settings, drop_width):
	number_drops_x = int(my_settings.screen_width / (2 * drop_width))
	return number_drops_x

def get_number_drops_y(my_settings, drop_height):
	number_drops_y = 3
	return number_drops_y

def create_drop(my_settings, screen, drops, drop_number, drop_rows):
	drop = Drop(my_settings, screen)
	drop.rect.x = 2 * drop.rect.width * drop_number
	drop.y = drop.rect.height * drop_rows
	drop.rect.y = drop.y
	drops.add(drop)

def create_drops(my_settings, screen, drops):
	#创建雨滴,等于先创建一个个实例
	
	drop = Drop(my_settings, screen)
	drop_width = drop.rect.width
	drop_height = drop.rect.height
	number_drops_x = get_number_drops_x(my_settings, drop_width)
	number_drops_y = get_number_drops_y(my_settings, drop_height)
	for drop_rows in range(number_drops_y): 
		for drop_number in range(number_drops_x):
			create_drop(my_settings, screen, drops, drop_number, drop_rows)
		
def fall_down(my_settings, drops):
	for drop in drops.sprites():
		drop.shower()
		
def update_drops(drops, screen):
	for drop in drops.copy():
		x = screen.get_rect()
		if drop.rect.top >= x.bottom:
			drops.remove(drop)
		
def create_one(my_settings, screen, drops):
	#创建一行雨滴
	drop = Drop(my_settings, screen)
	drop_width = drop.rect.width
	number_drops_x = get_number_drops_x(my_settings, drop_width)
	for drop_number in range(number_drops_x):
		create_one_drop(my_settings, screen, drops, drop_number)

def create_one_drop(my_settings, screen, drops, drop_number):
	drop = Drop(my_settings, screen)
	drop.rect.x = 2 * drop.rect.width * drop_number
	drop.rect.y = 0
	drops.add(drop)
