"""Enemies"""
from pygame import image, sprite, Surface
from pygame.math import Vector2
from pygame.locals import SRCALPHA
from random import choice

ENEMIES = {
    0: "images/Enemy_annulus.png",
    1: "images/Enemy_molecule.png",
    2: "images/Enemy_morph.png",
    3: "images/Enemy_orb.png",
    4: "images/Enemy_tetrahedron.png"
}

EXPLODE = "images/Enemy_explosions.png"
EXPLODE_CELLS = 6

WIDTH = 44
HEIGHT = 44
SPRITE_CELLS = 25


class Enemy(sprite.Sprite):
    def __init__(self, enemy_id, coords):
        """Enemy sprite constuctor.

        Args:
            enemy_id(int): Number representing type of enemy.
            coors((int, int)): X, Y coordinates of enemy.
        """
        super().__init__()
        self.spritesheet = image.load(ENEMIES[enemy_id])
        self.exploding_sheet = image.load(EXPLODE)
        self.direction = Vector2(choice([-1, 1]), choice([-1, 1]))

        self.animation_timer = 0
        self.animation_delay = 100  # Delay between frames (100 milliseconds)
        self.sprite_count = 25
        self.sprite_index = 0

        # Set initial sprite
        self.image = Surface((WIDTH, HEIGHT), SRCALPHA)
        self.image.blit(self.spritesheet, (0, 0),
                        (self.sprite_index % 5 * WIDTH,
                         self.sprite_index // 5 * HEIGHT,
                         WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
        self.position = Vector2(self.rect.center)
        self.exploding = False
        self.exploding_index = 0

    def alter_direction(self, direction):
        """Alter the direction of the enemy.

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
        """Alter the X and/or Y direction of the enemy.

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

    def bounce(self, bricks):
        """Calculate enemy direction after brick impact bounce.

        Args:
            bricks([pygame.Rect]): List of brick rects hit.
        """
        reverse_direction = -self.direction
        brick_count = len(bricks)
        if brick_count > 2:  # 3 bricks hit (only possible for inside corners)
            # More than 3 bricks
            if len(set(brick.x for brick in bricks)) == 1:
                # Brick in same column: Reverse X
                self.alter_direction_xy(True, False)
            else:
                # Bricks form corner: Reverse both directions
                self.alter_direction_xy(True, True)
        elif brick_count == 2:  # 2 bricks hit
            if bricks[0].x == bricks[1].x:
                # Bricks in same column:  Reverse X
                self.alter_direction_xy(True, False)
            elif bricks[0].y == bricks[1].y:
                # Bricks in same row:  Reverse Y
                self.alter_direction_xy(False, True)
            else:
                # Corner strike:  Reverse both directions
                self.alter_direction_xy(True, True)
        else:
            # Single brick hit
            intersection = self.rect.clip(bricks[0])
            if intersection.width > intersection.height:
                # Brick hit on top or bottom:  Reverse Y
                self.alter_direction_xy(False, True)
            elif intersection.width < intersection.height:
                # Brick hit on sides:  Reverse X
                self.alter_direction_xy(True, False)
            else:
                # Corner strike:  Reverse both directions
                self.alter_direction_xy(True, True)

        # Reverse enemy position along original path until outside of brick
        position = self.rect.center
        while self.rect.collidelist(bricks) > -1:
            position += reverse_direction
            self.rect.center = position

    def update(self, clock):
        """Update position and index of the enemy.

        Args:
            clock(pygame.time.Clock): Game clock
        """
        self.rect.move_ip(self.direction)  # Move the enemy

        # Clear the previous frame by filling with a transparent color
        self.image.fill((255, 255, 0, 0))

        # Increment the animation timer
        self.animation_timer += clock.get_time()

        if self.exploding:
            # Calculate the source rectangle for the current sprite
            self.image.blit(self.exploding_sheet, (0, 0),
                            (self.exploding_index * WIDTH,
                             0,
                             WIDTH, HEIGHT))
            # Check if it's time to update the sprite
            if self.animation_timer >= self.animation_delay:
                self.exploding_index += 1
                self.animation_timer = 0
        else:
            # Calculate the source rectangle for the current sprite
            self.image.blit(self.spritesheet, (0, 0),
                            (self.sprite_index % 5 * WIDTH,
                            self.sprite_index // 5 * HEIGHT,
                            WIDTH, HEIGHT))
            # Check if it's time to update the sprite
            if self.animation_timer >= self.animation_delay:
                self.sprite_index = (self.sprite_index + 1) % SPRITE_CELLS
                self.animation_timer = 0


class Enemies:
    """Enemies."""

    def __init__(self, enemy_locations, goal_top, goal_bottom):
        """Initialize Enemies.

        Args:
            enemy_locations((int, (int, int))): Enemy ID at X, Y location.
            goal_top(int): Top boundary of player 2 goal.
            goal_bottom(int): Bottom boundary of player 1 goal.
        """
        self.goal_top = goal_top
        self.goal_bottom = goal_bottom
        self.enemies = sprite.Group()

        for enemy_id, coords in enemy_locations:
            self.enemies.add(Enemy(enemy_id, coords))

    def check_collision_ball(self, ball):
        """Check for enemy collision with ball.

        Args:
            ball(pygame.Rect): Rectangle encompassing ball.
        """
        for enemy in self.enemies:
            if enemy.exploding:
                continue
            if enemy.rect.colliderect(ball):
                intersection = enemy.rect.clip(ball)
                if intersection.width > intersection.height + 1:
                    # Enemy hit on top or bottom:  Reverse Y
                    new_direction = (False, True)
                elif intersection.width < intersection.height + 1:
                    # Enemy hit on sides:  Reverse X
                    new_direction = (True, False)
                else:
                    # Enemy corner strike:  Reverse both directions
                    new_direction = (True, True)
                enemy.exploding = True
                return new_direction
        return None

    def check_collision_bricks(self, bricks):
        """Check for enemy collision with paddles.

        Args:
            bricks([pygame.SpriteGroup]): SpriteGroup of bricks
        """
        for enemy in self.enemies:
            if enemy.exploding:
                continue
            hit_bricks = sprite.spritecollide(enemy, bricks, False)
            if hit_bricks:
                enemy.bounce([hit_brick.rect for hit_brick in hit_bricks])

    def check_collision_other_enemies(self):
        """Check for enemy collision between each other."""
        colliding = []
        for enemy in self.enemies:
            if enemy in colliding:
                continue
            if enemy.exploding:
                continue
            enemies_to_check = [e for e in self.enemies if e != enemy]
            for enemy2 in enemies_to_check:
                if enemy.rect.colliderect(enemy2.rect):
                    colliding.extend([enemy, enemy2])
                    enemy.direction, enemy2.direction = \
                        enemy2.direction, enemy.direction
                    break

    def check_collision_paddles(self, paddle_rects):
        """Check for enemy collision with paddles.

        Args:
            paddle_rects([pygame.Rect]): Rectangles encompassing paddles.
        """
        for enemy in self.enemies:
            if enemy.exploding:
                continue
            if enemy.rect.colliderect(paddle_rects[0]):
                # Player 1 killed enemy.
                enemy.exploding = True
                return 0
            if enemy.rect.colliderect(paddle_rects[1]):
                # Player 2 killed enemy.
                enemy.exploding = True
                return 1
        return None

    def clear(self):
        """Clear all enemies."""
        self.enemies.empty()

    def draw(self, screen):
        """Draw enemies.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        self.enemies.draw(screen)

    def update(self, clock):
        """Update enemy position.

        Args:
            clock(pygame.time.Clock): Game clock
        """
        self.check_collision_other_enemies()
        for enemy in self.enemies:
            # Reverse direction if enemy in goal
            if enemy.direction.y == 1 and enemy.rect.bottom > self.goal_bottom:
                enemy.direction.y = -1
            elif enemy.direction.y == -1 and enemy.rect.top < self.goal_top:
                enemy.direction.y = 1
            # Update enemy
            if enemy.exploding and enemy.exploding_index >= EXPLODE_CELLS:
                self.enemies.remove(enemy)
            else:
                enemy.update(clock)
