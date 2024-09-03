import matplotlib.pyplot as plt
import numpy as np

# Given points and leading length
P1 = (4, 20)
P2 = (8, 3)
L = 5

# P1 = tuple(map(float, input("Enter P1 (x, y): ").split(',')))
# P2 = tuple(map(float, input("Enter P2 (x, y): ").split(',')))
# L = float(input("Enter leading length L: "))

Gap = L / 4
d_alpha = 0.5

# Calculate angle
theta = np.arctan2(P2[1] - P1[1], P2[0] - P1[0])
perp_theta = theta + np.pi / 2  # perpendicular angle
d_theta = np.pi/2 - perp_theta

# Calculate dimension line points
P1_lead = (P1[0] + L * np.cos(perp_theta), P1[1] + L * np.sin(perp_theta))
P2_lead = (P2[0] + L * np.cos(perp_theta), P2[1] + L * np.sin(perp_theta))
# Calculate leading line start points
P1_g = (P1[0] + Gap * np.cos(perp_theta), P1[1] + Gap * np.sin(perp_theta))
P2_g = (P2[0] + Gap * np.cos(perp_theta), P2[1] + Gap * np.sin(perp_theta))
#Calculate leading line end points
P1_lead_g = (P1[0] + (L + Gap) * np.cos(perp_theta), P1[1] + (L + Gap) * np.sin(perp_theta))
P2_lead_g = (P2[0] + (L + Gap) * np.cos(perp_theta), P2[1] + (L + Gap) * np.sin(perp_theta))
#dimension line points
P1_lead_d = (P1_lead[0] - d_alpha * np.cos(d_theta), P1_lead[1] + d_alpha * np.sin(d_theta))
P2_lead_d = (P2_lead[0] + d_alpha * np.cos(d_theta), P2_lead[1] - d_alpha * np.sin(d_theta))



# Plotting
fig, ax = plt.subplots(figsize=(18, 8)) #Set the screen size
# Remove the axes
ax.axis('off')

# Plot P1 and P2 as tiny black dots
ax.plot(*P1, 'ko', markersize=2)  # 'ko' is the format string for black circle markers, markersize sets the size
ax.plot(*P2, 'ko', markersize=2)
# Original line
# ax.plot(*zip(P1, P2), marker='', color='black', linestyle='-.')
# Leading lines
ax.plot(*zip(P1_g, P1_lead_g), color='black')
ax.plot(*zip(P2_g, P2_lead_g), color='black')
# Dimension line with arrows
ax.annotate('', xy=P1_lead_d, xytext=P2_lead_d, arrowprops=dict(arrowstyle='<|-|>, head_length=1.5, head_width=0.15', lw=1.5, color='black', shrinkA=0.01, shrinkB=0.01))
# Label
mid_point = ((P1_lead[0] + P2_lead[0]) / 2, (P1_lead[1] + P2_lead[1]) / 2)
length = np.linalg.norm(np.subtract(P2, P1))
ax.text(*mid_point, f'{length:.2f}(fs)', ha='center', va='bottom', 
        rotation=np.degrees(theta), rotation_mode='anchor')

ax.set_xlim([min(P1[0], P2[0]) - 10, max(P1[0], P2[0]) + 10])
ax.set_ylim([min(P1[1], P2[1]) - 10, max(P1[1], P2[1]) + 10])

ax.set_aspect('equal')
plt.show()