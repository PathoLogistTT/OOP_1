class Surgeon:
    def __init__(self, name, qualification, position):
        self.name = name
        self.qualification = qualification
        self.position = position

    def representation(self):
        return f"{self.name}, {self.qualification}, {self.position}"

class Patient:
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness

    def representation(self):
        return f" {self.name}, {self.age}, {self.illness}"


class Surgery:
    def __init__(self, name, surgeon, patients, time, day):
        self.name = name
        self.surgeon = surgeon
        self.patients = patients
        self.time = time
        self.day = day

    def representation(self):
        return f"{self.name}, {self.time}, {self.day}"

    def patient_list(self):
        return [p.representation() for p in self.patients]

# Инициализация
registry = []

# Главное меню
def main():
    while True:
        print("Меню:")
        print("1. Создать новый объект")
        print("2. Вывести содержимое объектов")
        print("3. Вывести представление конкретного объекта")
        print("4. Завершить работу")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == "1":
            print("\nВыберите тип объекта:")
            print("1. Хирург")
            print("2. Пациент")
            print("3. Операция")

            object_type = input("\nВведите номер типа объекта (1-3): ")

            if object_type == "1":
                name = input("Введите имя хирурга: ")
                qualification = input("Введите квалификацию хирурга: ")
                position = input("Введите должность хирурга: ")
                surgeon = Surgeon(name, qualification, position)
                registry.append(surgeon)
                print(f"Объект с номером {len(registry) - 1} успешно создан.")

            elif object_type == "2":
                name = input("Введите имя пациента: ")
                age = input("Введите возраст пациента: ")
                illness = input("Введите болезнь пациента: ")
                patient = Patient(name, age, illness)
                registry.append(patient)
                print(f"Объект с номером {len(registry) - 1} успешно создан.")

            elif object_type == "3":
                name = input("Введите название операции: ")
                time = input("Введите время операции: ")
                day = input("Введите день операции: ")
                surgeon = input("Введите имя хирурга: ")

                patients = []
                while True:
                    add_patient = input("\nДобавить пациента (да/нет): ")
                    if add_patient.lower() == "да":
                        patient_name = input("Введите имя пациента: ")
                        while True:
                            try:
                                patient_age = int(input("Введите возраст пациента: "))
                                break
                            except ValueError as a:
                                print("введён неверный символ, повторите попытку")
                        patient_illness = input("Введите болезнь пациента: ")
                        patient_ = Patient(patient_name, patient_age, patient_illness)
                        patients.append(patient_)
                    elif add_patient.lower() == "нет":
                        break

                surgeon_ = Surgeon(surgeon, "", "")
                surgery = Surgery(name, surgeon_, patients, time, day)
                registry.append(surgery)
                print(f"\nОбъект с номером {len(registry) - 1} успешно создан.")

        elif choice == "2":
            if len(registry) == 0:
                print("\nРеестр пуст.")
            else:
                for index, obj in enumerate(registry):
                    print(f"\n{index}: {obj.representation()}")
                    if isinstance(obj, Surgery):
                        for patient in obj.patient_list():
                            print(patient)

        elif choice == "3":
            if len(registry) == 0:
                print("\nРеестр пуст.")
            else:
                index = int(input("\nВведите индекс объекта: "))
                if index >= 0 and index < len(registry):
                    print(registry[index].representation())
                else:
                    print("\nНеверный индекс объекта.")

        elif choice == "4":
            break

        else:
            print("\nНеверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()