
class Car:
    def __init__(self, modelo, marca, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano


car_list = []

def add_car():
    while True:
        add_car = input('Adicionar mais um carro? [ s / n]:')

        if add_car.lower() == 's':

            modelo = input('Digite o modelo do carro: ')
            marca = input('Digite a marca do carro: ')
            cor = input('Digite a cor do carro: ')
            ano = input('Digite o ano do carro: ')

            car = Car(modelo, marca, cor, ano)
            car_list.append(car)
        elif add_car.lower() == 'n':
            break
        else:
            print('Digite uma opção valida!!! s ou n ')
        
           
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
