import controller as c

while True:
    out_input = input(str('Если хотиете завершить работу введите: q \n'))
    if out_input == str('q'):
        print('Спасибо что выбрали наше приложение! Заходите еще!!!')
        break
    else:
        c.button_click()
