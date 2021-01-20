# BMI Application
# Script to create a GUI App that calculates BMI of a person
# Author - Sandip Dutta

# main app setup
import tkinter as tk
root = tk.Tk()

# Setup of main layout
main_canvas = tk.Canvas(root, width=400, height=300)
main_canvas.pack()

# App heading mentioning what type of app it is
app_heading = tk.Label(root, text = 'Calculate BMI')
app_heading.config(font=('helvetica', 20))
main_canvas.create_window(200, 50, window = app_heading)

# Get the value of height











# Loop
root.mainloop()