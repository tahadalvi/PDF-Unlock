import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter
import os

def unlock_pdf():
    password = password_entry.get().strip()
    if not password:
        messagebox.showerror("Error", "Please enter the password.")
        return

    file_path = filedialog.askopenfilename(
        title="Select Locked PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not file_path:
        return

    try:
        reader = PdfReader(file_path)
        if reader.is_encrypted:
            reader.decrypt(password)

        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        output_path = os.path.splitext(file_path)[0] + "_unlocked.pdf"
        with open(output_path, "wb") as f:
            writer.write(f)

        messagebox.showinfo("Success", f"PDF unlocked!\nSaved as:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to unlock PDF:\n{str(e)}")

# GUI setup
root = tk.Tk()
root.title("🔓 PDF Unlocker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter PDF Password", font=("Arial", 14)).pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)

unlock_btn = tk.Button(
    root,
    text="Select Locked PDF & Unlock",
    command=unlock_pdf,
    bg="green",
    fg="white",
    font=("Arial", 12),
    relief="raised",
    padx=10,
    pady=5
)
unlock_btn.pack(pady=20)

tk.Label(root, text="Made with ❤️ in Python", font=("Arial", 9), fg="gray").pack(side="bottom", pady=5)

root.mainloop()
