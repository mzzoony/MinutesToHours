import tkinter as tk
from tkinter import ttk, messagebox


def minCal(minutes: float) -> float:
    return minutes / 60.0


def on_convert():
    raw = minutes_var.get().strip()
    if not raw:
        messagebox.showwarning("Input needed", "Please enter minutes.")
        return

    try:
        minutes = float(raw)
    except ValueError:
        messagebox.showerror("Invalid input", "Minutes must be a number (e.g., 37 or 37.5).")
        return

    if minutes < 0:
        messagebox.showerror("Invalid input", "Minutes cannot be negative.")
        return

    hours = minCal(minutes)
    result_var.set(f"{hours:.2f} hours")


def on_clear():
    minutes_var.set("")
    result_var.set("")


# ---- UI ----
root = tk.Tk()
root.title("Minutes → Hours Decimal")
root.resizable(False, False)

main = ttk.Frame(root, padding=16)
main.grid(row=0, column=0)

title = ttk.Label(main, text="Minutes → Hours Decimal", font=("Segoe UI", 14, "bold"))
title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

ttk.Label(main, text="Minutes:").grid(row=1, column=0, sticky="w")

minutes_var = tk.StringVar()
minutes_entry = ttk.Entry(main, textvariable=minutes_var, width=18)
minutes_entry.grid(row=1, column=1, sticky="w")
minutes_entry.focus()

convert_btn = ttk.Button(main, text="Convert", command=on_convert)
convert_btn.grid(row=1, column=2, padx=(10, 0))

ttk.Label(main, text="Result:").grid(row=2, column=0, sticky="w", pady=(10, 0))

result_var = tk.StringVar(value="")
result_label = ttk.Label(main, textvariable=result_var, font=("Segoe UI", 11))
result_label.grid(row=2, column=1, columnspan=2, sticky="w", pady=(10, 0))

clear_btn = ttk.Button(main, text="Clear", command=on_clear)
clear_btn.grid(row=3, column=0, pady=(14, 0), sticky="w")

quit_btn = ttk.Button(main, text="Quit", command=root.destroy)
quit_btn.grid(row=3, column=2, pady=(14, 0), sticky="e")

# Enter key triggers convert
root.bind("<Return>", lambda _e: on_convert())

root.mainloop()
