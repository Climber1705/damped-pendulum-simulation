
import pygame
import numpy as np

from pendulum import Pendulum
from view import Window
from graph import Graph

"""
    Controller class is the main class that controls the flow of the program.
    It initializes the pendulum, graph and window objects and runs the main loop.
    The main loop checks for events updates the pendulum and graph objects and
    updates the display.
"""

class Controller:

    WIDTH, HEIGHT = 600, 700
    FPS = 60
    PIVOT = np.array([WIDTH//2, HEIGHT//6])
    TRANSFORM_FRAME = np.array([[1, 0], [0, -1]])

    def __init__(self):
        self.pendulum = Pendulum(self, self.FPS, self.PIVOT)
        self.graph = Graph(self.pendulum)
        self.view = Window(self.WIDTH, self.HEIGHT, self.pendulum.RADIUS)
        self.clock = pygame.time.Clock()
    
    """
        Get the current mouse position.
        @return: the current mouse position as a numpy array.
    """
    def get_mouse_pos(self) -> np.array:
        return np.array(pygame.mouse.get_pos())
    
    """
        The main loop of the program.
    """
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.pendulum.clear()
                    self.graph.clear()
                    self.pendulum.set_position()
                    self.graph.set_runtime(self.pendulum.time_period)

            if self.pendulum.is_ready() and not self.graph.is_finished():
                self.view.draw(self.pendulum.position, self.pendulum.PIVOT)
                self.pendulum.update()
                self.graph.update()
            else:
                self.view.draw(self.get_mouse_pos(), self.PIVOT)
           
            self.clock.tick(self.FPS)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    controller = Controller()
    controller.run()
