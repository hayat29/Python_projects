'''`import tkinter as tk` is importing the `tkinter` module in Python and aliasing it as `tk`. This
 allows you to refer to the `tkinter` module using the shorter alias `tk` throughout your code. This
 is a common practice to make the code more concise and readable.'''


import tkinter as tk

class RegistrationForm:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Registration Form")

        # Center the window on the screen
        self.center_window()

        # Create the widgets for the form
        self.create_widgets()

    def center_window(self):
        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Get the window dimensions
        window_width = 300
        window_height = 150

        # Calculate the x and y coordinates for the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window position
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self):
        # Create and place the labels and entry fields
        labels = ["Name:", "Email:", "Age:"]
        self.entries = []

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=i, column=0)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        # Create and place the Submit button
        tk.Button(self.root, text="Submit", command=self.submit_form).grid(row=len(labels), columnspan=2)

    def submit_form(self):
        # Get the values from the entry fields
        values = [entry.get() for entry in self.entries]

        # Print the values to the console (or process them further)
        print(f"Name: {values[0]}, Email: {values[1]}, Age: {values[2]}")

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of the RegistrationForm class
    app = RegistrationForm(root)
    # Run the Tkinter main loop
    root.mainloop()