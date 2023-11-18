""" Модуль для распределения врачей для оказания помощи пациентам """


class Doctor:
    def __init__(self, name):
        self.name = name

    def visit_outpatient(self, outpatient):
        pass

    def visit_inpatient(self, inpatient):
        pass


class Therapist(Doctor):
    def visit_outpatient(self, outpatient):
        print(f"Therapist {self.name} examined outpatient: {outpatient.receive_appointment()}")

    def visit_inpatient(self, inpatient):
        print(f"Therapist {self.name} examined inpatient: {inpatient.receive_hospitalization()}")


class Surgeon(Doctor):
    def visit_outpatient(self, outpatient):
        print(f"Surgeon {self.name} consulted outpatient: {outpatient.receive_appointment()}")

    def visit_inpatient(self, inpatient):
        print(f"Surgeon {self.name} performed surgery on inpatient: {inpatient.receive_hospitalization()}")
