# from random import *
# LENGTH = 7
# d = [[randint(1,9) for i in range(LENGTH)]for j in range(LENGTH)]
# for i in range(LENGTH):
#     d[i][i] = 0
# for i in range(LENGTH):
#     for j in range(LENGTH):
#         print(d[i][j], end='\t')
#     print()
# def direct_indirect_distance(distance, city1, city2):
#     direct = d[city1][city2]
#     print(f'Direct Distance: {direct}')
#
#     for i in range(len(distance)):
#         if i != city1 and i != city2:
#             indirect_distance = distance[city1][i] + distance[i][city2]
#             print(f'via city{i}: {indirect_distance}')
#
# def taskb(distance, city1, city2):
#     direct = d[city1][city2]
#     shortest = direct
#     print(direct)
#     for i in range(len(distance)):
#         if i != city1 and i != city2:
#             indirect_distance = distance[city1][i] + distance[i][city2]
#             print(f'via city{i}: {indirect_distance}')
#         if indirect_distance < shortest:
#                 shortest = indirect_distance
#                 city_no = i
#     if shortest == direct:
#         print(f'Shortest distance between city{city1} and city{city2} is {shortest}.')
#     else:
#         print(f'Shortest distance between city{city1} and city{city2} is {shortest} via city {i}')
# def task2_c(distance, size):
#     min = 100
#     for i in range(size):
#         for j in range(size):
#             if i != j:
#                 if distance[i][j] < min:
#                     shortest= distance[i][j]
#                     city_one = i
#                     city_two = j
#     print(f'city {city_one} and city {city_two} has shortest direct distance {shortest}')

def task_2(distance, city1, city2):
    for i in range(5):
        random_i = randint(0,5)
        random_j = randint(0,5)
        distance[random_i][random_j] = -1
    print()
    for i in range(LENGTH):
        for j in range(LENGTH):
            print(distance[i][j], end='\t')
        print()
    for i in range(LENGTH):
        links = ''
        for j in range(LENGTH):
            if distance[i][j] != -1:
                links += ' ' + str(j)
        print(f'city {i} has direct link with {links}')

def task2_b(distance, city1, city2):
    for i in range(5):
        random_i = randint(0,5)
        random_j = randint(0,5)
        distance[random_i][random_j] = -1
    print()
    print()
    for i in range(LENGTH):
        for j in range(LENGTH):
            print(distance[i][j], end='\t')
        print()
    for city1 in range(LENGTH):
        for city2 in range(LENGTH):
            count_links = 0
            if distance[city1][city2] != -1:
                for i in range(len(distance)):
                    if i != city1 and i != city2:
                        mark = i
                        count_links += 1
            if count_links == 1:
                print(f'{city1} has indirect link with {city2} via {i}')
task2_b(distance, 1, 2)