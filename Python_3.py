def pForm(str):
    # Проверка на команду p---
    userInput = input('Введите номер документа: ')
    for doc in documents:
        for (key, value) in doc.items():
            if doc['number'] == userInput:
                print(f'Владелец документа: {doc["name"]}')
                return
    print('Документ не найден в базе')



def sForm(str):
    # Проверка на команду s---
        userInput = input('Введите номер документа: ')
        for (key, value) in directories.items():
            if userInput in value:
                print(f"Документ хранится на полке: {key} ")
                return key
        print('Документ не найден в базе')


def lForm(str):
    # Проверка на команду l---
        for doc in documents:
            for (key, value) in directories.items():
                if doc['number'] in value:
                    snumber = key
                    break
            print(f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {snumber}")


def adsForm(str):
    # Проверка на команду ads---
        userInput = input("Введите номер полки:")
        if userInput in directories:
            userInput = ', '.join(sorted(directories.keys())) #Сортирует и объединяет, добавляя между ними <,>
            print(f"Такая полка уже существует. Текущий перечень полок: {userInput}.")
        else:
            directories[userInput] = []
            userInput = ', '.join(sorted(directories.keys()))
            print(f"Полка добавлена. Текущий перечень полок: {userInput}.")


def dsForm(str):
    # Проверка на команду ds---
        userInput = input("Введите номер полки: ")
        if userInput not in directories:
            sh = ', '.join(sorted(directories.keys()))
            print(f"Такой полки не существует. Текущий перечень полок: {sh}.")
        elif directories[userInput]:
            sh = ', '.join(directories.keys())
            print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {sh}.")
        else:
            del directories[userInput]
            sh = ', '.join(sorted(directories.keys()))
            print(f"Полка удалена. Текущий перечень полок: {sh}.")


documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]


directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

while True:
    UserInputstr = input('Введите команду: ')
    if UserInputstr == "q":
        break
    if UserInputstr == 'p' or UserInputstr == 'P':
        pForm(UserInputstr)
    if UserInputstr == 's' or UserInputstr == 'S':
        sForm(UserInputstr)
    if UserInputstr == 'l' or UserInputstr == 'L':
        lForm(UserInputstr)
    if UserInputstr == 'ads' or UserInputstr == 'ASD':
        adsForm(UserInputstr)
    if UserInputstr == 'ds' or UserInputstr == 'DS':
        dsForm(UserInputstr)
