import sys
import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(screen, ai_settings, ship)
			bullets.add(new_bullet)


def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
	"""相应按键和鼠标事件"""

	for event in pygame.event.get():
		# 检测是否为退出请求，是的话退出
		if event.type == pygame.QUIT:
			print()
			print()
			sys.exit()
		# 检测到是向右移动时，向右移动
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,alien,bullets):
	"""更新屏幕上的图片，并切换到新屏幕"""
	# 让每次循环完都重绘屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	alien.blitme()

	# 让最近绘制的屏幕可见
	pygame.display.flip()
def update_bullets(bullets):
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)