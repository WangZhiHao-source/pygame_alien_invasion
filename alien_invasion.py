import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
	# 初始化游戏并常见一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("alien invasion")

	#创建一个飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建外星人编组
	aliens = Group()
	gf.create_feet(ai_settings,screen,aliens)
	# 开始游戏的主循环
	while True:
		# 监控键盘和鼠标实践
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		#更新屏幕
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()