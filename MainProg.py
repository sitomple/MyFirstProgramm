import pygame

pygame.init()
window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Zuma")

x = [100 , 250]

wight = 40
height = 40
speed = 5
radius = 30
k = 0

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if (x[0] > event.pos[0]):
                k = (abs(x[1] - event.pos[1]) / abs(x[0] - event.pos[0])) #abs(x[1] - event.pos[1]) / abs(x[0] - event.pos[0]))      abs(x[1] - event.pos[1]) / abs(x[0] - event.pos[0]))
                while x[0] > event.pos[0]:
                    x[0] -= 1
                    x[1] = k * x[0]
                    window.fill((0, 0, 0))
                    pygame.draw.circle(window, (0, 0, 255), (x[0], x[1]), radius)
                    pygame.display.update()

            if (x[0] < event.pos[0]):
                k = (abs(x[1] - event.pos[1]) / abs(x[0] - event.pos[0]))
                while x[0] < event.pos[0]:
                    x[0] += 1
                    x[1] = k * x[0]
                    window.fill((0, 0, 0))
                    pygame.draw.circle(window, (0, 0, 255), (x[0], x[1]), radius)
                    pygame.display.update()


    window.fill((0,0,0))
    pygame.draw.circle(window,(0,0,255),(x),radius)
    pygame.display.update()

pygame.quit()