from tinydb import TinyDB

forms = [
    {
        "name": "Данные пользователя",
        "login": "email",
        "tel": "phone"
    },
    {
        "name": "Форма заказа",
        "customer": "text",
        "order_id": "text",
        "дата_заказа": "date",
        "contact": "phone"
    },
    {
        "name": "Проба",
        "f_name1": "email",
        "f_name2": "date"
    }
]

db = TinyDB("database.json")
db.truncate()
db.insert_multiple(forms)
print("Шаблоны успешно загружены.")
