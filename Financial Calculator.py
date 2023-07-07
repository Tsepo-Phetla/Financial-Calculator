import tkinter as tk
import math

# Create GUI
root = tk.Tk()
root.title("Investment Calculator")

# Create labels and entries for investment calculation
inv_label = tk.Label(root, text="Investment Calculator", font=("Arial", 16, "bold"))
inv_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

inv_amount_label = tk.Label(root, text="Amount of money:", font=("Arial", 12))
inv_amount_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")
inv_amount_entry = tk.Entry(root, font=("Arial", 12))
inv_amount_entry.grid(row=1, column=1, padx=10, pady=5)

inv_rate_label = tk.Label(root, text="Interest rate (%):", font=("Arial", 12))
inv_rate_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")
inv_rate_entry = tk.Entry(root, font=("Arial", 12))
inv_rate_entry.grid(row=2, column=1, padx=10, pady=5)

inv_time_label = tk.Label(root, text="Years invested:", font=("Arial", 12))
inv_time_label.grid(row=3, column=0, padx=10, pady=5, sticky="W")
inv_time_entry = tk.Entry(root, font=("Arial", 12))
inv_time_entry.grid(row=3, column=1, padx=10, pady=5)

inv_interest_label = tk.Label(root, text="Interest type:", font=("Arial", 12))
inv_interest_label.grid(row=4, column=0, padx=10, pady=5, sticky="W")
inv_interest_var = tk.StringVar(value="Simple")
inv_interest_simple = tk.Radiobutton(root, text="Simple", font=("Arial", 12), variable=inv_interest_var, value="Simple")
inv_interest_simple.grid(row=4, column=1, padx=10, pady=5, sticky="W")
inv_interest_compound = tk.Radiobutton(root, text="Compound", font=("Arial", 12), variable=inv_interest_var, value="Compound")
inv_interest_compound.grid(row=4, column=1, padx=10, pady=5, sticky="E")

inv_answer_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
inv_answer_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create labels and entries for bond calculation
bond_label = tk.Label(root, text="Bond Calculator", font=("Arial", 16, "bold"))
bond_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

bond_value_label = tk.Label(root, text="Present value of the house:", font=("Arial", 12))
bond_value_label.grid(row=7, column=0, padx=10, pady=5, sticky="W")
bond_value_entry = tk.Entry(root, font=("Arial", 12))
bond_value_entry.grid(row=7, column=1, padx=10, pady=5)

bond_rate_label = tk.Label(root, text="Interest rate (%):", font=("Arial", 12))
bond_rate_label.grid(row=8, column=0, padx=10, pady=5, sticky="W")
bond_rate_entry = tk.Entry(root, font=("Arial", 12))
bond_rate_entry.grid(row=8, column=1, padx=10, pady=5)

bond_time_label = tk.Label(root, text="Years to pay off:", font=("Arial", 12))
bond_time_label.grid(row=9, column=0, padx=10, pady=5, sticky="W")
bond_time_entry = tk.Entry(root, font=("Arial", 12))
bond_time_entry.grid(row=9, column=1, padx=10, pady=5)

bond_answer_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
bond_answer_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Create function for investment calculation
def calculate_investment():
    inv_amount = float(inv_amount_entry.get())
    inv_rate = float(inv_rate_entry.get())
    inv_time = int(inv_time_entry.get())
    interest_type = inv_interest_var.get()

    if interest_type == "Simple":
        inv_answer = inv_amount * (1 + (inv_rate / 100) * inv_time)
    elif interest_type == "Compound":
        inv_answer = inv_amount * math.pow((1 + inv_rate / 100), inv_time)

    inv_answer_label.config(text=f"Your investment will be worth R{inv_answer:.2f}.")

# Create function for bond calculation
def calculate_bond():
    bond_value = float(bond_value_entry.get())
    bond_rate = float(bond_rate_entry.get())
    bond_time = int(bond_time_entry.get())

    bond_payment = bond_value / (((1 - math.pow((1 + bond_rate / 100), -bond_time))) / (bond_rate / 100))

    bond_answer_label.config(text=f"Your monthly payment will be R{bond_payment:.2f}.")

# Create buttons to calculate investment and bond
inv_button = tk.Button(root, text="Calculate Investment", font=("Arial", 12), command=calculate_investment)
inv_button.grid(row=11, column=0, padx=10, pady=10)

bond_button = tk.Button(root, text="Calculate Bond", font=("Arial", 12), command=calculate_bond)
bond_button.grid(row=11, column=1, padx=10, pady=10)

root.mainloop()
