"""Forcefields."""
from pygame import image, Rect, Surface, transform
from pygame.locals import SRCALPHA

DISINTEGRATION_SPRITE = "images/forcefield_disintegration.png"
REPULSION_FIELD = "images/forcefield_repulsion.png"
SPRITE_COUNT = 8


class Forcefields:
    """Forcefields over goals (disintegration or repulsion)."""

    def __init__(self, goal_top, goal_bottom, goal_left, goal_right):
        """Initialize force fields.

        Args:
            goal_top(int): Top boundary of player 2 goal.
            goal_bottom(int): Bottom boundary of player 1 goal.
            goal_left(int): Left boundary of player's goals.
            goal_right(int): Right boundary of player's goals.
        """
        self.spritesheet = image.load(DISINTEGRATION_SPRITE).convert_alpha()
        self.sprite_index = 0
        self.sprite_width = self.spritesheet.get_width()
        self.sprite_height = self.spritesheet.get_height() // SPRITE_COUNT
        self.width = goal_right - goal_left
        self.height = self.sprite_height
        self.x = goal_left
        self.y1 = goal_bottom - 20
        self.y2 = goal_top - 2
        self.animation_timer = 0
        self.animation_delay = 100  # Delay between frames (100 milliseconds)
        self.player1_repulse = False
        self.player2_repulse = False
        repulsion_image = image.load(REPULSION_FIELD)
        repulsion_height = repulsion_image.get_height()
        self.goal1_rect = Rect(self.x, self.y1 + 6, self.width,
                               repulsion_height)
        self.goal2_rect = Rect(self.x, self.y2 + 6, self.width,
                               repulsion_height)
        self.repulsion = transform.scale(repulsion_image, (self.width,
                                         repulsion_height))

    def check_collision(self, ball):
        """Check if ball collided with a force field.

        Args:
            ball (pygame.sprite): Ball sprite
        """
        if ball.rect.colliderect(self.goal1_rect):
            return 0
        elif ball.rect.colliderect(self.goal2_rect):
            return 1
        else:
            return None

    def draw(self, screen, clock):
        """Draw forcefields.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
            clock(pygame.time.Clock): Game clock
        """

        # Calculate the source rectangle for the current disinegration sprite
        source_rect = Rect(0, self.sprite_index * self.sprite_height,
                           self.sprite_width, self.sprite_height)
        # Create a surface with the same size as the disinegration sprite
        sprite_surface = Surface(source_rect.size, SRCALPHA)
        # Draw the current disinegration sprite onto the surface
        sprite_surface.blit(self.spritesheet, (0, 0), source_rect)
        # Scale up the disinegration sprite surface to fit the rectangle
        texture_surface = transform.scale(sprite_surface, (self.width,
                                                           self.height))
        # Draw either disinegration or repulsive
        if self.player1_repulse:
            screen.blit(self.repulsion, self.goal1_rect)
        else:
            screen.blit(texture_surface, (self.x, self.y1))
        if self.player2_repulse:
            screen.blit(self.repulsion, self.goal2_rect)
        else:
            screen.blit(texture_surface, (self.x, self.y2))

        # Increment the animation timer
        self.animation_timer += clock.get_time()

        # Check if it's time to update the sprite
        if self.animation_timer >= self.animation_delay:
            self.sprite_index = (self.sprite_index + 1) % SPRITE_COUNT
            self.animation_timer = 0

    def is_repulsion(self, player_id):
        """Check if player has repulsion forcefield enabled

        Args:
            player_id(int): Player ID to enable/disable
        """
        if player_id == 0:
            return self.player1_repulse
        elif player_id == 1:
            return self.player2_repulse

    def repulse(self, player_id, enable=True):
        """Enables repulsion instead of disintegration forcefield.

        Args:
            player_id(int): Player ID to enable/disable
            enable(bool): True=repulsion, False=disintegration
        """
        if player_id == 0:
            self.player1_repulse = enable
        elif player_id == 1:
            self.player2_repulse = enable
