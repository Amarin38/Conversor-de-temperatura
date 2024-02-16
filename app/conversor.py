class Conversor:

    def celsius_fahrenheit(self, temp):
        return temp * (9 / 5) + 32

    def celsius_kelvin(self, temp):
        return temp + 273.15

    def fahrenheit_celsius(self, temp):
        return (temp - 32) * (5 / 9)

    def fahrenheit_kelvin(self, temp):
        return (temp - 32) * (5 / 9) + 273.15

    def kelvin_celsius(self, temp):
        return temp - 273.15

    def kelvin_fahrenheit(self, temp):
        return (temp - 273.15) * (9 / 5) + 32
