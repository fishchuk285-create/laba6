
from player import create_player, show_player
from inventory import create_inventory, show_inventory
from alchemy import craft_potion
from potions import show_potions
from shop import sell_potions
from day import next_day
from game_over import check_game_over


def main():
    try:
        player = create_player()
        inventory = create_inventory()

        print("=" * 40)
        print("       ALchemist RPG")
        print("       ГРА ПРО АЛХІМІКА")
        print("=" * 40)

        print("\nТи — молодий алхімік.")
        print("Твоя мета — заробити 10000 золотих!")

        next_day(player, inventory)

        while True:
            print("\n========== ГОЛОВНЕ МЕНЮ ==========")
            print("1. Мій персонаж")
            print("2. Інвентар")
            print("3. Переглянути рецепти")
            print("4. Зварити зілля")
            print("5. Продати зілля")
            print("6. Завершити день")
            print("0. Вийти з гри")

            choice = input("\nТвій вибір: ")

            if choice == "1":
                show_player(player)

            elif choice == "2":
                show_inventory(inventory)

            elif choice == "3":
                show_potions()

            elif choice == "4":
                craft_potion(inventory)

            elif choice == "5":
                sell_potions(player, inventory)

            elif choice == "6":
                sell_potions(player, inventory)
                next_day(player, inventory)

            elif choice == "0":
                print("Дякуємо за гру!")
                break

            else:
                print("Неправильний вибір!")

            if check_game_over(player):
                break

    except Exception as error:
        print(f"Критична помилка гри: {error}")


if __name__ == "__main__":
    main()
