print("Добро пожаловать на виктарну Quiz по стартапам")
print("Ответь на следущие вопросы: ")

question1 = "Первый вопрос: назови основные звания в нашем классе?"
answer1 = "драник, панперс, кирлиз"
question2 = "Второй вопрос: назови два самых худших звания в нашем классе"
answer2 = "неприкосаемые, бадаладушки/бадаладушка"

question3 = "Какая твоя любимаая игра?"
question4 ="Оцени как ты играешь в эту игру от 1 до 10"
score = 0

print(question1)

user_input = input("Введи свой ответ: ")
if user_input.lower() == answer1.lower():
    score = score + 1
    print("ну ты сигма")
else:
    print("сколько нужно грамм для такого эффекта")

print(question2)

user_input = input("Введи свой ответ: ")
if user_input.lower() == answer2.lower():
    score = score + 1
    print("ну ты сигма")
else:
    print("сколько нужно грамм для такого эффекта")

questions = ["1. продолжи: а мой... ",
             "2. ты сигма:",
             "3. сколько ты бахаеш мефа за день?",
]

answers = [
    "милый дэнис тракторист я его доярочка",
     "да",
    "1488 грамм"
]



print(questions[0])

user_input = input("Введи свой ответ:(без точек и запятых ")
if user_input.lower() == answers[0].lower():
    score = score + 1
    print("ну ты сигма")
else:
    print("сколько нужно грамм для такого эффекта")

    print(questions[1])

user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[1].lower():
    score = score + 1
    print("ну ты сигма")
else:
    print("сколько нужно грамм для такого эффекта")

print(questions[2])

user_input = input("Введи свой ответ: ")
if user_input.lower() == answers[2].lower():
    score = score + 1
    print("ну ты сигма")
else:
    print("сколько нужно грамм для такого эффекта")


if score >= 5:
    print("какая ты всё-таки сигма вот тебе 1488 грамм мефа и медный бычок")
elif score > 3:
    print("сколько у тебя хромосом?")
else:
    print("ты теперь доярочка дэниса")
