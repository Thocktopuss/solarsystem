# simulation.py
from solar_system import SolarSystem
from sun import Sun
from planet import Planet
import turtle

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.__solar_system = solar_system
        self.__width = width
        self.__height = height
        self.__num_periods = num_periods
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = self.__width, height = self.__height)
        self.__screen.bgcolor("black")
        self.__t.clear()

    def run(self):
        self.__solar_system.show_planets()
        for a_move in range(self.__num_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()
    def freeze(self):
        self.__screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 1000000, 5800,0,0)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 100, 30, 75.0, 200.0, 50, 20, "green")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, 100, 20, 70.0, 125.0, 50,20, "red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 40000)
    simulation.run()





#     def add_sun(self, sun: Sun):
#         """
#         Adds a sun to the simulation's solar system.
#
#         Args:
#             sun (Sun): The Sun object to add.
#         """
#         self._solar_system.add_sun(sun)
#
#     def add_planet(self, planet: Planet):
#         """
#         Adds a planet to the simulation's solar system.
#
#         Args:
#             planet (Planet): The Planet object to add.
#         """
#         self._solar_system.add_planet(planet)
#
#     def run(self, time_step: float = 86400):  # 1 day in seconds as default time step
#         """
#         Runs the simulation for the specified number of periods.
#
#         Args:
#             time_step (float): The time interval for each simulation step (in seconds).
#         """
#         print("Starting simulation...")
#         for period in range(self._num_periods):
#             print(f"--- Period {period + 1} ---")
#             if self._solar_system._the_sun:
#                 print(self._solar_system._the_sun)
#             self._solar_system.show_planets()
#             self._solar_system.move_planets(time_step)
#         print("Simulation finished.")
#
# if __name__ == "__main__":
#     # Example usage (assuming the above files are in the same directory):
#     sun = Sun(name="Sol", radius=6.95e8, mass=1.989e30, temp=5778, x=0, y=0)
#     earth = Planet(name="Earth", radius=6.371e6, mass=5.972e24, distance=1.496e11, x=1.496e11, y=0, vel_x=0, vel_y=29783)
#     mars = Planet(name="Mars", radius=3.389e6, mass=6.39e23, distance=2.279e11, x=0, y=2.279e11, vel_x=-24077, vel_y=0)
#
#     simulation = Simulation(width=800, height=600, num_periods=10)
#     simulation.add_sun(sun)
#     simulation.add_planet(earth)
#     simulation.add_planet(mars)
#     simulation.run(time_step=86400 * 30) # Run for 10 periods, with a time step of 30 days