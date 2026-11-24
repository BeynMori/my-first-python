name = input("Как тебя зовут? ")
print(f"Привет, {name}! Python работает.")
print("Where is this world heading, and am I on the right path?")

answer = input("Ты готов продолжать учиться? (да/нет): ").lower()

if answer == "да":
    print(f"Отлично, {name}! Ты точно на верном пути.")
elif answer == "нет":
    print("Ничего страшного, сделай небольшой перерыв и возвращайся!")
else:
    print("Не совсем понял ответ, но практика всё равно делает тебя сильнее!")

