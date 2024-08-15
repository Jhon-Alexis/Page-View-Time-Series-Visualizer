import time_series_visualizer
import matplotlib.pyplot as plt
from unittest import main


fig1 = time_series_visualizer.draw_line_plot()
plt.show()
plt.close(fig1)

fig2 = time_series_visualizer.draw_bar_plot()
plt.show()
plt.close(fig2)

fig3 = time_series_visualizer.draw_box_plot()
plt.show()
plt.close(fig3)

main(module="test_module",exit=False)
