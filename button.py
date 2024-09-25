import pygame
from settings import *


class Button:
    def __init__(
        self,
        display: pygame.Surface,
        x_pos: float,
        y_pos: float,
        width: float,
        height: float,
        state: State | Difficulty,
    ):
        self.display = display
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.state = state
        self.hover_active: bool = False
        self.rect = pygame.FRect(self.x_pos, self.y_pos, self.width, self.height)

    def draw(self) -> None:
        pygame.draw.rect(self.display, BLACK, self.rect, 4, 4)
        text: pygame.Surface = text_font.render(self.state.name, True, BLACK)
        self.display.blit(
            text,
            (
                self.rect.centerx - text.get_width() / 2,
                self.rect.centery - text.get_height() / 2 + 4,
            ),
        )

    def mouse_hover(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def button_click(self) -> State | Difficulty | None:
        if self.mouse_hover():
            return self.state
        return None

    def draw_hover(self) -> None:
        if self.mouse_hover():
            self.hover_active = True
            pygame.draw.rect(self.display, WHITE, self.rect, 4, 4)
        else:
            self.hover_active = False
            pygame.draw.rect(self.display, BLACK, self.rect, 4, 4)

    def update(self) -> None:
        self.draw_hover()
