import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create a currency converter object
converter = CurrencyRates()

# Function to perform the conversion
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_combobox.get()
    to_currency = to_combobox.get()
    converted_amount = converter.convert(from_currency, to_currency, amount)
    result_label.config(text=f"Converted Amount: {converted_amount}")

# Create the amount entry field
amount_label = ttk.Label(window, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5)
amount_entry = ttk.Entry(window)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# Create the "From" currency combobox
from_label = ttk.Label(window, text="From:")
from_label.grid(row=1, column=0, padx=5, pady=5)
from_combobox = ttk.Combobox(window, values=["USD", "EUR", "INR"])
from_combobox.grid(row=1, column=1, padx=5, pady=5)
from_combobox.current(0)

# Create the "To" currency combobox
to_label = ttk.Label(window, text="To:")
to_label.grid(row=2, column=0, padx=5, pady=5)
to_combobox = ttk.Combobox(window, values=["USD", "EUR", "INR"])
to_combobox.grid(row=2, column=1, padx=5, pady=5)
to_combobox.current(1)

# Create the convert button
convert_button = ttk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create the result label
result_label = ttk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
