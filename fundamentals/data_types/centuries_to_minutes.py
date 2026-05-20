import math as m

centuries = int(input())

years = (centuries * 100)
days = m.floor(years * 365.2422)
hours = m.floor(days * 24)
minutes = (m.floor(hours) * 60)

print(f'{centuries} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes')