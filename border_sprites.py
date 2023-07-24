"""Border sprites."""
from pygame import image, sprite

CONNECTOR = 'images/Border_Connector_Vertical_22x89.png'
PIPE = 'images/Border_Pipe_Vertical_18x89.png'
PIPE_HT = 'images/Border_Pipe_Horiz_Top__218x18.png'
PIPE_HB = 'images/Border_Pipe_Horiz_Bottom__218x18.png'
CORNER_TL = 'images/Corner_Top_Left_21x25.png'
CORNER_TR = 'images/Corner_Top_Right_21x25.png'
CORNER_BL = 'images/Corner_Bottom_Left_21x25.png'
CORNER_BR = 'images/Corner_Bottom_Right_21x25.png'


class BorderSprite(sprite.Sprite):
    """Create class for border parts."""

    def __init__(self, path, position, anchor='center'):
        """Border sprite constructor.

        Args:
            path(string): Sprite image path (see constants above)
            position((int, int)): X, Y coordinates.
            anchor(string): Positioning anchor, default='center' (see notes)

        Notes:
            Valid anchor strings: x, y, left, right, top, bottom, centerx,
            centery, center, topleft, bottomleft, topright, bottomright,
            midleft, midright, midtop, midbottom.

        """
        super().__init__()
        self.image = image.load(path)
        self.rect = self.image.get_rect(**{anchor: position})
