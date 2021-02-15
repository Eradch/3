def personal_inf(**kwards):
   return ''.join(kwards.values())

name = input('Введите Имя -')
surname = input('Введите Фамилию -')
birthday = input('Введите Дату Рождения-')
city = input('Введите Дату Ваш Город-')
email = input('Введите Дату Ваш email-')
phone = input('Введите Дату Ваш Номер Телефона-')

print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))

