dayType = 2

weekend = 1
workday = 2
holliday = 3

if dayType == 1:
    print('weekend')
elif dayType == 2:
    pass
else:
    print('holliday')

print(None == False)

dayDescription = 'weekend' if dayType == 1 else 'workday' if dayType == 2 else 'holliday'
print(dayDescription)