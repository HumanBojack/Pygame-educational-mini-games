__version__ = "0.3"


import pygame


class Game:
    """The game class."""

    def __init__(self, width, height, game_rect=(0, 0, 640, 480 )):
        # Init the display
        self.width, self.height = width, height
        self.game_rect = game_rect
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Sofiane Game')
        # Creates the answer selector
        self.answer_selector = AnswerSelector(on_select=self.start)
        # Marks the game as running, but answer was not selected yet
        self.running = True
        self.started = False

    def start(self):
        """Starts the game"""
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
                self.answer_selector.update(event)
            else:
                self.puzzle.update(event)

    def draw(self):
        """Draws either the level selector or the game puzzle."""
        surface = self.screen
        if not self.started:
            self.answer_selector.draw(surface)
        else:
            self.puzzle.draw(surface)

    def game_loop(self):
        """Performs the game loop: process input, update screen etc."""
        clock = pygame.time.Clock()
        while self.running:
            self.screen.fill((0, 0, 0))
            self.update()
            self.draw()
            pygame.display.update()
        pygame.quit()


class AnswerSelector:
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
        self._answer = 0
        self._images = []
        for image in self.IMAGES:
            self._images.append(load_answer_image(image, image_size=(220, 220)))
        self._select = pygame.image.load("select.png").convert_alpha()

    def prev(self):
        """Slide to the previous image."""
        if self._answer > 0:
            self._answer -= 1

    def next(self):
        """Slide to the next image."""
        if self._answer < len(self._images) - 1:
            self._answer += 1

    def _current_answer(self):
        """Returns the image for the current level."""
        return self._images[self._answer]

    def _prev_answer(self):
        """Returns the image for the previous level (if exists)."""
        if self._answer > 0:
            return self._images[self._answer - 1]

    def _next_answer(self):
        """Returns the image for the next answer (if exists)."""
        if self._answer < len(self._images) - 1:
            return self._images[self._answer + 1]

    def update(self, event):
        """Processes user's input."""
        if event.type != pygame.KEYDOWN:
            return
        elif event.key == pygame.K_LEFT:
            self.prev()
        elif event.key == pygame.K_RIGHT:
            self.next()
        elif event.key == pygame.K_RETURN:
            if self._answer== 0:
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
        # Draws a white border around the current image and the `select answer` image
        pygame.draw.rect(surface, (255, 255, 255), (80  , 94, 240, 240), 3)
        surface.blit(self._select, (127, 40))



def load_answer_image(path, image_size):
    """Loads the answer image. The image is scaled to the `image_size` param."""
    surface = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(surface, image_size)



if __name__ == '__main__':
    game = Game(
        width=640,
        height=440,
        game_rect=(36, 50, 328, 328)
    )
    game.game_loop()
