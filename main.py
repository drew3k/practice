from bokeh.plotting import figure, show
import numpy as np

# Создание массива значений x от 0 до 2π
x = np.linspace(0, 2*np.pi, 100)

# Вычисление значений функции sin(x)
y = np.sin(x)

# Создание объекта Figure
p = figure(title="График функции sin(x)", x_axis_label='x', y_axis_label='sin(x)')

# Добавление графика на объект Figure
p.line(x, y, line_width=2)

# Отображение графика
show(p)


# import matplotlib.pyplot as plt
# import numpy as np
#
# # Создание массива значений x от -5 до 5 с шагом 0.1
# x = np.arange(-5, 5, 0.1)
#
# # Вычисление значений функции y = x^2
# y = x ** 2
#
# # Создание нового графика
# plt.figure()
#
# # Построение графика
# plt.plot(x, y, label='y = x^2')
#
# # Добавление заголовка графика
# plt.title('График функции y = x^2')
#
# # Добавление подписей к осям
# plt.xlabel('x')
# plt.ylabel('y')
#
# # Добавление сетки на график
# plt.grid(True)
#
# # Добавление легенды
# plt.legend()
#
# # Отображение графика
# plt.show()

# import plotly.graph_objects as go
# import numpy as np
#
# # Создание массива значений x от 0 до 2π с шагом 0.1
# x = np.arange(0, 2*np.pi, 0.1)
#
# # Вычисление значений функции y = sin(x)
# y = np.sin(x)
#
# # Создание объекта Figure
# fig = go.Figure()
#
# # Добавление графика на объект Figure
# fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='sin(x)'))
#
# # Настройка макета графика
# fig.update_layout(
#     title='Scatter Plot',
#     xaxis_title='x',
#     yaxis_title='y',
#     showlegend=True,
#     hovermode='closest',
# )
#
# # Отображение графика
# fig.show()
