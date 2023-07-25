"""Arkapong game board."""
from border_sprites import BorderSprite
from border_sprites import CONNECTOR, PIPE, PIPE_HT, PIPE_HB
from border_sprites import CORNER_TL, CORNER_TR, CORNER_BL, CORNER_BR
from game_fonts import GameFonts, Size
from game_sounds import GameSounds
from pygame import Color, event, key, Rect, sprite, quit, time, transform
from pygame.locals import KEYDOWN, KEYUP, QUIT

VRES = {912: 1, 1278: 2}  # Resoltion thresholds for vertical size


class Board:
    """Akarpong game board."""

    def __init__(self, screen_width, screen_height, key_select, key_exit):
        """Create game board.

        Args:
            screen_width (int): Overall screen width of game.
            screen_height (int): Overall screen height of game.
            key_select(pygame.key): Keyboard key for selection
            key_exit(pygame.key): Keyboard key to exit game
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center = (screen_width // 2, screen_height // 2)

        self.key_select = key_select
        self.key_exit = key_exit

        self.fonts = GameFonts()
        self.sounds = GameSounds()

        self.border = sprite.Group()
        self.build_border()

    def build_border(self):
        """Configure sprites that comprise border."""
        center_y = self.screen_height // 2
        left_x = 13
        right_x = self.screen_width - 13
        # Draw initial vertical connectors
        self.border.add(BorderSprite(CONNECTOR, (left_x, center_y)))
        self.border.add(BorderSprite(CONNECTOR, (right_x, center_y)))
        y_offset = center_y - self.border.sprites()[0].rect.top
        for i in range(next((value for limit,
                            value in VRES.items()
                            if self.screen_height < limit), 3)):
            # Draw additional pipes
            self.border.add(BorderSprite(PIPE, (left_x, center_y - y_offset),
                            'midbottom'))
            self.border.add(BorderSprite(PIPE, (right_x, center_y - y_offset),
                            'midbottom'))
            self.border.add(BorderSprite(PIPE, (left_x,
                            center_y + y_offset + 1), 'midtop'))
            self.border.add(BorderSprite(PIPE, (right_x,
                            center_y + y_offset + 1), 'midtop'))
            y_offset += 89
            # Draw additional connectors
            self.border.add(BorderSprite(CONNECTOR, (left_x,
                                         center_y - y_offset), 'midbottom'))
            self.border.add(BorderSprite(CONNECTOR, (right_x,
                                         center_y - y_offset), 'midbottom'))
            self.border.add(BorderSprite(CONNECTOR, (left_x,
                                         center_y + y_offset + 1), 'midtop'))
            self.wall_left = self.border.sprites()[-1].rect.right  # Wall left
            self.border.add(BorderSprite(CONNECTOR, (right_x,
                                         center_y + y_offset + 1), 'midtop'))
            self.wall_right = self.border.sprites()[-1].rect.left  # Wall right
            y_offset += 89
        # Draw corners
        self.border.add(BorderSprite(CORNER_TL, (left_x + 1,
                        center_y - y_offset), 'midbottom'))
        self.border.add(BorderSprite(CORNER_TR, (right_x - 2,
                        center_y - y_offset), 'midbottom'))
        self.border.add(BorderSprite(CORNER_BR, (right_x - 2,
                        center_y + y_offset + 1), 'midtop'))
        self.border.add(BorderSprite(CORNER_BL, (left_x + 1,
                        center_y + y_offset + 1), 'midtop'))
        # Draw horizontal pipes
        y_offset = self.border.sprites()[-1].rect.bottom - center_y
        x_offset = self.border.sprites()[-1].rect.right
        self.border.add(BorderSprite(PIPE_HB, (x_offset, center_y + y_offset),
                        'bottomleft'))
        self.goal_left = self.border.sprites()[-1].rect.right  # Goal left
        self.goal_bottom = self.border.sprites()[-1].rect.bottom  # Goal bottom
        self.wall_bottom = self.border.sprites()[-1].rect.top  # Wall bottom
        self.info_left = self.border.sprites()[-1].rect.centerx  # Info left
        self.border.add(BorderSprite(PIPE_HB, (self.screen_width - x_offset,
                        center_y + y_offset), 'bottomright'))
        self.border.add(BorderSprite(PIPE_HT, (x_offset,
                        center_y - y_offset + 1), 'topleft'))
        self.border.add(BorderSprite(PIPE_HT, (self.screen_width - x_offset,
                        center_y - y_offset + 1), 'topright'))
        self.goal_right = self.border.sprites()[-1].rect.left - 1  # Goal right
        self.goal_top = self.border.sprites()[-1].rect.top  # Goal top
        self.wall_top = self.border.sprites()[-1].rect.bottom  # Wall top
        self.info_right = self.border.sprites()[-1].rect.centerx  # Info right

    def check_collision(self, item):
        """Check if rect collided with game border.

        Args:
            item (pygame.sprite): sprite to check.
        """
        # check for border impact
        collisions = sprite.spritecollide(item, self.border, False)

        if not collisions:
            return None

        direction = [0, 0]
        if item.rect.left <= self.wall_left:
            # Left wall
            direction[0] = 1
        elif item.rect.right >= self.wall_right:
            # Right wall
            direction[0] = -1
        if item.rect.top <= self.wall_top:
            # Top wall
            direction[1] = 1
        elif item.rect.bottom >= self.wall_bottom:
            # Bottom wall
            direction[1] = -1

        if direction[1]:  # Check for goal post hits
            if (item.rect.centerx >= self.goal_left and
                    item.rect.centerx < self.center[0]):
                # Left goal post hit
                direction[0] = 1
            elif (item.rect.centerx <= self.goal_right and
                    item.rect.centerx > self.center[0]):
                # Right goal post hit
                direction[0] = -1

        return direction

    def draw(self, screen):
        """Draw the play area.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        self.border.draw(screen)

    def draw_fps(self, screen, clock):
        """Draw the frame frate (FPS)

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
            clock(pygame.time.Clock): Game clock
        """
        fps_text = f"FPS: {int(clock.get_fps())}"
        _, fps_height = self.fonts.measure(fps_text, Size.SMALL)
        fps_pos = (self.center[0], self.screen_height - fps_height)
        self.fonts.draw(fps_text, Size.SMALL, fps_pos, screen,
                        Color("Yellow"), center=False)

    def draw_score(self, scores, screen):
        """Display the player's score.

        Args:
            scores((int, int)): The 2 scores.
            screen(pygame.Surface): Graphical window to display graphics.
        """
        for index, score in enumerate(scores):
            score_text = f"{score:0>2}"
            flip = False
            if index:
                score_pos = (self.info_left, self.goal_top - 15)
                flip = True
            else:
                score_pos = (self.info_right, self.goal_bottom + 15)
            self.fonts.draw(score_text, Size.MEDIUM, score_pos, screen,
                            Color("White"), center=True, flip=flip)

    def game_over(self, level, screen, display):
        """Display game over and wait for select key press and release.

        Args:
            level(int): Level number to resume
            screen(pygame.Surface): Graphical window to display graphics.
            display(pygame.display): Visual output.
        """
        game_text = " GAME "
        _, game_height = self.fonts.measure(game_text, Size.CODA)
        game_y = self.center[1] - game_height * .8
        self.fonts.draw(game_text,
                        Size.CODA,
                        (self.center[0], game_y),
                        screen,
                        Color("white"),
                        background=Color("Navy"),
                        center=True)

        over_text = " OVER "
        self.fonts.draw(over_text,
                        Size.CODA,
                        self.center,
                        screen,
                        Color("white"),
                        background=Color("Navy"),
                        center=True)

        msg_text = f"Press {key.name(self.key_select).upper()} to resume"
        msg_text += f" LeveL {level}"
        msg_text += f" or {key.name(self.key_exit).upper()} to exit."
        msg_y = self.center[1] + self.center[1] // 2
        self.fonts.draw(msg_text,
                        Size.SMALL,
                        (self.center[0], msg_y),
                        screen,
                        Color("blue"),
                        background=Color("black"),
                        center=True)

        display.flip()
        waiting = True
        while waiting:  # Pause until CTRL pressed or ESC to quit
            for e in event.get():
                if (e.type == QUIT or
                        e.type == KEYDOWN and e.key == self.key_exit):
                    quit()
                    exit()
                elif e.type == KEYUP and e.key == self.key_select:
                    waiting = False

    def display_level_number(self, level, players, screen, display):
        """Display level number.

        Args:
            level(int): Level number
            players(int): Number of players
            screen(pygame.Surface): Graphical window to display graphics
            display(pygame.display): Visual output
        """
        centerx = self.center[0]
        centery = self.center[1]
        level_text = f" Level {level} "
        level_width, level_height = self.fonts.measure(level_text, Size.MEDIUM)
        level_y_p2 = (self.goal_bottom - centery) // 2
        level_y_p1 = centery + level_y_p2
        self.fonts.draw(level_text,
                        Size.MEDIUM,
                        (centerx, level_y_p1),
                        screen,
                        Color("white"),
                        center=True)
        if players > 1:  # Display inverted level for player 2
            lev_rect = Rect(centerx - level_width // 2,
                            level_y_p1 - (level_height // 2),
                            level_width,
                            level_height)
            lev = screen.subsurface(lev_rect).copy()
            rotated_lev = transform.rotate(lev, 180)
            screen.blit(rotated_lev,
                        (centerx - level_width // 2,
                         self.goal_top + level_y_p2 - (level_height // 2)))
        display.flip()
        time.delay(2000)
