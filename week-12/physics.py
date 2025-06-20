
import tkinter as tk
from tkinter import messagebox
import math

# --- Physics Calculation Functions ---

def solve_problem_15_14(area, magnetic_field, emf, angle_plane_field, num_turns = 1):
    # The formula for induced EMF in a rotating loop is EMF = N * B * A * omega * sin 0,
    angle_normal_field_rad = math.radians(90 - angle_plane_field)

    try:
        # Check for conditions that would lead to division by zero or invalid results.
        if math.isclose(math.sin(angle_normal_field_rad), 0.0):
            return "Error: The angle causes sin(theta) to be zero, leading to division by zero."
        if num_turns == 0:
             return "Error: Number of turns cannot be zero."
        if magnetic_field == 0:
            return "Error: Magnetic field strength cannot be zero."
        if area == 0:
            return "Error: Loop area cannot be zero."

        # Rearrange the EMF formula to solve for omega (angular speed):
        # omega = EMF / (N * B * A * sin(theta))
        omega = emf / (num_turns * magnetic_field * area * math.sin(angle_normal_field_rad))
        return omega
    except ZeroDivisionError:
        return "Error: Division by zero. Please check the input values, especially the angle."
    except Exception as e:
        return f"An unexpected error occurred in solve_problem_15_14: {e}"

def solve_problem_15_15(length_cm, num_turns, area_cm2):
    mu_0 = 4 * math.pi * (10**-7)  # Permeability of free space in T*m/A

    # Convert units from cm to meters (m) and cm^2 to m^2, as mu_0 is in SI units.
    length_m = length_cm / 100
    area_m2 = area_cm2 / (100**2)  # 1 cm^2 = 10^-4 m^2

    try:
        # Check if the length is zero to prevent division by zero.
        if length_m == 0:
            return "Error: Solenoid length cannot be zero."
        
        # Calculate inductance using the formula.
        inductance = (mu_0 * (num_turns**2) * area_m2) / length_m
        return inductance
    except ZeroDivisionError:
        return "Error: Division by zero. Check if solenoid length is zero."
    except Exception as e:
        return f"An unexpected error occurred in solve_problem_15_15: {e}"

def solve_problem_15_16(inductance_mH, current_rate_change):
    # Convert inductance from millihenrys (mH) to Henrys (H) for SI consistency.
    inductance_H = inductance_mH / 1000
    try:
        # Calculate induced EMF.
        emf_induced = inductance_H * current_rate_change
        return emf_induced
    except Exception as e:
        return f"An unexpected error occurred in solve_problem_15_16: {e}"
    
    
