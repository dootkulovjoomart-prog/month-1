data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations=[]
codes=[]

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)

operators=dict(zip(designations,[set([code]) for  code in codes]))

del operators['Fonex']
operators.pop('Katel')

operators['Megacom'].update(['0999','0555'])
operators["O!"].update(['0708','0503'])
operators["Beeline"].update(['0222','0777'])
for key,value in operators.items():
    print(f'{key} - {value}')
