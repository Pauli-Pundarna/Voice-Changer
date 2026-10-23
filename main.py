import tkinter as tk
from tkinter import ttk
import sounddevice as sd


def find_microphones():
    microphones = []
    for device in sd.query_devices():
        if device["max_input_channels"] > 0:
            microphones.append(device["name"])
    return microphones


def main():
    window = tk.Tk()
    window.title("VoiceBox")
    window.geometry("700x400")

    # Input: välj mikrofon (vänster kolumn)
    tk.Label(window, text="Input (mikrofon):").grid(row=0, column=0, padx=20, pady=20)
    microphones = find_microphones()
    input_select = ttk.Combobox(window, values=microphones, state="readonly", width=35)
    if microphones:
        input_select.current(0)
    input_select.grid(row=1, column=0, padx=20)

    # Output: inget kan väljas än (höger kolumn)
    tk.Label(window, text="Output:").grid(row=0, column=1, padx=20, pady=20)
    output_select = ttk.Combobox(window, values=[], state="disabled", width=35)
    output_select.grid(row=1, column=1, padx=20)

    window.mainloop()


if __name__ == "__main__":
    main()
