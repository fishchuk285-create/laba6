
from potions import POTIONS


def sell_potions(player, inventory):
    try:
        if not inventory["potions"]:
            print("У тебе немає зіль для продажу!")
            return

        print("\n=== МАГАЗИН ===")

        total = 0

        for name, amount in inventory["potions"]:
            price = POTIONS[name]["price"]
            earned = price * amount
            total += earned

            print(f"{name}: {amount} шт. = {earned} золота")

        print(f"\nЗагальний заробіток: {total} золота")

        answer = input("Продати всі зілля? (так/ні): ")

        if answer.lower() == "так":
            player["gold"] += total
            inventory["potions"].clear()
            print("Зілля продано!")
            print(f"Тепер у тебе {player['gold']} золота.")

    except Exception as error:
        print(f"Помилка магазину: {error}")
