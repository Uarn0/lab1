import math

import tkinter as tk

from tkinter import ttk, simpledialog, messagebox

from dataclasses import dataclass

from typing import Optional


@dataclass

class CalcResult:

    sub_function: str

    value: Optional[float] = None

    error: Optional[str] = None


    @property

    def is_success(self) -> bool:

        return self.error is None


def evaluate_function(x: float) -> CalcResult:

    if x < 1:

        sub_func = "y = ln(sin(x) + 0.5)"

        x_rad = math.radians(x)

        ln_arg = math.sin(x_rad) + 0.5


        if ln_arg <= 0:

            return CalcResult(sub_func, error="Значення (sin(x) + 0.5) <= 0. Логарифм не існує.")

        return CalcResult(sub_func, value=math.log(ln_arg))


    elif x > 10:

        sub_func = "y = ctg(x^2) / sqrt(1 - arcsin(x))"


        if not (-1 <= x <= 1):

            return CalcResult(sub_func, error="Аргумент arcsin(x) виходить за межі [-1; 1].")


        arcsin_val = math.asin(x)

        sqrt_arg = 1 - arcsin_val


        if sqrt_arg <= 0:

            msg = "Знаменник = 0." if sqrt_arg == 0 else "Вираз під коренем < 0."

            return CalcResult(sub_func, error=msg)


        x_sq_rad = math.radians(x**2)

        sin_x_sq = math.sin(x_sq_rad)


        if sin_x_sq == 0:

            return CalcResult(sub_func, error="sin(x^2) дорівнює нулю, ctg(x^2) не існує.")


        ctg_val = math.cos(x_sq_rad) / sin_x_sq

        y = ctg_val / math.sqrt(sqrt_arg)

        return CalcResult(sub_func, value=y)


    return CalcResult("-", error="Функція не визначена для x ∈ [1; 10].")



class FunctionApp(tk.Tk):

    def __init__(self) -> None:

        super().__init__()

       

        self.withdraw()

       

        self.stop_key = simpledialog.askstring(

            "Налаштування",

            "Введіть 'ключове' значення для змінної x, яке буде закривати програму:",

            parent=self

        )

       

        if not self.stop_key:

            messagebox.showinfo("Завершення", "Ключове значення не задано. Програму буде закрито.")

            self.destroy()

            return

           

        self.stop_key = self.stop_key.strip()

       

        self.deiconify()

        self.title("Обчислення складної функції (Модифікована)")

        self.geometry("550x260")

        self.resizable(False, False)

       

        self.style = ttk.Style(self)

        if 'clam' in self.style.theme_names():

            self.style.theme_use('clam')

           

        self._init_ui()


    def _init_ui(self) -> None:

        main_frame = ttk.Frame(self, padding=20)

        main_frame.pack(fill=tk.BOTH, expand=True)


        ttk.Label(

            main_frame,

            text=f"Введіть x (або '{self.stop_key}' для виходу):",

            font=("Arial", 12, "bold")

        ).pack(pady=(0, 10))


        self.entry_x = ttk.Entry(main_frame, font=("Arial", 12), width=15)

        self.entry_x.pack(pady=(0, 10))

        self.entry_x.bind('<Return>', lambda _: self._on_calculate())


        ttk.Button(

            main_frame,

            text="Обчислити",

            command=self._on_calculate

        ).pack(pady=(0, 15))


        self.lbl_subfunc = ttk.Label(main_frame, text="Підфункція: -", font=("Arial", 11, "italic"))

        self.lbl_subfunc.pack(pady=(0, 5))


        self.lbl_result = tk.Label(main_frame, text="Результат з'явиться тут", font=("Arial", 12, "bold"))

        self.lbl_result.pack(pady=(0, 10))


    def _on_calculate(self) -> None:

        user_input = self.entry_x.get().strip()

       

        # ЗАВДАННЯ 2: Перевірка на ключове значення

        if user_input == self.stop_key:

            messagebox.showinfo("До побачення!", f"Введено ключове значення '{self.stop_key}'. Роботу завершено.")

            self.destroy()

            return

           

        try:

            x_val = float(user_input)

        except ValueError:

            self._render_result(CalcResult("-", error="Будь ласка, введіть коректне число."))

            return


        result = evaluate_function(x_val)

        self._render_result(result)


    def _render_result(self, result: CalcResult) -> None:

        self.lbl_subfunc.config(text=f"Підфункція: {result.sub_function}")

       

        if result.is_success:

            self.lbl_result.config(text=f"Результат: y = {result.value:.5f}", fg="#15803d")

        else:

            self.lbl_result.config(text=f"Помилка: {result.error}", fg="#b91c1c")



if __name__ == "__main__":

    app = FunctionApp()

    app.mainloop() 