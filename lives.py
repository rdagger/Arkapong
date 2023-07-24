"""Lives."""
from pygame import image, sprite

SPRITE_PATHS = {
    0: 'images/Players1_29x7.png',
    1: 'images/Players2_29x7.png'
}


class Life(sprite.Sprite):
    """Life sprites."""

    def __init__(self, player_id, position, anchor='midleft'):
        """Lives sprite constructor.

        Args:
            player_id(int): Index of player lives sprite
            position((int, int)): X, Y coordinates.
            anchor(string): Positioning anchor, default='midleft' (see notes)

        Notes:
            Valid anchor strings: x, y, left, right, top, bottom, centerx,
            centery, center, topleft, bottomleft, topright, bottomright,
            midleft, midright, midtop, midbottom.

        """
        super().__init__()
        self.image = image.load(SPRITE_PATHS[player_id])
        self.rect = self.image.get_rect(**{anchor: position})


class Lives:
    """Player lives."""

    def __init__(self, lives_per_player, goal_top, goal_bottom, info_left,
                 info_right):
        """Lives constructor.

        Args:
            lives_per_player (int): Number of lives per player
            goal_top(int): Top boundary of player 2 goal.
            goal_bottom(int): Bottom boundary of player 1 goal.
            info_left(int): Left info boundary.
            info_right(int): Right info boundary.
        """
        self.goal_top = goal_top
        self.goal_bottom = goal_bottom
        self.info_left = info_left
        self.info_right = info_right
        self.lives_per_player = lives_per_player
        self.lives = (sprite.Group(), sprite.Group())  # Player lives
        self.reset()

    def decrease_lives(self, player_id, lives=1):
        """Remove lives from the player information display.

        Args:
            player_id (int): Player ID (0 or 1)
            lives (int): The number of lives to remove.
        """
        for i in range(lives):
            if len(self.lives[player_id]) > 0:
                last_life = self.lives[player_id].sprites()[-1]
                self.lives[player_id].remove(last_life)

    def draw(self, screen):
        """Display lives left for players.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        self.lives[0].draw(screen)  # Player 1
        self.lives[1].draw(screen)  # Player 2

    def get_lives(self, player_id):
        """Get number of player lives left.

        Args:
            player_id (int): Player ID (0 or 1)
        """
        return len(self.lives[player_id])

    def increase_lives(self, player_id, lives=1):
        """Add lives to the player information display.

        Args:
            player_id (int): Player ID (0 or 1)
            lives (int): The number of lives to add.
        """
        for i in range(lives):
            if player_id:
                # Player 2
                if self.lives[player_id]:
                    last_life = self.lives[player_id].sprites()[-1]
                    life_left = last_life.rect.left - 5
                else:
                    # No lives
                    life_left = self.info_right + 100
                life_sprite = Life(player_id,
                                   (life_left, self.goal_top - 10),
                                   anchor='midright')
            else:
                # Player 1
                if self.lives[player_id]:
                    last_life = self.lives[player_id].sprites()[-1]
                    life_right = last_life.rect.right + 5
                else:
                    # No lives
                    life_right = self.info_left - 100
                life_sprite = Life(player_id,
                                   (life_right, self.goal_bottom + 10),
                                   anchor='midleft')
            self.lives[player_id].add(life_sprite)

    def reset(self):
        """Reset player's lives. """
        self.lives[0].empty()
        self.lives[1].empty()
        # Add player 1 lives
        self.increase_lives(player_id=0, lives=self.lives_per_player)
        # MAY REQUIRE CHANGE IF PLAYING AGAINST COMPUTER ADDED!!!
        # Add player 2 lives
        self.increase_lives(player_id=1, lives=self.lives_per_player)
