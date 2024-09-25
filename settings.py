from enum import Enum, auto
import pygame

pygame.font.init()
text_font: pygame.Font = pygame.font.SysFont("Consolas", 32)
FPS: int = 60
SCREEN_WIDTH: int = 900
SCREEN_HEIGHT: int = 700
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
SILVER: tuple[int, int, int] = (150, 150, 150)
RED: tuple[int, int, int] = (246, 82, 82)


class Difficulty(Enum):
    EASY: int = auto()
    MEDIUM: int = auto()
    HARD: int = auto()


class State(Enum):
    START: int = auto()
    DIFFICULTY: int = auto()
    LEVEL: int = auto()
    QUIT: int = auto()
