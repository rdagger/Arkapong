"""Power-ups."""
from pygame import image, Rect, sprite, Surface
from pygame.locals import SRCALPHA
from random import choices

POWERUPS_SPRITE = "images/spritesheet_powerups_44x24.png"
SPRITE_COUNT = 16
SPRITE_CELLS = 8
WIDTH = 44
HEIGHT = 24
SPEED = 3

POWERUPS = ["L", "E", "C", "S", "R", "M", "D", "B", "P", "W", "V", "T", "I",
            "N", "G", "F"]
PUP_ODDS = [0.0, 0.4, 0.99, 0.4, 0.2, 0.0, 0.4, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.4]
NONE_ODDS = 0.8  # Odds of no power-up per brick hit


class PowerUp(sprite.Sprite):
    def __init__(self, letter, coords, player_id, spritesheet):
        """Power-up sprite constuctor.

        Args:
            letter(string): Letter representing type of power-up.
            coors((int, int)): X, Y coordinates of power-up.
            player_id(int): Player ID who released power-up.
            spritesheet(pygame.image): Spritesheet of power-ups.
        """
        super().__init__()
        self.letter = letter
        self.player_id = player_id
        if self.player_id:  # Set direction and index based on player
            self.direction = (0, -SPEED)
            self.sprite_index = SPRITE_CELLS - 1
        else:
            self.direction = (0, SPEED)
            self.sprite_index = 0

        # Crop sprite sheet to power-up
        index = POWERUPS.index(letter)
        row_width = spritesheet.get_width()
        self.spritesheet = Surface((row_width, HEIGHT), SRCALPHA)
        self.spritesheet.blit(spritesheet, (0, 0),
                              (0, index * HEIGHT, row_width, HEIGHT))
        # Set initial sprite
        self.image = Surface((WIDTH, HEIGHT), SRCALPHA)
        self.image.blit(self.spritesheet, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = coords

        self.animation_timer = 0
        self.animation_delay = 100  # Delay between frames (100 milliseconds)

    def update(self, clock):
        """Update position and index of the power-up.

        Args:
            clock(pygame.time.Clock): Game clock
        """
        self.rect.move_ip(self.direction)  # Move the power-up

        # Calculate the source rectangle for the current sprite
        source_rect = Rect(self.sprite_index * WIDTH, 0, WIDTH, HEIGHT)
        self.image.blit(self.spritesheet, (0, 0), source_rect)

        # Increment the animation timer
        self.animation_timer += clock.get_time()

        # Check if it's time to update the sprite
        if self.animation_timer >= self.animation_delay:
            increment = -1 if self.player_id else 1
            self.sprite_index = (self.sprite_index + increment) % SPRITE_CELLS
            self.animation_timer = 0


class PowerUps:
    """Power-ups."""

    def __init__(self, goal_top, goal_bottom):
        """Initialize power-ups.

        Args:
            goal_top(int): Top boundary of player 2 goal.
            goal_bottom(int): Bottom boundary of player 1 goal.
        """
        self.goal_top = goal_top
        self.goal_bottom = goal_bottom
        self.spritesheet = image.load(POWERUPS_SPRITE)
        self.sprite_index = 0
        self.sprite_width = self.spritesheet.get_width() // SPRITE_CELLS
        self.sprite_height = self.spritesheet.get_height() // SPRITE_COUNT
        # Calculate the adjusted probabilities
        sum_odds = sum(PUP_ODDS)
        self.adjusted_odds = [(1 - NONE_ODDS) * p / sum_odds for p in PUP_ODDS]
        self.adjusted_odds.append(NONE_ODDS)
        self.powerups = sprite.Group()

    def check_collision(self, paddle_rects):
        """Check for power-up collision with paddles.

        Args:
            paddle_rects([pygame.Rect]): Rectangles encompassing paddles.
        """
        for powerup in self.powerups:
            result = powerup.letter
            if powerup.rect.colliderect(paddle_rects[0]):
                # Player 1 collected power-up.
                self.powerups.remove(powerup)
                return result, 0
            if powerup.rect.colliderect(paddle_rects[1]):
                # Player 2 collected power-up.
                self.powerups.remove(powerup)
                return result, 1
        return None, None

    def clear(self):
        """Clear all power-ups."""
        self.powerups.empty()

    def draw(self, screen):
        """Draw power-ups.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        self.powerups.draw(screen)

    def roll_dice(self, player_id, brick_rect):
        """Decide randomly if a power-up should appear.

        Args:
            player_id(int): Player ID who hit brick.
            brick_rect(pygame.Rect): Rect encompassing brick.
        """
        if len([pu for pu in self.powerups if pu.player_id == player_id]) >= 2:
            # Only allow 2 power-ups per player at a time
            return

        result = choices(POWERUPS + [None], self.adjusted_odds, k=1)[0]
        if result:
            self.powerups.add(PowerUp(result, brick_rect.center, player_id,
                                      self.spritesheet))

    def update(self, clock):
        """Update all power-ups.

        Args:
            clock(pygame.time.Clock): Game clock
        """
        for powerup in self.powerups:
            powerup.update(clock)
            # Check if power-up is out-of-bounds.
            if powerup.player_id:
                if powerup.rect.top <= self.goal_top:
                    self.powerups.remove(powerup)
            else:
                if powerup.rect.bottom >= self.goal_bottom:
                    self.powerups.remove(powerup)
