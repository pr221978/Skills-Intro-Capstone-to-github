import tkinter as tk
from tkinter import messagebox, ttk

# Data for travel recommendations
places = {
    "India": {
        "Wildlife Tourism": ["Jim Corbett", "Kanha National Park", "Ranthambore"],
        "Medical Tourism": ["Chennai", "Mumbai", "Delhi"],
        "Eco Tourism": ["Munnar", "Sundarbans", "Coorg"],
        "Cultural Tourism": ["Jaipur", "Varanasi", "Kolkata"],
        "Adventure Tourism": ["Manali", "Rishikesh", "Leh"],
        "Beach Tourism": ["Goa", "Pondicherry", "Andaman"]
    },
    "International": {
        "Wildlife Tourism": ["Kenya", "Tanzania", "South Africa"],
        "Medical Tourism": ["USA", "Germany", "Thailand"],
        "Eco Tourism": ["Costa Rica", "New Zealand", "Norway"],
        "Cultural Tourism": ["Italy", "France", "Egypt"],
        "Adventure Tourism": ["Switzerland", "Canada", "Nepal"],
        "Beach Tourism": ["Maldives", "Bali", "Hawaii"]
    }
}

# Estimated Costs
costs = {
    "Hotel": {"Budget": 2000, "Standard": 5000, "Luxury": 10000},
    "Food": 1000,
    "Flight": {"Domestic": 5000, "International": 30000},
    "Train": 2000,
    "Sightseeing": 2000,  # Extra per day
    "Local Transport": 500  # Extra per day
}

def calculate_budget():
    try:
        budget = int(budget_entry.get())
        days = int(days_entry.get())
        trip_type = trip_type_var.get()
        destination_type = destination_type_var.get()
        selected_place = place_var.get()
        hotel_choice = hotel_var.get()

        if trip_type == "National":
            travel_mode = transport_var.get()
            travel_cost = costs["Flight"]["Domestic"] if travel_mode == "Flight" else costs["Train"]
        else:
            travel_cost = costs["Flight"]["International"]
        
        hotel_cost = costs["Hotel"][hotel_choice] * days
        food_cost = costs["Food"] * days
        sightseeing_cost = costs["Sightseeing"] * days
        local_transport_cost = costs["Local Transport"] * days
        total_cost = hotel_cost + food_cost + sightseeing_cost + local_transport_cost + travel_cost

        result_text = (f"Destination: {selected_place}\n"
                       f"Hotel Type: {hotel_choice} (Rs. {costs['Hotel'][hotel_choice]} per night)\n"
                       f"Food Cost per day: Rs. {costs['Food']}\n"
                       f"Local Transport per day: Rs. {costs['Local Transport']}\n"
                       f"Travel Cost: Rs. {travel_cost}\n"
                       f"Sightseeing Cost: Rs. {sightseeing_cost}\n"
                       f"Total Estimated Cost: Rs. {total_cost}\n")
        
        if total_cost > budget:
            result_text += "⚠️ Warning: Your estimated budget exceeds your limit!"
        else:
            result_text += "✅ Your budget is sufficient for this trip."

        messagebox.showinfo("Travel Plan Summary", result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for budget and days.")

# GUI Setup
root = tk.Tk()
root.title("Travel Planner")
root.geometry("500x500")

# Budget Input
tk.Label(root, text="Enter your budget (INR):").pack()
budget_entry = tk.Entry(root)
budget_entry.pack()

# Trip Type
trip_type_var = tk.StringVar(value="National")
tk.Label(root, text="Select Trip Type:").pack()
tk.Radiobutton(root, text="National", variable=trip_type_var, value="India").pack()
tk.Radiobutton(root, text="International", variable=trip_type_var, value="International").pack()

# Number of Days
tk.Label(root, text="Number of Days:").pack()
days_entry = tk.Entry(root)
days_entry.pack()

# Destination Type
tk.Label(root, text="Select Destination Type:").pack()
destination_type_var = tk.StringVar()
destination_dropdown = ttk.Combobox(root, textvariable=destination_type_var, values=list(places["India"].keys()))
destination_dropdown.pack()

def update_places(*args):
    trip_type = trip_type_var.get()
    destination_type = destination_type_var.get()
    
    if trip_type and destination_type:
        place_dropdown["values"] = places[trip_type][destination_type]

destination_dropdown.bind("<<ComboboxSelected>>", update_places)

# Place Selection
tk.Label(root, text="Select Place:").pack()
place_var = tk.StringVar()
place_dropdown = ttk.Combobox(root, textvariable=place_var)
place_dropdown.pack()

# Hotel Selection
tk.Label(root, text="Select Hotel Type:").pack()
hotel_var = tk.StringVar(value="Budget")
hotel_dropdown = ttk.Combobox(root, textvariable=hotel_var, values=["Budget", "Standard", "Luxury"])
hotel_dropdown.pack()

# Transport Selection
tk.Label(root, text="Select Transport Mode (for National Trips):").pack()
transport_var = tk.StringVar(value="Flight")
transport_dropdown = ttk.Combobox(root, textvariable=transport_var, values=["Flight", "Train"])
transport_dropdown.pack()

# Calculate Budget Button
tk.Button(root, text="Calculate Budget", command=calculate_budget).pack()

root.mainloop()
