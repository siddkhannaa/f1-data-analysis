import fastf1 as ff1
import fastf1.plotting

from matplotlib import pyplot as plt

ff1.plotting.setup_mpl()

session = ff1.get_session(2023, 'Italy', 'Q')

session.load()

fastLeClerc = session.laps.pick_driver('LEC').pick_fastest()
lecCarData = fastLeClerc.get_car_data()
t = lecCarData['Time']
vCar = lecCarData['Speed']

# rest is plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('LeClerc is')
ax.legend()
plt.show()