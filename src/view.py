
import pygame

"""
    The window class is responsible for creating the window and drawing the pendulum.
    It has a method for drawing the pendulum.
    The drawing method involves drawing the pendulum on the window.
"""
class Window:

    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    GREY = pygame.Color("Grey")
    
    def __init__(self,WIDTH, HEIGHT, radius):    
        pygame.display.set_caption("Damping Pendulum")
        self.RES = self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.radius = radius
        self.screen = pygame.display.set_mode(self.RES)

    """
        Draw the pendulum on the window.
        @param position: the position of the pendulum.
        @param pivot: the pivot of the pendulum.
    """
    def draw(self, position, pivot) -> None:
        self.screen.fill(self.BLACK)
        pygame.draw.line(self.screen, self.WHITE, pivot, position, 2)
        pygame.draw.circle(self.screen, self.BLACK, pivot, 5)
        pygame.draw.circle(self.screen, self.WHITE, position, self.radius)
