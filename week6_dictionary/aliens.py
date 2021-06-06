alien_0 = {
    'color':'greew',
    'point':5,
}
alien_1 = {
    'color':'yellow',
    'point':10,
}
alien_2 = {
    'color':'red',
    'point':20,
}
aliens = [alien_0,alien_1,alien_2]
for i in aliens:
    print(i)
aliens = []
for j in range(1,31):
    new_alien = {
            'color':'color_'+str(j),
            'point':j,
        }
    aliens.append(new_alien)
for i in aliens[:5]:
    print(i)
print(len(aliens))