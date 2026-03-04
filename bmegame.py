import tkinter as tk
import random
import os
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from time import sleep
from playsound import playsound


def randomize(class_1, class_2, path_to_icons, seed=None):
    first_year_courses = [
        "MAT 21A", "CHE 2A", "BIM 1",
        "GE/AP/IB", "GE/AP/IB"
    ]
    second_year_courses = [
        "MAT 21B", "CHE 2B", "BIS 2A",
        "MAT 21C", "CHE 2C", "PHY 9A",
        "MAT 21D", "CHE 8A/118A", "PHY 9B", "ENG 6"
    ]
    third_year_courses = [
        "MAT 22A/27A", "CHE 8B/118B", "PHY 9C",
        "MAT 22B/27B", "BIM 20", "BIM 20L", "ENG 17/17V",
        "BIM 105/MAT 107", "BIM 116/NPB 101"
    ]
    fourth_year_courses = [
        "BIM 106", "BIM 107", "ENG/EEC 100",
        "BIM 109", "BIM 111"
    ]
    above_courses = [
        "ENG 105", "ENG 190", "BIM 110"
    ]
    random.seed(seed)
    course_list = fourth_year_courses
    possible_avatars = os.listdir('./resources/icons/')
    avatar_1 = './resources/icons/hamster.png'
    avatar_2 = './resources/icons/frog.png'
    return course_list, avatar_1, avatar_2


def calculate_stats(grades, gpa, seed=None):
    random.seed(seed)
    # The fighter_stats should have the following elements:
    # attack: base attack power calculated by provided formula
    # defense: base defense power calculated by provided formula
    # Both attack and defense should be a tuple of 5 numbers.
    # skill: a tuple of four numbers, each being a probability
    # of a successful attack of a certain type
    # (0: heal, 1: light, 2: normal, 3: heavy)
    # speed: a number representing the speed of the fighter
    # combo: a percentage representing the combo probability
    # dodge: a percentage representing the dodge probability
    fighter_stats = {}
    return fighter_stats


def fighter_attack(attacker, course_no, seed=None):
    random.seed(seed)
    unmodified_damage = 0
    type_attack = 0
    return unmodified_damage, type_attack


def fighter_defend(defender, attack_power, course_no, seed=None):
    random.seed(seed)
    modified_damage = 0
    return modified_damage


def fight_a_round(fighter_1, fighter_2, messages, ses, update_text, seed=None):
    random.seed(seed)
    fighter_1_loss = 0
    fighter_2_loss = 0
    fight_string = ""
    return


def fight(fighter_1, fighter_2, messages, ses, update_text, seed=None):
    update_text(100, 100, "Fight started!\n")
    # Implement the main loop of the fight here!
    pass


