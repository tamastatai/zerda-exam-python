# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################

class Rocket():
    def __init__(self, rocket_type, starting_fuel_level, number_of_launches):
        self.type = rocket_type
        self.fuel = starting_fuel_level
        self.launches = number_of_launches

    def launch(self):
        if self.type == "falcon1":
            self.fuel -= 1
            self.launches += 1

        elif self.type == "falcon9":
            self.fuel -= 9
            self.launches += 1

    def refill(self):
        if self.type == "falcon1":
            used_fuel = 5 - self.fuel
            self.fuel = 5

        elif self.type == "falcon9":
            used_fuel = 20 - self.fuel
            self.fuel = 20
        return used_fuel

    def getStats(self):
        return("name: " + self.type + "", " + 'fuel: " + str(self.fuel))


falcon1 = Rocket('falcon1', 4, 1)
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
