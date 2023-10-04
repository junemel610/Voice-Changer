import tkinter as tk
from tkinter import filedialog
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

class VoiceChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Changer App")

        self.file_path = None

        # Create UI elements
        self.label = tk.Label(root, text="Select an audio file:")
        self.label.pack()

        self.open_file_button = tk.Button(root, text="Open", command=self.open_file_dialog)
        self.open_file_button.pack()

        self.pitch_scale_label = tk.Label(root, text="Pitch Scaling Factor:")
        self.pitch_scale_label.pack()

        self.pitch_scale_entry = tk.Entry(root)
        self.pitch_scale_entry.insert(0, "1.0")
        self.pitch_scale_entry.pack()

        self.change_pitch_button = tk.Button(root, text="Change Pitch", command=self.change_pitch)
        self.change_pitch_button.pack()

    def open_file_dialog(self):
        self.file_path = filedialog.askopenfilename()
        self.label.config(text=f"Selected File: {self.file_path}")

    def change_pitch(self):
        if self.file_path is not None:
            try:
                pitch_scale_factor = float(self.pitch_scale_entry.get())
                changed_audio_path = self.apply_pitch_scaling(self.file_path, pitch_scale_factor)
                tk.messagebox.showinfo("Success", "Pitch changed successfully!")
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid pitch scaling factor. Please enter a valid number.")
        else:
            tk.messagebox.showerror("Error", "Please select an audio file first.")

    def apply_pitch_scaling(self, audio_path, factor):
        # Load audio file
        y, sr = librosa.load(audio_path)

        # Apply pitch scaling
        y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=factor)

        # Save the changed audio
        changed_audio_path = "changed_audio.wav"
        librosa.output.write_wav(changed_audio_path, y_shifted, sr)
        
        return changed_audio_path

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceChangerApp(root)
    root.mainloop()
