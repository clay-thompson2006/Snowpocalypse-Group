import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create the main application window
root = tk.Tk()

# Add a label widget
label = tk.Label(root, text="Welcome to Snowpocalypse.")
label.pack()  # Add the label to the window

# Start the Tkinter event loop
root.mainloop()