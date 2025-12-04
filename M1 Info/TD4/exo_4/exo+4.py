import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation
import os

# --- 1. Visual Styling (Dark Mode Setup) ---
plt.rcParams.update({
    'figure.facecolor': (0.102, 0.102, 0.102),
    'axes.facecolor': (0.102, 0.102, 0.102),
    'axes.labelcolor': (0.878, 0.878, 0.878),
    'text.color': (0.878, 0.878, 0.878),
    'xtick.color': (0.627, 0.627, 0.627),
    'ytick.color': (0.627, 0.627, 0.627),
    'axes.edgecolor': (0.188, 0.188, 0.188),
    'grid.color': (0.227, 0.227, 0.227),
    'figure.titlesize': 16,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.figsize': (14, 8),
    'figure.dpi': 100
})

# Create folder if it doesn't exist
if not os.path.exists('Graphiques'):
    os.makedirs('Graphiques')

# --- 2. Physics Constants ---
g = 9.81
r = 0.03
vy0 = 0.0

# --- 3. Calculation Function ---
def calculate_fall(y0, dt):
    """Calculates the Euler trajectory."""
    y = y0
    vy = vy0
    t = 0.0

    y_values = [y0]
    vy_values = [vy0]
    time_values = [t]

    while y > r:
        vy = vy - g * dt
        y = y + vy * dt
        t += dt
        y_values.append(y)
        vy_values.append(vy)
        time_values.append(t)

    return np.array(time_values), np.array(y_values), np.array(vy_values)

# --- 4. Plot Layout Setup ---
# We create 3 plots side by side
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

# IMPORTANT: Adjust bottom margin to make room for Sliders and Button
plt.subplots_adjust(bottom=0.25, wspace=0.3)

fig.suptitle(f'Interactive Ball Fall (Terminal Mode)', color='white')

# Initialize Empty Lines (we will update these later)
line1_euler, = ax1.plot([], [], 'c-', label='Euler')
line1_analyt, = ax1.plot([], [], 'r--', label='Analytical')
line2, = ax2.plot([], [], 'g-', label='Velocity')
# The ball for the animation
ball_line, = ax3.plot([], [], 'o', color='gold', markersize=12)

# Text objects to show real-time values
time_text = ax3.text(0.05, 0.95, '', transform=ax3.transAxes, color='white')
pos_text = ax3.text(0.05, 0.90, '', transform=ax3.transAxes, color='white')

# Configure Axes Labels
for ax in [ax1, ax2, ax3]:
    ax.grid(True)
    ax.set_xlabel('Time (s)')

ax1.set_title('Position vs Time')
ax1.set_ylabel('Position (m)')
ax1.legend(loc='upper right')

ax2.set_title('Velocity vs Time')
ax2.set_ylabel('Velocity (m/s)')

ax3.set_title('Real-time Animation')
ax3.get_yaxis().set_visible(False) # Hide Y axis on animation for clean look

# --- 5. Creating the Interactive Widgets ---
# We manually define where the sliders go on the screen [left, bottom, width, height]
ax_height = plt.axes([0.25, 0.12, 0.50, 0.03])
ax_dt     = plt.axes([0.25, 0.07, 0.50, 0.03])
ax_button = plt.axes([0.80, 0.07, 0.10, 0.08])

# Create the Slider Objects
s_height = Slider(ax_height, 'Height (m)', 0.5, 20.0, valinit=1.5, valstep=0.1)
s_dt     = Slider(ax_dt,     'Dt (s)',     0.001, 0.1, valinit=0.01, valstep=0.001)

# Create the Button Object
button = Button(ax_button, 'LAUNCH', color='0.2', hovercolor='0.3')
button.label.set_color('white')

# --- 6. The Animation Logic ---
# This variable keeps the animation alive
anim = None

def run_animation(event):
    global anim

    # 1. Get values from Sliders
    h_val = s_height.val
    dt_val = s_dt.val

    # 2. Calculate Math
    t_data, y_data, v_data = calculate_fall(h_val, dt_val)

    # Analytical solution for comparison
    t_analyt = np.linspace(0, t_data[-1], 100)
    y_analyt = h_val - 0.5 * g * t_analyt**2

    # 3. Update Static Graphs
    line1_euler.set_data(t_data, y_data)
    line1_analyt.set_data(t_analyt, y_analyt)
    line2.set_data(t_data, v_data)

    # Rescale Axes to fit new data
    ax1.set_xlim(0, t_data[-1]*1.1)
    ax1.set_ylim(0, h_val*1.1)

    ax2.set_xlim(0, t_data[-1]*1.1)
    ax2.set_ylim(min(v_data)*1.1, 0)

    ax3.set_xlim(0, t_data[-1]*1.1)
    ax3.set_ylim(0, h_val*1.1)

    # 4. Define the Frame Update function for Animation
    def update_frame(frame):
        # frame is just an integer index (0, 1, 2...)
        if frame < len(t_data):
            t_curr = t_data[frame]
            y_curr = y_data[frame]

            ball_line.set_data([t_curr], [y_curr])
            time_text.set_text(f'T: {t_curr:.2f} s')
            pos_text.set_text(f'Y: {y_curr:.2f} m')
        return ball_line, time_text, pos_text

    # Stop previous animation if it exists
    if anim is not None:
        anim.event_source.stop()

    # Start new animation
    # interval is in milliseconds. We match it to dt to look "real time"
    anim = FuncAnimation(fig, update_frame, frames=len(t_data),
                         interval=dt_val*1000, blit=True, repeat=False)

    plt.draw()

# --- 7. Launch ---
# Connect the button click to the function
button.on_clicked(run_animation)

# Run once at start so the graph isn't empty
run_animation(None)

plt.show()
