import matplotlib.pyplot as plt
import numpy as np

def draw_dimension_line(ax, start, end, text, text_offset=0.1, line_offset=0.05, color='black'):
    """
    Draws a dimension line with an arrow between two points
    """
    # Unpack start and end positions
    (x1, y1), (x2, y2) = start, end
    
    # Calculate the middle of the line for placing the text
    text_x = (x1 + x2) / 2
    text_y = (y1 + y2) / 2 + text_offset
    
    # Draw the line with arrows
    ax.annotate(
        '',
        xy=start, 
        xytext=end,
        arrowprops=dict(arrowstyle='<->', color=color),
        annotation_clip=False
    )
    
    # Add text annotation above the line
    ax.text(text_x, text_y, text, ha='center', va='bottom', color=color)
    
    # Create vertical/horizontal lines to indicate dimension (offset)
    if x1 == x2:  # vertical dimension
        ax.plot([x1 - line_offset, x1 + line_offset], [y1, y1], color=color)
        ax.plot([x2 - line_offset, x2 + line_offset], [y2, y2], color=color)
    elif y1 == y2:  # horizontal dimension
        ax.plot([x1, x1], [y1 - line_offset, y1 + line_offset], color=color)
        ax.plot([x2, x2], [y2 - line_offset, y2 + line_offset], color=color)

# Example usage
fig, ax = plt.subplots(figsize=(8, 4))

# Set limits and aspect
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_aspect('equal')

# Example lines to show dimension between two points
line1_start = (2, 2)
line1_end = (8, 2)

# Draw a dimension line
draw_dimension_line(ax, line1_start, line1_end, line_offset=1, text='6 units')

# Additional customization to make it clear
plt.scatter([line1_start[0], line1_end[0]], [line1_start[1], line1_end[1]], color='red') # Points
ax.plot([line1_start[0], line1_end[0]], [line1_start[1], line1_end[1]], color='blue')   # Line

# Hide axes
ax.axis('off')

plt.show()