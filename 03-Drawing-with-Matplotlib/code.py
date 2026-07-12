import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(8, 6))

# ----------------------------
# Hut Base
# ----------------------------
plt.plot([1, 10], [1, 1])      # Bottom
plt.plot([1, 1], [1, 4])       # Left wall
plt.plot([4, 4], [1, 4])       # Middle wall
plt.plot([10, 10], [1, 6])     # Right wall

# ----------------------------
# Roof
# ----------------------------
plt.plot([1, 2.5], [4, 6])     # Left roof
plt.plot([2.5, 4], [6, 4])     # Right roof
plt.plot([2.5, 10], [6, 6])    # Top roof

# ----------------------------
# Upper Floor Line
# ----------------------------
plt.plot([4, 10], [4, 4])

# ----------------------------
# Door
# ----------------------------
plt.plot([2, 2], [1, 2.5])
plt.plot([2, 3], [2.5, 2.5])
plt.plot([3, 3], [2.5, 1])

# ----------------------------
# Window
# ----------------------------
plt.scatter(
    2.5,
    4.5,
    s=900,
    color="skyblue",
    edgecolors="black"
)

# ----------------------------
# Figure Settings
# ----------------------------
plt.title("Hut using Matplotlib")
plt.xlim(0, 10.5)
plt.ylim(0.5, 6.3)
plt.gca().set_aspect("equal")

plt.show()
