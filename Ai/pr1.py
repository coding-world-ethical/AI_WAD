H = {}
adjac_lis = {}
lst = []

num1 = int(input('NUMBER OF LOCATIONS : '))

for x in range(num1):
    print()

    ver1 = input("ENTER THE NAME OF CITY : ")
    h = int(input(f"ENTER THE h VALUE FOR THE CITY {ver1}: "))
    H[ver1] = h

    num2 = int(input("ENTER THE NUMBER OF CONNECTED LOCATIONS : "))

    for y in range(num2):
        ver2 = str(input("ENTER THE ADJACENT CITY : "))
        dist = int(input("ENTER THE DISTANCE : "))
        lst.append((ver2, dist))

    if (len(lst) > 0):
        adjac_lis[ver1] = lst

    lst = []

print(adjac_lis)
print("\n")

print(H)
print("\n")

print(lst)


def get_neighbors(z):
    return adjac_lis[z]


def heuristic(n):
    return H[n]


def a_star_algorithm(start, stop):
    open_listy = set([start])
    closed_listy = set([])

    G = {}
    G[start] = 0

    par = {}
    par[start] = start

    while len(open_listy) > 0:
        n = None

        for z in open_listy:
            if n == None or G[z] + heuristic(z) < G[n] + heuristic(n):
                n = z

        if n == None:
            print('GIVEN PATH DOES NOT EXIST!!!')
            return None

        if n == stop:
            path = []

            while par[n] != n:
                path.append(n)
                n = par[n]

            path.append(start)
            path.reverse()

            print('GIVEN PATH IS FOUND : {}'.format(path))
            return path

        for (m, dist) in get_neighbors(n):
            if m not in open_listy and m not in closed_listy:
                open_listy.add(m)
                par[m] = n
                G[m] = G[n] + dist

            else:
                if G[m] > G[n] + dist:
                    G[m] = G[n] + dist
                    par[m] = n

                    if m in closed_listy:
                        closed_listy.remove(m)
                        open_listy.add(m)

        print(G)
        open_listy.remove(n)
        closed_listy.add(n)

    print('GIVEN PATH DOES NOT EXIST!!!')
    return None


start = input("START CITY : ")
goal = input("GOAL CITY : ")

a_star_algorithm(start, goal)