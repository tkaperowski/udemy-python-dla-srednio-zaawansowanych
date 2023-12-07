number = 10
print("Variable int:", number, id(number))
number +=2
print("Int variable is immutable:", number, id(number)) #inne id czyli inna pamiec czyli niezmienna (immutable)

text = "aaa"
print("Variable text:", text, id(text))
text = text + "b"
print("Str variable is immutable:", text, id(text))

list = [1,2,3]
print("Variable list:", list, id(list))
list = list + [4]
print("List variable is mutable:", list, id(list))

days = ['mon', 'tues', 'wed', 'thu', 'fri', 'sat', 'sun']
print("zmianna days: ", days, id(days))
workdays = days.copy() #robisz kopię zmiennej, odcinasz sie od oryginału
print("zmianna workdays: ", workdays, id(workdays))
workdays.remove('sat') # nie zmieniasz zmiennej przez remove()
workdays.remove('sun')
print("zmianna days: ", days, id(days))
print("zmianna workdays: ", workdays, id(workdays))

