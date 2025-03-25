
import numpy as np

"""
    The pendulum class is the class that models the pendulum.
    It calculates the position of the pendulum at each time step.
    It also calculates the angle of the pendulum at each time step.
    It also calculates the time period of the pendulum.
"""

class Pendulum:

    g = 9.80665
    DAMPING_COEFFICIENT = 0.15
    RADIUS = 20
    MASS = 1
    STOPPING_TOLERANCE = 0.01

    def __init__(self, control, FPS, pivot):
        self.control = control
        self.dt = FPS / 1000
        self.PIVOT = pivot
        self.clear()

    """
        Clear the pendulum's attributes.
    """
    def clear(self) -> None:
        self.time = 0
        self.w = 0
        self.orientation = None
        self.angle = None
        self.position = None
    
    """
        Check if the pendulum is ready to be used.
        @return: True if the pendulum is ready, False otherwise.
    """
    def is_ready(self) -> bool:
        return self.orientation is not None

    """
        Set the position of the pendulum.
    """
    def set_position(self) -> None:
        self.position = self.control.get_mouse_pos()
        self.orientation = np.matmul(self.control.TRANSFORM_FRAME, self.position - self.PIVOT)
        self.length = np.linalg.norm(self.orientation)
        self.angle = np.arccos(np.dot(self.orientation, np.array([0, -1])) / self.length)
        if self.orientation[0] < 0:
            self.angle = -self.angle
        self.time_period = (1/self.DAMPING_COEFFICIENT) * np.log(self.angle / self.STOPPING_TOLERANCE)
        print(self.time_period)
            
    """
        Update the pendulum's position and angle.
    """
    def update(self) -> None:
        if not self.is_ready():
            return
        self.time += self.dt
        deltaw = -self.g/self.length * np.sin(self.angle) - (self.DAMPING_COEFFICIENT * self.w)
        self.w += deltaw * self.dt
        self.angle += self.w
        self.orientation = np.array([self.length * np.sin(self.angle), self.length * -np.cos(self.angle)])
        self.position = np.matmul(self.control.TRANSFORM_FRAME, self.orientation) + self.PIVOT
