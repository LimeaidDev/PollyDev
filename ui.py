import tempfile
import customtkinter
import subprocess
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")# Themes: "blue" (standard), "green", "dark-blue"
lock_file = ".lock"

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON)

        self.iconbitmap(default=ICON_PATH)

        def quit_me():
            self.quit()
            self.destroy()

        self.protocol("WM_DELETE_WINDOW", quit_me)
        # configure window
        self.title("Polly Canary")
        self.geometry(f"{1000}x{600}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Polly Canary", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Turn On", command=self.sidebar_button_event_on)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Turn Off", command=self.sidebar_button_event_off)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.discord_token_button = customtkinter.CTkButton(self, text="Set Discord Bot Token",
                                                           command=self.open_input_dialog_event_disc)
        self.discord_token_button.grid(row=1, column=0, padx=20, pady=20)
        self.open_ai_button = customtkinter.CTkButton(self, text="Set OpenAI API Key",
                                                           command=self.open_input_dialog_event_ai)
        self.open_ai_button.grid(row=2, column=0, padx=20, pady=20)
        self.textbox = customtkinter.CTkEntry(self)
        self.textbox = customtkinter.CTkTextbox(self, width=100)
        self.textbox.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox.yview_moveto(1.0)
        self.root = customtkinter.CTk()
        self.entry = customtkinter.CTkEntry(self)
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 180), pady=(20, 20), sticky="nsew")
        self.button = customtkinter.CTkButton(self, text="Send Command", command=self.send_command)
        self.button.grid(row=3, column=2, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox.configure(state="normal", font=('System', 13))
        self.update_textbox_from_file("data/settingsdata/text.txt")

    def send_command(self):
        content = self.entry.get()
        self.entry.delete(0, "end")
        try:
            command, value = content.split(" ", 1)
        except:
            command = content
            value = "None"
        if str(command) == "help":
            self.update_log("""Help
clearlogs - clears info logs
setbottemp <value> - Sets the bot temperature from 0-2""")
        if str(command) == "clearlogs":
            open("data/settingsdata/text.txt", "w+").write("")
        if str(command) == "setbottemp":
            try:
                if int(value) > 2 or int(value) < 0 :
                    self.update_log("[ERROR] Temperature range is from 0-2")
                else:
                    open("data/settingsdata/temp", "w+").write(value)
                    self.update_log(f"[INFO] Temperature set to {value}")
            except ValueError:
                self.update_log("[ERROR] Temperature needs to be a value")
        if str(command) == "setbotprefix":
            open("data/settingsdata/prefix").write(value)
            self.update_log(f"[INFO] Set bot prefix to '{value}'")
        if str(command) == "setbotmodel":
            open("data/settingsdata/model").write(value)
            self.update_log(f"[INFO] Set bot model to '{value}'. WARNING: If a invalid model was set the bot will not respond to messages. set the model to 'gpt-3.5-turbo' if bot becomes unresponive")
        if str(command) == "setbotsystem":
            open("data/settingsdata/model").write(value)
            self.update_log(f"[INFO] Set bot system to '{value}'")
    def update_log(self, text: str):
        with open("data/settingsdata/text.txt", "a+") as log:
            log.seek(0)
            content = log.read()
            print(content + text + "\n")
            print(content)
            print(text)
            log.write(text + "\n")

    def update_textbox_from_file(self, file_path):
        with open(file_path, 'r') as f:
            file_contents = f.read()
        scroll_pos = self.textbox.yview()[0]
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.insert("end", file_contents, ('foreground', 'red'))
        self.textbox.configure(state="disabled")
        self.textbox.yview_moveto(scroll_pos)
        self.after(1000, lambda: self.update_textbox_from_file("data/settingsdata/text.txt"))

    def open_input_dialog_event_disc(self):
        dialog = customtkinter.CTkInputDialog(
            text="Paste your Discord bot token",
            title="Discord Bot Token",
        )
        dialog.after(20, lambda: dialog._entry.configure(show="*"))
        dval = dialog.get_input()
        if not str(dval) == "None":
            open("secrets/DIS_BOT_TKN", "w+").write(dval)

    def open_input_dialog_event_ai(self):
        dialog = customtkinter.CTkInputDialog(
            text="Paste your OpenAI API key",
            title="OpenAI API Key",
        )
        dialog.after(20, lambda: dialog._entry.configure(show="*"))
        dval = dialog.get_input()
        if not str(dval) == "None":
            open("secrets/GPT_API_KEY", "w+").write(dval)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def re_enable_on_button(self):
        self.sidebar_button_1.configure(state=customtkinter.NORMAL)
        self.sidebar_button_2.configure(state=customtkinter.NORMAL)

    def re_enable_off_button(self):
        self.sidebar_button_1.configure(state=customtkinter.NORMAL)
        self.sidebar_button_2.configure(state=customtkinter.NORMAL)

    def sidebar_button_event_on(self):
        self.sidebar_button_1.configure(state="disabled")
        self.sidebar_button_2.configure(state="disabled")
        if os.path.exists(lock_file):
            self.update_log("[INFO] Bot already started")
        else:
            subprocess.Popen("start.bat", shell=True)
            self.update_log("[INFO] Starting Runtime")

            open(lock_file, 'w+')
            os.system(f'attrib +h {lock_file}')
        self.after(10000, self.re_enable_on_button)

    def sidebar_button_event_off(self):
        self.sidebar_button_1.configure(state="disabled")
        self.sidebar_button_2.configure(state="disabled")
        if not os.path.exists(lock_file):
            self.update_log("[INFO] Bot isn't running")
        else:
            subprocess.Popen("kill.bat", shell=True)
            self.update_log("[INFO] Stopping Runtime")
            os.remove(lock_file)
        self.after(10000, self.re_enable_on_button)

if __name__ == "__main__":
    app = App()
    app.mainloop()


