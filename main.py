from car import add_car, car_list

while True:
    menu = input(''' 
        [1]. adicionar carro
        [2]. Mostrar carros cadastrados
        [3]. Sair
        escolha uma opção
    ''')

    if menu == '1':
        add_car()

    elif menu == '2':
        for car in car_list:
            print(f'Modelo: {car.modelo}, Marca: {car.marca}, cor : {car.cor}, ano: {car.ano}')

    elif menu == '3':
        break

    else:
        print('Digite uma opção valida: ')