#!/usr/bin/python3

def hd_list():
    import hidden_4

    List = dir(hidden_4)
    N_List = []

    i = 0
    n = len(List)
    List.sort()

    while (i < n):
        if ((List[i])[ : 2] != "__"):
            N_List.append(List[i])
        i += 1

    n_list_len = len(N_List)
    j = 0

    while j < n_list_len:
        print(N_List[j])
        j += 1

if __name__ == "__main__":
    hd_list()
