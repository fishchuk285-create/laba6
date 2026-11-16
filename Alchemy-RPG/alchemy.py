
from potions import POTIONS


def craft_potion(inventory):
    try:
        print("\n=== АЛХІМІЧНА ЛАБОРАТОРІЯ ===")

        for name in POTIONS:
            print("-", name)

        potion_name = input("\nЯке зілля створити? ")

        if potion_name not in POTIONS:
            print("Такого рецепта немає!")
            return

        recipe = POTIONS[potion_name]["recipe"]

        for ingredient, amount in recipe.items():
            if inventory["ingredients"].get(ingredient, 0) < amount:
                print(f"Недостатньо: {ingredient}")
                return

        potions = inventory["potions"]

        # Шукаємо слот з місцем для такого зілля
        existing = next(
            (p for p in potions
             if p[0] == potion_name and p[1] < 10),
            None
        )

        # Якщо немає вільного слота
        if existing is None and len(potions) >= 10:
            print("Інвентар зіль заповнений!")
            return

        # Витрачаємо інгредієнти
        for ingredient, amount in recipe.items():
            inventory["ingredients"][ingredient] -= amount

        if existing:
            index = potions.index(existing)
            potions[index] = (potion_name, existing[1] + 1)
        else:
            potions.append((potion_name, 1))

        print(f"Успішно створено: {potion_name}!")

    except Exception as error:
        print(f"Помилка алхімії: {error}")
