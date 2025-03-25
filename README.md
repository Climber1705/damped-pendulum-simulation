# Damped Pendulum Simulation
## Overview
This repository offers a simulation of a damped pendulum, modelling its motion under the influence of gravity and damping forces. The simulation numerically solves the governing differential equations and visualises the pendulum's behaviour over time.

## Features
- **Numerical Solver:** Implements numerical methods to solve the equations of motion for the damped pendulum.
- **Visualisation:** This animation of the pendulum's motion plots key parameters such as displacement and linear velocity over time.
 - **Parameter Customization:** Users can adjust physical parameters like pendulum length, damping coefficient, and initial conditions.

## Installation
1. **Clone the Repository:**
```bash
   git clone https://github.com/Climber1705/damped-pendulum-simulation.git
   cd damped-pendulum-simulation
```
2. **Install Dependencies:**
Ensure you have Python installed. Install the required packages using the following:
```bash
   pip install -r requirements.txt
```

## Usage
To run the simulation:
```bash
python src/control.py
```
This command initialises the simulation with default parameters. To customise the parameters, modify the src/control.py file before execution.
Repository Structure


## Improvements
Future enhancements could include:
- Implementing additional numerical solvers for comparison.
- Adding a graphical user interface (GUI) for interactive parameter adjustments.
- Extending the simulation to model-driven pendulums or coupled pendulum systems.

## Resources
For further reading on damped pendulum dynamics and simulations:
- [Pendulum (mechanics) – Wikipedia](https://en.wikipedia.org/wiki/Pendulum_(mechanics))

## License
This project is licensed under the GNU General Public License v3.0. The [LICENSE]() file provides more details.
