
import random

PLANTS = [
    "Троянда", "Мандрагора", "Гриб", "Орхідея",
    "Лотос", "Папороть", "Конюшина", "Лілія",
    "Кактус", "Плющ", "Півонія", "Ромашка",
    "Лаванда", "Пшениця", "М'ята", "Паприка",
    "Ялівець", "Пшоно", "Шавлія", "Полин"
]

TYPES = [
    "Червона", "Синя", "Золота", "Темна",
    "Світла", "Місячна", "Сонячна", "Магічна",
    "Стародавня", "Крижана"
]

INGREDIENTS = {
    f"{kind} {plant}": random.randint(2, 15)
    for plant in PLANTS
    for kind in TYPES
}


def get_daily_ingredients():
    try:
        return random.sample(list(INGREDIENTS.keys()), 5)
    except Exception as error:
        print(f"Помилка: {error}")
        return []


def show_ingredients():
    try:
        print("\n=== СПИСОК ІНГРЕДІЄНТІВ ===")
        for name, price in INGREDIENTS.items():
            print(f"{name} — {price} золота")
        print(f"Всього: {len(INGREDIENTS)}")
    except Exception as error:
        print(f"Помилка: {error}")
