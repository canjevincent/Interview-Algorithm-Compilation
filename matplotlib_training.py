import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Resize your Graph ( dpi specifies pixels per inch. when saving probably should use 300 if possible )
# plt.figure(figsize=(5,3), dpi=250)

# x,y = [0,1,2,3,4], [0,2,4,6,8]

# plt.plot(x,y, label="2x", color="red", linewidth=2, marker=".", linestyle="--", markersize=10, markeredgecolor="blue")

# Shorthand notation
# fmt = "[color][marker][line]"
# plt.plot(x,y, "b^--", label="2x")

## Line 2

# Select interval we want to plot points at
# x2 = np.arange(0,4.5,0.5)

# Plot part of the graph as line
# plt.plot(x2[:6], x2[:6]**2, "r", label="x^2")

# Plot reminder of graph as a dot
# plt.plot(x2[5:], x2[5:]**2, "r--")

# Add a title (specify font paramters with fontdict)
# plt.title("Our First Graph", fontdict={"fontname":"Comic Sans MS", "fontsize": 20})

# X and Y labels
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")

# plt.xticks([0,1,2,3,4])
# plt.yticks([0,2,4,6,8,10])

# Add a Legend
# plt.legend()

# Save figure ( dpi 300 is good when saving so graph has high resolution )
# plt.savefig("mygraph.png", dpi=250)

# Show plot
# plt.show()

# BAR GRAPH

# labels = ["A","B","C"]
# values = [1,4,2]

# bars = plt.bar(labels, values)

# patterns = ["/","O","*"]

# for bar in bars:
#     bar.set_hatch(patterns.pop())

# bars[0].set_hatch("/")
# bars[1].set_hatch("0")
# bars[2].set_hatch("*")

# plt.figure(figsize=(6,4))

# plt.show()

# Display CSV File

gas = pd.read_csv("gas_prices.csv")

plt.title("Gas Prices Over Time (In USD)")

plt.plot(gas.Year, gas.USA, "b.-", label="USA")
plt.plot(gas.Year, gas.Canada, "r.-", label="Canada")
plt.plot(gas.Year, gas["South Korea"], "g.-", label="South Korea")

plt.xticks(gas.Year[::3])

plt.legend()

# print(gas.Year[::3])

plt.show()

# print(gas)