import pygame
from pygame.locals import *
import random

size = width, height = (900,700)
road_w = int(width/1.6)
roadmark_w = int(width/80)
rigth_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ruben's Car Game")
screen.fill((60,220,0))



pygame.display.update()




#load images
car = pygame.image.load("car-yellow.png")
car= pygame.transform.scale(car, (90, 90))
car_loc = car.get_rect()
car_loc.center = rigth_lane, height*0.8

car2 = pygame.image.load("car-down-red.png")
car2= pygame.transform.scale(car2, (120, 120))
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0

while running:
    counter += 1
    if counter == 4000:
        speed += 0.15
        counter = 0
        print("Level up", speed)


    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = rigth_lane, -200
        else:
            car2_loc.center = left_lane, -200

     #end game
    if car_loc[0] == car2_loc[0] and car_loc[1] > car2_loc[1] -90:
        print("GAME OVER!!")
        break




    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a,K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d,K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

    pygame.draw.rect(
        screen,
        (50,50,50),
        (width/2-road_w/2, 0, road_w, height))

    pygame.draw.rect(
        screen,
        (255,240,60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()




pygame.quit()