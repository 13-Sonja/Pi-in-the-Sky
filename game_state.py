from settings import State


class GameStateManager:
    def __init__(self, current_state: State):
        self.current_state = current_state

    def get_state(self) -> State:
        return self.current_state

    def set_state(self, state: State) -> None:
        self.current_state = state
