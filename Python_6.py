import requests

def my_sum(x, y):
    return x + y

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        self.grade += 1

    def publish_grade(self):
        return f"{self.name} — грейд: {self.grade}"

class Designer(Employee):
    def __init__(self, name, seniority=0, awards=2):
        initial_seniority = seniority + awards * 2
        super().__init__(name, initial_seniority)
        self.awards = awards 

    def get_award(self):
        self.awards += 1
        self.seniority += 2
        print(f'{self.name} получила премию №{self.awards}')

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1
        if self.seniority % 7 == 0:
            self.grade_up()
        return self.publish_grade()

class Rate:
    def __init__(self, format='value', diff=False):
        self.format = format
        self.diff = diff 

    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]
            if self.format == 'value':
                if self.diff and currency in ('USD', 'EUR'):
                    return response[currency]['Value'] - response[currency]['Previous']
                return response[currency]['Value']
        return 'Error'

    def eur(self):
        return self.make_format('EUR')

    def usd(self):
        return self.make_format('USD')

def get_max_currency_name():
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    valutes = r.json()['Valute']
    max_val = max(valutes.values(), key=lambda x: x['Value'])
    return max_val['Name']

def simulate_designer_promotions():
    elena = Designer(name="Елена", awards=2)
    print(f"\nНачальный статус: {elena.publish_grade()}, seniority = {elena.seniority}")
    for i in range(1, 21):
        result = elena.check_if_it_is_time_for_upgrade()
        print(f"После {i}-й аккредитации: {result}, seniority = {elena.seniority}")

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Узнать курс валюты")
        print("2. Найти валюту с максимальным курсом")
        print("3. Узнать изменение курса USD (diff)")
        print("4. Узнать изменение курса EUR (diff)")
        print("5. Запустить симуляцию повышения грейда дизайнера")
        print("0. Выход")
        
        choice = input("Ваш выбор: ").strip()

        if choice == '1':
            rate = Rate('value')
            user_input = input("Введите код валюты (например, USD, EUR): ").upper()
            result = rate.make_format(user_input)
            print(f"\nКурс {user_input}: {result}")

        elif choice == '2':
            try:
                name = get_max_currency_name()
                print(f"\nВалюта с максимальным курсом: {name}")
            except Exception as e:
                print(f"\nОшибка при получении данных: {e}")

        elif choice == '3':
            rate = Rate('value', diff=True)
            try:
                print(f"\nИзменение курса USD: {rate.usd()}")
            except Exception as e:
                print(f"\nОшибка: {e}")

        elif choice == '4':
            rate = Rate('value', diff=True)
            try:
                print(f"\nИзменение курса EUR: {rate.eur()}")
            except Exception as e:
                print(f"\nОшибка: {e}")

        elif choice == '5':
            simulate_designer_promotions()

        elif choice == '0':
            print("\nВыход.")
            break

        else:
            print("\nНеверный выбор. Попробуйте снова.")
