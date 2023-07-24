"""Ball."""
from math import cos, pi, sin
from pygame import draw, image, sprite
from pygame.math import Vector2
from random import choice, uniform, randint
from time import time

MIN_SPEED = 5
MAX_SPEED = 11

HIT = 1
CAUGHT = 2

BALL_PATH = "images/Tennis_ball_23x23.png"


class Ball(sprite.Sprite):
    """Ball."""

    def __init__(self, centery, location=None,
                 speed=MIN_SPEED, paddle_rect=None,
                 current_player=0, on_paddle_delay=4):
        """Initialize ball.

        Args:
            centert(int):  Center Y coordinate of screen
            location((int, int) Optional X,Y coordinates of ball
            speed(int): Initial ball speed (Default=Minimum)
            paddle_rect(pygame.Rect): Optional rect encompassing paddle
            current_player(int): Player in possesion of ball
            on_paddle_delay(int): Time in seconds before ball released
        """
        super().__init__()
        self.image = image.load(BALL_PATH)
        self.current_player = current_player
        self.on_paddle_timer = time()
        self.on_paddle = True if paddle_rect else False
        self.on_paddle_delay = on_paddle_delay
        self.paddle_offset = 0  # Ball distance from center of paddle
        self.centery = centery
        self.speed = speed
        if not self.on_paddle:
            # Set initial direction
            horizontal_component = choice([x for x in range(-5, 6) if x != 0])
            vertical_component = choice([x for x in range(-5, 6) if x != 0])
            self.direction = Vector2(horizontal_component, vertical_component)
            # Scale vector down to length 1 without changing its orientation
            self.direction.normalize_ip()
            self.direction *= self.speed
            self.direction = Vector2(self.direction.x, self.direction.y)
            location = Vector2(location)
            self.rect = self.image.get_rect(center=location)
        else:
            # Set initial direction
            horizontal_component = choice([x for x in range(-3, 4) if x != 0])
            if self.current_player:
                # Player 2
                self.rect = self.image.get_rect(midtop=paddle_rect.midbottom)
                vertical_component = randint(3, 5)
            else:
                # Player 1
                self.rect = self.image.get_rect(midbottom=paddle_rect.midtop)
                vertical_component = randint(-5, -3)
            self.direction = Vector2(horizontal_component, vertical_component)
            # Scale vector down to length 1 without changing its orientation
            self.direction.normalize_ip()
            self.direction *= self.speed
            self.direction = Vector2(self.direction.x, self.direction.y)
        self.position = Vector2(self.rect.center)

    def alter_direction(self, direction):
        """Alter the direction of the ball.

        Args:
            direction((int, int)): 1=positive, -1=negative, 0=no change
        """
        if direction[0] == -1:
            self.direction.x = -abs(self.direction.x)
        elif direction[0] == 1:
            self.direction.x = abs(self.direction.x)
        if direction[1] == -1:
            self.direction.y = -abs(self.direction.y)
        elif direction[1] == 1:
            self.direction.y = abs(self.direction.y)

    def alter_direction_xy(self, x=False, y=False):
        """Alter the X and/or Y direction of the ball.

        Args:
            x(bool): Alter X direction
            y(bool): Alter Y direction
        """
        if x and y:
            self.direction = -self.direction
        elif x:
            self.direction.x = -self.direction.x
        elif y:
            self.direction.y = -self.direction.y
        # Add stochasticity
        self.direction.x += uniform(-0.1, 0.1)
        self.direction.y += uniform(-0.1, 0.1)

    def bounce(self, bricks):
        """Calculate ball direction after brick impact bounce.

        Args:
            bricks([pygame.Rect]): List of brick rects hit.
        """
        # Reverse ball position along original path until outside of brick
        while self.rect.collidelist(bricks) > -1:
            self.position -= self.direction.normalize()
            self.rect.center = self.position

        brick_count = len(bricks)
        if self.direction.x == 0:
            self.alter_direction_xy(False, True)
        elif brick_count >= 2:  # 2+ bricks hit
            if len(set(brick.x for brick in bricks)) == 1:
                # Bricks in same column:  Reverse X
                self.alter_direction_xy(True, False)
            elif len(set(brick.y for brick in bricks)) == 1:
                # Bricks in same row:  Reverse Y
                self.alter_direction_xy(False, True)
            else:
                # Corner strike:  Reverse both directions
                self.alter_direction_xy(True, True)
        else:
            # Single brick hit
            # Calculate intrusion point as the next position of the ball
            intrusion_point = self.position + self.direction.normalize()
            # Get the four corners of the brick
            tl = Vector2(bricks[0].topleft)
            tr = Vector2(bricks[0].topright)
            bl = Vector2(bricks[0].bottomleft)
            br = Vector2(bricks[0].bottomright)
            # Check if intrusion_point lies on one of the brick's edges
            if tl.y < intrusion_point.y < bl.y:  # Intrusion point left
                self.alter_direction_xy(True, False)
            elif tr.y < intrusion_point.y < br.y:  # Intrusion point right
                self.alter_direction_xy(True, False)
            elif tl.x < intrusion_point.x < tr.x:  # Intrusion point top
                self.alter_direction_xy(False, True)
            elif bl.x < intrusion_point.x < br.x:  # Intrusion point bottom
                self.alter_direction_xy(False, True)
            else:  # Intrusion point is on or near one of the corners
                if ((self.direction.x > 0 and self.direction.y > 0 and
                     intrusion_point == tl) or
                    (self.direction.x < 0 and self.direction.y < 0 and
                     intrusion_point == br) or
                    (self.direction.x > 0 and self.direction.y < 0 and
                     intrusion_point == bl) or
                    (self.direction.x < 0 and self.direction.y > 0 and
                     intrusion_point == tr)):
                    self.alter_direction_xy(True, True)
                elif ((self.direction.x > 0 and self.direction.y > 0 and
                       intrusion_point.y <= tl.y) or
                        (self.direction.x < 0 and self.direction.y < 0 and
                         intrusion_point.y >= br.y) or
                        (self.direction.x > 0 and self.direction.y < 0 and
                         intrusion_point.y >= bl.y) or
                        (self.direction.x < 0 and self.direction.y > 0 and
                         intrusion_point.y <= tr.y)):
                    self.alter_direction_xy(False, True)
                else:
                    self.alter_direction_xy(True, False)

    def catch(self, on_paddle_delay=2):
        """Catch ball on paddle.

        Args:
            on_paddle_delay(int): Time in seconds before ball released
        """
        self.on_paddle = True
        self.on_paddle_timer = time()
        self.on_paddle_delay = on_paddle_delay

    def check_paddle_hit(self, paddle_rect, human, players_catch):
        """Check if a ball has hit the paddle.

        Args:
            paddle_rect(pygame.Rect): Rect encompassing paddle
            human(bool): If player is human
            is_bottom(bool): Is the paddle at the bottom or not
            players_catch([bool, bool]): Determines if player is set to catch
        """
        if self.on_paddle:  # Ignore collision if on paddle
            return 0

        is_bottom = True if self.rect.centery > self.centery else False

        if self.rect.colliderect(paddle_rect):  # Check for collision
            paddle_center_x = paddle_rect.centerx
            ball_center_x = self.rect.centerx

            distance = ball_center_x - paddle_center_x
            normalized_distance = distance / (paddle_rect.width / 2)

            maob_denominator = 4 if human else 2.75  # Restrict human bounce
            max_bounce_angle = pi / maob_denominator  # Maximum angle of bounce

            # Determine angle based on where the ball hits the paddle
            angle = normalized_distance * max_bounce_angle

            # Reflect the direction vector off the normal for Y
            self.direction.reflect_ip(Vector2(0, 1))

            # Adjust the direction's x component based on the angle and speed
            speed = self.direction.length()
            self.direction = Vector2(speed * sin(angle), -speed * cos(angle))

            self.increase_speed()

            # Set ball Y direction
            if is_bottom:
                self.direction.y = -abs(self.direction.y)
            else:
                self.direction.y = abs(self.direction.y)

            # Adjust ball position along new course until outside of paddle
            direction = self.direction.normalize()
            while self.rect.colliderect(paddle_rect):
                self.position += direction
                self.rect.center = self.position

            self.position = self.rect.center

            # Check for catch
            if is_bottom and players_catch[0]:
                # Player 1 catch
                self.rect = self.image.get_rect(midbottom=paddle_rect.midtop)
                self.rect.y -= 2
                self.position = self.rect.center
                return CAUGHT
            elif not is_bottom and players_catch[1]:
                # Player 2 catch
                self.rect = self.image.get_rect(midtop=paddle_rect.midbottom)
                self.rect.y += 2
                self.position = self.rect.center
                return CAUGHT
            else:
                return HIT
        return 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        # Draw line indicating direction if on paddle
        if self.on_paddle:
            normalized_direction = self.direction.normalize()
            arrow = (self.rect.centerx + int(normalized_direction.x * 9),
                     self.rect.centery + int(normalized_direction.y * 9))
            draw.line(surface, (0, 255, 0), self.rect.center, arrow, 2)

    def get_direction(self):
        """Get direction signed tuple."""
        x_sign = 1 if self.direction.x >= 0 else -1
        y_sign = 1 if self.direction.y >= 0 else -1
        return (x_sign, y_sign)

    def get_distance(self, goal_y):
        """Get x coordinate and relative Y coordinate of ball to goal.

        Args:
            goal_y(int): Goal Y coordinate
        """
        y_distance = abs(self.rect.centery - goal_y)  # Ball distance to goal
        screen_height = abs(self.centery - goal_y) * 2  # Screen height
        # Adjust distance if ball travelling away from paddle
        if ((goal_y < self.centery and self.direction.y >= 0) or
                (goal_y > self.centery and self.direction.y <= 0)):
            y_distance = screen_height + (screen_height - y_distance)
        return y_distance

    def increase_speed(self):
        """Increase ball speed."""
        if self.speed >= MAX_SPEED:
            return
        self.speed += 1
        self.direction.normalize_ip()
        self.direction *= self.speed
        self.direction = Vector2(self.direction.x, self.direction.y)

    def release(self):
        """Release ball from paddle."""
        self.on_paddle = False
        self.on_paddle_timer = 0

    def set_on_paddle_location(self, paddle_rect):
        """Set the on paddle ball location relative to the paddle.

        Args:
            paddle_rect(pygame.Rect): Rectangle encompassing paddle
        """
        if self.current_player == 0:
            # Player 1
            self.rect.bottom = paddle_rect.top - 2
        else:
            # Player 2
            self.rect.top = paddle_rect.bottom + 2
        self.rect.centerx = paddle_rect.centerx + self.paddle_offset
        self.position = self.rect.center
        # Check paddle timer
        if time() - self.on_paddle_timer >= self.on_paddle_delay:
            self.release()

    def slow_speed(self):
        """Reduce ball speed to minimum."""
        self.speed = MIN_SPEED
        self.direction.normalize_ip()
        self.direction *= self.speed
        self.direction = Vector2(self.direction.x, self.direction.y)

    def update(self):
        """Update position of the ball."""
        if not self.on_paddle:
            self.position += self.direction
            self.rect.center = self.position
