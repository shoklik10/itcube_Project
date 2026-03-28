import tkinter as tk
from tkinter import font as tkfont
import random


# БАЗА ДАННЫХ ВОПРОСОВ
# Структура: словарь {тема: [(вопрос, правильный_ответ, [варианты]), ...]}
# Варианты: список из 4 строк, включая правильный ответ

TOPICS = {
    "🔢 Математика": [
        ("Чему равно π (пи) приблизительно?", "3.14", ["3.14", "2.71", "1.41", "1.73"]),
        ("Сколько градусов в прямом угле?", "90", ["90", "45", "180", "60"]),
        ("Что такое квадрат числа 7?", "49", ["49", "42", "56", "36"]),
        ("Наименьшее простое число:", "2", ["2", "0", "1", "3"]),
        ("Сколько сторон у шестиугольника?", "6", ["6", "5", "7", "8"]),
        ("Чему равно 12 × 12?", "144", ["144", "122", "132", "154"]),
        ("Корень квадратный из 144:", "12", ["12", "14", "11", "13"]),
        ("Сумма углов треугольника (°):", "180", ["180", "360", "90", "270"]),
        ("Что такое факториал 5 (5!)?", "120", ["120", "60", "24", "720"]),
        ("Процентов в целом числе:", "100", ["100", "10", "1000", "50"]),
        ("Чему равно 2 в степени 10?", "1024", ["1024", "512", "2048", "100"]),
        ("Сколько нулей в миллиарде?", "9", ["9", "6", "12", "8"]),
        ("Площадь квадрата со стороной 5:", "25", ["25", "20", "10", "50"]),
        ("Чему равно sin(90°)?", "1", ["1", "0", "-1", "0.5"]),
        ("Чему равно cos(0°)?", "1", ["1", "0", "-1", "0.5"]),
        ("Периметр квадрата со стороной 4:", "16", ["16", "8", "12", "20"]),
        ("Дробь 1/4 в процентах:", "25%", ["25%", "20%", "40%", "50%"]),
        ("Наибольший однозначный простой:", "7", ["7", "9", "8", "6"]),
        ("Сколько секунд в минуте?", "60", ["60", "100", "30", "120"]),
        ("Чему равно 0.1 + 0.2 (математически)?", "0.3", ["0.3", "0.12", "1.2", "3.0"]),
    ],
    "🌍 География": [
        ("Столица Австралии:", "Канберра", ["Канберра", "Сидней", "Мельбурн", "Брисбен"]),
        ("Самая длинная река мира:", "Нил", ["Нил", "Амазонка", "Янцзы", "Волга"]),
        ("Самая высокая гора:", "Эверест", ["Эверест", "К2", "Аконкагуа", "Эльбрус"]),
        ("Самый большой океан:", "Тихий", ["Тихий", "Атлантический", "Индийский", "Северный Ледовитый"]),
        ("Сколько континентов на Земле?", "7", ["7", "5", "6", "8"]),
        ("Самая большая страна по площади:", "Россия", ["Россия", "Канада", "США", "Китай"]),
        ("Столица Бразилии:", "Бразилиа", ["Бразилиа", "Рио-де-Жанейро", "Сан-Паулу", "Манаус"]),
        ("Самое глубокое озеро мира:", "Байкал", ["Байкал", "Каспийское", "Танганьика", "Верхнее"]),
        ("На каком материке Египет?", "Африка", ["Африка", "Азия", "Европа", "Австралия"]),
        ("Столица Японии:", "Токио", ["Токио", "Осака", "Киото", "Йокогама"]),
        ("Самая длинная река России:", "Обь", ["Обь", "Волга", "Енисей", "Лена"]),
        ("Самый маленький материк:", "Австралия", ["Австралия", "Антарктида", "Европа", "Южная Америка"]),
        ("Столица Канады:", "Оттава", ["Оттава", "Торонто", "Монреаль", "Ванкувер"]),
        ("Где находится Килиманджаро?", "Танзания", ["Танзания", "Кения", "Эфиопия", "ЮАР"]),
        ("Самая большая пустыня мира:", "Антарктида", ["Антарктида", "Сахара", "Гоби", "Аравийская"]),
        ("Столица Германии:", "Берлин", ["Берлин", "Мюнхен", "Гамбург", "Франкфурт"]),
        ("Через какой город течёт Темза?", "Лондон", ["Лондон", "Париж", "Берлин", "Рим"]),
        ("Самый высокий водопад:", "Анхель", ["Анхель", "Ниагарский", "Виктория", "Игуасу"]),
        ("На каком океане Россия не омывается?", "Индийском", ["Индийском", "Тихом", "Северном Ледовитом", "Атлантическом"]),
        ("Столица Аргентины:", "Буэнос-Айрес", ["Буэнос-Айрес", "Монтевидео", "Сантьяго", "Лима"]),
    ],
    "⚗️ Наука": [
        ("Химическое обозначение воды:", "H₂O", ["H₂O", "CO₂", "NaCl", "O₂"]),
        ("Сколько хромосом у человека?", "46", ["46", "23", "48", "44"]),
        ("Скорость света (км/с):", "300 000", ["300 000", "150 000", "3 000 000", "30 000"]),
        ("Самый распространённый газ атмосферы:", "Азот", ["Азот", "Кислород", "Углекислый газ", "Аргон"]),
        ("Кто открыл закон гравитации?", "Ньютон", ["Ньютон", "Эйнштейн", "Галилей", "Коперник"]),
        ("Единица электрического тока:", "Ампер", ["Ампер", "Вольт", "Ватт", "Ом"]),
        ("Что такое ДНК?", "Носитель генетической информации", ["Носитель генетической информации", "Тип белка", "Вид сахара", "Фермент"]),
        ("Периодический закон открыл:", "Менделеев", ["Менделеев", "Дальтон", "Бор", "Резерфорд"]),
        ("Самый лёгкий элемент таблицы:", "Водород", ["Водород", "Гелий", "Литий", "Бериллий"]),
        ("Из чего состоит атомное ядро?", "Протонов и нейтронов", ["Протонов и нейтронов", "Только протонов", "Электронов", "Нейтронов и электронов"]),
        ("Единица силы в СИ:", "Ньютон", ["Ньютон", "Джоуль", "Паскаль", "Ватт"]),
        ("Что изучает орнитология?", "Птиц", ["Птиц", "Насекомых", "Рыб", "Млекопитающих"]),
        ("Формула поваренной соли:", "NaCl", ["NaCl", "KCl", "CaCO₃", "H₂SO₄"]),
        ("Какой орган вырабатывает инсулин?", "Поджелудочная железа", ["Поджелудочная железа", "Печень", "Почки", "Щитовидная железа"]),
        ("Температура кипения воды (°C):", "100", ["100", "90", "212", "80"]),
        ("Что такое фотосинтез?", "Синтез органики из CO₂ на свету", ["Синтез органики из CO₂ на свету", "Дыхание растений", "Деление клеток", "Транспорт воды"]),
        ("Самая твёрдая природная вещь:", "Алмаз", ["Алмаз", "Корунд", "Кварц", "Сталь"]),
        ("Чему равна абсолютная нулевая температура?", "-273°C", ["-273°C", "0°C", "-100°C", "-459°F"]),
        ("Что такое квант света?", "Фотон", ["Фотон", "Электрон", "Нейтрон", "Протон"]),
        ("Закон Ома связывает:", "Ток, напряжение и сопротивление", ["Ток, напряжение и сопротивление", "Силу и массу", "Теплоту и работу", "Давление и объём"]),
    ],
    "📜 История": [
        ("Год основания Рима:", "753 до н.э.", ["753 до н.э.", "476 до н.э.", "509 до н.э.", "1000 до н.э."]),
        ("Кто написал «Войну и мир»?", "Толстой", ["Толстой", "Достоевский", "Тургенев", "Чехов"]),
        ("Когда началась Первая мировая война?", "1914", ["1914", "1939", "1905", "1918"]),
        ("Первый президент США:", "Вашингтон", ["Вашингтон", "Линкольн", "Джефферсон", "Адамс"]),
        ("Когда пал Советский Союз?", "1991", ["1991", "1989", "1985", "1993"]),
        ("Кто был первым в космосе?", "Гагарин", ["Гагарин", "Армстронг", "Титов", "Глен"]),
        ("Где воздвигнута Берлинская стена?", "Берлин", ["Берлин", "Мюнхен", "Дрезден", "Гамбург"]),
        ("Кто открыл Америку (1492)?", "Колумб", ["Колумб", "Веспуччи", "Магеллан", "Кабот"]),
        ("Год Бородинской битвы:", "1812", ["1812", "1814", "1807", "1815"]),
        ("Какой народ построил пирамиды?", "Египтяне", ["Египтяне", "Греки", "Шумеры", "Римляне"]),
        ("Когда закончилась Вторая мировая?", "1945", ["1945", "1944", "1946", "1943"]),
        ("Первый царь России:", "Иван IV (Грозный)", ["Иван IV (Грозный)", "Пётр I", "Иван III", "Борис Годунов"]),
        ("Год Октябрьской революции в России:", "1917", ["1917", "1905", "1918", "1921"]),
        ("Кто построил Версаль?", "Людовик XIV", ["Людовик XIV", "Людовик XVI", "Наполеон", "Генрих IV"]),
        ("Где сжигали Джордано Бруно?", "Рим", ["Рим", "Флоренция", "Венеция", "Неаполь"]),
        ("Год основания Санкт-Петербурга:", "1703", ["1703", "1712", "1695", "1721"]),
        ("Кто такой Хаммурапи?", "Царь Вавилона", ["Царь Вавилона", "Фараон Египта", "Правитель Персии", "Вождь галлов"]),
        ("Год Куликовской битвы:", "1380", ["1380", "1362", "1395", "1410"]),
        ("Кто изобрёл печатный станок?", "Гутенберг", ["Гутенберг", "Леонардо", "Архимед", "Дагер"]),
        ("Кто победил при Ватерлоо?", "Веллингтон", ["Веллингтон", "Наполеон", "Блюхер", "Кутузов"]),
    ],
}


