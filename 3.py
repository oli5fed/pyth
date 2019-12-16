import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
from math import pi



cat = ['Соя', 'Хлопчатник', 'Подсолнечник', 'Конопля', 'Клещевина']
values = [25, 29, 57, 38, 59]
N = len(cat)
x_as = [n / float(N) * 2 * pi for n in range(N)]
values += values[:1]
x_as += x_as[:1]
plt.rc('axes', linewidth=0.5, edgecolor="#888888")
ax = plt.subplot(111, polar=True)

ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)

plt.xticks(x_as[:-1], [])
plt.yticks([30, 60], ["30", "60"])
ax.plot(x_as, values, linewidth=0, linestyle='solid', zorder=3)
ax.fill(x_as, values, 'b', alpha=0.3)
plt.ylim(0, 80)


for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 100 + distance_ax, cat[i], size=10, horizontalalignment=ha, verticalalignment="center")

plt.show()

