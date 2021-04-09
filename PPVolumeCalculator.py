print('Enter PP length in cm:')
pplength = float(input())
print('Enter PP thickness:')
ppthickness = float(input())
ppvolume = ppthickness/2**2*3.14*pplength
print('your pp is %s cm3'%ppvolume)
if ppvolume > 23:
  print('U Hav Beeg PP')
elif ppvolume < 19:
  print('U Hav Smol PP')
else:
  print('U Hav Normie PP')
