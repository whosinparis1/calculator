import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sympy import symbols, diff, integrate, limit, sympify, simplify, latex
from sympy.utilities.lambdify import lambdify
import math
import re

class CalculusCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculus Calculator")
        self.root.geometry("1000x700")
        
        # Initialize symbol
        self.x = symbols('x')
        
        self.setup_gui()
    
    def setup_gui(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for different sections
        self.calculus_frame = ttk.Frame(self.notebook)
        self.graphing_frame = ttk.Frame(self.notebook)
        self.trig_frame = ttk.Frame(self.notebook)
        self.aviation_frame = ttk.Frame(self.notebook)
        self.basic_math_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.calculus_frame, text="Calculus")
        self.notebook.add(self.graphing_frame, text="Graphing")
        self.notebook.add(self.trig_frame, text="Trigonometry")
        self.notebook.add(self.aviation_frame, text="Aviation")
        self.notebook.add(self.basic_math_frame, text="Basic Math")
        
        self.setup_calculus_tab()
        self.setup_graphing_tab()
        self.setup_trig_tab()
        self.setup_aviation_tab()
        self.setup_basic_math_tab()
        
        # Results display
        self.setup_results_area()
    
    def setup_calculus_tab(self):
        # Derivative Section
        ttk.Label(self.calculus_frame, text="Derivative", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=(10,5))
        
        ttk.Label(self.calculus_frame, text="Function f(x):").grid(row=1, column=0, sticky='w')
        self.deriv_entry = ttk.Entry(self.calculus_frame, width=30)
        self.deriv_entry.grid(row=1, column=1, padx=5, pady=2)
        self.deriv_entry.insert(0, "x**2 + sin(x)")
        
        ttk.Label(self.calculus_frame, text="Evaluate at x = (optional):").grid(row=2, column=0, sticky='w')
        self.deriv_point_entry = ttk.Entry(self.calculus_frame, width=10)
        self.deriv_point_entry.grid(row=2, column=1, sticky='w', padx=5, pady=2)
        
        ttk.Button(self.calculus_frame, text="Calculate Derivative", 
                  command=self.calculate_derivative).grid(row=3, column=0, columnspan=2, pady=5)
        
        # Integral Section
        ttk.Label(self.calculus_frame, text="Integral", font=('Arial', 12, 'bold')).grid(row=4, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.calculus_frame, text="Function f(x):").grid(row=5, column=0, sticky='w')
        self.integral_entry = ttk.Entry(self.calculus_frame, width=30)
        self.integral_entry.grid(row=5, column=1, padx=5, pady=2)
        self.integral_entry.insert(0, "x**2")
        
        ttk.Label(self.calculus_frame, text="Lower limit (definite):").grid(row=6, column=0, sticky='w')
        self.lower_limit_entry = ttk.Entry(self.calculus_frame, width=10)
        self.lower_limit_entry.grid(row=6, column=1, sticky='w', padx=5, pady=2)
        
        ttk.Label(self.calculus_frame, text="Upper limit (definite):").grid(row=7, column=0, sticky='w')
        self.upper_limit_entry = ttk.Entry(self.calculus_frame, width=10)
        self.upper_limit_entry.grid(row=7, column=1, sticky='w', padx=5, pady=2)
        
        ttk.Button(self.calculus_frame, text="Calculate Indefinite Integral", 
                  command=lambda: self.calculate_integral('indefinite')).grid(row=8, column=0, pady=5)
        ttk.Button(self.calculus_frame, text="Calculate Definite Integral", 
                  command=lambda: self.calculate_integral('definite')).grid(row=8, column=1, pady=5)
        
        # Limit Section
        ttk.Label(self.calculus_frame, text="Limit", font=('Arial', 12, 'bold')).grid(row=9, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.calculus_frame, text="Function f(x):").grid(row=10, column=0, sticky='w')
        self.limit_entry = ttk.Entry(self.calculus_frame, width=30)
        self.limit_entry.grid(row=10, column=1, padx=5, pady=2)
        self.limit_entry.insert(0, "sin(x)/x")
        
        ttk.Label(self.calculus_frame, text="x approaches:").grid(row=11, column=0, sticky='w')
        self.limit_point_entry = ttk.Entry(self.calculus_frame, width=10)
        self.limit_point_entry.grid(row=11, column=1, sticky='w', padx=5, pady=2)
        self.limit_point_entry.insert(0, "0")
        
        ttk.Button(self.calculus_frame, text="Calculate Limit", 
                  command=self.calculate_limit).grid(row=12, column=0, columnspan=2, pady=5)
        
        # Simplify Section
        ttk.Label(self.calculus_frame, text="Simplify Expression", font=('Arial', 12, 'bold')).grid(row=13, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.calculus_frame, text="Expression:").grid(row=14, column=0, sticky='w')
        self.simplify_entry = ttk.Entry(self.calculus_frame, width=30)
        self.simplify_entry.grid(row=14, column=1, padx=5, pady=2)
        self.simplify_entry.insert(0, "(x+1)**2 - x**2")
        
        ttk.Button(self.calculus_frame, text="Simplify", 
                  command=self.simplify_expression).grid(row=15, column=0, columnspan=2, pady=5)
    
    def setup_graphing_tab(self):
        ttk.Label(self.graphing_frame, text="Function Graphing", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=(10,5))
        
        ttk.Label(self.graphing_frame, text="Function f(x):").grid(row=1, column=0, sticky='w')
        self.graph_entry = ttk.Entry(self.graphing_frame, width=30)
        self.graph_entry.grid(row=1, column=1, padx=5, pady=2)
        self.graph_entry.insert(0, "sin(x)")
        
        ttk.Label(self.graphing_frame, text="X Min:").grid(row=2, column=0, sticky='w')
        self.xmin_entry = ttk.Entry(self.graphing_frame, width=10)
        self.xmin_entry.grid(row=2, column=1, sticky='w', padx=5, pady=2)
        self.xmin_entry.insert(0, "-10")
        
        ttk.Label(self.graphing_frame, text="X Max:").grid(row=3, column=0, sticky='w')
        self.xmax_entry = ttk.Entry(self.graphing_frame, width=10)
        self.xmax_entry.grid(row=3, column=1, sticky='w', padx=5, pady=2)
        self.xmax_entry.insert(0, "10")
        
        ttk.Button(self.graphing_frame, text="Plot Function", 
                  command=self.plot_function).grid(row=4, column=0, columnspan=2, pady=10)
    
    def setup_trig_tab(self):
        # Degrees/Radians Conversion
        ttk.Label(self.trig_frame, text="Angle Conversion", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=(10,5))
        
        ttk.Label(self.trig_frame, text="Value:").grid(row=1, column=0, sticky='w')
        self.angle_entry = ttk.Entry(self.trig_frame, width=15)
        self.angle_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(self.trig_frame, text="Degrees → Radians", 
                  command=self.deg_to_rad).grid(row=2, column=0, pady=5)
        ttk.Button(self.trig_frame, text="Radians → Degrees", 
                  command=self.rad_to_deg).grid(row=2, column=1, pady=5)
        
        # Right Triangle
        ttk.Label(self.trig_frame, text="Right Triangle", font=('Arial', 12, 'bold')).grid(row=3, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.trig_frame, text="Adjacent:").grid(row=4, column=0, sticky='w')
        self.adj_entry = ttk.Entry(self.trig_frame, width=10)
        self.adj_entry.grid(row=4, column=1, padx=5, pady=2)
        
        ttk.Label(self.trig_frame, text="Opposite:").grid(row=5, column=0, sticky='w')
        self.opp_entry = ttk.Entry(self.trig_frame, width=10)
        self.opp_entry.grid(row=5, column=1, padx=5, pady=2)
        
        ttk.Button(self.trig_frame, text="Calculate Hypotenuse", 
                  command=self.calculate_hypotenuse).grid(row=6, column=0, columnspan=2, pady=5)
        
        # Trig Functions
        ttk.Label(self.trig_frame, text="Trigonometric Functions", font=('Arial', 12, 'bold')).grid(row=7, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.trig_frame, text="Angle (degrees):").grid(row=8, column=0, sticky='w')
        self.trig_angle_entry = ttk.Entry(self.trig_frame, width=10)
        self.trig_angle_entry.grid(row=8, column=1, padx=5, pady=2)
        
        ttk.Button(self.trig_frame, text="sin(x)", 
                  command=lambda: self.calculate_trig('sin')).grid(row=9, column=0, pady=2)
        ttk.Button(self.trig_frame, text="cos(x)", 
                  command=lambda: self.calculate_trig('cos')).grid(row=9, column=1, pady=2)
        ttk.Button(self.trig_frame, text="tan(x)", 
                  command=lambda: self.calculate_trig('tan')).grid(row=10, column=0, pady=2)
        
        # Descent Rate
        ttk.Label(self.trig_frame, text="3° Descent Rate", font=('Arial', 12, 'bold')).grid(row=11, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.trig_frame, text="Groundspeed (knots):").grid(row=12, column=0, sticky='w')
        self.gs_entry = ttk.Entry(self.trig_frame, width=10)
        self.gs_entry.grid(row=12, column=1, padx=5, pady=2)
        
        ttk.Button(self.trig_frame, text="Calculate Descent Rate", 
                  command=self.calculate_descent_rate).grid(row=13, column=0, columnspan=2, pady=5)
    
    def setup_aviation_tab(self):
        # Vref Speed
        ttk.Label(self.aviation_frame, text="Vref Speed Calculator", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=(10,5))
        
        ttk.Label(self.aviation_frame, text="Stall Speed:").grid(row=1, column=0, sticky='w')
        self.stall_entry = ttk.Entry(self.aviation_frame, width=10)
        self.stall_entry.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(self.aviation_frame, text="Headwind:").grid(row=2, column=0, sticky='w')
        self.headwind_entry = ttk.Entry(self.aviation_frame, width=10)
        self.headwind_entry.grid(row=2, column=1, padx=5, pady=2)
        
        ttk.Label(self.aviation_frame, text="Gust Factor:").grid(row=3, column=0, sticky='w')
        self.gust_entry = ttk.Entry(self.aviation_frame, width=10)
        self.gust_entry.grid(row=3, column=1, padx=5, pady=2)
        
        ttk.Button(self.aviation_frame, text="Calculate Vref", 
                  command=self.calculate_vref).grid(row=4, column=0, columnspan=2, pady=5)
        
        # Fuel Factor
        ttk.Label(self.aviation_frame, text="Fuel Factor Calculator", font=('Arial', 12, 'bold')).grid(row=5, column=0, sticky='w', pady=(20,5))
        
        ttk.Label(self.aviation_frame, text="Flight Distance (NM):").grid(row=6, column=0, sticky='w')
        self.distance_entry = ttk.Entry(self.aviation_frame, width=10)
        self.distance_entry.grid(row=6, column=1, padx=5, pady=2)
        
        ttk.Button(self.aviation_frame, text="Calculate Fuel Factor", 
                  command=self.calculate_fuel_factor).grid(row=7, column=0, columnspan=2, pady=5)
    
    def setup_basic_math_tab(self):
        ttk.Label(self.basic_math_frame, text="Basic Math Calculator", font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=(10,5))
        
        ttk.Label(self.basic_math_frame, text="Expression:").grid(row=1, column=0, sticky='w')
        self.math_entry = ttk.Entry(self.basic_math_frame, width=30)
        self.math_entry.grid(row=1, column=1, padx=5, pady=2)
        self.math_entry.insert(0, "2 + 3 * 4")
        
        ttk.Button(self.basic_math_frame, text="Calculate", 
                  command=self.calculate_basic_math).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Example expressions
        examples = [
            "2 + 3 * 4",
            "sqrt(16)",
            "math.sin(math.pi/2)",
            "2**8",
            "math.log(100, 10)"
        ]
        
        ttk.Label(self.basic_math_frame, text="Try these examples:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky='w', pady=(20,5))
        
        for i, example in enumerate(examples):
            btn = ttk.Button(self.basic_math_frame, text=example, 
                           command=lambda ex=example: self.math_entry.delete(0, tk.END) or self.math_entry.insert(0, ex))
            btn.grid(row=4+i, column=0, columnspan=2, pady=2, sticky='ew')
    
    def setup_results_area(self):
        # Results text area
        ttk.Label(self.root, text="Results:", font=('Arial', 11, 'bold')).pack(anchor='w', padx=10)
        
        self.results_text = scrolledtext.ScrolledText(self.root, height=15, width=100)
        self.results_text.pack(fill='both', expand=True, padx=10, pady=5)
        self.results_text.config(state=tk.DISABLED)
    
    def preprocess_expression(self, expr_str):
        """Preprocess the expression string for sympy"""
        expr_str = expr_str.strip()
        if '=' in expr_str:
            expr_str = expr_str.split('=')[1].strip()
        
        expr_str = expr_str.replace('^', '**')
        expr_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr_str)
        
        return expr_str
    
    def add_result(self, result):
        """Add result to the results text area"""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.insert(tk.END, result + '\n' + '-'*50 + '\n')
        self.results_text.see(tk.END)
        self.results_text.config(state=tk.DISABLED)
    
    def calculate_derivative(self):
        try:
            expr_str = self.preprocess_expression(self.deriv_entry.get())
            expr = sympify(expr_str)
            derivative_result = diff(expr, self.x)
            
            point_str = self.deriv_point_entry.get().strip()
            if point_str:
                point = float(point_str)
                value = derivative_result.subs(self.x, point)
                result = f"Derivative: {derivative_result}\nValue at x={point}: {value}"
            else:
                result = f"Derivative: {derivative_result}"
            
            self.add_result(result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating derivative: {e}")
    
    def calculate_integral(self, integral_type):
        try:
            expr_str = self.preprocess_expression(self.integral_entry.get())
            expr = sympify(expr_str)
            
            if integral_type == 'indefinite':
                result = integrate(expr, self.x)
                self.add_result(f"Indefinite Integral: {result} + C")
            else:
                lower = float(self.lower_limit_entry.get())
                upper = float(self.upper_limit_entry.get())
                result = integrate(expr, (self.x, lower, upper))
                self.add_result(f"Definite Integral from {lower} to {upper}: {result}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating integral: {e}")
    
    def calculate_limit(self):
        try:
            expr_str = self.preprocess_expression(self.limit_entry.get())
            expr = sympify(expr_str)
            val = float(self.limit_point_entry.get())
            result = limit(expr, self.x, val)
            self.add_result(f"Limit as x → {val}: {result}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating limit: {e}")
    
    def simplify_expression(self):
        try:
            expr_str = self.preprocess_expression(self.simplify_entry.get())
            expr = sympify(expr_str)
            simplified = simplify(expr)
            self.add_result(f"Original: {expr}\nSimplified: {simplified}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error simplifying expression: {e}")
    
    def plot_function(self):
        try:
            func_input = self.graph_entry.get().strip()
            func = sympify(self.preprocess_expression(func_input))
            f = lambdify(self.x, func, 'numpy')
            
            x_min = float(self.xmin_entry.get())
            x_max = float(self.xmax_entry.get())
            
            x_vals = np.linspace(x_min, x_max, 400)
            y_vals = f(x_vals)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x_vals, y_vals, 'b-', linewidth=2)
            ax.grid(True)
            ax.set_title(f"Graph of {func_input}")
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.axhline(y=0, color='k')
            ax.axvline(x=0, color='k')
            
            plt.show()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error plotting function: {e}")
    
    def deg_to_rad(self):
        try:
            deg = float(self.angle_entry.get())
            rad = math.radians(deg)
            self.add_result(f"{deg}° = {rad:.6f} radians")
        except Exception as e:
            messagebox.showerror("Error", f"Error converting degrees to radians: {e}")
    
    def rad_to_deg(self):
        try:
            rad = float(self.angle_entry.get())
            deg = math.degrees(rad)
            self.add_result(f"{rad} radians = {deg:.6f}°")
        except Exception as e:
            messagebox.showerror("Error", f"Error converting radians to degrees: {e}")
    
    def calculate_hypotenuse(self):
        try:
            adj = float(self.adj_entry.get())
            opp = float(self.opp_entry.get())
            hyp = math.hypot(adj, opp)
            self.add_result(f"Hypotenuse = {hyp:.6f}")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating hypotenuse: {e}")
    
    def calculate_trig(self, func_name):
        try:
            angle = float(self.trig_angle_entry.get())
            rad = math.radians(angle)
            funcs = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan}
            result = funcs[func_name](rad)
            self.add_result(f"{func_name}({angle}°) = {result:.6f}")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating {func_name}: {e}")
    
    def calculate_descent_rate(self):
        try:
            gs = float(self.gs_entry.get())
            descent = gs * 100 * math.tan(math.radians(3))
            self.add_result(f"Descent rate for {gs} knots = {descent:.1f} ft/min")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating descent rate: {e}")
    
    def calculate_vref(self):
        try:
            stallspeed = float(self.stall_entry.get())
            headwind = float(self.headwind_entry.get())
            gust = float(self.gust_entry.get())
            vref = 1.3 * stallspeed + (headwind / 2) + gust
            self.add_result(f"Vref speed = {vref:.2f} knots")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating Vref: {e}")
    
    def calculate_fuel_factor(self):
        try:
            distance = float(self.distance_entry.get())
            if distance < 500:
                factor = "P20–P30"
            elif distance < 1500:
                factor = "P30–P50"
            else:
                factor = "P50–P80"
            self.add_result(f"For {distance} NM flight, use {factor}")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating fuel factor: {e}")
    
    def calculate_basic_math(self):
        try:
            # Safe evaluation of basic math expressions
            expr = self.math_entry.get()
            # Replace common math functions
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('tan', 'math.tan')
            expr = expr.replace('log', 'math.log')
            expr = expr.replace('pi', 'math.pi')
            
            result = eval(expr, {"__builtins__": None}, {"math": math})
            self.add_result(f"{expr} = {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating expression: {e}")

def main():
    root = tk.Tk()
    app = CalculusCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()