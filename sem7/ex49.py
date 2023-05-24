import math

def find_farthest_orbit(list_of_orbits):
    orb_filter = list(filter(lambda x: x[0] != x[1], orbits))
    # print(orb_filter)
    
    s = []
    max_sq = orb_filter[0][0]*orb_filter[0][1]*math.pi
    res = None
    for i in range(len(orb_filter)):
        dif_sq =  orb_filter[i][0]*orb_filter[i][1]*math.pi
        if max_sq <dif_sq:
            max_sq = dif_sq
            res = i
    return orb_filter[res]
    
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))