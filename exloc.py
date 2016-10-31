loc_vec = []
with open('loc_front.txt') as fp:
    for k in fp:
        loc_x = float(k.strip().split(' ')[1].replace(',', ''))
        loc_y = float(k.strip().split(' ')[2])
        loc_vec.append([loc_x, loc_y])


with open('loc_for_js.txt', 'w') as fp:
    fp.write(str(loc_vec))
