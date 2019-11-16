#%%
def findJudge1(N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    if N == 1:
        return N

    town = {}
    for person, they_trust in trust:
        town.setdefault(person, []).append(they_trust)

    count = 1
    for person in range(1,N+1):
        if count not in town.keys():
            town[count] = [0]
        count +=1

    i = 1 # individual
    if [0] in town.values():
        for person, they_trust in town.items():
            trusted_by = 0 # needs to be N-1 for judge (doesn't trust themselves)
            if they_trust == [0]:
                while i <= len(town):
                    if person in town[i]:
                        trusted_by += 1
                        if trusted_by == len(town)-1:
                            return person
                    i += 1
        return -1
    else:
        return -1

#%%
def findJudge(N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    people = set(range(1, N+1)) - set(a for a, _ in trust)
    if len(people) != 1:
        return -1
    judge = people.pop()
    return judge if sum(1 for _, b in trust if b == judge) == N-1 else -1



#%%
findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])

#%%
findJudge(4, [[1, 3], [2, 3], [3, 1]])

#%%
findJudge(2, [[1, 2]])


#%%
'''
    town = {}
    for person, they_trust in trust:
        town.setdefault(person, []).append(they_trust)
    #{1: [3, 4], 2: [3, 4], 4: [3]}

    count = 1
    for key in list(town.keys()):
        if count != key:
            town[count] = 0
        count +=1

    print(town)

    i = 1 # individual
    if 0 in town.values():
        trusted_by = 0 # needs to be N-1 for judge (doesn't trust themselves)
        for person, they_trust in town.items():
            if they_trust == 0:
                while i < len(town) and person in town[i]:
                    trusted_by += 1
                    if trusted_by == len(town)-1:
                        return person
                    i += 1
    else:
        return -1
'''