# ЦВЕТОВАЯ ПАЛИТРА И СТИЛИ

COLORS = {
    "bg":           "#0D0D1A",
    "surface":      "#16162A",
    "surface2":     "#1E1E38",
    "accent":       "#7B5CBE",
    "accent2":      "#A888E8",
    "correct":      "#2ECC71",
    "wrong":        "#E74C3C",
    "text":         "#E8E8F0",
    "text_dim":     "#8888AA",
    "gold":         "#F0C040",
    "border":       "#2A2A4A",
    "btn_hover":    "#9B6EE8",
}


# КЛАСС ПРИЛОЖЕНИЯ

class QuizCards(tk.Tk):

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.title("🧠 QuizCards")
        self.geometry("820x620")
        self.minsize(700, 550)
        self.configure(bg=COLORS["bg"])
        self.resizable(True, True)

        self.center_window(820, 620)

        # Состояние игры
        self.current_topic = None
        self.questions = []
        self.current_index = 0
        self.correct_count = 0
        self.total_attempts = 0
        self.answered_correctly = set()

        # Шрифты
        self.font_title  = tkfont.Font(family="Georgia", size=26, weight="bold")
        self.font_subtitle = tkfont.Font(family="Georgia", size=13)
        self.font_question = tkfont.Font(family="Georgia", size=16, weight="bold")
        self.font_btn    = tkfont.Font(family="Helvetica", size=12, weight="bold")
        self.font_small  = tkfont.Font(family="Helvetica", size=10)
        self.font_big    = tkfont.Font(family="Georgia", size=48, weight="bold")

        # Активный экран
        self.current_frame = None

        self.show_menu()


    # УТИЛИТЫ

    def center_window(self, w, h):
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w - w) // 2
        y = (screen_h - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def show_screen(self, builder_func):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = builder_func()
        self.current_frame.pack(fill="both", expand=True)

    def make_frame(self):
        return tk.Frame(self, bg=COLORS["bg"])

    def make_button(self, parent, text, command, color=None, text_color=None, width=None):
        bg = color or COLORS["accent"]
        fg = text_color or COLORS["text"]

        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=self.font_btn,
            bg=bg,
            fg=fg,
            activebackground=COLORS["btn_hover"],
            activeforeground=COLORS["text"],
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            width=width or 0,
        )

        btn.bind("<Enter>", lambda e: btn.config(bg=COLORS["btn_hover"]))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    def animated_label(self, parent, text, font, fg, delay_ms=0, **kwargs):
        lbl = tk.Label(parent, text=text, font=font, fg=COLORS["bg"], bg=COLORS["bg"], **kwargs)

        def fade_in(step=0):
            if step <= 10:
                r1, g1, b1 = self.winfo_rgb(COLORS["bg"])
                r2, g2, b2 = self.winfo_rgb(fg)
                r = int(r1 + (r2 - r1) * step / 10) >> 8
                g = int(g1 + (g2 - g1) * step / 10) >> 8
                b = int(b1 + (b2 - b1) * step / 10) >> 8
                lbl.config(fg=f"#{r:02x}{g:02x}{b:02x}")
                self.after(30, lambda: fade_in(step + 1))

        self.after(delay_ms, fade_in)
        return lbl


    # ЭКРАН 1 - ГЛАВНОЕ МЕНЮ

    def show_menu(self):
        self.show_screen(self._build_menu)

    def _build_menu(self):
        frame = self.make_frame()

        top_bar = tk.Frame(frame, bg=COLORS["accent"], height=4)
        top_bar.pack(fill="x")

        content = tk.Frame(frame, bg=COLORS["bg"])
        content.pack(expand=True)

        self.animated_label(
            content, "🧠 QuizCards",
            self.font_title, COLORS["accent2"],
            delay_ms=0
        ).pack(pady=(40, 5))

        self.animated_label(
            content, "Выбери тему и докажи свои знания",
            self.font_subtitle, COLORS["text_dim"],
            delay_ms=200
        ).pack(pady=(0, 30))

        tk.Frame(content, bg=COLORS["border"], height=1, width=400).pack(pady=10)

        for i, topic in enumerate(TOPICS.keys()):
            btn = self.make_button(
                content,
                text=f"  {topic}  —  20 вопросов  ",
                command=lambda t=topic: self.start_game(t),
                color=COLORS["surface2"],
                width=40,
            )
            btn.pack(pady=6)
            btn.config(fg=COLORS["text_dim"])

            def animate_btn(b=btn, d=300 + i * 100):
                self.after(d, lambda: b.config(fg=COLORS["text"]))
            animate_btn()

        tk.Frame(content, bg=COLORS["border"], height=1, width=400).pack(pady=20)

        self.animated_label(
            content, "Правила: отвечай на все вопросы правильно — только тогда победишь!",
            self.font_small, COLORS["text_dim"],
            delay_ms=600
        ).pack()

        return frame


    # ЛОГИКА ИГРЫ

    def start_game(self, topic):
        self.current_topic = topic
        self.questions = list(TOPICS[topic])
        random.shuffle(self.questions)

        self.current_index = 0
        self.correct_count = 0
        self.total_attempts = 0
        self.answered_correctly = set()

        self.show_question()

    def show_question(self):
        self.show_screen(self._build_question_screen)

    def _build_question_screen(self):
        frame = self.make_frame()

        q_index = self.current_index
        question_text, correct, options = self.questions[q_index]
        shuffled_options = options[:]
        random.shuffle(shuffled_options)

        # Верхняя панель (тема + прогресс)
        top = tk.Frame(frame, bg=COLORS["surface"], pady=12)
        top.pack(fill="x")

        back_btn = tk.Label(
            top, text="← Меню",
            font=self.font_small, fg=COLORS["text_dim"],
            bg=COLORS["surface"], cursor="hand2"
        )
        back_btn.pack(side="left", padx=20)
        back_btn.bind("<Button-1>", lambda e: self.show_menu())
        back_btn.bind("<Enter>", lambda e: back_btn.config(fg=COLORS["accent2"]))
        back_btn.bind("<Leave>", lambda e: back_btn.config(fg=COLORS["text_dim"]))

        # Название темы
        tk.Label(
            top, text=self.current_topic,
            font=self.font_small, fg=COLORS["accent2"],
            bg=COLORS["surface"]
        ).pack(side="left", padx=10)

        done = len(self.answered_correctly)
        progress_text = f"✅ {done} / {len(self.questions)}"
        tk.Label(
            top, text=progress_text,
            font=self.font_small, fg=COLORS["correct"],
            bg=COLORS["surface"]
        ).pack(side="right", padx=20)

        # Прогресс-бар
        bar_bg = tk.Frame(frame, bg=COLORS["surface2"], height=6)
        bar_bg.pack(fill="x")

        # Заполненная часть
        total = len(self.questions)
        fill_ratio = done / total if total > 0 else 0

        bar_canvas = tk.Canvas(frame, bg=COLORS["surface2"], height=6, highlightthickness=0)
        bar_canvas.pack(fill="x")

        def draw_bar():
            w = bar_canvas.winfo_width()
            if w > 1:
                bar_canvas.delete("all")
                bar_canvas.create_rectangle(
                    0, 0, int(w * fill_ratio), 6,
                    fill=COLORS["correct"], outline=""
                )
        bar_canvas.bind("<Configure>", lambda e: draw_bar())
        self.after(50, draw_bar)

        # Карточка вопроса
        content = tk.Frame(frame, bg=COLORS["bg"])
        content.pack(expand=True, fill="both", padx=60, pady=30)

        # Номер вопроса
        tk.Label(
            content,
            text=f"Вопрос {q_index + 1} из {total}",
            font=self.font_small, fg=COLORS["text_dim"],
            bg=COLORS["bg"]
        ).pack(anchor="w", pady=(0, 10))


        card_outer = tk.Frame(content, bg=COLORS["accent"], pady=2, padx=2)
        card_outer.pack(fill="x", pady=5)

        card = tk.Frame(card_outer, bg=COLORS["surface"], padx=25, pady=20)
        card.pack(fill="both")

        # Текст вопроса
        q_label = tk.Label(
            card,
            text=question_text,
            font=self.font_question,
            fg=COLORS["text"],
            bg=COLORS["surface"],
            wraplength=600,
            justify="left"
        )
        q_label.pack(anchor="w")

        # Варианты ответов
        feedback_label = tk.Label(
            content, text="",
            font=self.font_btn,
            bg=COLORS["bg"]
        )
        feedback_label.pack(pady=5)

        answers_frame = tk.Frame(content, bg=COLORS["bg"])
        answers_frame.pack(fill="x", pady=10)

        for i, option in enumerate(shuffled_options):
            row = i // 2
            col = i % 2

            btn_frame = tk.Frame(answers_frame, bg=COLORS["surface2"], padx=2, pady=2)
            btn_frame.grid(row=row, column=col, padx=8, pady=6, sticky="ew")
            answers_frame.columnconfigure(col, weight=1)

            btn = tk.Button(
                btn_frame,
                text=option,
                font=self.font_btn,
                bg=COLORS["surface2"],
                fg=COLORS["text"],
                activebackground=COLORS["accent"],
                activeforeground=COLORS["text"],
                relief="flat",
                cursor="hand2",
                padx=15,
                pady=12,
                wraplength=250,
                command=lambda opt=option: self.check_answer(
                    opt, correct, feedback_label, answers_frame
                )
            )
            btn.pack(fill="both")

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=COLORS["accent"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=COLORS["surface2"]))

        # Нижняя подсказка
        hint = "💡 Неправильный ответ — вопрос вернётся снова!"
        tk.Label(
            content, text=hint,
            font=self.font_small, fg=COLORS["text_dim"],
            bg=COLORS["bg"]
        ).pack(pady=(5, 0))

        return frame

    def check_answer(self, chosen, correct, feedback_label, answers_frame):
        self.total_attempts += 1

        if chosen == correct:
            self.answered_correctly.add(self.current_index)
            feedback_label.config(text="✅ Верно!", fg=COLORS["correct"])

            self._disable_buttons(answers_frame)

            if len(self.answered_correctly) == len(self.questions):
                self.after(700, self.show_victory)
            else:
                self.after(700, self.next_question)
        else:
            feedback_label.config(
                text=f"❌ Неверно! Правильный ответ: {correct}",
                fg=COLORS["wrong"]
            )
            self._disable_buttons(answers_frame)
            self.after(1200, self.next_question)

    def _disable_buttons(self, frame):
        for widget in frame.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(state="disabled", cursor="arrow")

    def next_question(self):
        total = len(self.questions)
        next_idx = (self.current_index + 1) % total

        attempts = 0
        while next_idx in self.answered_correctly and attempts < total:
            next_idx = (next_idx + 1) % total
            attempts += 1

        self.current_index = next_idx
        self.show_question()


    # ЭКРАН ПОБЕДЫ

    def show_victory(self):
        self.show_screen(self._build_victory_screen)

    def _build_victory_screen(self):
        frame = self.make_frame()

        tk.Frame(frame, bg=COLORS["gold"], height=4).pack(fill="x")

        content = tk.Frame(frame, bg=COLORS["bg"])
        content.pack(expand=True)

        trophy_canvas = tk.Canvas(
            content, width=120, height=120,
            bg=COLORS["bg"], highlightthickness=0
        )
        trophy_canvas.pack(pady=(30, 10))

        trophy_canvas.create_oval(10, 10, 110, 110, fill=COLORS["surface2"], outline=COLORS["gold"], width=3)
        trophy_canvas.create_text(60, 60, text="🏆", font=("Arial", 40))

        def pulse(size=0):
            trophy_canvas.delete("glow")
            s = 5 + abs(size % 20 - 10)
            trophy_canvas.create_oval(
                10 - s, 10 - s, 110 + s, 110 + s,
                outline=COLORS["gold"], width=1,
                stipple="gray25", tags="glow"
            )
            self.after(80, lambda: pulse(size + 1))
        pulse()

        # Тексты результата
        self.animated_label(
            content, "ПОЗДРАВЛЯЕМ!",
            self.font_title, COLORS["gold"],
            delay_ms=100
        ).pack(pady=(5, 0))

        self.animated_label(
            content, f"Тема «{self.current_topic}» пройдена!",
            self.font_subtitle, COLORS["text"],
            delay_ms=300
        ).pack(pady=5)

        # Статистика в карточке
        stat_frame = tk.Frame(content, bg=COLORS["surface2"], padx=40, pady=20)
        stat_frame.pack(pady=20)

        accuracy = int((len(self.questions) / max(self.total_attempts, 1)) * 100)
        stats = [
            ("🎯 Правильных ответов", f"{len(self.questions)} / {len(self.questions)}"),
            ("📊 Всего попыток",       str(self.total_attempts)),
            ("⚡ Точность",             f"{accuracy}%"),
        ]

        for i, (label, value) in enumerate(stats):
            row = tk.Frame(stat_frame, bg=COLORS["surface2"])
            row.pack(fill="x", pady=4)

            self.animated_label(row, label, self.font_small, COLORS["text_dim"], delay_ms=400 + i * 100).pack(side="left")
            self.animated_label(row, value, self.font_btn, COLORS["accent2"], delay_ms=400 + i * 100).pack(side="right", padx=(40, 0))

        # Оценка результата
        if accuracy == 100:
            grade_text, grade_color = "Идеально! Без единой ошибки! 🌟", COLORS["gold"]
        elif accuracy >= 70:
            grade_text, grade_color = "Отличный результат! 👍", COLORS["correct"]
        elif accuracy >= 50:
            grade_text, grade_color = "Хороший результат, но есть куда расти!", COLORS["accent2"]
        else:
            grade_text, grade_color = "Продолжай практиковаться — всё придёт! 💪", COLORS["text_dim"]

        self.animated_label(
            content, grade_text, self.font_subtitle, grade_color, delay_ms=700
        ).pack(pady=10)

        # Кнопки действий
        btns = tk.Frame(content, bg=COLORS["bg"])
        btns.pack(pady=20)

        self.make_button(
            btns, "🔄 Повторить тему",
            command=lambda: self.start_game(self.current_topic),
            color=COLORS["accent"]
        ).pack(side="left", padx=10)

        self.make_button(
            btns, "📚 Выбрать другую тему",
            command=self.show_menu,
            color=COLORS["surface2"]
        ).pack(side="left", padx=10)

        return frame

app = QuizCards()
app.mainloop()