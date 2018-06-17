import numpy as np

def cf():
    # with open('test.txt', 'rt') as input:
    #     first_line = f.read()
    #     print(first_line)
    first_line = raw_input().split()
    num_of_items = int(first_line[0])
    num_of_users = int(first_line[1])
    list_of_lists = []
    for i in range(num_of_items):
        line = raw_input().split()
        list_of_lists.append(np.genfromtxt(line))
    m = np.stack(list_of_lists)
    print(m)
    mean_reduced_matrix = np.copy(m)
    mean_matrix = np.nanmean(m, axis = 1, keepdims = True)
    print(mean_matrix)
    mean_reduced_matrix -= mean_matrix
    print(mean_reduced_matrix)


    num_of_queries = int(raw_input())
    for i in range(num_of_queries):
        line = raw_input().split()
        item = int(line[0])
        user = int(line[1])
        # type of similarity, 0 = item-item, 1 = user-user
        t = int(line[2])
        # maximum cardinal number, used when deciding how many items we compare
        # to the current one
        k = int(line[3])


if __name__=='__main__':
    cf()
