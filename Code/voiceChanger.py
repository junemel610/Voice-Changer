import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

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
                changed_audio = self.apply_pitch_scaling(self.file_path, pitch_scale_factor)
                tk.messagebox.showinfo("Success", "Pitch changed successfully!")
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid pitch scaling factor. Please enter a valid number.")
        else:
            tk.messagebox.showerror("Error", "Please select an audio file first.")

    def apply_pitch_scaling(self, audio_path, factor):
        sound = AudioSegment.from_file(audio_path)
        sound = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * factor)
        })
        changed_audio_path = "changed_audio.wav"
        sound.export(changed_audio_path, format="wav")
        return changed_audio_path

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceChangerApp(root)
    root.mainloop()