class GameApp(tk.Frame):
    # Main GUI starts here
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.w = 512
        self.w_img = 96
        self.n_courses = 5
        self.base_font_size = 9
        self.base_width = 1100
        self.base_height = 800
        self.create_widgets()
        # Bind window resize event to scale fonts
        self.master.bind('<Configure>', self.on_window_resize)
        return super().__init__(master, cnf, **kw)

    def update_icon(self, fighter, f_name):
        fighter.icon = Image.open(f_name)
        fighter.icon_tk = ImageTk.PhotoImage(
            fighter.icon.resize((self.w_img, self.w_img))
        )
        fighter.icon_label = ttk.Label(fighter, image=fighter.icon_tk)
        fighter.icon_label.grid(
            row=2, rowspan=2,
            column=0, columnspan=2,
            sticky=tk.N + tk.S + tk.E + tk.W,
            padx=(self.w // 2 - self.w_img), pady=0)

    def update_text(self, hp_1, hp_2, string_to_append):
        hp_1_string = f"{hp_1:.2f}/100"
        hp_2_string = f"{hp_2:.2f}/100"
        self.fighter_1.hp_string.set(hp_1_string)
        self.fighter_2.hp_string.set(hp_2_string)
        self.fight_text.text.insert(tk.END, string_to_append)
        self.fight_text.text.see(tk.END)
        self.fight_text.text.update()

    def on_window_resize(self, event):
        # Only respond to resize events from the main window
        if event.widget != self.master:
            return

        # Calculate scaling factor based on window size
        current_width = self.master.winfo_width()
        current_height = self.master.winfo_height()

        width_scale = current_width / self.base_width
        height_scale = current_height / self.base_height
        scale_factor = min(width_scale, height_scale)

        # Calculate new font size (minimum of 8, maximum of 16)
        new_font_size = int(self.base_font_size * scale_factor)
        new_font_size = max(8, min(16, new_font_size))
        self.w_img = int(96 * scale_factor)
        self.fighter_1.icon_tk = ImageTk.PhotoImage(
            self.fighter_1.icon.resize((self.w_img, self.w_img))
        )
        self.fighter_1.icon_label.configure(image=self.fighter_1.icon_tk)
        self.fighter_2.icon_tk = ImageTk.PhotoImage(
            self.fighter_2.icon.resize((self.w_img, self.w_img))
        )
        self.fighter_2.icon_label.configure(image=self.fighter_2.icon_tk)

        # Update the style font
        self.style.configure('.', font=('TkDefaultFont', new_font_size))

        # Update Text widget font separately (not affected by ttk style)
        if hasattr(self, 'fight_text'):
            self.fight_text.text.configure(
                font=('TkDefaultFont', new_font_size))

    def create_fighter(self, fighter):
        for idx in range(self.n_courses + 8):
            fighter.rowconfigure(idx, weight=1)
        fighter.columnconfigure(0, weight=1)
        fighter.columnconfigure(1, weight=1)
        fighter.name_label = ttk.Label(fighter, text="Name:")
        fighter.name_label.grid(
            row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.name_box = ttk.Entry(fighter)
        fighter.name_box.grid(
            row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.class_label = ttk.Label(fighter, text="Class:")
        fighter.class_label.grid(
            row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.class_box = ttk.Combobox(fighter)
        fighter.class_box["values"] = (
            "1st year", "2nd year", "3rd year", "4th year", "5+th year")
        fighter.class_box.grid(
            row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.update_icon(fighter, "./resources/default/user.png")
        fighter.course_label = ttk.Label(fighter, text="Courses:")
        fighter.course_label.grid(
            row=5, column=0,
            sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.course_names = [None, None, None, None, None]
        fighter.course_name_labels = [None, None, None, None, None]
        for idx in range(self.n_courses):
            fighter.course_names[idx] = tk.StringVar()
            fighter.course_names[idx].set(f"Course {idx + 1}")
            fighter.course_name_labels[idx] = ttk.Label(
                fighter, textvariable=fighter.course_names[idx])
            fighter.course_name_labels[idx].grid(
                row=6 + idx, column=0,
                sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.courses = [None, None, None, None, None]
        for idx in range(self.n_courses):
            fighter.courses[idx] = ttk.Combobox(fighter, state=tk.DISABLED)
            fighter.courses[idx]["values"] = (
                "A+", "A", "A-", "B+", "B", "B-",
                "C+", "C", "C-", "D+", "D", "D-",
                "F", "NG", "Not Taken"
            )
            fighter.courses[idx].grid(
                row=6 + idx, column=1,
                sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.gpa_label = ttk.Label(fighter, text="GPA:",
                                      state=tk.DISABLED)
        fighter.gpa_label.grid(
            row=6 + self.n_courses, column=0,
            sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.gpa_box = ttk.Entry(fighter)
        fighter.gpa_box.grid(
            row=6 + self.n_courses, column=1,
            sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.hp_label = ttk.Label(fighter, text="HP:")
        fighter.hp_label.grid(
            row=7 + self.n_courses, column=0,
            sticky=tk.N + tk.S + tk.E + tk.W)
        fighter.hp_string = tk.StringVar()
        fighter.hp_string.set("100/100")
        fighter.hp_box = ttk.Entry(fighter, state=tk.DISABLED,
                                   textvariable=fighter.hp_string)
        fighter.hp_box.grid(
            row=7 + self.n_courses, column=1,
            sticky=tk.N + tk.S + tk.E + tk.W)

    def create_widgets(self):
        # Setting the top window which is not related to our application
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        # You may enable these lines if you have ttkthemes package
        self.style = ThemedStyle(self)
        self.style.set_theme_advanced("ubuntu", 1, 0.6, 0.7, True, None)

        # Set initial font size
        self.style.configure('.', font=('TkDefaultFont', self.base_font_size))

        # Create the main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(
            row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=self.n_courses + 8)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)

        # Create the information block
        self.helper = tk.LabelFrame(
            self, text="Play Guide", width=self.w)
        self.helper.rowconfigure(0, weight=1)
        self.helper.columnconfigure(0, weight=1)
        self.helper.grid(row=0, column=0,
                         sticky=tk.N + tk.S + tk.E + tk.W,
                         columnspan=2)
        self.helper.current_text = tk.StringVar()
        self.helper.current_text.set(
            "1. Input the name of the person and their class standing.\n" +
            "2. Click the 'Randomize!' Button to generate" +
            " a list of courses.\n" +
            "3. Input the grades corresponding to the courses" +
            " and the overall GPA\n" +
            "4. Click the 'Fight!' Button to start the game!")
        self.helper.help_widget = ttk.Label(
            self.helper, textvariable=self.helper.current_text)
        self.helper.help_widget.grid(
            row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Create the fighter one Canvas
        self.fighter_1 = tk.LabelFrame(
            self, text="Fighter 1", width=self.w)
        self.fighter_1.grid(
            row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.create_fighter(self.fighter_1)

        # Create the fighter two Canvas
        self.fighter_2 = tk.LabelFrame(
            self, text="Fighter 2", width=self.w)
        self.fighter_2.grid(
            row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.create_fighter(self.fighter_2)

        # Create fight text history
        self.fight_text = tk.LabelFrame(
            self, text="Fight History", width=self.w)
        self.fight_text.grid(
            row=2, column=0, columnspan=2,
            sticky=tk.N + tk.S + tk.E + tk.W)
        self.fight_text.rowconfigure(0, weight=1)
        self.fight_text.columnconfigure(0, weight=1)
        self.fight_text.text = tk.Text(
            self.fight_text, wrap=tk.WORD, state=tk.DISABLED)
        self.fight_text.text.grid(
            row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Build the button frame
        self.button_canvas = tk.Frame(self, width=self.w)
        self.button_canvas.grid(
            row=3, column=0, columnspan=2,
            sticky=tk.N + tk.S + tk.E + tk.W)
        self.button_canvas.rowconfigure(0, weight=1)
        self.button_canvas.rowconfigure(1, weight=1)
        self.button_canvas.columnconfigure(0, weight=1)
        self.button_canvas.columnconfigure(1, weight=1)

        # Build the Randomize! button
        self.button_canvas.randomize = ttk.Button(
            self.button_canvas, text="Randomize!", command=self.randomize)
        self.button_canvas.randomize.grid(
            row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.button_canvas.fight = ttk.Button(
            self.button_canvas, text="Fight!", command=self.fight)
        self.button_canvas.fight.grid(
            row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        # Build the quit button
        self.button_canvas.quit = ttk.Button(
            self.button_canvas, text="Quit", command=self.quit_app)
        self.button_canvas.quit.grid(
            row=1, column=0, columnspan=2,
            sticky=tk.N + tk.S + tk.E + tk.W)

    def randomize(self):
        # Call randomize function to get course lists
        class_1 = self.fighter_1.class_box.get()
        class_2 = self.fighter_2.class_box.get()
        course_list, avatar_1, avatar_2 = randomize(
            class_1, class_2, "./resources/icons/")
        # Update the course list and avatars
        for idx in range(5):
            self.fighter_1.course_names[idx].set(course_list[idx])
            self.fighter_2.course_names[idx].set(course_list[idx])
        self.update_icon(self.fighter_1, avatar_1)
        self.update_icon(self.fighter_2, avatar_2)
        # Enable the course comboboxes and GPA boxes
        self.fighter_1.gpa_label["state"] = tk.NORMAL
        self.fighter_2.gpa_label["state"] = tk.NORMAL
        for idx in range(5):
            self.fighter_1.courses[idx]["state"] = tk.NORMAL
            self.fighter_2.courses[idx]["state"] = tk.NORMAL

    def print_fighter_into(self, fighter):
        text_to_append = ''
        text_to_append += f"Name: {fighter['name']}\n"
        for idx in range(5):
            pass

    def fight(self):
        # Pack fighter information
        fighter_1 = {
            "name": self.fighter_1.name_box.get(),
            "courses": [self.fighter_1.courses[idx].get()
                        for idx in range(5)],
            "course_names": [self.fighter_1.course_names[idx].get()
                             for idx in range(5)],
            "gpa": self.fighter_1.gpa_box.get(),
            "hp": 100,
            "stats": {}
        }
        fighter_2 = {
            "name": self.fighter_2.name_box.get(),
            "courses": [self.fighter_2.courses[idx].get()
                        for idx in range(5)],
            "course_names": [self.fighter_2.course_names[idx].get()
                             for idx in range(5)],
            "gpa": self.fighter_2.gpa_box.get(),
            "hp": 100,
            "stats": {}
        }
        # Calculate stats
        fighter_1["stats"] = calculate_stats(
            fighter_1["courses"], fighter_1["gpa"])
        fighter_2["stats"] = calculate_stats(
            fighter_2["courses"], fighter_2["gpa"])
        self.fight_text.text["state"] = tk.NORMAL
        self.fight_text.text.delete(1.0, tk.END)
        self.text_path = "./resources/default/"
        self.se_path = "./resources/audio/"
        file_list = ['heal.txt', 'light.txt', 'normal.txt', 'heavy.txt']
        messages = [[] for elem in file_list]
        for idx, file in enumerate(file_list):
            with open(os.path.join(self.text_path, file), "r") as f:
                lines = f.readlines()
                for line in lines:
                    messages[idx].append(line.strip())
        ses = {
            "attack": [
                os.path.join(self.se_path, "attack-1.mp3"),
                os.path.join(self.se_path, "attack-2.mp3"),
                os.path.join(self.se_path, "attack-3.mp3")
            ],
            "block": os.path.join(self.se_path, "block.mp3"),
            "heal": os.path.join(self.se_path, "heal.mp3"),
            "dodge": os.path.join(self.se_path, "dodge.mp3"),
            "hit": os.path.join(self.se_path, "uhh.mp3"),
            "finish": os.path.join(self.se_path, "dud.mp3"),
        }
        fight(fighter_1, fighter_2, messages, ses, self.update_text)
        if fighter_1["hp"] <= 0:
            self.update_text(0, fighter_2["hp"], f"{fighter_2['name']} won!\n")
        else:
            self.update_text(fighter_1["hp"], 0, f"{fighter_1['name']} won!\n")
        playsound(ses["finish"])
        self.fight_text.text["state"] = tk.DISABLED

    def quit_app(self):
        self.destroy()
        exit(0)


def run_app():
    app = GameApp()
    app.master.title("The BIM Academic Fight Game!")

    # Get screen dimensions
    screen_width = app.master.winfo_screenwidth()
    screen_height = app.master.winfo_screenheight()

    # Set maximum window size to 90% of screen dimensions
    max_height = int(screen_height * 0.9)
    app.master.maxsize(screen_width, max_height)

    app.mainloop()


if __name__ == "__main__":
    run_app()
