import sys

import pygame

from settings import Settings

def run_game():
	# 初始化游戏并常见一个屏幕对象
	pygame.init()
	ai_setting = Settings()
	creen = pygame.display.set_mode((ai_setting.screen_width,
									 ai_setting.screen_height))
	pygame.display.set_caption("alien invasion")

	# 开始游戏的主循环
	while True:

		# 监控键盘和鼠标实践
		for even in pygame.event.get():
			if even.type == pygame.QUIT:
				sys.exit()

		# 让每次循环完都重绘屏幕
		creen.fill(ai_setting.bg_color)

		#让最近绘制的屏幕可见
		pygame.display.flip()
run_game()