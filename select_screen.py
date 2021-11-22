import pygame
import pygame.image

pygame.init() #기본설정
screenSize = (1000, 700)
Screen = pygame.display.set_mode(screenSize)
Screen.fill((20, 103, 53))  # 배경 색
pygame.display.set_caption('Veginner')

arrow_size = 100
arrow_margin_top = 100
arrow_margin_left =400

# 화살표 만들기
arrow_top = pygame.Rect(400,100,100,100)
arrow_top.center = (400,100)
arrow_bottom = pygame.Rect(400,600,100,100)


def display_start_screen(): # 시작 화면 함수
    startButton = pygame.image.load("starticon.png")
    startButton = pygame.transform.scale(startButton, (350, 350))
    Screen.blit(startButton, (320,200))


def display_select_screen(): # 고르기 화면 함수
    upArrow = pygame.image.load("arrowup.png")
    Screen.blit(upArrow, (320,200))


start = None

# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if startButtonPos.collidepoint(pos):
        start = True


startButtonPos = pygame.Rect(0,0,350,350)
startButtonPos.center = (320,200)

 #게임 시작 여부 판단
runningCode = True  #게임 실행중
click_pos = None

while runningCode:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningCode = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    if start:
        display_select_screen()
    else:
        display_start_screen()

    if click_pos: # 어딘가 클릭함
        check_buttons(click_pos)

    pygame.display.update() #화면 업데이트

pygame.quit()  # 종료