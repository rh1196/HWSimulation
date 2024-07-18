import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np

class HardyWeinbergSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Hardy-Weinberg Simulation")
        
        self.q_label = tk.Label(root, text="Frequency of the recessive allele (q):")
        self.q_label.pack()
        self.q_entry = tk.Entry(root)
        self.q_entry.pack()
        
        self.num_steps_label = tk.Label(root, text="Number of generations to simulate:")
        self.num_steps_label.pack()
        self.num_steps_entry = tk.Entry(root)
        self.num_steps_entry.pack()
        
        self.initial_genotype_label = tk.Label(root, text="Initial genotype (aa, Aa, or AA):")
        self.initial_genotype_label.pack()
        self.initial_genotype_entry = tk.Entry(root)
        self.initial_genotype_entry.pack()
        
        self.simulate_button = tk.Button(root, text="Simulate", command=self.simulate)
        self.simulate_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def hardy_weinberg_simulation(self, initial_genotype, q, num_steps):
        p = 1 - q
        
        transition_matrix = {
            'aa': [q, p, 0],
            'Aa': [q / 2, 0.5, p / 2],
            'AA': [0, p, q]
        }
        
        state_labels = ['aa', 'Aa', 'AA']
        current_state = initial_genotype
        
        results = [current_state]
        for _ in range(num_steps):
            new_state_prob = transition_matrix[current_state]
            new_state = np.random.choice(state_labels, p=new_state_prob)
            current_state = new_state
            results.append(current_state)
        
        return results

    def simulate(self):
        try:
            q = float(self.q_entry.get())
            num_steps = int(self.num_steps_entry.get())
            initial_genotype = self.initial_genotype_entry.get()
            
            if initial_genotype not in ['aa', 'Aa', 'AA']:
                raise ValueError("Initial genotype must be 'aa', 'Aa', or 'AA'")
            
            results = self.hardy_weinberg_simulation(initial_genotype, q, num_steps)
            
            result_text = " -> ".join(results)
            self.result_label.config(text=f"Result: {result_text}")
            
            messagebox.showinfo("Simulation Complete", f"The final state after {num_steps} generations is: {results[-1]}")
        
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = HardyWeinbergSimulation(root)
    root.mainloop()
