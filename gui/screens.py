import tkinter as tk
from tkinter import messagebox
from gui.components import CountryList, CountryDetail
from api.rest_countries import RestCountriesAPI
from data.storage import save_data, load_data

LIGHT_THEME = {
    'bg': '#f8f9fa',
    'fg': '#222',
    'font': ('Segoe UI', 12),
    'button_bg': '#e0e0e0',
    'button_fg': '#222'
}
DARK_THEME = {
    'bg': '#23272f',
    'fg': '#f8f9fa',
    'font': ('Segoe UI', 12),
    'button_bg': '#444',
    'button_fg': '#f8f9fa'
}

class MainScreen(tk.Frame):
    def __init__(self, master, switch_screen, theme):
        super().__init__(master, bg=theme['bg'])
        self.pack(fill='both', expand=True)
        self.switch_screen = switch_screen
        self.theme = theme
        self.countries = []
        self.loading_label = tk.Label(self, text='Carregando países...', font=theme['font'], bg=theme['bg'], fg=theme['fg'])
        self.loading_label.pack(pady=20)
        self.list_component = None
        self.load_countries()

    def load_countries(self):
        self.loading_label.config(text='Carregando países...')
        self.update()
        data, error = RestCountriesAPI.get_all()
        if error:
            self.loading_label.config(text=f'Erro ao carregar países: {error}')
            btn = tk.Button(self, text='Tentar novamente', command=self.load_countries, font=self.theme['font'], bg=self.theme['button_bg'], fg=self.theme['button_fg'], relief='raised', bd=2, activebackground='#bdbdbd')
            btn.pack(pady=10)
            btn.bind('<Enter>', lambda e: btn.config(bg='#bdbdbd'))
            btn.bind('<Leave>', lambda e: btn.config(bg=self.theme['button_bg']))
        elif not data or not isinstance(data, list):
            self.loading_label.config(text='Nenhum dado recebido da API.')
        else:
            self.countries = data
            save_data({'countries': data})
            self.loading_label.pack_forget()
            self.list_component = CountryList(self, self.countries, self.switch_screen, self.theme)
            self.list_component.pack(fill='both', expand=True, pady=20)

class DetailScreen(tk.Frame):
    def __init__(self, master, country, switch_screen, theme):
        super().__init__(master, bg=theme['bg'])
        self.pack(fill='both', expand=True)
        CountryDetail(self, country, theme).pack(fill='both', expand=True)
        btn = tk.Button(self, text='Voltar', command=lambda: switch_screen(), font=theme['font'], bg=theme['button_bg'], fg=theme['button_fg'], relief='raised', bd=2, activebackground='#bdbdbd')
        btn.pack(pady=10)
        btn.bind('<Enter>', lambda e: btn.config(bg='#bdbdbd'))
        btn.bind('<Leave>', lambda e: btn.config(bg=theme['button_bg']))


def run_app():
    root = tk.Tk()
    root.title('REST Countries App')
    root.geometry('700x500')
    theme = LIGHT_THEME
    current_screen = None

    def toggle_theme():
        nonlocal theme
        theme = DARK_THEME if theme == LIGHT_THEME else LIGHT_THEME
        switch_screen()

    def switch_screen(country=None):
        nonlocal current_screen
        if current_screen:
            current_screen.destroy()
        if country:
            current_screen = DetailScreen(root, country, switch_screen, theme)
        else:
            current_screen = MainScreen(root, switch_screen, theme)
        # Centralizar tudo
        current_screen.pack(expand=True)

    theme_btn = tk.Button(root, text='Alternar tema', command=toggle_theme, font=theme['font'], bg=theme['button_bg'], fg=theme['button_fg'], relief='raised', bd=2, activebackground='#bdbdbd')
    theme_btn.pack(pady=10)
    theme_btn.bind('<Enter>', lambda e: theme_btn.config(bg='#bdbdbd'))
    theme_btn.bind('<Leave>', lambda e: theme_btn.config(bg=theme['button_bg']))
    switch_screen()
    root.mainloop()
