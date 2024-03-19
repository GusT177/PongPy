import pygame

WIDTH = 1280
HEIGHT = 720
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
running = True


def Player():
    PlayerPosX = 10
    PlayerPosY = 10
    spd = 5
    PlayerWidth, PlayerHeight = 50, 260
    blue = (0,0,255)
    PlayerRect = (PlayerPosX, PlayerPosY, PlayerWidth, PlayerHeight)
    pygame.draw.rect(window,blue,PlayerRect)

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        PlayerPosY += spd




def Enemy():
    EnemyPosX = 100
    EnemyPosY = 100
    EnemyWidth, EnemyHeight = 50, 260
    red = (255,0,0)
    EnemyRect = (EnemyPosX, EnemyPosY, EnemyWidth, EnemyHeight)
    pygame.draw.rect(window,red,EnemyRect)




def Ball():
    BallPos = 0



while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = false
            pygame.quit()

    window.fill("black")
    Player()
    Enemy()
    clock.tick(60)
    pygame.display.flip()



