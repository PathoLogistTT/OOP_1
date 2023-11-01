def __init__(self, name, qualification, position):
    '''
    Метод инициализации объекта Surgeon.

    Параметры:
    - name : Имя хирурга
    - qualification : Квалификация хирурга
    - position : Должность хирурга
    '''

def __init__(self, name, age, illness):
    '''
    Метод инициализации объекта Patient

    Параметры:
    - name : Имя пациента
    - age : Возраст пациента
    - illness : Заболевание пациента
    '''

class Surgery:
    def __init__(self, name, surgeon, patients, time, day):
        '''
        Метод инициализации объекта Surgery.

        Параметры:
        - name : Название операции
        - surgeon : Хирург, выполняющий операцию
        - patients : Список пациентов, участвующих в операции
        - time : Время проведения операции
        - day : День проведения операции
        '''

    def patient_list(self):
        # Метод, возвращающий список строковых представлений пациентов.
        pass

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
                print("Хирург успешно создан.")
            elif object_type == "2":
                name = input("Введите имя пациента: ")
                age = input("Введите возраст пациента: ")
                illness = input("Введите болезнь пациента: ")
                print(f"Пациент успешно создан.")

            elif object_type == "3":
                name = input("Введите название операции: ")
                time = input("Введите время операции: ")
                day = input("Введите день операции: ")
                surgeon = input("Введите имя хирурга: ")

                patients = []
                while True:
                    add_patient = input("\nДобавить пациента (да/нет): ")
                    if add_patient == "да":
                        patient_name = input("Введите имя пациента: ")
                        patient_age = int(input("Введите возраст пациента: "))
                        patient_illness = input("Введите болезнь пациента: ")
                        print("Пациент добавлен")
                    else:
                        break
                print(f"\nОбъект успешно создан.")

        elif choice == "2":
            if len(registry) == 0:
                print("\nРеестр пуст.")
            else:
                pass

        elif choice == "3":
            if len(registry) == 0:
                print("\nРеестр пуст.")
            else:
                index = int(input("\nВведите индекс объекта: "))
                if index >= 0 and index < len(registry):
                    print("Распечатать добавленные объекты")
                else:
                    print("\nНеверный индекс объекта.")

        elif choice == "4":
            break

        else:
            print("\nНеверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
