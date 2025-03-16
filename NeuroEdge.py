
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load dataset
file_path = "foodAllergenDataset.csv"
df = pd.read_csv(file_path)


# Check if required columns exist
if "Allergens" not in df.columns or "Alternative Suggestions" not in df.columns:
    raise ValueError("Required columns not found in dataset!")

# Create allergen-to-alternative mapping from dataset
allergen_mapping = {}

for _, row in df.dropna(subset=["Allergens", "Alternative Suggestions"]).iterrows():
    allergens = row["Allergens"].lower().split(", ")  # Convert to lowercase for consistency
    alternative = row["Alternative Suggestions"]

    for allergen in allergens:
        allergen_mapping[allergen] = alternative  # Store first found alternative

def check_allergens():
    user_input = entry.get().strip().lower()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter some ingredients!")
        return

    ingredients = user_input.split(", ")
    detected_allergens = [ing for ing in ingredients if ing in allergen_mapping]
    alternatives = {ing: allergen_mapping.get(ing, "No alternative found") for ing in ingredients}

    result_text.set(f"Detected Allergens: {', '.join(detected_allergens) if detected_allergens else 'None'}\n\n"
                    f"Alternatives:\n" + "\n".join([f"{k} → {v}" for k, v in alternatives.items()]))

# Tkinter UI setup
root = tk.Tk()
root.title("Allergen Detection System")
root.geometry("500x400")
root.configure(bg="lightblue")

# UI Elements
tk.Label(root, text="Enter Ingredients:", font=("Arial", 12), bg="lightblue").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Allergens", command=check_allergens, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="lightblue", justify="left", wraplength=450)
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()