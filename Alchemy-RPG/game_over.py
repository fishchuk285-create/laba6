
def check_game_over(player):
    try:
        if player["gold"] >= 10000:
            print("\n🏆 ВІТАЮ! ТИ ПЕРЕМІГ!")
            print("Ти став найвідомішим алхіміком королівства!")
            return True

        if player["day"] >= 30 and player["gold"] < 1000:
            print("\n💀 ТИ ПРОГРАВ!")
            print("Твої запаси закінчилися, а лабораторія закрилася.")
            return True

        return False

    except Exception as error:
        print(f"Помилка завершення гри: {error}")
        return True
