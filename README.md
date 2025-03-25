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

## Repository Structure
```graphql
damped-pendulum-simulation/
│
├── src/
│   ├── control.py        # Entry point to run the simulation
│   ├── graph.py          # Handles plotting of pendulum motion and energy graphs
│   ├── pendulum.py       # Defines the pendulum class and equations of motion
│   └── view.py           # Handles visualization and animation of the pendulum
│
├── requirements.txt      # List of Python dependencies
├── README.md             # Project documentation
└── LICENSE               # Project license (GNU)
```

## Derivation: Stopping Time of a Damped Pendulum

A damped pendulum experiences resistive forces (e.g., air resistance or friction at the pivot), causing its oscillations to decay over time. The equation of motion for a simple damped pendulum is:
```math
\frac{d^2\theta}{dt^2} + 2\beta \frac{d\theta}{dt} + \frac{g}{L} \sin\theta = 0
```

where:
- $$\(\theta\)$$ is the angular displacement,
- $$\(g\)$$ is the acceleration due to gravity,
- $$\(L\)$$ is the length of the pendulum,
- $$\(\beta = \frac{b}{2m}\)$$ is the damping coefficient, with \(b\) being the damping force per unit velocity and \(m\) the pendulum's mass.

### Approximation for Small Angles and Overdamped Regime

For small angles $$(\(\sin\theta \approx \theta\))$$, the equation simplifies to:

```
\frac{d^2\theta}{dt^2} + 2\beta \frac{d\theta}{dt} + \omega_0^2 \theta = 0
```
where ```\(\omega_0 = \sqrt{g/L}\)``` is the natural frequency.

The general solution for a weakly damped $$(\(\beta < \omega_0\))$$ system is:

```math
\theta(t) = \theta_0 e^{-\beta t} \cos(\omega_d t + \phi)
```

where $$\(\omega_d = \sqrt{\omega_0^2 - \beta^2}\)$$ is the damped frequency.

The pendulum is considered to have "stopped" when its amplitude falls below a small threshold $$\(\theta_{min}\)$$, typically close to zero.

### Stopping Time Estimation

Setting $$\(\theta(t_{stop}) = \theta_{min}\)$$, we solve:

```math
\theta_{min} = \theta_0 e^{-\beta t_{stop}}
```
Taking the natural logarithm:

```math
t_{stop} = \frac{1}{\beta} \ln\left(\frac{\theta_0}{\theta_{min}}\right)
```
This formula estimates the time required for the pendulum to effectively come to rest under damping.

## Improvements
Future enhancements could include:
- Implementing additional numerical solvers for comparison.
- Adding a graphical user interface (GUI) for interactive parameter adjustments.
- Extending the simulation to model-driven pendulums or coupled pendulum systems.

## Help and Resources
For further reading on damped pendulum dynamics and simulations:
- [Pendulum (mechanics) – Wikipedia](https://en.wikipedia.org/wiki/Pendulum_(mechanics))
- [Stopping time of a damped pendulum - Physics Stack Exchange](https://physics.stackexchange.com/questions/621912/stopping-time-of-a-damped-pendulum)
- [Damped Oscillations - Physics LibreTexts](https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_%28OpenStax%29/Book%3A_University_Physics_I_-_Mechanics_Sound_Oscillations_and_Waves_%28OpenStax%29/15%3A_Oscillations/15.06%3A_Damped_Oscillations)

## License
This project operates under the GNU General Public License v3.0. The [LICENSE](https://choosealicense.com/licenses/gpl-3.0/) file provides details.