# --- Tkinter GUI Setup ---
class PhysicsCalculatorGUI:
    def __init__(self, master):
        """
        Initializes the main GUI window and sets up all its components.

        Args:
            master (tk.Tk): The root Tkinter window instance.
        """
        self.master = master
        master.title("Physics Problem Solver")
        master.geometry("700x900")  # Set initial window size (width x height)
        master.resizable(False, False) # Prevent window from being resized by the user

        # Configure styling for various GUI elements
        master.configure(bg='#F0F0F0') # Background color for the main window
        self.font_title = ('Helvetica', 16, 'bold') # Font for problem titles
        self.font_label = ('Helvetica', 10)         # Font for input labels
        self.font_entry = ('Helvetica', 10)         # Font for input fields
        self.font_result = ('Helvetica', 12, 'bold')# Font for displaying results
        self.button_style = {
            'bg': '#4CAF50',  # Green background
            'fg': 'white',    # White text
            'font': self.font_label,
            'relief': 'raised',
            'bd': 3           # Border thickness
        }
        self.entry_style = {
            'bg': 'white',    # White background
            'fg': 'black',    # Black text
            'font': self.font_entry,
            'relief': 'sunken',
            'bd': 2
        }
        self.result_label_style = {
            'font': self.font_result,
            'bg': '#E0E0E0',  # Light grey background for result labels
            'fg': 'blue',     # Blue text for results
            'wraplength': 450 # Wrap text after 450 pixels to prevent labels from stretching too wide
        }

        # Dictionary to store references to Entry widgets. This allows easy access
        # to their values later using their assigned names (keys).
        self.entries = {} 

        # Create a main frame to hold all problem sections. This helps with overall padding and organization.
        self.main_frame = tk.Frame(master, bg='#F0F0F0', padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both') # Allow frame to expand and fill available space

        # --- Problem 15.14 Frame Setup ---
        # Create a labeled frame for the first problem (Angular Speed).
        self.frame_15_14 = tk.LabelFrame(self.main_frame, text="Problem 15.14: Angular Speed", 
                                       font=self.font_title, bg='#E0E0E0', 
                                       padx=15, pady=15, relief='groove', bd=2)
        self.frame_15_14.pack(pady=10, fill='x') # Pack the frame, adding vertical padding and making it fill horizontally

        # Create input fields for Problem 15.14 using the helper method.
        self.create_input_field(self.frame_15_14, "Area (m²):", "entry_area_14", 0, default_value="0.173")
        self.create_input_field(self.frame_15_14, "Magnetic Field (T):", "entry_b_14", 1, default_value="0.354")
        self.create_input_field(self.frame_15_14, "EMF (V):", "entry_emf_14", 2, default_value="8.41")
        self.create_input_field(self.frame_15_14, "Angle (degrees, plane to field):", "entry_angle_14", 3, default_value="45.0")

        # Create the "Calculate" button for Problem 15.14.
        # When clicked, it calls the `calculate_15_14` method.
        self.btn_15_14 = tk.Button(self.frame_15_14, text="Calculate Angular Speed", command=self.calculate_15_14, **self.button_style)
        self.btn_15_14.grid(row=4, column=0, columnspan=2, pady=10) # Place button using grid layout

        # Label to display the calculation result for Problem 15.14.
        self.result_label_15_14 = tk.Label(self.frame_15_14, text="Result: ", **self.result_label_style)
        self.result_label_15_14.grid(row=5, column=0, columnspan=2, pady=5) # Place result label

        # --- Problem 15.15 Frame Setup ---
        # Create a labeled frame for the second problem (Self-Inductance).
        self.frame_15_15 = tk.LabelFrame(self.main_frame, text="Problem 15.15: Self-Inductance", 
                                       font=self.font_title, bg='#E0E0E0', 
                                       padx=15, pady=15, relief='groove', bd=2)
        self.frame_15_15.pack(pady=10, fill='x')

        # Create input fields for Problem 15.15.
        self.create_input_field(self.frame_15_15, "Length (cm):", "entry_length_15", 0, default_value="5.0")
        self.create_input_field(self.frame_15_15, "Number of Turns:", "entry_turns_15", 1, default_value="10")
        self.create_input_field(self.frame_15_15, "Area (cm²):", "entry_area_15", 2, default_value="1.0")

        # Create the "Calculate" button for Problem 15.15.
        self.btn_15_15 = tk.Button(self.frame_15_15, text="Calculate Self-Inductance", command=self.calculate_15_15, **self.button_style)
        self.btn_15_15.grid(row=3, column=0, columnspan=2, pady=10)
        # Label to display the calculation result for Problem 15.15.
        self.result_label_15_15 = tk.Label(self.frame_15_15, text="Result: ", **self.result_label_style)
        self.result_label_15_15.grid(row=4, column=0, columnspan=2, pady=5)

        # --- Problem 15.16 Frame Setup ---
        # Create a labeled frame for the third problem (Induced EMF).
        self.frame_15_16 = tk.LabelFrame(self.main_frame, text="Problem 15.16: Induced EMF", 
                                       font=self.font_title, bg='#E0E0E0', 
                                       padx=15, pady=15, relief='groove', bd=2)
        self.frame_15_16.pack(pady=10, fill='x')

        # Create input fields for Problem 15.16.
        self.create_input_field(self.frame_15_16, "Inductance (mH):", "entry_inductance_16", 0, default_value="25")
        self.create_input_field(self.frame_15_16, "Rate of Current Change (A/s):", "entry_dIdt_16", 1, default_value="1.25e-2")

        # Create the "Calculate" button for Problem 15.16.
        self.btn_15_16 = tk.Button(self.frame_15_16, text="Calculate Induced EMF", command=self.calculate_15_16, **self.button_style)
        self.btn_15_16.grid(row=2, column=0, columnspan=2, pady=10)
        # Label to display the calculation result for Problem 15.16.
        self.result_label_15_16 = tk.Label(self.frame_15_16, text="Result: ", **self.result_label_style)
        self.result_label_15_16.grid(row=3, column=0, columnspan=2, pady=5)


    def create_input_field(self, parent_frame, label_text, entry_name, row, default_value=""):
        """
        Helper method to create a label and an associated Entry (input) widget.

        Args:
            parent_frame (tk.LabelFrame or tk.Frame): The frame widget where this input field will be placed.
            label_text (str): The text to display next to the input field (e.g., "Area (m²):").
            entry_name (str): A unique string name for this entry, used as a key to store and retrieve it
                              from the `self.entries` dictionary.
            row (int): The grid row number where the label and entry will be placed.
            default_value (str, optional): The initial text to display in the Entry field. Defaults to an empty string.
        """
        # Create and place the label.
        label = tk.Label(parent_frame, text=label_text, font=self.font_label, bg=parent_frame['bg'])
        label.grid(row=row, column=0, padx=5, pady=5, sticky='w') # 'w' aligns to the west (left)

        # Create and place the Entry widget.
        entry = tk.Entry(parent_frame, **self.entry_style)
        entry.insert(0, default_value) # Insert the default value at the beginning of the entry.
        entry.grid(row=row, column=1, padx=5, pady=5, sticky='ew') # 'ew' makes it expand horizontally

        # Store the Entry widget in the `self.entries` dictionary using its `entry_name` as the key.
        self.entries[entry_name] = entry 
        
        # Configure the second column of the parent frame (where entries are) to expand horizontally.
        parent_frame.grid_columnconfigure(1, weight=1) 

    def get_float_input(self, entry_name):
        """
        Retrieves the text from a specified Entry widget and attempts to convert it to a float.
        Includes robust error handling for invalid input or missing entries.

        Args:
            entry_name (str): The key used to identify the desired Entry widget in `self.entries`.

        Returns:
            float: The numerical value obtained from the Entry widget.
        """
        try:
            # Check if the key exists in the dictionary before attempting to access it.
            if entry_name not in self.entries:
                raise KeyError(f"Entry with name '{entry_name}' not found in self.entries.")
            
            value_str = self.entries[entry_name].get() # Get the string content from the Entry widget.
            return float(value_str) # Convert the string to a floating-point number.
        except ValueError:
            # Catch ValueError if `float()` conversion fails (e.g., non-numeric input).
            # Re-raise with a more user-friendly message.
            raise ValueError(f"Invalid input for '{entry_name.replace('entry_', '').replace('_', ' ').title()}'. Please enter a valid number.")
        except KeyError as ke:
            # Catch KeyError if `entry_name` is not a valid key in `self.entries`.
            # Re-raise it directly so it can be handled by the calling `calculate_` method.
            raise ke
        except Exception as e:
            # Catch any other unexpected exceptions during the process.
            raise Exception(f"An unexpected error occurred in get_float_input for '{entry_name}': {e}")


    def calculate_15_14(self):
        """
        Reads input values for Problem 15.14, calls the `solve_problem_15_14` function,
        and displays the result or an error message in the GUI.
        Handles various potential errors during input retrieval and calculation.
        """
        try:
            # Retrieve and convert input values from the Entry widgets.
            area = self.get_float_input("entry_area_14")
            magnetic_field = self.get_float_input("entry_b_14")
            emf = self.get_float_input("entry_emf_14")
            angle_plane_field = self.get_float_input("entry_angle_14")
            num_turns = 1 # Number of turns is fixed for this problem as per description.

            # Call the physics calculation function.
            result = solve_problem_15_14(area, magnetic_field, emf, angle_plane_field, num_turns)
            
            # Update the result label based on the outcome of the calculation.
            if isinstance(result, str): # If the result is a string, it indicates an error.
                self.result_label_15_14.config(text=f"Error: {result}", fg='red')
            else: # Otherwise, display the numerical result formatted to 3 decimal places.
                self.result_label_15_14.config(text=f"Result: {result:.3f} rad/s", fg='blue')
        except ValueError as e:
            # Catch and display user input validation errors.
            self.result_label_15_14.config(text=f"Input Error: {e}", fg='red')
        except KeyError as e:
            # Catch and display configuration errors (if an entry widget is unexpectedly missing).
            self.result_label_15_14.config(text=f"Configuration Error: Missing input field {e}. Please restart the application.", fg='red')
        except Exception as e:
            # Catch and display any other unexpected errors during the process.
            self.result_label_15_14.config(text=f"An unexpected error occurred: {type(e).__name__}: {e}", fg='red')

    def calculate_15_15(self):
        """
        Reads input values for Problem 15.15, calls the `solve_problem_15_15` function,
        and displays the result or an error message in the GUI.
        Handles various potential errors during input retrieval and calculation.
        """
        try:
            # Retrieve and convert input values. `num_turns` is cast to int as it's typically a whole number.
            length_cm = self.get_float_input("entry_length_15")
            num_turns = int(self.get_float_input("entry_turns_15"))
            area_cm2 = self.get_float_input("entry_area_15")

            # Call the physics calculation function.
            result = solve_problem_15_15(length_cm, num_turns, area_cm2)
            
            # Update the result label.
            if isinstance(result, str):
                self.result_label_15_15.config(text=f"Error: {result}", fg='red')
            else: # Display result in scientific notation (e.g., 2.51e-07 H).
                self.result_label_15_15.config(text=f"Result: {result:.2e} H", fg='blue')
        except ValueError as e:
            self.result_label_15_15.config(text=f"Input Error: {e}", fg='red')
        except KeyError as e:
            self.result_label_15_15.config(text=f"Configuration Error: Missing input field {e}. Please restart the application.", fg='red')
        except Exception as e:
            self.result_label_15_15.config(text=f"An unexpected error occurred: {type(e).__name__}: {e}", fg='red')

    def calculate_15_16(self):
        """
        Reads input values for Problem 15.16, calls the `solve_problem_15_16` function,
        and displays the result or an error message in the GUI.
        Handles various potential errors during input retrieval and calculation.
        """
        try:
            # Retrieve and convert input values.
            inductance_mH = self.get_float_input("entry_inductance_16")
            current_rate_change = self.get_float_input("entry_dIdt_16")

            # Call the physics calculation function.
            result = solve_problem_15_16(inductance_mH, current_rate_change)
            
            # Update the result label.
            if isinstance(result, str):
                self.result_label_15_16.config(text=f"Error: {result}", fg='red')
            else: # Display result in scientific notation (e.g., 3.1250e-04 V).
                self.result_label_15_16.config(text=f"Result: {result:.4e} V", fg='blue')
        except ValueError as e:
            self.result_label_15_16.config(text=f"Input Error: {e}", fg='red')
        except KeyError as e:
            self.result_label_15_16.config(text=f"Configuration Error: Missing input field {e}. Please restart the application.", fg='red')
        except Exception as e:
            self.result_label_15_16.config(text=f"An unexpected error occurred: {type(e).__name__}: {e}", fg='red')

# Main execution block
if __name__ == "__main__":
    # Create the root Tkinter window.
    root = tk.Tk()
    # Create an instance of the PhysicsCalculatorGUI class, passing the root window.
    app = PhysicsCalculatorGUI(root)
    # Start the Tkinter event loop. This keeps the window open and responsive to user interactions.
    root.mainloop()