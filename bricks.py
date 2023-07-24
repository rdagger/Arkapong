"""Bricks."""
from levels import get_dimensions, get_level, max_levels
from levels import BRICK_WIDTH, BRICK_HEIGHT
from pygame import image, Rect, sprite

BRICK_SPRITES = "images/Bricks.png"
COLORS = ['W', 'R', 'B', 'O', 'C', 'G', 'Y', 'M', 'S', 'S2', 'A']

DESTROYED = 1
DAMAGED = 2
UNDAMAGED = 3


class Brick(sprite.Sprite):
    def __init__(self, color, coords, spritesheet):
        """Brick sprite constuctor.

        Args:
            color(string): Letter representing color.
            coors((int, int)): X, Y coordinates of brick.
            spritesheet(pygame.image): Spritesheet of bricks.
        """
        super().__init__()
        self.color = color
        self.coords = coords
        self.spritesheet = spritesheet
        self.required_hits = 2 if color == "S" else 1
        self.impervious = True if color == "A" else False
        self.load_brick()

    def hit(self):
        """Handle ball impact with brick."""
        if self.impervious:
            return UNDAMAGED  # Brick unbreakable
        self.required_hits -= 1
        if not self.required_hits:
            return DESTROYED  # Brick destroyed
        else:
            # Partial brick damage
            self.color = "S2"
            self.load_brick()
            return DAMAGED

    def load_brick(self):
        """Load brick sprite."""
        # Define the sprite's position and dimensions within the spritesheet
        rect = Rect(0, COLORS.index(self.color) * BRICK_HEIGHT, BRICK_WIDTH,
                    BRICK_HEIGHT)

        # Create surface for the individual sprite and copy the sprite's image
        sprite_surface = self.spritesheet.subsurface(rect).convert_alpha()

        # Create a sprite object and assign the surface and rect attributes
        self.image = sprite_surface
        self.rect = sprite_surface.get_rect()
        self.rect.topleft = self.coords


class Bricks:
    """Bricks."""

    def __init__(self, wall_left, wall_right, centery):
        """Initialize bricks.

        Args:
            wall_left(int): X coordinate of left wall.
            wall_right(int): X coordinate of right wall.
            centery(int): Y coordinate of screen center.
        """
        self.wall_left = wall_left
        self.wall_right = wall_right
        self.centery = centery
        self.playfield_width = wall_right - wall_left
        self.spritesheet = image.load(BRICK_SPRITES).convert_alpha()
        self.bricks = sprite.Group()
        self.level = 1
        self.impervious_bricks = 0

    def build(self):
        """Build brick shapes."""
        enemies = []
        self.impervious_bricks = 0
        self.bricks.empty()
        shapes = get_level(self.level)
        shape_count = len(shapes)
        shapes_dim = get_dimensions(self.level)
        total_width = sum(w for w, _ in shapes_dim)
        free_width = self.playfield_width - total_width
        buffer = free_width // (shape_count + 1)
        start_x = self.wall_left + buffer
        for index, shape in enumerate(shapes):
            height = shapes_dim[index][1]
            y = self.centery - height // 2
            for row in shape:
                x = start_x
                for cell in row:
                    if cell.isnumeric():
                        # Enemy
                        enemies.append((int(cell), (x, y)))
                    elif cell != ".":
                        if cell == "A":
                            self.impervious_bricks += 1
                        self.bricks.add(Brick(cell, (x, y), self.spritesheet))
                    x += BRICK_WIDTH
                y += BRICK_HEIGHT
            x += buffer
            start_x = x
        return enemies

    def brick_count(self):
        """Return number of breakable bricks left on the screen."""
        return len(self.bricks) - self.impervious_bricks

    def check_hit(self, ball_rect):
        """Check if ball hit a brick.

        Args:
            ball_rect(pygame.Rect): Rectangle encompassing ball.
        """
        hit_bricks = []
        results = []
        for brick in self.bricks:
            if brick.rect.colliderect(ball_rect):
                result = brick.hit()
                results.append(result)
                hit_bricks.append(brick.rect)
                if result == DESTROYED:
                    self.bricks.remove(brick)
        return results, hit_bricks

    def draw(self,  screen):
        """Draw the bricks.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        self.bricks.draw(screen)

    def increment_level(self):
        """Draw the bricks.

        Args:
            screen(pygame.Surface): Graphical window to display graphics.
        """
        self.level += 1
        if self.level > max_levels():  # Check for maximum level
            self.level = 1  # Loop back to level 1
