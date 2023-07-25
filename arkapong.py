"""Pygame Arkapong."""
from ball import Ball, CAUGHT
from bricks import Bricks, DESTROYED
from configparser import ConfigParser
from enemies import Enemies
from forcefields import Forcefields
from game_board import Board
from game_options import Options
from game_sounds import GameSounds
from lives import Lives
from player import Player
from powerups import PowerUps
from pygame import display, event, init, mouse, quit, sprite, time
from pygame.locals import FULLSCREEN, KEYDOWN, MOUSEMOTION, QUIT
from random import choice, random
from sys import exit, modules

BRICK_VALUE = 25
ENEMY_VALUE = 125
GOAL_VALUE = 200
LEVEL_UP_VALUE = 150


class Game:
    """Arkapong."""

    def __init__(self):
        """Game constructor."""
        init()  # Initialize pygame library
        self.clock = time.Clock()
        # Load game settings file
        config = ConfigParser()
        config.read('settings.ini')
        screen_width = config.getint('GameSettings', 'screen_width')
        screen_height = config.getint('GameSettings', 'screen_height')
        full_screen = config.getboolean('GameSettings', 'full_screen')
        self.fps = config.getint('GameSettings', 'speed')
        lives = config.getint('GameSettings', 'lives')
        difficulty = config.getint('GameSettings', 'computer_difficulty')
        self.mouse_rel = config.getboolean('GameSettings', 'mouse_relative')
        self.show_fps = config.getboolean('GameSettings', 'frame_rate')

        # Get keyboard input keys for each player
        self.input_keys = {}
        for player_num in range(1, 3):
            player = "Player{}".format(player_num)
            self.input_keys[player] = {}
            key = config.get(player, "button1_key")
            self.input_keys[player]["button1"] = getattr(
                modules["pygame"], key)
        self.key_select = getattr(modules["pygame"],
                                  config.get("Player1", "select_key"))
        self.skip_level = getattr(modules["pygame"],
                                  config.get("Player1", "skip_level"))
        self.key_exit = getattr(modules["pygame"],
                                config.get("Player1", "exit_key"))
        # Initialize screen
        if full_screen:
            self.screen = display.set_mode((0, 0), FULLSCREEN)
        else:
            self.screen = display.set_mode((screen_width, screen_height))

        self.board = Board(screen_width, screen_height,
                           self.key_select, self.key_exit)
        self.lives = Lives(lives, self.board.goal_top, self.board.goal_bottom,
                           self.board.info_left, self.board.info_right)
        self.options = Options(self.key_select,  # In game user options
                               self.key_exit)
        self.options.prompt(self.screen)  # Prompt user for options

        self.players = [Player(
            id=i,
            screen_width=screen_width,
            goal_top=self.board.goal_top,
            goal_bottom=self.board.goal_bottom,
            wall_left=self.board.wall_left,
            wall_right=self.board.wall_right,
            human=True if i < self.options.players else False,
            computer_difficulty=difficulty
            ) for i in range(2)]

        self.sounds = GameSounds()
        self.forcefields = Forcefields(self.board.goal_top,
                                       self.board.goal_bottom,
                                       self.board.goal_left,
                                       self.board.goal_right)
        self.balls = sprite.Group()
        self.balls.add(Ball(centery=self.board.center[1],
                            paddle_rect=self.players[0].paddle_rect(),
                            current_player=0))
        self.bricks = Bricks(self.board.wall_left,
                             self.board.wall_right,
                             self.board.center[1])
        enemies = self.bricks.build()
        self.spawn_enemies(enemies)
        self.scores = [0, 0]
        self.powerups = PowerUps(self.board.goal_top, self.board.goal_bottom)

    def explode(self, player_id):
        """Explode player's vaus.

        Args:
            player_id(int): The player_id to explode.
        """
        self.sounds.play("explode")  # Play explosion sound
        player = self.players[player_id]
        player.explode = True  # Set player to explode on render
        # Play the 5 paddle explosion frames
        for i in range(5):
            self.render()
            display.flip()
            time.wait(200)
        player.explode = False
        time.wait(500)

    def handle_input(self):
        """Handle keyboard and mouse input."""
        mouse_x, mouse_y = None, None
        for e in event.get():
            if (e.type == QUIT or e.type == KEYDOWN and
                    e.key == self.key_exit):
                quit()
                exit()
            if e.type == KEYDOWN:
                # Loop through players and check for button 1
                for i in range(self.options.players):
                    if e.key == self.input_keys[f"Player{i + 1}"]["button1"]:
                        for ball in self.balls:
                            if ball.on_paddle and ball.current_player == i:
                                ball.release()
                if e.key == self.skip_level:
                    # Skip level
                    self.bricks.increment_level()
                    enemies = self.bricks.build()
                    self.spawn_enemies(enemies)
                    self.render()
                    self.board.display_level_number(self.bricks.level,
                                                    self.options.players,
                                                    self.screen, display)
            if self.mouse_rel and e.type == MOUSEMOTION:
                x_movement, y_movement = e.rel  # Relative mouse movement
                mouse_x = self.players[0].x + x_movement
                mouse_y = self.players[1].x + y_movement

        if not self.mouse_rel:
            mouse_x, mouse_y = mouse.get_pos()  # Actual mouse position

        if self.players[0].human:  # Human player 1
            if mouse_x:
                self.players[0].move(mouse_x)
        else:
            # Computer controlled paddle player 1
            closest_ball = min(self.balls, key=lambda ball: ball.get_distance(
                self.board.goal_bottom))
            self.players[0].move_toward(closest_ball.rect.centerx)
            if closest_ball.on_paddle and closest_ball.current_player == 0:
                if random() < 0.01:
                    closest_ball.release()

        if self.players[1].human:  # Human player 2
            if mouse_y:
                self.players[1].move(mouse_y)
        else:
            # Computer controlled paddle player 2
            closest_ball = min(self.balls, key=lambda ball: ball.get_distance(
                self.board.goal_top))
            self.players[1].move_toward(closest_ball.rect.centerx)
            if closest_ball.on_paddle and closest_ball.current_player == 1:
                if random() < 0.01:
                    closest_ball.release()

    def handle_powerup(self, letter, player_id):
        """Handle power-ups.

        Args:
            letter(string): Letter representing type of power-up.
            player_id(int): Player ID who released power-up.
        """
        if self.players[player_id].size == "long" and letter == "E":
            # Already expanded so do nothing
            return
        elif self.players[player_id].size == "narrow" and letter == "R":
            # Already reduced so do nothing
            return
        elif (self.players[player_id].size != "regular" and
              letter not in ["E", "R"]):
            # Reset paddle length unless the power-up will change the length
            self.players[player_id].set_size("regular")
            self.sounds.play("resize")
        if not letter == "C":
            # Reset catch unless the power-up is a catch
            self.players[player_id].catch = False  # Reset player catch
            for ball in self.balls:  # Releaes any caught balls
                if ball.on_paddle and ball.current_player == player_id:
                    ball.release()
        if letter == "B":  # Break out to next level
            self.sounds.play("levelup")
            self.next_level()
            self.scores[player_id] += LEVEL_UP_VALUE
        elif letter == "E":  # Expand paddle size
            self.players[player_id].set_size("long")
            self.sounds.play("resize")
        elif letter == "R":  # Reduce paddle size
            self.players[player_id].set_size("narrow")
            self.sounds.play("resize")
        elif letter == "C" and self.players[player_id].human:  # Catch ball
            if not self.players[player_id].catch:
                self.players[player_id].catch = True
                self.sounds.play("catch")
        elif letter == "D":  # Disruption (splits ball into 3 balls)
            for i in range(2):
                self.balls.add(Ball(self.board.center[1],
                               location=self.balls.sprites()[0].rect.center,
                               speed=self.balls.sprites()[0].speed,
                               current_player=player_id))
        elif letter == "F":  # Force field repulsion mode
            if not self.forcefields.is_repulsion(player_id):
                self.sounds.play("fieldon")
                self.forcefields.repulse(player_id)
        elif letter == "S":  # Slow balls
            for ball in self.balls:
                ball.slow_speed()
        elif letter == "P":  # Player gets extra life
            self.lives.increase_lives(player_id)
            self.sounds.play("extralife")

    def next_level(self):
        """Load next level."""
        self.bricks.increment_level()
        enemies = self.bricks.build()
        self.reset()
        self.spawn_enemies(enemies)
        self.render()  # Render board so level number is over next level
        self.board.display_level_number(self.bricks.level,
                                        self.options.players,
                                        self.screen, display)

    def render(self):
        """Render game elements."""
        self.screen.fill((0, 0, 0))  # Background color
        self.board.draw(self.screen)  # Game board
        self.board.draw_score(self.scores, self.screen)
        self.lives.draw(self.screen)
        self.forcefields.draw(self.screen, self.clock)
        self.players[0].draw(self.screen, self.clock)
        self.players[1].draw(self.screen, self.clock)
        for ball in self.balls:
            ball.draw(self.screen)
        self.bricks.draw(self.screen)
        self.powerups.draw(self.screen)
        self.enemies.draw(self.screen)
        if self.show_fps:
            self.board.draw_fps(self.screen, self.clock)

    def reset(self):
        """Reset players, balls and power-ups."""
        # Select random player
        player_id = choice([0, 1])
        # Reset catch
        for player in self.players:
            player.catch = False
            player.set_size("regular")
        # Reset balls
        self.balls.empty()
        self.balls.add(Ball(
            self.board.center[1],
            paddle_rect=self.players[player_id].paddle_rect(),
            current_player=player_id))
        self.forcefields.repulse(player_id=0, enable=False)
        self.forcefields.repulse(player_id=1, enable=False)
        self.powerups.clear()

    def run(self):
        """Run game."""
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.update()
            self.render()
            display.flip()

    def spawn_enemies(self, enemies):
        """Generate enemies.

        Args:
            enemy_locations((int, (int, int))): Enemy ID at X, Y location.
        """
        self.enemies = Enemies(enemies, self.board.goal_top,
                               self.board.goal_bottom)

    def update(self):
        """Update player position and check for collisions."""
        for ball in self.balls.sprites():
            if not ball.on_paddle:
                ball.update()  # Not on paddle so just update
            else:
                # Pass paddle rect if on paddle
                ball.set_on_paddle_location(
                    self.players[ball.current_player].paddle_rect())

            # Check for ball collision with paddles
            for player in self.players:
                if not ball.on_paddle:  # Check for collision if off paddle
                    hit = ball.check_paddle_hit(player.paddle_rect(),
                                                player.human,
                                                (self.players[0].catch,
                                                self.players[1].catch))
                    if hit:
                        self.sounds.play("paddle")  # Play paddle hit sound
                        ball.current_player = player.id  # Set player with ball
                        if hit == CAUGHT:
                            ball.catch()
                        player.hits += 1

            # Check for ball collision with walls
            new_direction = self.board.check_collision(ball)
            if new_direction:
                ball.alter_direction(new_direction)
            else:  # Only check for goal if no border contact
                # Check for ball collision with goal forcefield
                player_id = self.forcefields.check_collision(ball)
                if player_id is not None:
                    if self.forcefields.is_repulsion(player_id):
                        # Repulsion forcefield
                        self.sounds.play("fieldoff")
                        self.forcefields.repulse(player_id, False)  # Disable
                        direction = (0, -1) if player_id == 0 else (0, 1)
                        ball.alter_direction(direction)
                    elif len(self.balls) == 1:
                        # Goal against player 1 or player 2
                        self.scores[player_id ^ 1] += GOAL_VALUE
                        self.explode(player_id)
                        self.lives.decrease_lives(player_id)
                        if self.lives.get_lives(player_id) > 0:
                            self.reset()
                        else:
                            # Game Over
                            self.board.game_over(self.bricks.level,
                                                 self.screen, display)
                            self.scores = [0, 0]
                            self.lives.reset()
                            self.reset()
                            enemies = self.bricks.build()
                            self.spawn_enemies(enemies)
                    else:
                        self.balls.remove(ball)

            # Check for ball collision with bricks
            results, bricks = self.bricks.check_hit(ball.rect)
            if results:
                ball.bounce(bricks)
                self.sounds.play(['brick' + str(num) for num in set(results)])
                if DESTROYED in results:  # Possible power-up
                    self.powerups.roll_dice(ball.current_player,
                                            bricks[results.index(DESTROYED)])

                # Increment score
                self.scores[ball.current_player] += (BRICK_VALUE *
                                                     results.count(DESTROYED))
                # Check brick count
                if not self.bricks.brick_count():
                    # Next level achieved
                    self.scores[ball.current_player] += LEVEL_UP_VALUE
                    self.next_level()
                    break

            # Check for ball collision with enemies
            new_direction = self.enemies.check_collision_ball(ball.rect)
            if new_direction:
                self.sounds.play("enemy")
                ball.alter_direction_xy(*new_direction)
                self.scores[ball.current_player] += ENEMY_VALUE

        self.enemies.update(self.clock)
        # Check for enemy collision with paddle
        paddle_hit = self.enemies.check_collision_paddles(
            (self.players[0].paddle_rect(), self.players[1].paddle_rect()))
        if paddle_hit is not None:
            self.sounds.play("enemy")
            self.scores[paddle_hit] += ENEMY_VALUE
        # Check for enemy collsion with bricks
        self.enemies.check_collision_bricks(self.bricks.bricks)
        # Check for other enemy collision
        for enemy in self.enemies.enemies:
            # Check for enemy collision with wall
            new_direction = self.board.check_collision(enemy)
            if new_direction:
                enemy.alter_direction(new_direction)

        self.powerups.update(self.clock)
        letter, player_id = self.powerups.check_collision(
            (self.players[0].paddle_rect(),
             self.players[1].paddle_rect()))
        if letter:
            self.handle_powerup(letter, player_id)


if __name__ == "__main__":
    while True:
        game = Game()
        game.run()
