"""Arkapong game options."""
from game_fonts import GameFonts, Size
from pygame import Color, draw, display, event, key, quit, Rect, Surface
from pygame.locals import KEYDOWN, KEYUP, MOUSEMOTION, QUIT


class Options:
    """Arkapong game options."""

    def __init__(self, key_select, key_exit):
        """Game options constructor.

        Args:
            key_select(pygame.key): Keyboard key for selection
            key_exit(pygame.key): Keyboard key to exit game
        """
        self.players = 1  # Number of players
        self.key_select = key_select
        self.key_exit = key_exit

    def prompt(self, screen):
        """Prompt for the number of players.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        fonts = GameFonts()
        title_text = "ArkaPong"
        input_text = "ENTER # OF PLAYERS"

        _, y_offset = fonts.measure(input_text, Size.LARGE)
        y_offset *= 1.5

        screen_width, screen_height = screen.get_size()
        play_area = Rect(int(screen_width * 0.1),
                         int(screen_height * 0.1),
                         int(screen_width * 0.8),
                         int(screen_height * 0.8))

        # Create a new surface for the gradient
        gradient_surface = Surface((screen_width, screen_height))
        # Define the gradient colors
        colors = [(255, 0, 0), (0, 0, 255), (0, 162, 232)]
        # Define the transition height
        trans_height = screen_height // (len(colors) - 1)
        for i in range(len(colors) - 1):
            for y in range(trans_height):
                # Get the start and end colors
                start_color = colors[i]
                end_color = colors[i + 1]
                # Calculate the transition ratio
                ratio = y / trans_height
                # Interpolate the color
                color = [int(start * (1 - ratio) + end * ratio) for start,
                         end in zip(start_color, end_color)]
                # Draw the line on the gradient surface
                draw.line(gradient_surface, color, (0, i * trans_height + y),
                          (screen_width, i * trans_height + y))
        x_movement = 0
        while True:
            for e in event.get():
                if (e.type == QUIT or
                        e.type == KEYDOWN and e.key == self.key_exit):
                    quit()
                    exit()
                elif e.type == MOUSEMOTION:
                    # Check mouse X movement
                    x_movement += e.rel[0]
                    if x_movement > 75:
                        self.players = 2
                    elif x_movement < -75:
                        self.players = 0
                    else:
                        self.players = 1
                elif e.type == KEYUP:
                    if e.key == self.key_select:
                        return

            # Blit the gradient surface onto the screen
            screen.blit(gradient_surface, (0, 0))

            draw.rect(screen, Color('black'), play_area, 0)  # Play area
            # ArkaPong title
            _, title_height = fonts.measure(title_text, Size.TITLE)
            title_x = play_area.centerx
            title_y = play_area.top // 2
            fonts.draw(title_text, Size.TITLE, (title_x, title_y),
                       screen, Color("blue"), center=True)
            # Directions
            dir_text = "LEFT/RIGHT Keys or Mouse to SeLeCT - "
            dir_text += f"{key.name(self.key_select).upper()} to Continue - "
            dir_text += f"{key.name(self.key_exit).upper()} to Exit"
            _, dir_height = fonts.measure(dir_text, Size.SMALL)
            dir_x = play_area.centerx
            dir_y = screen_height - play_area.top // 2
            fonts.draw(dir_text, Size.SMALL, (dir_x, dir_y),
                       screen, Color("blue"), center=True)
            # Set input either players or games
            input_value = self.players
            # Draw input prompt and value
            fonts.draw(input_text, Size.LARGE,
                       (play_area.centerx, play_area.centery - y_offset),
                       screen, Color("red"), center=True)
            fonts.draw(str(input_value), Size.HUGE,
                       (play_area.centerx, play_area.centery + y_offset),
                       screen, Color("white"), center=True)
            display.flip()
