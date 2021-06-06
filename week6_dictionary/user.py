user_0 = {'first_name':'alex',
          'family_name':'he',
          'user_name':'alexies_he2233'
}
for i,j in user_0.items():
    print("\nThe 'Key' is",i)
    print("The 'Value' is",j)
for i in user_0.keys():#等效为for i in user_0
    print('\n\nThe Value is',i.title())
favorite = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
} 
friends = ['phil','sarah']
for i,j in favorite.items():
    print(i.title())
    if i in friends:
      print(' Hi '+i.title()+',I see your favorite language is '+j.title())
      print(' Hi %s,I see your favorite language is %s'%(i.title(),j.title()))
    else:
      pass
for i in set(sorted(favorite.values(),reverse=False)):
    print(i.title())