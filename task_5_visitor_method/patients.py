""" Модуль для регистрации посетителей как пациентов больницы """


class Patient:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        pass


# класс для регистрации пациентов на амбулаторное лечение
class Outpatient(Patient):
    def receive_appointment(self):
        return self.name

    def accept(self, visitor):
        visitor.visit_outpatient(self)


# класс для регистрации пациентов на стационарное лечение
class Inpatient(Patient):
    def receive_hospitalization(self):
        return self.name

    def accept(self, visitor):
        visitor.visit_inpatient(self)
