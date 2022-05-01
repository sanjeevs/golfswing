class State:
    def __init__(self):
        self.name = "Base"

    def exit_action(self):
        assert False, "Derived class must override this"

    def update(self, key_pressed):
        next_state = None
        if key_pressed == ord('q'):
            next_state = QuitState()
        elif key_pressed == ord('h'):
            next_state = TargetHintState()
        elif key_pressed == ord('s'):
            next_state = SaveState()
        elif key_pressed == ord('l'):
            next_state = LiveState()

        return next_state

class SetupState(State):
    def __init__(self):
        self.name = "SetupState"

    def exit_action(self):
        pass


class QuitState(State):
    def __init__(self):
        self.name = "QuitState"

    def exit_action(self):
        pass

class HintState(State):
    def update(self, key_pressed):
        next_state = None
        if key_pressed == ord('t'):
            next_state = TargetHintState()
        elif key_pressed == ord('c'):
            next_state = ClubHintState()
        elif key_pressed == ord('p'):
            next_state = PlaneHintState()
        else :
            next_state = super().update(key_pressed)
            # Just return to prevent double exit action
            return next_state

        if next_state is not None:
            self.exit_action()

        return next_state

    def exit_action(self):
        pass

class TargetHintState(HintState):
    def __init__(self):
        self.name = "TargetHintState"

class ClubHintState(HintState):
    def __init__(self):
        self.name = "ClubHintState"

class PlaneHintState(HintState):
    def __init__(self):
        self.name = "PlaneHintState"

class LiveState(State):
    def __init__(self):
        self.name = "LiveState"

class SaveState(State):
    def __init__(self):
        self.name = "SaveState"

    def exit_action(self):
        pass
