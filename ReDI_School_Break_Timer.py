import tkinter as tk
import time
import winsound
import ctypes

# Create a Tkinter window
root = tk.Tk()
root.title("Timer")


# Set the window width and height
window_width = 1500
window_height = 760


# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window on the screen
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label to display the time remaining
label = tk.Label(root, font=("Helvetica", 50, "bold"))
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Set the initial time in seconds
time_remaining = 1 * 60  # 1 minutes in seconds

# Remove the default Tkinter icon
root.iconbitmap('')

# Remove the title bar and decorations from the window
root.overrideredirect(True)

# Function to update the time remaining
def update_timer():
    global time_remaining
    if time_remaining > 0:
        # Convert time_remaining to minutes and seconds
        minutes = time_remaining // 60
        seconds = time_remaining % 60

        # Update the label text
        label.config(text=f"Time Remaining: {minutes} Minutes {seconds} Seconds")

        # Decrease time_remaining by 1 second
        time_remaining -= 1

    else:
        # Timer has reached 0, stop updating
        label.config(text="Get ReDI Time Is Up!")

        # Play a sound at the end of the timer
        winsound.PlaySound("path/to/sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    # Call update_timer() again after 1 second
    label.after(1000, update_timer)

# Call update_timer() to start updating the time
update_timer()

# Start the Tkinter event loop
root.mainloop()

