import sys

def create_city_matrix(size):
    city_matrix = [[0 for x in range(size)] for y in range(size)]
    return city_matrix

def initialise_city_matrix(city_matrix, file, size):
    for i in range(size):
        data = file.readline().split()
        for j in range(size):
            datum = int(data[j])
            if datum < 0 or datum > 1000:
                print('Out of limit: Distance')
                sys.exit()
            city_matrix[i][j] = datum

def read_orders(input_file, output_file, city_matrix, size):
    for _ in range(size):
        data = input_file.readline().split()
        row = int(data[0]) - 1
        column = int(data[1]) - 1
        output_file.write(str(city_matrix[row][column]) + '\n')

input_file = open('input.txt', 'r')
number_of_cities = int(input_file.readline())
if number_of_cities < 1 or number_of_cities > 100:
    print('Out of limit: City')
    sys.exit()
city_matrix = create_city_matrix(number_of_cities)
initialise_city_matrix(city_matrix, input_file, number_of_cities)
number_of_orders = int(input_file.readline())
if number_of_orders < 1 or number_of_orders > 1000:
    print('Out of limit: Order')
    sys.exit()
output_file = open('output.txt', 'w')
read_orders(input_file, output_file, city_matrix, number_of_orders)