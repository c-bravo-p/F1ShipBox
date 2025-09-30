import fastf1 
from fastf1 import plotting
import matplotlib.pyplot as plt
import os

cache_dir = ".cache"

os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(cache_dir)

session = fastf1.get_session(2023, "Monaco", "Q")
session.load()

leclerc = session.laps.pick_driver("LEC")

best_lap = leclerc.pick_fastest()
print(f"Best lap time: {best_lap["LapTime"]}")

telemetry = best_lap.get_telemetry()

plt.figure(figsize=(10,4))
plt.plot(telemetry['Distance'], telemetry['Speed'], label='LEC')
plt.xlabel('Distancia en pista [m]')
plt.ylabel('Velocidad [km/h]')
plt.title('Velocidad vs Distancia – LEC')
plt.legend()
plt.grid(True)
plt.show()