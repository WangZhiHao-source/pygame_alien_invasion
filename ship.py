import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		"""初始化屏幕并设置其初始值"""
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞传图像并获取其外接矩形
		self.image = pygame.image.load('images//ship.bmp')
		#get_rect()使图片矩形化，获取图像区域用于定位，（返回rect对象，获得对象位置和大小）
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		#在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)

	def update(self):
		"""根据移动标志调整飞船的位置"""
		#更新飞船的center值而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center
	def blitme(self):
		"""在指定位置绘制飞船"""
		# blit方法是将一个图像表面（surface）复制到另一个表面上，用于图形的绘制和显示
		self.screen.blit(self.image,self.rect)