def same_by(characteristic, objects):
    res = list(map(lambda obj: characteristic(obj) == characteristic(objects[0]), objects))
    return res
    
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')