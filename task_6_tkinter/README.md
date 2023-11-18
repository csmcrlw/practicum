## Задание 6

С помощью класса Canvas создадим холст размером 600х600. В магическом методе __init__ объявим переменные self.speed и self.angle для скорости и направления движения точки по окружности. С помощью метода draw_circle отрисуем окружность с радиусом 200 по центру холста. Метод draw_moving_point отвечает за создание движущейся по окружности точки: сначала вычисляем координаты движения точки с учетом заданного направления, далее удаляем точку после каждого перемещения. Увеличиваем переменную self.angle на self.speed, чтобы точка могла двигаться с заданной скоростью. Чтобы точка двигалась постоянно, функция self.draw_moving_point вызывает сама себя рекурсивно через каждые 10 миллисекунд с помощью self.root.after. Метод draw_on_canvas позволяет нам рисовать на холсте: в event.x и event.y записываются координаты курсора, а create_oval создает черную точку при нажатии левой кнопки мыши.