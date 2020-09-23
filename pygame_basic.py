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

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지의 (가로,세로) 크기를 얻음
character_width = character_size[0] # 캐릭터의 가로 크기(140)
character_height = character_size[1] # 캐릭터의 세로 크기(190)
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

# 이벤트 루프
running = True # 게임이 진행중인가를 확인

while running:
	for event in pygame.event.get(): # 어떤 이벤트가 발생하였는지 체크
		if event.type == pygame.QUIT: # 오른쪽 상단 x버튼을 누르면 종료
			running = False

	screen.blit(background, (0, 0)) # 배경그리기 .blit(배경사진, (가로, 세로))

	screen.blit(character, (character_x_pos, character_y_pos))

	pygame.display.update() # 게임 화면을 계속해서 다시 그리기!

# pygame 종료
pygame.quit()