def celsiusToFarenheit(temperature):
  return temperature * (9 / 5) + 32

def farenheitToCelsius(temperature):
  return (temperature - 32) * (5 / 9)


print(f'32 C = {celsiusToFarenheit(32)} F')
print(f'32 F = {farenheitToCelsius(32)} C')