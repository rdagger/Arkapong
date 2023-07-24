"""Game sound generation."""
from pygame import mixer
from os import path

SOUND_EFFECTS = ['brick1', 'brick2', 'brick3', 'catch', 'enemy', 'explode',
                 'extralife', 'fieldoff', 'fieldon', 'levelup', 'paddle',
                 'resize']


class GameSounds():
    """Class to generate, load and play sounds."""
    def __init__(self, volume=1.0):
        """Game sounds constructor.

        Args:
            volume(float): Volume 0 - 1.0 (Default 1.0)
        """
        mixer.init()

        # Define the number of channels (modern PC's should support up to 32)
        num_channels = len(SOUND_EFFECTS)
        # Use multiple channels allows for simultaneous sound effects
        mixer.set_num_channels(num_channels)

        self.volume = volume
        self.sound_effects = {}
        self.load_sound_effects()

    def load_sound_effects(self):
        """Load all game sound effects"""
        for effect in SOUND_EFFECTS:
            self.sound_effects[effect] = mixer.Sound(path.join("sounds",
                                                     effect + ".mp3"))

    def play(self, effects, pause=False):
        """Play sound effect(s).

        Args:
            effects(string or [string]): Effect(s) to play.
            pause(bool): True to pause until sound is played
        """
        if isinstance(effects, str):  # Handle single effect
            effects = [effects]
        # Play effect(s)
        for effect in effects:
            channel_number = SOUND_EFFECTS.index(effect)  # Use unique channels
            channel = mixer.Channel(channel_number)
            channel.play(self.sound_effects[effect])
            if pause:
                while channel.get_busy():
                    continue
