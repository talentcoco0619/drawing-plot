import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
from matplotlib.patches import FancyArrowPatch


def draw_dimension_line(ax, P1, P2, L, color='black'):
    """
    Draws a dimension line with an arrow between two points
    """
    # Unpack start and end positions
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
    ax.text(*mid_point, f'{length:.2f}(units)', ha='center', va='bottom', 
            rotation=np.degrees(theta), rotation_mode='anchor')

def draw_angle_dimension(ax, vertex, P1, P2, radius=7, color='black'):
    """
    Draws an angle dimension arc and annotates the angle between two lines originating from a vertex.
    """
    # Calculate the angle between the two lines in degrees
    line1 = np.array(P1) - np.array(vertex)
    line2 = np.array(P2) - np.array(vertex)

    # Calculate distances from the vertex to each point
    distance1 = np.linalg.norm(line1)
    distance2 = np.linalg.norm(line2)
    
    # Find the minimum distance and subtract 1
    min_distance = min(distance1, distance2) - 1
    
    # Normalize the vectors
    line1_normalized = line1 / distance1
    line2_normalized = line2 / distance2
    
    # Scale the normalized vectors to the new length
    point1 = vertex + line1_normalized * min_distance
    point2 = vertex + line2_normalized * min_distance

    # Create the curved line (arc) with arrows at both ends
    arc = FancyArrowPatch(point1, point2, 
                          connectionstyle="arc3,rad=0.2", # The radius can be adjusted
                          color=color, 
                          arrowstyle="<|-|>", # Arrow style with arrowhead at both ends
                          mutation_scale=10, # Size of the arrowhead
                          linewidth=1.5)
    
    # Add the arc to the plot
    ax.add_patch(arc)
    
    
    angle_rad = np.arctan2(line2[1], line2[0]) - np.arctan2(line1[1], line1[0])
    angle_deg = np.degrees(angle_rad)
    if angle_deg < 0:
        angle_deg += 360
    
    arc_angle = min(angle_deg, 360 - angle_deg)
    
    # Define the angle start
    start_angle = np.degrees(np.arctan2(line1[1], line1[0]))
    end_angle = start_angle + arc_angle

    # Draw the vertex point
    ax.plot(*vertex, 'ko', markersize=1)
    # Draw the lines
    ax.plot([vertex[0], P1[0]], [vertex[1], P1[1]], color=color)
    ax.plot([vertex[0], P2[0]], [vertex[1], P2[1]], color=color)
    
    # # Draw the arc
    # arc = Arc(vertex, 2*radius, 2*radius, angle=0, 
    #           theta1=start_angle, theta2=end_angle, 
    #           color=color, linewidth=1.5)
    # ax.add_patch(arc)
    
    # Annotate the angle in the middle of the arc
    arc_mid_angle = start_angle + arc_angle / 2
    text_x = vertex[0] + (radius - 0.5) * np.cos(np.radians(arc_mid_angle))
    text_y = vertex[1] + (radius - 0.5) * np.sin(np.radians(arc_mid_angle))
    
    # Rotate the label perpendicular to the angle bisector
    label_rotation = arc_mid_angle + 90 if arc_angle < 180 else arc_mid_angle - 90
    
    # Position the label toward the angle, closer to the vertex
    ax.text(text_x, text_y, f'{arc_angle:.2f}°', color=color, ha='center', va='center',
            rotation=label_rotation, rotation_mode='anchor')



# Given points and leading length
# P1 = tuple(map(float, input("Enter P1 (x, y): ").split(',')))
# P2 = tuple(map(float, input("Enter P2 (x, y): ").split(',')))
# L = float(input("Enter leading length L: "))

# # Plotting
# fig, ax = plt.subplots(figsize=(18, 8)) #Set the screen size
# # Remove the axes
# ax.axis('off')

# ax.set_xlim(-10, 20)
# ax.set_ylim(-10, 20)

# draw_dimension_line(ax, P1, P2, L)

# draw_angle_dimension(ax, vertex, P1, P2)

# ax.set_aspect('equal')
# plt.show()


# Initialize the plot outside the loop
fig, ax = plt.subplots(figsize=(18, 8))  # Set the screen size
# ax.axis('off')  # Remove the axes
ax.set_xlim(-10, 20)
ax.set_ylim(-10, 20)

# while True:
#     # Ask the user for the type of drawing
#     option = input("Enter 'line' to draw a dimension line, 'angle' to draw an angle, or 'quit' to exit: ").lower()
    
#     if option == 'line':
#         P1 = tuple(map(float, input("Enter P1 (x, y): ").split(',')))
#         P2 = tuple(map(float, input("Enter P2 (x, y): ").split(',')))
#         L = float(input("Enter leading length L: "))
        
#         draw_dimension_line(ax, P1, P2, L)
        
#     elif option == 'angle':
#         vertex = tuple(map(float, input("Enter vertex (x, y): ").split(',')))
#         P1 = tuple(map(float, input("Enter P1 (x, y): ").split(',')))
#         P2 = tuple(map(float, input("Enter P2 (x, y): ").split(',')))
        
#         draw_angle_dimension(ax, vertex, P1, P2)
        
#     elif option == 'quit':
#         break
#     else:
#         print("Invalid option. Please enter 'line', 'angle', or 'quit'.")

draw_angle_dimension(ax, (2, 2), (10, 2), (8, 8))

ax.set_aspect('equal')
plt.show()