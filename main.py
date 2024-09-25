import sys
import time
from typing import Any
from settings import *
from menu import StartMenu, DifficultyMenu
from level import Level
from game_state import GameStateManager


with open("digits_of_pi.txt") as f:
    digits_of_pi: str = "".join([line.strip() for line in f])


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Pi in the Sky")
        self.running: bool = True
        self.win: pygame.Surface = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.clock: pygame.Clock = pygame.time.Clock()

        self.difficulty: Difficulty = Difficulty.EASY

        self.start_menu: StartMenu = StartMenu(self.win)
        self.difficulty_menu: DifficultyMenu = DifficultyMenu(self.win)
        self.level: Level = Level(self.win, digits_of_pi, self.difficulty)
        self.start_menu.draw()
        self.states: dict[State, Any] = {
            State.START: self.start_menu,
            State.LEVEL: self.level,
            State.DIFFICULTY: self.difficulty_menu,
        }
        self.game_state_manager: GameStateManager = GameStateManager(State.START)

    def run(self) -> None:
        prev_time: float = time.time()
        while self.running:
            dt: float = time.time() - prev_time
            prev_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_state_manager.get_state() == State.START:
                        if self.start_menu.start_button.mouse_hover():
                            self.game_state_manager.set_state(State.LEVEL)
                        if self.start_menu.difficulty_button.mouse_hover():
                            self.difficulty_menu.draw()
                            self.game_state_manager.set_state(State.DIFFICULTY)
                        if self.start_menu.end_button.mouse_hover():
                            self.running = False
                    elif self.game_state_manager.get_state() == State.DIFFICULTY:
                        for button in self.difficulty_menu.buttons:
                            if button.mouse_hover():
                                self.difficulty = button.button_click()
                                self.level.difficulty = self.difficulty
                                self.game_state_manager.set_state(State.LEVEL)
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key == pygame.K_ESCAPE
                        and self.game_state_manager.get_state() == State.DIFFICULTY
                    ):
                        self.game_state_manager.set_state(State.START)
                        self.start_menu.draw()

            self.states[self.game_state_manager.get_state()].update(dt)
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
