
class Emp_Buffer:
    def __init__(self):
        self._state = {}

    def save_state(self, key, state):
        self._state[key] = state

    def get_state(self, key):
        return self._state.get(key)


