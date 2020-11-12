#! python3
# break_notification - Alerts to take break.

import tkinter as tk
from tkinter import messagebox

class Reminder(object):
    def __init__(self, hide_interval):
        self.hide_interval = hide_interval
        
        # Create and configure root
        self.root = tk.Tk()
        self.root.title("Break Notification")
        self.root.geometry("350x120")
        
        # Create and configure frame
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0)

        # Create labels and buttons
        my_label = tk.Label(self.root, text="Take a break and stop studying when time is up")
        my_label.grid(row=0, column=1, columnspan=3, pady=5)

        self.button1 = tk.Button(text="Click to hide until next break", command=self.hide)
        self.button1.grid(row=1, column=1, columnspan=3, pady=10)

        self.button2 = tk.Button(text="Click to shutdown", command=self.close)
        self.button2.grid(row=2, column=1, columnspan=3, pady=10)

        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=1)
    
    def close(self):
        self.root.destroy()

    def hide(self):
        # Hides window for desired time in seconds
        self.root.withdraw()
        self.root.after(1000 * self.hide_interval, self.show) # Schedule self.show() in hide_interval seconds
    
    def show(self):
        self.root.deiconify()
        messagebox.showwarning("Break Time", "Please take a break!")

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    r = Reminder(3) # Enter number of seconds to hide window
    r.start()