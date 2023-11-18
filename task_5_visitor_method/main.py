""" Главный модуль для создания больницы и регистрации приемов """


from patients import Outpatient, Inpatient
from doctors import Therapist, Surgeon


class Hospital:
    def create_appointment(self):
        outpatient_ann = Outpatient('Ann')
        inpatient_bob = Inpatient('Bob')
        outpatient_liz = Outpatient('Liz')
        inpatient_mike = Inpatient('Mike')

        therapist_smith = Therapist('Mr. Smith')
        surgeon_addams = Surgeon('Mrs. Addams')
        therapist_taylor = Therapist('Mrs. Taylor')
        surgeon_miller = Surgeon('Mr. Miller')

        outpatient_ann.accept(therapist_smith)
        inpatient_bob.accept(therapist_smith)

        outpatient_ann.accept(surgeon_addams)
        inpatient_bob.accept(surgeon_addams)

        outpatient_liz.accept(therapist_taylor)
        inpatient_mike.accept(therapist_taylor)

        outpatient_liz.accept(surgeon_miller)
        inpatient_mike.accept(surgeon_miller)


if __name__ == "__main__":
    hospital = Hospital()
    hospital.create_appointment()
