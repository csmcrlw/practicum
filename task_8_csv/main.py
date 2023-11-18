import zipfile
import json
import csv
import os


def main():
    # Разархивируем файл students.json из архива students.zip
    with zipfile.ZipFile('students.zip', 'r') as zip_ref:
        zip_ref.extract('students.json', '.')

    # Прочитаем данные из файла students.json
    with open('students.json', 'r') as json_file:
        students_data = json.load(json_file)

    # Создадим CSV файл и запишем в него фамилии и имена студентов
    csv_filename = 'students.csv'
    with open(csv_filename, 'w', newline='') as csv_file:
        fieldnames = ['firstname', 'lastname']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        # Заголовок CSV файла
        writer.writeheader()

        for student in students_data[0]:
            writer.writerow({'firstname': student['firstname'], 'lastname': student['lastname']})

    # Заархивируем CSV файл
    with zipfile.ZipFile('students_csv.zip', 'w') as zip_ref:
        zip_ref.write(csv_filename)

    # Удаляем временные JSON и CSV файлы
    os.remove('students.json')
    os.remove(csv_filename)

    print("CSV файл заархивирован в students_csv.zip")


if __name__ == "__main__":
    main()
