import pymysql as pms


con = pms.connect('localhost',
                  'root',
                  '7895',
                  'Laba')

cur = con.cursor()

print('Добро пожаловать!\n')
while True:
    a = input('Нажмите:\n'
              '1 - если вы новый пользователь\n'
              '2 - если вы наш клиент\n'
              '3 - для выхода\n')

    if a == '1':
        q = input('Создать нового пользователя(д/н)\n')
        if q == 'д':
            name = input('Введите ваше имя и фамилию\n')
            name = name.split()
            date = input('Введите дату вашего рождения в формате: yyyy-mm-dd\n')
            sql = """INSERT INTO `Клиенты` (`client_id`, `Имя`, `Фамилия`, `Дата рождения`)
                VALUES (NULL, '{f}', '{s}', '{t}')""".format(f=name[0], s=name[1], t=date)
            try:
                cur.execute(sql)
                con.commit()
                print('Все прошло удачно\n')
                cur.execute("""SELECT `client_id` FROM `Клиенты` WHERE `client_id`=LAST_INSERT_ID() """)
                i = (str(cur.fetchall())).replace('(', '').replace(')', '').replace(',', '')
                print('Ваш id -', i, '\nНе сообщайте его никому!')
            except:
                print('Произошла ошибка, попробуйте еще раз\n')

    elif a == '2':
        id = input('Введите свой id\n')
        print('Мы рады вас снова видеть\n')
        q = input('Выбрать команду:\n'
                  '1 - Посмотреть свои вклады\n'
                  '2 - Создать вклад\n'
                  '3 - Вернуться обратно\n')
        if q == '1':
            cur.execute("""SELECT * FROM `Вклады` WHERE `client_id`={} """.format(id))
            ans = str(cur.fetchall()).replace(' ', '').replace('(', '').replace(')', '')
            anss = ans.split(',')
            for i in range(len(anss) // 4):
                l = i * 4
                print(anss[l] + ' - ' + anss[l + 2] + 'руб. (под ' + anss[l + 3] + '%)')
        elif q == '2':
            print('Процентная ставка зависит от суммы вклады:\n'
                  'от 100руб. до 1000руб. - 6%\n'
                  'от 1001руб. до 5000руб. - 10%\n'
                  'от 5001руб. до 10000руб. - 14%\n'
                  'Меньше 100руб. и больше 10000руб. невозможно положить\n')
            while True:
                q = input('Введите сумму или "quit" для выхода')
                if q == 'quit':
                    break
                else:
                    if int(q) >= 100 and int(q) <= 1000:
                        proc = 6
                    elif int(q) >= 1001 and int(q) <= 5000:
                        proc = 10
                    elif int(q) >= 5001 and int(q) <= 10000:
                        proc = 14
                    else:
                        print('Недопустимая сумма')
                        break
                    sql = """INSERT INTO `Вклады` (`client_id`, `Сумма вклада`, `Процентная ставка`)
                VALUES ({f}, '{s}', '{t}')""".format(f=id, s=q, t=proc)
                    try:
                        cur.execute(sql)
                        con.commit()
                        print('Все прошло удачно\n')
                    except:
                        print('Произошла ошибка, попробуйте еще раз\n')
                    break
        else:
            None
    elif a == '3':
        print('До новых встреч!')
        quit(1)

    elif a == '9789':
        while True:
            print('Приветствую тебя, мой Господин!')
            q = input('Команды:\n'
                      '1 - Посмотреть всех пользователей\n'
                      '2 - Посмотреть все вклады\n'
                      '3 - Посмотреть все вклады по id клиента\n'
                      '4 - Выйти из админской панели\n')
            if q == '1':
                cur.execute("""SELECT * FROM `Клиенты`""")
                ans = str(cur.fetchall()).replace(' ', '').replace(',', '-').replace('))', ')\n').replace("'", "")
                ans = ans.replace('-(', '').replace('datetime.date', '').replace('((', '(')
                print(ans)
            elif q == '2':
                cur.execute("""SELECT * FROM `Вклады`""")
                ans = str(cur.fetchall()).replace('(', '').replace(')', '')
                ans = ans.split(',')
                for w in range(len(ans) // 4):
                    p = w * 4
                    print(ans[p + 1] + ' id -' + ans[p + 2] + 'руб.' + ans[p + 3] + '%')
            elif q == '3':
                id = input('Введите id\n')
                cur.execute("""SELECT * FROM `Вклады` WHERE `client_id`={} """.format(int(id)))
                ans = str(cur.fetchall()).replace('(', '').replace(')', '')
                ans = ans.split(',')
                for w in range(len(ans) // 4):
                    p = w * 4
                    print(ans[p + 2] + 'руб.' + ans[p + 3] + '%')
            elif q == '4':
                break
            else:
                None
    else:
        print('Возможно вы неправильно что-то ввели\n'
              'или произошла неизвестная ошибка\n')
