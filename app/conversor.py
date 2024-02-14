class Conversor:

    def celsius_fahrenheit(self, temp):
        result = temp * (9 / 5) + 32
        print(round(result, 2))

    def celsius_kelvin(self, temp):
        result = temp + 273.15
        print(round(result, 2))

    def fahrenheit_celsius(self, temp):
        result = (temp - 32) * (5 / 9)
        print(round(result, 2))

    def fahrenheit_kelvin(self, temp):
        result = (temp - 32) * (5 / 9) + 273.15
        print(round(result, 2))

    def kelvin_celsius(self, temp):
        result = temp - 273.15
        print(round(result, 2))

    def kelvin_fahrenheit(self, temp):
        result = (temp - 273.15) * (9 / 5) + 32
        print(round(result, 2))
