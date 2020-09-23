import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 800 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 이벤트 루프
running = True # 게임이 진행중인가를 확인

while running:
	for event in pygame.event.get(): # 어떤 이벤트가 발생하였는지 체크
		if event.type == pygame.QUIT: # 오른쪽 상단 x버튼을 누르면 종료
			running = False

	#screen.fill((0, 0, 255)) # 배경그리기 .fill((r,g,b))
	screen.blit(background, (0, 0)) # 배경그리기 .blit(배경사진, (가로, 세로))

	pygame.display.update() # 게임 화면을 계속해서 다시 그리기!

# pygame 종료
pygame.quit()