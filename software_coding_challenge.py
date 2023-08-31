class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        distance_to_earth = abs(self.distance_from_sun - 147_000_000)  # Assuming 147 million km as Earth-Sun distance
        return {'distance to earth': distance_to_earth}

# Example usage
planet_mars = Planet('Mars', 225_000_000, 'Terrestrial')
distance_info = planet_mars.get_distance_to_earth()
print(f"{planet_mars.name} is {distance_info['distance to earth']:,} kilometers away from Earth.")


class Mercury(Planet):
    def __init__(self, distance_from_sun, planet_type):
        super().__init__('Mercury', distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        mercury_year_in_earth_days = 88
        print(
            f"Happy New Year on Mercury! A year on Mercury lasts approximately {mercury_year_in_earth_days} Earth days.")


# Creating an instance of the Mercury class
mercury_properties = {
    'distance_from_sun': 58_000_000,
    'planet_type': 'Terrestrial'
}
mercury = Mercury(**mercury_properties)

# Printing attributes and calling methods
print(f"Name: {mercury.name}")
print(f"Distance from Sun: {mercury.distance_from_sun} km")
print(f"Planet Type: {mercury.planet_type}")
distance_info = mercury.get_distance_to_earth()
print(f"Distance to Earth: {distance_info['distance to earth']:,} km")
Mercury.happy_new_year()


class Jupiter(Planet):
    def __init__(self, distance_from_sun, planet_type, number_of_moons):
        super().__init__('Jupiter', distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        jupiter_year_in_earth_days = 4383
        print(
            f"Happy New Year on Jupiter! A year on Jupiter lasts approximately {jupiter_year_in_earth_days} Earth days.")


# Creating an instance of the Jupiter class
jupiter_properties = {
    'distance_from_sun': 779_000_000,
    'planet_type': 'Gas Giant',
    'number_of_moons': 80
}
jupiter = Jupiter(**jupiter_properties)

# Printing attributes and calling methods
print(f"Name: {jupiter.name}")
print(f"Distance from Sun: {jupiter.distance_from_sun} km")
print(f"Planet Type: {jupiter.planet_type}")
print(f"Number of Moons: {jupiter.number_of_moons}")
distance_info = jupiter.get_distance_to_earth()
print(f"Distance to Earth: {distance_info['distance to earth']:,} km")
Jupiter.happy_new_year()
