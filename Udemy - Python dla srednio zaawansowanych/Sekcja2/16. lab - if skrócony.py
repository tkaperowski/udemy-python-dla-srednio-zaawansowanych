
price = 123
bonus = 23
bonus_granted = False

# if bonus_granted:
#     price -= bonus
# print(price)

price = price - bonus if bonus_granted else price
print(price)


rating = 5
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('week')

ocena = 'very good' if rating == 5 else 'good' if rating == 4 else 'week'
print(ocena)

print('very good' if rating == 5 else 'good' if rating == 4 else 'week')


today_weekday = 'poniedziałęk'

if today_weekday == 'poniedziałęk':
    print('ja nie mogę bo pomagam mamie')
elif today_weekday == 'wtorek':
    print('ty masz w domu pranie')
elif today_weekday == 'sroda':
    print('ty masz w domu pranie')
elif today_weekday == 'czwartek':
    print('ja mam dyżur')
elif today_weekday == 'piątek':
    print('ja mam dwa zebrania')
elif today_weekday == 'sobota':
    print('ty na lekcje ganiasz')
else:
    print('niedziela będzie dla nas')

print('ja nie mogę bo pomagam mamie' if today_weekday == 'poniedziałęk' else 'ty masz w domu pranie' if today_weekday == 'wtorek' or today_weekday == 'sroda' else 'ja mam dyżur' if today_weekday == 'czwartek' else 'ja mam dwa zebrania')

