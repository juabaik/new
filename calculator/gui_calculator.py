#!/usr/bin/env python3
"""
Graphical Calculator Application
A calculator with a graphical user interface using tkinter.
"""

import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("400x600")
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.current = "0"
        self.previous = None
        self.operation = None
        self.start_new = True
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg='#2c3e50')
        display_frame.pack(pady=20, padx=20, fill='x')
        
        # Display
        self.display = tk.Entry(
            display_frame, 
            font=('Arial', 24, 'bold'),
            bg='#ecf0f1',
            fg='#2c3e50',
            justify='right',
            bd=10,
            relief='flat'
        )
        self.display.insert(0, "0")
        self.display.pack(fill='x', padx=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Button style
        button_style = {
            'font': ('Arial', 18, 'bold'),
            'bd': 0,
            'relief': 'flat',
            'width': 4,
            'height': 2
        }
        
        # Number buttons
        numbers = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '.', '=']
        ]
        
        for i, row in enumerate(numbers):
            for j, num in enumerate(row):
                if num == '=':
                    btn = tk.Button(
                        button_frame, 
                        text=num, 
                        bg='#e74c3c',
                        fg='white',
                        command=lambda x=num: self.button_click(x),
                        **button_style
                    )
                else:
                    btn = tk.Button(
                        button_frame, 
                        text=num, 
                        bg='#3498db',
                        fg='white',
                        command=lambda x=num: self.button_click(x),
                        **button_style
                    )
                btn.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
        
        # Operation buttons
        operations = ['+', '-', '*', '/', 'C', '⌫', '√', '^']
        
        for i, op in enumerate(operations):
            if op == 'C':
                bg_color = '#e67e22'
            elif op == '⌫':
                bg_color = '#e74c3c'
            elif op in ['√', '^']:
                bg_color = '#9b59b6'
            else:
                bg_color = '#95a5a6'
            
            btn = tk.Button(
                button_frame,
                text=op,
                bg=bg_color,
                fg='white',
                command=lambda x=op: self.button_click(x),
                **button_style
            )
            btn.grid(row=i//2, column=j+1+(i%2), padx=5, pady=5, sticky='nsew')
        
        # Configure grid weights
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)
    
    def button_click(self, value):
        if value.isdigit() or value == '.':
            self.number_click(value)
        elif value in ['+', '-', '*', '/']:
            self.operation_click(value)
        elif value == '=':
            self.equals_click()
        elif value == 'C':
            self.clear_click()
        elif value == '⌫':
            self.backspace_click()
        elif value == '√':
            self.sqrt_click()
        elif value == '^':
            self.power_click()
    
    def number_click(self, value):
        if self.start_new:
            self.current = value
            self.start_new = False
        else:
            if value == '.' and '.' in self.current:
                return
            self.current += value
        self.update_display()
    
    def operation_click(self, value):
        if self.previous is not None and not self.start_new:
            self.equals_click()
        
        self.previous = float(self.current)
        self.operation = value
        self.start_new = True
    
    def equals_click(self):
        if self.previous is None or self.operation is None:
            return
        
        try:
            current = float(self.current)
            if self.operation == '+':
                result = self.previous + current
            elif self.operation == '-':
                result = self.previous - current
            elif self.operation == '*':
                result = self.previous * current
            elif self.operation == '/':
                if current == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = self.previous / current
            
            self.current = str(result)
            self.previous = None
            self.operation = None
            self.start_new = True
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clear_click(self):
        self.current = "0"
        self.previous = None
        self.operation = None
        self.start_new = True
        self.update_display()
    
    def backspace_click(self):
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
        self.update_display()
    
    def sqrt_click(self):
        try:
            value = float(self.current)
            if value < 0:
                messagebox.showerror("Error", "Cannot calculate square root of negative number!")
                return
            result = math.sqrt(value)
            self.current = str(result)
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def power_click(self):
        if self.previous is not None and not self.start_new:
            self.equals_click()
        
        self.previous = float(self.current)
        self.operation = '^'
        self.start_new = True
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()