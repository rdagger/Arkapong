"""Player."""
from math import copysign
from pygame import image, Rect

VAUS = {
    0: {
        'regular': 'images/Vaus_red_regular.png',
        'long': 'images/Vaus_red_long.png',
        'narrow': 'images/Vaus_red_narrow.png'
    },
    1: {
        'regular': 'images/Vaus_blue_regular.png',
        'long': 'images/Vaus_blue_long.png',
        'narrow': 'images/Vaus_blue_narrow.png'
    }
}

WIDTHS = {
    'regular': 88,
    'long': 132,
    'narrow': 44
}
HEIGHT = 22

X_ADJUST = {44: 18, 88: 40, 132: 62}

EXPLODE = {
    0: {
        'regular': 'images/Explode_red_regular.png',
        'long': 'images/Explode_red_long.png',
        'narrow': 'images/Explode_red_narrow.png'
    },
    1: {
        'regular': 'images/Explode_blue_regular.png',
        'long': 'images/Explode_blue_long.png',
        'narrow': 'images/Explode_blue_narrow.png'
    }
}
EXPLODE_HEIGHT = 51


class Player:
    """Player."""

    def __init__(self, id, screen_width, goal_top, goal_bottom,
                 wall_left, wall_right, computer_difficulty, human=True):
        """Initialize player.

        Args:
            id(int): Player ID
            screen_width(int): Width of screen
            goal_top(int): Y coordinate of top goal
            goal_bottom(int): Y coordinate of bottom goal
            wall_left(int): X coordinate of left wall
            wall_right(int): X coordinate of right wall
            computer_difficulty(int): Speed of computer player
            human(bool): Player type True=Human, False=Computer
        """
        self.id = id
        self.human = human
        self.computer_difficulty = computer_difficulty
        if not human:
            self.yspeed = 0
        self.hits = 0
        self.set_size("regular")  # Paddle size
        self.x = (screen_width - WIDTHS[self.size]) // 2
        self.screen_width = screen_width
        self.wall_left = wall_left
        self.wall_right = wall_right
        if self.id:
            # Player 2
            self.y = goal_top + 20
        else:
            # Player 1
            self.y = goal_bottom - 42

        self.sprites = {}
        self.explode_sprites = {}
        self.load_sprites()  # Load sprite sheets

        self.animation_timer = 0
        self.animation_delay = 200  # Delay between frames (500 milliseconds)
        self.sprite_count = 4
        self.sprite_index = 0
        self.sprite_direction = 1
        self.catch = False  # Determines if player should catch ball
        self.explode = False  # Used to destroy paddle on goal
        self.explode_index = 0

    def paddle_rect(self):
        """Get rect for current paddle."""
        return Rect(self.x, self.y, WIDTHS[self.size], HEIGHT)

    def load_sprites(self):
        """Load all sprites into dict."""
        # Vaus
        for size, image_path in VAUS[self.id].items():
            img = image.load(image_path).convert_alpha()
            sprite_images = []
            for i in range(4):
                sprite_rect = Rect(0, i * HEIGHT, img.get_width(),
                                   HEIGHT)
                sprite_image = img.subsurface(sprite_rect)
                sprite_images.append(sprite_image)
            self.sprites[size] = sprite_images
        # Vaus explosions
        for size, image_path in EXPLODE[self.id].items():
            img = image.load(image_path).convert_alpha()
            explode_sprites = []
            for i in range(4):
                sprite_rect = Rect(0, i * EXPLODE_HEIGHT, img.get_width(),
                                   EXPLODE_HEIGHT)
                sprite_image = img.subsurface(sprite_rect)
                explode_sprites.append(sprite_image)
            self.explode_sprites[size] = explode_sprites

    def draw(self, screen, clock):
        """Draw player paddle.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
            clock(pygame.time.Clock): Game clock
        """
        if self.explode:
            # Drawing exploding vaus
            if self.explode_index < self.sprite_count:
                screen.blit(
                    self.explode_sprites[self.size][self.explode_index],
                    (self.x, self.y))
                # Increment explosion index (timing handled by calling method)
                self.explode_index += 1
            else:
                # Reset explode index
                self.explode_index = 0
        else:
            # Draw Vaus
            screen.blit(self.sprites[self.size][self.sprite_index],
                        (self.x, self.y))
            # Increment the animation timer
            self.animation_timer += clock.get_time()
            # Check if it's time to update the sprite
            if self.animation_timer >= self.animation_delay:
                self.sprite_index += self.sprite_direction
                if self.sprite_index not in range(self.sprite_count):
                    self.sprite_direction *= -1
                    self.sprite_index += self.sprite_direction
                self.animation_timer = 0

    def move(self, x):
        """Move paddle.

        Args:
            x(int): X position of paddle
        """
        if x <= self.wall_left:
            self.x = self.wall_left + 1
        elif x + WIDTHS[self.size] >= self.wall_right:
            self.x = self.wall_right - WIDTHS[self.size] - 1
        else:
            self.x = x

    def move_toward(self, x):
        """Move paddle towards an X position.

        Args:
            x(int): X position to move toward.
        Notes:
            self.sprite_index used for stochasticity
        """
        if not self.hits % 8:  # Minimize offset every 8 hits to avoid deadlock
            offset = self.sprite_index * copysign(1, x - self.x)
        elif x <= (self.screen_width // 2):  # Ball on left side of screen
            offset = min(X_ADJUST[self.length] + self.sprite_index,
                         self.screen_width // 2 - x)
        elif x > (self.screen_width // 2):  # Ball on right side of screen
            offset = max(-X_ADJUST[self.length] - self.sprite_index,
                         self.screen_width // 2 - x)

        x -= (WIDTHS[self.size] // 2) + offset
        x = self.x + min(abs(x - self.x),
                         self.computer_difficulty) * copysign(1, x - self.x)
        if x <= self.wall_left + 30:  # Limit computer player closeness to wall
            self.x = self.wall_left + 31 + self.sprite_index
        elif x + WIDTHS[self.size] + 30 >= self.wall_right:
            self.x = self.wall_right - WIDTHS[self.size] - (
                30 + self.sprite_index)
        else:
            self.x = x

    def set_size(self, size):
        """Move paddle.

        Args:
            size(string): Paddle size (regular, long or narrow)
        """
        self.size = size
        self.length = WIDTHS[size]
