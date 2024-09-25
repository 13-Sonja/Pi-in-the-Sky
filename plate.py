from settings import *
from pygame.key import ScancodeWrapper
from pie import Pie


class Plate:
    def __init__(self, xpos: float, ypos: float):
        self.xpos: float = xpos
        self.ypos: float = ypos
        self.width: int = 100
        self.height: int = 10
        self.colour: tuple[int, int, int] = SILVER
        self.velocity: int = 250

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.rect(
            win,
            self.colour,
            (
                self.xpos - (self.width // 2),
                self.ypos - self.height,
                self.width,
                self.height,
            ),
        )

    def move(self, keys: ScancodeWrapper, dt: float) -> None:
        if keys[pygame.K_LEFT] and self.xpos - self.width // 2 >= 0:
            self.xpos -= self.velocity * dt
        if keys[pygame.K_RIGHT] and self.xpos + self.width // 2 <= SCREEN_WIDTH:
            self.xpos += self.velocity * dt

    def catch_pie(self, pie: Pie) -> bool:
        return (
            pie.ypos >= self.ypos
            and self.xpos - self.width // 2 <= pie.xpos <= self.xpos + self.width // 2
        )
