import pygame
import random
from pygame.key import ScancodeWrapper

from plate import Plate
from pie import Pie
from settings import *


class Level:
    def __init__(
        self, display: pygame.Surface, digits_of_pi: str, difficulty: Difficulty
    ):
        self.display = display
        self.digits_of_pi = digits_of_pi
        self.difficulty = difficulty

        self.plate: Plate = Plate(xpos=SCREEN_WIDTH // 2, ypos=SCREEN_HEIGHT)
        self.pies: list[Pie] = []
        self.pi_counter: str = "3."
        self.pi_index: int = len(self.pi_counter) - 2
        self.lives: int = 3

    def draw(self, pies: list[Pie], plate: Plate, pi_counter: str) -> None:
        self.display.fill(BLACK)
        for pie in pies:
            pie.draw(self.display)
        plate.draw(self.display)
        border: pygame.Rect = pygame.draw.rect(
            self.display, SILVER, (0, 0, SCREEN_WIDTH, 60)
        )
        pi_display: pygame.Surface = text_font.render(pi_counter, True, BLACK)
        self.display.blit(pi_display, border)
        target_digits: pygame.Surface = text_font.render(
            str(self.digits_of_pi[len(pi_counter) - 2 : len(pi_counter) + 2]), True, RED
        )
        if self.difficulty == Difficulty.MEDIUM or self.difficulty == Difficulty.HARD:
            lives_display = text_font.render(f"Lives: {self.lives}", True, BLACK)
            self.display.blit(lives_display, (0, 26))
        self.display.blit(target_digits, (SCREEN_WIDTH / 2, 60))

    def update(self, dt: float) -> None:
        if random.randint(0, FPS) <= 3:
            self.pies.append(Pie(self.display, self.difficulty))
        for pie in self.pies:
            pie.update(dt)

            if pie.ypos - pie.radius * 2 > SCREEN_HEIGHT:
                self.pies.remove(pie)
            if self.plate.catch_pie(pie):
                if str(pie.digit) == self.digits_of_pi[len(self.pi_counter) - 2]:
                    self.pi_counter += str(pie.digit)
                elif (
                    str(pie.digit) != self.digits_of_pi[len(self.pi_counter) - 2]
                    and self.difficulty == Difficulty.MEDIUM
                    or self.difficulty == Difficulty.HARD
                ):
                    self.lives -= 1
                self.pies.remove(pie)

        if self.lives > 0:
            self.draw(self.pies, self.plate, self.pi_counter)
            keys: ScancodeWrapper = pygame.key.get_pressed()
            self.plate.move(keys, dt)
        elif self.lives <= 0:
            self.display.fill(BLACK)
            game_over_text: pygame.Surface = text_font.render("GAME OVER!", True, RED)
            self.display.blit(
                game_over_text,
                (SCREEN_WIDTH / 2 - game_over_text.get_width() / 2, SCREEN_HEIGHT / 2),
            )
