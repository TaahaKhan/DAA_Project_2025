import customtkinter as ctk
import os
from algorithms.closest_pair import closest_pair
from algorithms.karatsuba_str import multiply
from parsers.parse_points import parse_points_file
from parsers.parse_bigints import parse_bigint_file


# GLOBAL UI CONFIG 
ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("green")  



# Button 

class CuteButton(ctk.CTkButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(
            master,
            corner_radius=18,
            height=45,
            font=("Helvetica", 15, "bold"),
            fg_color="#8AB5E8",       
            hover_color="#6F9DD1",    
            text_color="white",
            **kwargs
        )



#  Card Frame

class Card(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(
            master,
            corner_radius=20,
            fg_color="#ffffff",
            border_color="#C9D9F0",
            border_width=2,
            **kwargs
        )



# MAIN MENU

class MainMenu(ctk.CTkFrame):
    def __init__(self, master, switch_page):
        super().__init__(master)
        self.switch_page = switch_page

        # Gradient-style pseudo header
        header = ctk.CTkFrame(self, fg_color="#AEC8F2", corner_radius=0)
        header.pack(fill="x")
        ctk.CTkLabel(
            header,
            text="✨ Divide & Conquer Visual Runner ✨",
            font=("Helvetica", 26, "bold"),
            text_color="white"
        ).pack(pady=25)

        # Center card
        # --- FIX APPLIED HERE ---
        card = Card(self, width=400, height=300) # Set fixed size
        card.pack_propagate(False)               # Prevent shrinking
        card.pack(pady=60, padx=40)

        ctk.CTkLabel(card, text="Choose Algorithm",
                     font=("Helvetica", 20, "bold")).pack(pady=(30, 20))

        CuteButton(card, text="Closest Pair of Points",
                   width=280,
                   command=lambda: switch_page("closest")).pack(pady=15)

        CuteButton(card, text="Karatsuba Multiplication",
                   width=280,
                   command=lambda: switch_page("karatsuba")).pack(pady=15)


 
# FILE SELECTION PAGE

class FileSelection(ctk.CTkFrame):
    def __init__(self, master, switch_page, algo):
        super().__init__(master)

        folder = "closest_inputs" if algo == "closest" else "karatsuba_string_inputs"

        header = ctk.CTkFrame(self, fg_color="#AEC8F2", corner_radius=0)
        header.pack(fill="x")
        ctk.CTkLabel(
            header,
            text=f"Select Input File — { 'Closest Pair' if algo=='closest' else 'Karatsuba' }",
            font=("Helvetica", 24, "bold"),
            text_color="white"
        ).pack(pady=25)

        card = Card(self)
        card.pack(pady=40, padx=60)

        self.files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])

        for fname in self.files:
            CuteButton(
                card,
                text=fname,
                width=320,
                command=lambda f=fname: switch_page("result", algo, f)
            ).pack(pady=8)



# RESULT PAGE

class ResultPage(ctk.CTkFrame):
    def __init__(self, master, algo, filename, switch_page):
        super().__init__(master)

        folder = "closest_inputs" if algo == "closest" else "karatsuba_string_inputs"
        filepath = os.path.join(folder, filename)

        # Header
        header = ctk.CTkFrame(self, fg_color="#AEC8F2", corner_radius=0)
        header.pack(fill="x")
        ctk.CTkLabel(
            header,
            text=f"Results — {filename}",
            font=("Helvetica", 24, "bold"),
            text_color="white"
        ).pack(pady=25)

        # Main content card
        card = Card(self)
        card.pack(pady=30, padx=40)

        # Columns layout
        input_box = ctk.CTkTextbox(card, width=330, height=380,
                                   font=("Consolas", 12), corner_radius=15)
        input_box.grid(row=0, column=0, padx=20, pady=20)

        output_box = ctk.CTkTextbox(card, width=330, height=380,
                                    font=("Consolas", 12), corner_radius=15)
        output_box.grid(row=0, column=1, padx=20, pady=20)

        # Fill input text
        with open(filepath, "r") as f:
            input_box.insert("1.0", f.read())

        # Compute output
        if algo == "closest":
            points = parse_points_file(filepath)
            result = closest_pair(points)
            output_box.insert("1.0", f"Closest Pair Distance:\n{result}")
        else:
            A, B = parse_bigint_file(filepath)
            result = multiply(A, B)
            output_box.insert("1.0", f"Product:\n{result}")

        # Back button
        CuteButton(self, text="⟵  Back to Home",
                   command=lambda: switch_page("home")).pack(pady=20)



# APP CONTROLLER

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Algo")
        self.geometry("900x700")

        self.current_page = None
        self.show("home")

    def show(self, page, algo=None, fname=None):
        if self.current_page:
            self.current_page.destroy()

        if page == "home":
            self.current_page = MainMenu(self, self.show)
        elif page == "closest":
            self.current_page = FileSelection(self, self.show, "closest")
        elif page == "karatsuba":
            self.current_page = FileSelection(self, self.show, "karatsuba")
        elif page == "result":
            self.current_page = ResultPage(self, algo, fname, self.show)

        self.current_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    App().mainloop()