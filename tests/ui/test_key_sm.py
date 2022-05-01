import unittest
from golfswing.ui import key_sm

class TestTracker(unittest.TestCase):
    def test_main_loop_simple(self):
        sm = key_sm.SetupState()

        sm = sm.update(ord('h'))
        self.assertEqual(sm.name, "TargetHintState")

        sm = sm.update(ord('c'))
        self.assertEqual(sm.name, "ClubHintState")

        sm = sm.update(ord('p'))
        self.assertEqual(sm.name, "PlaneHintState")

        sm = sm.update(ord('s'))
        self.assertEqual(sm.name, "SaveState")

        sm = sm.update(ord('q'))
        self.assertEqual(sm.name, "QuitState")

    def test_club_hint(self):
        sm = key_sm.SetupState()

        # Negative test, ignore the key 'c'
        tmp = sm.update(ord('c'))
        self.assertIsNone(tmp)

        # First move to hint stage.
        next_state = sm.update(ord('h'))
        sm = next_state
        self.assertEqual(sm.name, "TargetHintState")
        sm = sm.update(ord('c'))
        self.assertEqual(sm.name, "ClubHintState")
        sm = sm.update(ord('q'))
        self.assertEqual(sm.name, "QuitState")