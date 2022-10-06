from lib2to3.pgen2.token import PERCENT
import psutil
battery = psutil.sensors_battery()
percent = str(battery.percent)
print(f'No momento você tem {percent} % de bateria!')
