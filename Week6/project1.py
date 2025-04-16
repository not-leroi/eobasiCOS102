import tkinter as tk

def calculate_charge():
    location = location_var.get()
    weight = float(weight_entry.get())

    if location == "Ibeju-Lekki":
        if weight >= 10:
            charge = 5000
        else:
            charge = 3500
    elif location == "Epe":
        if weight >= 10:
            charge = 10000
        else:
            charge = 5000
    else:
        charge = 0

    result_label.config(text=f"Delivery Charge: ₦{charge}")


root = tk.Tk()
root.title("Simi Services Delivery Calculator")
root.geometry("400x300")


tk.Label(root, text="Select Location:").pack(pady=5)


location_var = tk.StringVar()
location_var.set("Ibeju-Lekki")
locations = ["Ibeju-Lekki", "Epe"]
tk.OptionMenu(root, location_var, *locations).pack(pady=5)


tk.Label(root, text="Enter Package Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=10)


result_label = tk.Label(root, text="Delivery Charge: ₦0")
result_label.pack(pady=10)


root.mainloop()
