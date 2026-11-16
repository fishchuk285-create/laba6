
from ingredients import get_daily_ingredients
from inventory import add_ingredient


def next_day(player, inventory):
    try:
        player["day"] += 1

        print(f"\n=== ДЕНЬ {player['day']} ===")
        print("Ти отримуєш 5 інгредієнтів!")

        for ingredient in get_daily_ingredients():
            if add_ingredient(inventory, ingredient):
                print(f"+ {ingredient}")
            else:
                print(f"Немає місця для: {ingredient}")

    except Exception as error:
        print(f"Помилка нового дня: {error}")
