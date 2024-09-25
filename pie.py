import random
from math import pi
from settings import *


class Pie:
    def __init__(self, display: pygame.Surface, difficulty: Difficulty):
        self.display = display
        self.difficulty = difficulty
        self.radius: int = 25
        self.xpos: int = random.randint(
            0 + self.radius // 2, SCREEN_WIDTH - self.radius // 2
        )
        self.ypos: int | float = random.randint(-100, -30)
        self.colour: tuple[int, int, int] = WHITE
        self.digit: int = random.randint(0, 9)
        self.speed: float = 0.01
        self.two_pi: float = pi * 2

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.circle(win, self.colour, (self.xpos, self.ypos), self.radius)
        if self.difficulty == Difficulty.HARD:
            for i in range(self.digit):
                pygame.draw.arc(
                    win,
                    SILVER,
                    [
                        self.xpos - self.radius,
                        self.ypos - self.radius,
                        self.radius * 2,
                        self.radius * 2,
                    ],
                    i * self.two_pi / 9,
                    (i + 1) * self.two_pi / 9,
                    100,
                )
                pygame.draw.arc(
                    win,
                    WHITE,
                    [
                        self.xpos - self.radius,
                        self.ypos - self.radius,
                        self.radius * 2,
                        self.radius * 2,
                    ],
                    i * self.two_pi / 9,
                    (i + 1) * self.two_pi / 9,
                    1,
                )
        else:
            digit: pygame.Surface = text_font.render(str(self.digit), True, RED)
            win.blit(digit, (self.xpos - self.radius / 3, self.ypos - self.radius / 2))

    def update(self, dt: float) -> None:
        self.ypos += self.speed * dt
        if self.difficulty == Difficulty.EASY:
            self.speed += 50 * dt
        else:
            self.speed += 80 * dt
