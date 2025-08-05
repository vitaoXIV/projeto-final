import tkinter as tk
from tkinter import ttk

class CountryList(tk.Frame):
    def __init__(self, master, countries, switch_screen, theme):
        super().__init__(master, bg=theme['bg'])
        self.countries = countries
        self.switch_screen = switch_screen
        self.theme = theme
        self.search_var = tk.StringVar()
        self.region_var = tk.StringVar(value='Todas')
        self.pop_var = tk.StringVar(value='Todas')
        # Busca por nome
        # Ícone de busca
        try:
            from PIL import Image, ImageTk
            import os
            icon_path = os.path.join(os.path.dirname(__file__), 'search_icon.png')
            if os.path.exists(icon_path):
                search_img = Image.open(icon_path).resize((20, 20))
                search_icon = ImageTk.PhotoImage(search_img)
                icon_label = tk.Label(self, image=search_icon, bg=self.theme['bg'])
                icon_label.image = search_icon
                icon_label.pack(pady=2)
        except Exception:
            pass
        tk.Label(self, text='Buscar país:', font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg']).pack()
        search_entry = tk.Entry(self, textvariable=self.search_var, font=self.theme['font'], relief='solid', bd=2, bg='#ffffff', fg=self.theme['fg'], highlightthickness=2, highlightbackground='#a3a3a3')
        search_entry.pack(pady=5)
        search_entry.bind('<Return>', self.search)
        search_entry.bind('<FocusIn>', lambda e: search_entry.config(highlightbackground='#0078d7'))
        search_entry.bind('<FocusOut>', lambda e: search_entry.config(highlightbackground='#a3a3a3'))
        # Animação de entrada
        def animate_entry():
            orig_bg = search_entry.cget('bg')
            search_entry.config(bg='#e3f2fd')
            self.after(300, lambda: search_entry.config(bg=orig_bg))
        search_entry.bind('<FocusIn>', lambda e: animate_entry())
        # Filtro por região
        # Ícone de filtro região
        try:
            icon_path = os.path.join(os.path.dirname(__file__), 'region_icon.png')
            if os.path.exists(icon_path):
                region_img = Image.open(icon_path).resize((20, 20))
                region_icon = ImageTk.PhotoImage(region_img)
                icon_label = tk.Label(self, image=region_icon, bg=self.theme['bg'])
                icon_label.image = region_icon
                icon_label.pack(pady=2)
        except Exception:
            pass
        tk.Label(self, text='Filtrar por região:', font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg']).pack()
        regions = ['Todas'] + sorted({c.get('region', 'N/A') for c in self.countries})
        region_menu = tk.OptionMenu(self, self.region_var, *regions, command=lambda _: self.apply_filters())
        region_menu.config(font=self.theme['font'], bg=self.theme['button_bg'], fg=self.theme['button_fg'], relief='groove', bd=2)
        region_menu.pack(pady=5)
        region_menu.bind('<Enter>', lambda e: region_menu.config(bg='#0078d7', fg='#fff'))
        region_menu.bind('<Leave>', lambda e: region_menu.config(bg=self.theme['button_bg'], fg=self.theme['button_fg']))
        # Filtro por população
        # Ícone de filtro população
        try:
            icon_path = os.path.join(os.path.dirname(__file__), 'pop_icon.png')
            if os.path.exists(icon_path):
                pop_img = Image.open(icon_path).resize((20, 20))
                pop_icon = ImageTk.PhotoImage(pop_img)
                icon_label = tk.Label(self, image=pop_icon, bg=self.theme['bg'])
                icon_label.image = pop_icon
                icon_label.pack(pady=2)
        except Exception:
            pass
        tk.Label(self, text='Filtrar por população:', font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg']).pack()
        pop_options = ['Todas', 'Até 1M', '1M-10M', '10M-100M', '100M+']
        pop_menu = tk.OptionMenu(self, self.pop_var, *pop_options, command=lambda _: self.apply_filters())
        pop_menu.config(font=self.theme['font'], bg=self.theme['button_bg'], fg=self.theme['button_fg'], relief='groove', bd=2)
        pop_menu.pack(pady=5)
        pop_menu.bind('<Enter>', lambda e: pop_menu.config(bg='#0078d7', fg='#fff'))
        pop_menu.bind('<Leave>', lambda e: pop_menu.config(bg=self.theme['button_bg'], fg=self.theme['button_fg']))
        # Lista de países
        self.listbox = tk.Listbox(self, font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg'], relief='solid', bd=2, highlightthickness=2, highlightbackground='#a3a3a3', selectbackground='#0078d7', selectforeground='#fff')
        self.listbox.pack(fill='both', expand=True, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self._on_listbox_select)
        self.update_list()
        # Animação de seleção
        def animate_listbox():
            orig_bg = self.listbox.cget('bg')
            self.listbox.config(bg='#e3f2fd')
            self.after(300, lambda: self.listbox.config(bg=orig_bg))
        self._animate_listbox = animate_listbox

    def _on_listbox_select(self, event):
        self._animate_listbox()
        if not self.listbox.curselection():
            return
        idx = self.listbox.curselection()[0]
        name = self.listbox.get(idx)
        # Buscar no filtro atual, não no self.countries
        filtered = [c for c in self.countries if name == c.get('name', {}).get('common', '')]
        country = filtered[0] if filtered else None
        if country:
            self.switch_screen(country)
        tk.Label(self, text='Filtrar por região:', font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg']).pack()
        regions = ['Todas'] + sorted({c.get('region', 'N/A') for c in self.countries})
        region_menu = tk.OptionMenu(self, self.region_var, *regions, command=lambda _: self.apply_filters())
        region_menu.config(font=self.theme['font'], bg=self.theme['button_bg'], fg=self.theme['button_fg'], relief='groove', bd=2)
        region_menu.pack(pady=5)
        region_menu.bind('<Enter>', lambda e: region_menu.config(bg='#0078d7', fg='#fff'))
        region_menu.bind('<Leave>', lambda e: region_menu.config(bg=self.theme['button_bg'], fg=self.theme['button_fg']))
        # Filtro por população
        # Ícone de filtro população
        try:
            icon_path = os.path.join(os.path.dirname(__file__), 'pop_icon.png')
            if os.path.exists(icon_path):
                pop_img = Image.open(icon_path).resize((20, 20))
                pop_icon = ImageTk.PhotoImage(pop_img)
                icon_label = tk.Label(self, image=pop_icon, bg=self.theme['bg'])
                icon_label.image = pop_icon
                icon_label.pack(pady=2)
        except Exception:
            pass
        tk.Label(self, text='Filtrar por população:', font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg']).pack()
        pop_options = ['Todas', 'Até 1M', '1M-10M', '10M-100M', '100M+']
        pop_menu = tk.OptionMenu(self, self.pop_var, *pop_options, command=lambda _: self.apply_filters())
        pop_menu.config(font=self.theme['font'], bg=self.theme['button_bg'], fg=self.theme['button_fg'], relief='groove', bd=2)
        pop_menu.pack(pady=5)
        pop_menu.bind('<Enter>', lambda e: pop_menu.config(bg='#0078d7', fg='#fff'))
        pop_menu.bind('<Leave>', lambda e: pop_menu.config(bg=self.theme['button_bg'], fg=self.theme['button_fg']))
        # Lista de países
        self.listbox = tk.Listbox(self, font=self.theme['font'], bg=self.theme['bg'], fg=self.theme['fg'], relief='solid', bd=2, highlightthickness=2, highlightbackground='#a3a3a3', selectbackground='#0078d7', selectforeground='#fff')
        self.listbox.pack(fill='both', expand=True, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self._on_listbox_select)

    def apply_filters(self):
        region = self.region_var.get()
        pop = self.pop_var.get()
        filtered = self.countries
        if region != 'Todas':
            filtered = [c for c in filtered if c.get('region', 'N/A') == region]
        if pop != 'Todas':
            def pop_filter(p):
                val = p.get('population', 0)
                if pop == 'Até 1M': return val <= 1_000_000
                if pop == '1M-10M': return 1_000_000 < val <= 10_000_000
                if pop == '10M-100M': return 10_000_000 < val <= 100_000_000
                if pop == '100M+': return val > 100_000_000
                return True
            filtered = [c for c in filtered if pop_filter(c)]
        self.update_list(filtered)

    def update_list(self, filtered=None):
        self.listbox.delete(0, tk.END)
        for country in filtered if filtered is not None else self.countries:
            self.listbox.insert(tk.END, country.get('name', {}).get('common', ''))

    def search(self, event=None):
        term = self.search_var.get().strip().lower()
        if not term:
            self.apply_filters()
            return
        filtered = [c for c in self.countries if term in c.get('name', {}).get('common', '').lower()]
        self.update_list(filtered)

    def on_select(self, event):
        if not self.listbox.curselection():
            return
        idx = self.listbox.curselection()[0]
        name = self.listbox.get(idx)
        country = next((c for c in self.countries if c.get('name', {}).get('common', '') == name), None)
        if country:
            self.switch_screen(country)

class CountryDetail(tk.Frame):
    def __init__(self, master, country, theme):
        super().__init__(master, bg=theme['bg'])
        name = country.get('name', {}).get('common', 'N/A')
        capital = country.get('capital', ['N/A'])[0]
        region = country.get('region', 'N/A')
        population = country.get('population', 'N/A')
        area = country.get('area', 'N/A')
        currencies = ', '.join(country.get('currencies', {}).keys()) or 'N/A'
        flag_url = country.get('flags', {}).get('png')

        title = tk.Label(self, text=f'País: {name}', font=(theme['font'][0], 16, 'bold'), bg=theme['bg'], fg=theme['fg'])
        title.pack(pady=10)
        if flag_url:
            try:
                import urllib.request
                from PIL import Image, ImageTk
                import io
                with urllib.request.urlopen(flag_url) as u:
                    raw_data = u.read()
                im = Image.open(io.BytesIO(raw_data)).resize((120, 80))
                photo = ImageTk.PhotoImage(im)
                flag_label = tk.Label(self, image=photo, bg=theme['bg'])
                flag_label.image = photo
                flag_label.pack(pady=5)
            except Exception:
                tk.Label(self, text='(Bandeira não disponível)', bg=theme['bg'], fg=theme['fg']).pack()
        info_frame = tk.Frame(self, bg=theme['bg'])
        info_frame.pack(pady=10)
        tk.Label(info_frame, text=f'Capital: {capital}', font=theme['font'], bg=theme['bg'], fg=theme['fg']).pack(anchor='w')
        tk.Label(info_frame, text=f'Região: {region}', font=theme['font'], bg=theme['bg'], fg=theme['fg']).pack(anchor='w')
        tk.Label(info_frame, text=f'População: {population}', font=theme['font'], bg=theme['bg'], fg=theme['fg']).pack(anchor='w')
        tk.Label(info_frame, text=f'Área: {area} km²', font=theme['font'], bg=theme['bg'], fg=theme['fg']).pack(anchor='w')
        tk.Label(info_frame, text=f'Moedas: {currencies}', font=theme['font'], bg=theme['bg'], fg=theme['fg']).pack(anchor='w')
