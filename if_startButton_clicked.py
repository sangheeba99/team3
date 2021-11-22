import pygame
import pygame.image

pygame.init() #기본설정
screenSize = (1000, 700)
startScreen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('Veginner')
clock = pygame.time.Clock()

# 시작 화면 코드
def display_start_screen():
    startButton = pygame.image.load("starticon.png")
    startButton = pygame.transform.scale(startButton, (350, 350))
    startScreen.blit(startButton, (320,200))

startButtonPos = pygame.Rect(0,0,350,350)
startButtonPos.center = (320,200)

#pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if startButtonPos.collidepoint(pos):
        start = True

def display_select_screen(): # 고르기 화면 함수
    print("SELECT!!!")


runningCode = True  #게임 실행중
start = False #게임 시작 여부 판단
click_pose = None

while runningCode:  # 무한루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫히는 이벤트
            runningCode = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pose = pygame.mouse.get_pos()
            print(click_pose)

    if start:
        display_select_screen()
    else:
        display_start_screen()

    if click_pose: # 어딘가 클릭함
        check_buttons(click_pose)


    startScreen.fill((20, 103, 53))   #배경 색

    display_start_screen()  #시작 화면

    pygame.display.update() #화면 업데이트

pygame.quit()  # 종료