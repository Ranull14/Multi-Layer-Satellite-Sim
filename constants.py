#
#   PROJECT : Satellite Network Simulation
#
#   FILENAME : constants.py
#
#   DESCRIPTION :
#       Simulate a network of satellite nodes to compare performance
#       compared to regular ground nodes.
#
#
#   NOTES :
#       - ...
#
#   AUTHOR(S) : Noah Arcand Da Silva    START DATE : 2022.11.26 (YYYY.MM.DD)
#
#   CHANGES :
#       - ...
#
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.11.26  Noah            Creation of project.
#   0.0.2a      2023.01.09  Noah            Basic simulation of LEO satellite constellation.
#   0.0.2b      2023.01.19  Noah            Advanced simulation of LEO satellite constellation.
#   0.0.2c      2023.01.21  Noah/Ranul      Added distortion to LEO satellite orbit to better represent Mercator Projection.
#   0.1.0       2023.01.22  Noah            Added path from ground station to nearest satellite and shortest path algorithm.
#   0.1.1a      2023.01.22  Noah            Allows to run multiple endpoint pairs at once (not recommended).
#   0.1.1b      2023.02.04  Ranul           Fine tuning the satellite speed equation for more accurate and precise travel time.
#

from math import cos, acos, sin


# Window size
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
SCALE = 5
FPS = 30
SIMULATION_SPEED_MULTIPLIER = 1

# PyGame colours
WHITE = (255, 255, 255)
ORANGE = (247, 127, 0)
RED = (247, 37, 133)
YELLOW = (255, 214, 112)
GREEN = (66, 171, 52)

# Astronomy
GRAVITATIONAL_CONSTANT = 6.67428e-11    # Nm^2 / kg^2
EARTH_MASS = 5.9722 * 10**24    # kg
EARTH_RADIUS = 6.3781 * 10**6   # m
EARTH_MESOSPHERE = 85   # km

# Starlink v2.0
ORBIT_HEIGHT = 550
TIME_TO_COMPLETE_ORBIT = 60    # minutes (seconds for simulation)
SATELLITE_MASS = 1250

# Sin wave data
# Ensures a constellation that will never loop on itself. (frequency = 0.0007222222222222223)
FREQUENCY = 1 / (WINDOW_WIDTH / (1.3))
AMPLITUDE = WINDOW_HEIGHT / 2 - WINDOW_WIDTH / 10
SATELLITE_SPEED = cos(WINDOW_WIDTH) * (WINDOW_WIDTH) / \
    TIME_TO_COMPLETE_ORBIT
MAX_SATELLITE_COUNT = 600
