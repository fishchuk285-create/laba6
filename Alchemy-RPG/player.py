
def create_player():
    try:
        return {
            "name": "Алхімік",
            "gold": 100,
            "day": 0
        }
    except Exception as error:
        print(f"Помилка створення гравця: {error}")
        return None


def show_player(player):
    try:
        print("\n=== ТВОЄГО ПЕРСОНАЖА ===")
        print(f"Ім'я: {player['name']}")
        print(f"Золото: {player['gold']}")
        print(f"Ігровий день: {player['day']}")
    except Exception as error:
        print(f"Помилка: {error}")
