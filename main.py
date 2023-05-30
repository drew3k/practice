import numpy as np

while(True):
    # Получение выбора пользователя
    choice = int(input("Выберите программу для запуска:\n1)Matplotlib\n2)Plotly\n3)Bokeh\n0)Выход\n"))

    if choice == 0:
        print("Программа завершена.")
        break

    if choice == 1:
        import matplotlib.pyplot as plt

        # Создание массива значений x от -5 до 5 с шагом 0.1
        x = np.arange(-5, 5, 0.1)

        # Вычисление значений функции y = x^2
        y = x ** 2

        # Создание нового графика
        plt.figure()

        # Построение графика
        plt.plot(x, y, label='y = x^2')

        # Добавление заголовка графика
        plt.title('График функции y = x^2')

        # Добавление подписей к осям
        plt.xlabel('x')
        plt.ylabel('y')

        # Добавление сетки на график
        plt.grid(True)

        # Добавление легенды
        plt.legend()

        # Отображение графика
        plt.show()

    elif choice == 2:
        import plotly.graph_objects as go

        # Создание массива значений x от 0 до 2π с шагом 0.1
        x = np.arange(0, 2 * np.pi, 0.1)

        # Вычисление значений функции y = sin(x)
        y = np.sin(x)

        # Создание объекта Figure
        fig = go.Figure()

        # Добавление графика на объект Figure
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='sin(x)'))

        # Настройка макета графика
        fig.update_layout(
            title='Scatter Plot',
            xaxis_title='x',
            yaxis_title='y',
            showlegend=True,
            hovermode='closest',
        )

        # Отображение графика
        fig.show()

    elif choice == 3:
        from bokeh.plotting import figure, show

        # Создание массива значений x от 0 до 2π
        x = np.linspace(0, 2 * np.pi, 100)

        # Вычисление значений функции sin(x)
        y = np.sin(x)

        # Создание объекта Figure
        p = figure(title="График функции sin(x)", x_axis_label='x', y_axis_label='sin(x)')

        # Добавление графика на объект Figure
        p.line(x, y, line_width=2)

        # Отображение графика
        show(p)

    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 3.")
