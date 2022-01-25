__version__ = "0.3"

from random import choice

import pygame


class Game:
    """The game class."""

    def __init__(self, width, height, game_rect=(0, 0, 640, 480 )):
        # Init the display
        self.width, self.height = width, height
        self.game_rect = game_rect
        self.screen = pygame.display.set_mode((1000, 520))
        pygame.display.set_caption('Pygame Slide Puzzle')
        # Creates the level selector
        self.level_selector = LevelSelector(on_select=self.start)
        # Marks the game as running, but level was not selected yet
        self.running = True
        self.started = False

    def start(self, image_path):
        """Starts the game, loads and shuffles the image."""
        self.started = True

    def update(self):
        """Processes input events and updates the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type != pygame.KEYDOWN:
                continue
            # Pass the control to the level selector if game is not started
            if not self.started:
                self.level_selector.update(event)
            else:
                self.puzzle.update(event)

    def draw(self):
        """Draws either the level selector or the game puzzle."""
        surface = self.screen
        if not self.started:
            self.level_selector.draw(surface)
        else:
            self.puzzle.draw(surface)

    def game_loop(self):
        """Performs the game loop: process input, update screen etc."""
        clock = pygame.time.Clock()
        while self.running:
            elapsed = clock.tick(30)
            self.screen.fill((0, 0, 0))
            self.update()
            self.draw()
            pygame.display.update()
        pygame.quit()


class LevelSelector:
    """The level selector scene."""

    IMAGES = [
        "puzzles/deepelf.png",
        "puzzles/demilich.png",
        "puzzles/dragonwhelp.png",
    ]

    # IMAGES_2 = [
    #     "puzzles/deepelf.png",
    #     "puzzles/demilich.png",
    #     "puzzles/dragonwhelp.png",
    # ]
    
    # IMAGES_3 = [
    #     "puzzles/deepelf.png",
    #     "puzzles/demilich.png",
    #     "puzzles/dragonwhelp.png",
    # ]
    def __init__(self, on_select):
        self.on_select = on_select # Callback to start the game
        self._level = 0
        self._images = []
        for image in self.IMAGES:
            self._images.append(load_answer_image(image, image_size=(220, 220)))
        self._select = pygame.image.load("select.png").convert_alpha()

    def prev(self):
        """Slide to the previous image."""
        if self._level > 0:
            self._level -= 1

    def next(self):
        """Slide to the next image."""
        if self._level < len(self._images) - 1:
            self._level += 1

    def _current_answer(self):
        """Returns the image for the current level."""
        return self._images[self._level]

    def _prev_answer(self):
        """Returns the image for the previous level (if exists)."""
        if self._level > 0:
            return self._images[self._level - 1]

    def _next_answer(self):
        """Returns the image for the next answer (if exists)."""
        if self._level < len(self._images) - 1:
            return self._images[self._level + 1]

    def update(self, event):
        """Processes user's input."""
        if event.type != pygame.KEYDOWN:
            return
        elif event.key == pygame.K_LEFT:
            self.prev()
        elif event.key == pygame.K_RIGHT:
            self.next()
        elif event.key == pygame.K_RETURN:
            if self._level == 0:
                print("good")
            else:
                print("bad")

    def draw(self, surface):
        """Draws current state."""
        pos = ((-180, 90), (90, 104), (360, 90))
        levels = (self._prev_answer(),
                  self._current_answer(),
                  self._next_answer())
        # Draws the images at the predefined positions
        for level, p in zip(levels, pos):
            if level is not None:
                surface.blit(level, p)
        # Draws a white border around the current image and the `select puzzle` image
        pygame.draw.rect(surface, (255, 255, 255), (80  , 94, 240, 240), 3)
        surface.blit(self._select, (127, 40))



# def make_puzzle(image_path, board_rect):
#     """Creates the game puzzle"""
#     x, y, width, height = board_rect
#     puzzle_image = load_puzzle_image(image_path,
#                                      image_size=(width, height))
#     image_pieces = list(make_subsurfaces(puzzle_image,
#                                          offset=(x, y)))
#     # Create the puzzle, leaving out the last piece of the image.
#     return Puzzle(x, y, image_pieces[:-1])


def load_answer_image(path, image_size):
    """Loads the answer image. The image is scaled to the `image_size` param."""
    surface = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(surface, image_size)


# def make_subsurfaces():
#     pass


if __name__ == '__main__':
    game = Game(
        width=640,
        height=440,
        game_rect=(36, 50, 328, 328)
    )
    game.game_loop()
