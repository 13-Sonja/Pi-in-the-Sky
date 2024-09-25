from abc import ABC, abstractmethod

import pygame
from settings import *
from button import Button


class Menu(ABC):
    def __init__(self, display: pygame.Surface):
        self.display = display
        self.buttons: list[Button] = []
        self.base_rect: pygame.Rect = pygame.Rect(
            (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )

        self.x_pos: float = self.base_rect.width - self.base_rect.width / 4
        self.y_pos: float = self.base_rect.height / 3 - self.base_rect.height / 12
        self.width: float = self.base_rect.width / 2
        self.height: float = self.base_rect.height / 6

    @abstractmethod
    def button_setup(self, *args, **kwargs) -> None:
        pass

    def draw(self, *args, **kwargs) -> None:
        pygame.draw.rect(self.display, SILVER, self.base_rect, 0, 4, 4, 4, 4)
        pygame.draw.rect(self.display, WHITE, self.base_rect, 4, 4, 4, 4, 4)
        for button in self.buttons:
            button.draw()

    def mouse_hover(self) -> None:
        for button in self.buttons:
            button.mouse_hover()
            button.update()
            if button.hover_active:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self, dt) -> None:
        self.mouse_hover()


class StartMenu(Menu):
    def __init__(self, display: pygame.Surface):
        super().__init__(display)
        self.button_setup()

    def button_setup(self) -> None:
        self.start_button: Button = Button(
            self.display,
            self.x_pos,
            self.y_pos + self.base_rect.height / 3,
            self.width,
            self.height,
            State.START,
        )
        self.difficulty_button: Button = Button(
            self.display,
            self.x_pos,
            self.y_pos + (self.base_rect.height / 3) * 2,
            self.width,
            self.height,
            State.DIFFICULTY,
        )
        self.end_button: Button = Button(
            self.display,
            self.x_pos,
            self.y_pos + (self.base_rect.height / 3) * 3,
            self.width,
            self.height,
            State.QUIT,
        )
        self.buttons.extend(
            (self.start_button, self.difficulty_button, self.end_button)
        )


class DifficultyMenu(Menu):
    def __init__(self, display: pygame.Surface):
        super().__init__(display)
        self.button_setup()

    def button_setup(self) -> None:
        self.easy_button: Button = Button(
            self.display,
            self.x_pos,
            self.y_pos + self.base_rect.height / 3,
            self.width,
            self.height,
            Difficulty.EASY,
        )
        self.medium_button: Button = Button(
            self.display,
            self.x_pos,
            self.y_pos + (self.base_rect.height / 3) * 2,
            self.width,
            self.height,
            Difficulty.MEDIUM,
        )
        self.hard_button: Button = Button(
            self.display,
            self.x_pos,
            self.y_pos + (self.base_rect.height / 3) * 3,
            self.width,
            self.height,
            Difficulty.HARD,
        )
        self.buttons.extend((self.easy_button, self.medium_button, self.hard_button))
