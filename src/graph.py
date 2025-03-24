
import matplotlib.pyplot as plt
import numpy as np

"""
    Graph class is the class that models
    the graph of the displacement and velocity
    of the pendulum.
    It has methods to update the graph and clear it.
"""

class Graph:

    def __init__(self, pendulum):
        # Initialize figure and subplots
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(8, 6))

        self.fig.subplots_adjust(hspace=0.4)

        # Data storage
        self.time = []
        self.displacement = []
        self.linear_velocity = []
        self.runtime = float("inf")
        self.pendulum = pendulum

        # Initialize plot lines
        self.line1, = self.ax1.plot([], [], label="Displacement", color="blue")
        self.line2, = self.ax2.plot([], [], label="Velocity", color="red")

        # Add equilibrium lines
        self.ax1.axhline(0, color="black", linestyle="--", linewidth=1)
        self.ax2.axhline(0, color="black", linestyle="--", linewidth=1)

        # Set titles and labels
        self.ax1.set_title("Displacement Function")
        self.ax2.set_title("Velocity Function")
        self.ax1.legend()
        self.ax2.legend()

        # Enable interactive mode
        plt.ion()
        plt.show()

    """
        Set the runtime of the graph
        @param runtime: the runtime of the graph
    """
    def set_runtime(self, runtime):
        self.runtime = runtime

    """
        Check if the graph is finished
        @return: True if the graph is finished, False otherwise
    """
    def is_finished(self):
        if self.pendulum.time > self.runtime:
            return True
        return False

    """
        Clear the graph and reset the data
    """
    def clear(self):
        self.time.clear()
        self.displacement.clear()
        self.linear_velocity.clear()

        # Reset the plot lines
        self.line1.set_data([], [])
        self.line2.set_data([], [])

        # Reset x-axis range
        self.ax1.set_xlim(0, 1)
        self.ax2.set_xlim(0, 1)

        # Redraw the plots
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    """
        Update the graph with the new data
    """
    def update(self):
        if not self.pendulum.is_ready():
            return
        
        self.time.append(self.pendulum.time)
        self.displacement.append(self.pendulum.angle * self.pendulum.length)
        self.linear_velocity.append(self.pendulum.w * self.pendulum.length)

        self.d_padding = max(self.displacement) * 0.1
        self.v_padding = max(self.linear_velocity) * 0.1

        self.ax1.set_ylim(min(self.displacement) - self.d_padding, max(self.displacement) + self.d_padding)
        self.ax2.set_ylim(min(self.linear_velocity) - self.v_padding, max(self.linear_velocity) + self.v_padding)

        # Update the line data
        self.line1.set_data(self.time, self.displacement)
        self.line2.set_data(self.time, self.linear_velocity)

        # Adjust x-axis dynamically
        self.ax1.set_xlim(0, max(self.time) + 1)
        self.ax2.set_xlim(0, max(self.time) + 1)

        # Redraw the plots
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()