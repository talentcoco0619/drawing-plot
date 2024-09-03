import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

def draw_angle_dimension(ax, vertex, p1, p2, angle_text, radius=1.0, color='black'):
    """
    Draws an angle dimension arc and annotates the angle between two lines originating from a vertex.
    """
    # Calculate the angle between the two lines in degrees
    line1 = np.array(p1) - np.array(vertex)
    line2 = np.array(p2) - np.array(vertex)
    
    angle_rad = np.arctan2(line2[1], line2[0]) - np.arctan2(line1[1], line1[0])
    angle_deg = np.degrees(angle_rad)
    if angle_deg < 0:
        angle_deg += 360
    
    arc_angle = min(angle_deg, 360 - angle_deg)
    
    # Define the angle start
    start_angle = np.degrees(np.arctan2(line1[1], line1[0]))
    
    # Draw the lines
    ax.plot([vertex[0], p1[0]], [vertex[1], p1[1]], color=color)
    ax.plot([vertex[0], p2[0]], [vertex[1], p2[1]], color=color)
    
    # Draw the arc
    arc = Arc(vertex, 2*radius, 2*radius, angle=0, 
              theta1=start_angle, theta2=start_angle + arc_angle, 
              color=color, linewidth=1.5)
    ax.add_patch(arc)
    
    # Annotate the angle in the middle of the arc
    arc_mid_angle = start_angle + arc_angle / 2
    text_x = vertex[0] + (radius + 0.1) * np.cos(np.radians(arc_mid_angle))
    text_y = vertex[1] + (radius + 0.1) * np.sin(np.radians(arc_mid_angle))
    ax.text(text_x, text_y, angle_text, color=color, ha='center', va='center')

# Example usage
fig, ax = plt.subplots(figsize=(6, 6))

# Define the vertex and the two points forming the angle
vertex = (2, 2)
point1 = (4, 2)
point2 = (1, 4)

# Draw the angle dimension
draw_angle_dimension(ax, vertex, point1, point2, angle_text='60°')

# Set limits, maintain aspect ratio, and turn off the axes
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

plt.show()
