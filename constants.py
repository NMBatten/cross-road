from pygame.locals import *
import pygame

pygame.init()


class Constants:

    # Screen and data setup
    SCREEN_HEIGHT = 400
    SCREEN_WIDTH = 500
    FPS = 60

    # Colors
    grass_green = (20, 230, 5)
    river_blue = (5, 10, 230)
    road_gray = (200, 200, 200)
    truck_color = (240, 0, 10)
    log_brown = (185, 100, 100)

    # Object data
    HARDNESS = 1
    CAR_SPEED = 2
    TRUCK_SPEED = 1
    LOG_SPEED = 1

    GENRANGE_START = 45
    GENRANGE_END = 200

    def set_hardness(hardness):
        HARDNESS = hardness
