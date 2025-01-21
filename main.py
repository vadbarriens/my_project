from src.utils import fin_transaction_json
from src.transactions import (
    read_transactions_csv, read_transactions_excel,
    get_filter_transactions, count_transactions_by_categories
)


def main():
    """Программа получения информации о банковских операциях"""
    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор (1/2/3): ")

        if choice == "1":
            file_path = r"C:\Users\burin87\PycharmProjects\my_project1\data\operations.json"
            transactions = fin_transaction_json(file_path)
        elif choice == "2":
            file_path = r"C:\Users\burin87\PycharmProjects\my_project1\data\transactions.csv"
            transactions = read_transactions_csv(file_path)
        elif choice == "3":
            file_path = r"C:\Users\burin87\PycharmProjects\my_project1\data\transactions_1.xlsx"
            transactions = read_transactions_excel(file_path)
        else:
            print("Вы ввели цифру вне диапазона выбора. Программа завершена.")
            return

        if not transactions:
            print("Не удалось загрузить данные. Программа завершена.")
            return

        # Запрос статуса с улучшенной обработкой некорректного ввода
        valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
        while True:
            status = input(f"\nВведите статус для фильтрации ({', '.join(valid_statuses)}): ").strip().upper()
            if status in valid_statuses:
                break
            print(
                f"Некорректный статус: '{status}'. Пожалуйста, выберите один из доступных: {', '.join(valid_statuses)}."
            )

        # Фильтрация по статусу
        filtered_transactions = [t for t in transactions if t.get("state") == status]
        print(f"\nОперации отфильтрованы по статусу '{status}'.")

        # Сортировка по дате
        if input("\nОтсортировать операции по дате? (Да/Нет): ").strip().lower() == "да":
            order = input("Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").strip().lower()
            reverse_order = order == "убыванию"
            filtered_transactions = sorted(filtered_transactions, key=lambda t: t["date"], reverse=reverse_order)
            print("\nОперации отсортированы по дате.")

        # Фильтрация по ключевому слову
        if input("\nОтфильтровать список транзакций по слову в описании? (Да/Нет): ").strip().lower() == "да":
            keyword = input("Введите ключевое слово: ").strip()
            filtered_transactions = get_filter_transactions(filtered_transactions, keyword)

        # Подсчет категорий
        categories = ["вклад", "карта", "услуг"]
        category_count = count_transactions_by_categories(filtered_transactions, categories)
        print("\nПодсчет категорий операций:")
        for category, count in category_count.items():
            print(f"{category}: {count} операций")

        # Результат
        if filtered_transactions:
            print("\nРаспечатываю итоговый список транзакций...")
            for transaction in filtered_transactions:
                print(transaction)
        else:
            print("\nНе найдено ни одной транзакции, подходящей под ваш запрос.")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
