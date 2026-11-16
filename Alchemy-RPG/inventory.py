
POTION_SLOTS = 10
INGREDIENT_SLOTS = 25


def create_inventory():
    try:
        return {
            "potions": [],
            "ingredients": {}
        }
    except Exception as error:
        print(f"Помилка інвентаря: {error}")
        return None


def add_ingredient(inventory, name, amount=1):
    try:
        ingredients = inventory["ingredients"]

        if name in ingredients:
            if ingredients[name] + amount <= 25:
                ingredients[name] += amount
                return True
            return False

        if len(ingredients) < INGREDIENT_SLOTS and amount <= 25:
            ingredients[name] = amount
            return True

        return False

    except Exception as error:
        print(f"Помилка додавання інгредієнта: {error}")
        return False


def show_inventory(inventory):
    try:
        print("\n=== ІНГРЕДІЄНТИ ===")

        for name, amount in inventory["ingredients"].items():
            print(f"{name}: {amount}/25")

        print(f"Зайнято слотів: {len(inventory['ingredients'])}/25")

        print("\n=== ЗІЛЛЯ ===")

        for index, (name, amount) in enumerate(
            inventory["potions"], start=1
        ):
            print(f"Слот {index}: {name} — {amount}/10")

        print(
            f"Зайнято слотів: "
            f"{len(inventory['potions'])}/10"
        )

    except Exception as error:
        print(f"Помилка показу інвентаря: {error}")
