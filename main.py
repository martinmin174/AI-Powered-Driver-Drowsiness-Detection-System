import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

# Function to run blink detection script
def run_blink_detection():
    try:
        subprocess.call(["python", "blinkDetect.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run blink detection:\n{e}")

def main():
    root = tk.Tk()
    root.title("Driver Drowsiness Detection - Blink Detection")
    root.geometry("800x500")
    root.configure(bg="#1e1e2e")  # Dark background

    # Title label
    title_label = tk.Label(
        root,
        text="AI-Powered Driver Drowsiness Detection System",
        font=("Segoe UI", 22, "bold"),
        fg="#ffffff",
        bg="#1e1e2e"
    )
    title_label.pack(pady=30)

    # Frame for buttons
    frame = tk.Frame(root, bg="#1e1e2e")
    frame.pack(expand=True)

    # Style for modern buttons
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "Modern.TButton",
        font=("Segoe UI", 14, "bold"),
        foreground="#ffffff",
        background="#3b82f6",
        padding=15,
        relief="flat"
    )
    style.map(
        "Modern.TButton",
        background=[("active", "#2563eb")],
        relief=[("pressed", "flat")]
    )

    # Blink detection button
    btn_blink = ttk.Button(frame, text="Start Blink Detection", style="Modern.TButton", command=run_blink_detection)
    btn_blink.grid(row=0, column=0, padx=20, pady=20)

    # Quit button (different color)
    style.configure(
        "Quit.TButton",
        font=("Segoe UI", 14, "bold"),
        foreground="#ffffff",
        background="#ef4444",
        padding=15,
        relief="flat"
    )
    style.map(
        "Quit.TButton",
        background=[("active", "#dc2626")]
    )

    btn_quit = ttk.Button(frame, text="Quit", style="Quit.TButton", command=root.destroy)
    btn_quit.grid(row=0, column=1, padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
