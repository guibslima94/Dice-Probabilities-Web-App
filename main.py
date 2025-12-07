import tkinter as tk
from tkinter import messagebox
import math

class DiceProbabilityApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Probability App")
        self.geometry("400x300")  # Set explicit window size
        
        # Create variables to store input values
        self.num_dices = tk.IntVar()
        self.target_value = tk.IntVar()
        self.num_dices_reaching_target = tk.IntVar()
        
        # Create label and entry widgets for input values with padding
        tk.Label(self, text="Number of Dices:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        tk.Entry(self, textvariable=self.num_dices).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Target Value:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        tk.Entry(self, textvariable=self.target_value).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Number of Dices Reaching Target:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        tk.Entry(self, textvariable=self.num_dices_reaching_target).grid(row=2, column=1, padx=10, pady=5)
        
        # Create buttons for calculating probability and displaying the last run
        tk.Button(self, text="Calculate Probability", command=self.calculate_probability).grid(row=3, column=0, columnspan=2, pady=10)
        self.last_run_label = tk.Label(self, text="Last Run: N/A")
        self.last_run_label.grid(row=4, column=0, columnspan=2, pady=10)
    
    def calculate_probability(self):
        try:
            num_dices = self.num_dices.get()
            target_value = self.target_value.get()
            num_dices_reaching_target = self.num_dices_reaching_target.get()
            
            probability = calculate_dice_probability(num_dices, target_value, num_dices_reaching_target)
            messagebox.showinfo("Probability Result", f"The probability is: {probability:.2f}")
            self.last_run_label.configure(text=f"Last Run: Probability = {probability:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def calculate_dice_probability(number_of_dice, target_value, num_dices_reaching_target):
    num_faces = 6
    successful_outcomes = num_faces - target_value + 1
    total_outcomes = num_faces ** number_of_dice
    probability = sum(comb(number_of_dice, i) * (successful_outcomes ** i) * ((num_faces - successful_outcomes) ** (number_of_dice - i))
                      for i in range(num_dices_reaching_target, number_of_dice + 1)) / total_outcomes
    return probability

def comb(n, r):
    return math.comb(n, r)

if __name__ == "__main__":
    app = DiceProbabilityApp()
    app.mainloop()
