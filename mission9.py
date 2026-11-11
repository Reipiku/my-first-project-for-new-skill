nama_mesin_cuci = {'artis': 'rapi amat', 'influencer': 'widih salim'}
# contoh penggunaan defaultdict dalam error handling
from collections import defaultdict
hitung = defaultdict(int)
for key in nama_mesin_cuci:
    hitung[key] += 1
    print(hitung[key])

# contoh penggunaan get() dalam error handling
nama_mesin_cuci = {'artis': 'rapi amat', 'influencer': 'widih salim'}
print(nama_mesin_cuci.get('antek_antek_asing'))
print(nama_mesin_cuci.get('antek_antek_asing', 'tidak ada'))

# contoh penggunaan in if else dalam error handling
nama_mesin_cuci = {'artis': 'rapi amat', 'influencer': 'widih salim'}
if 'antek_antek_asing' in nama_mesin_cuci:
    print(nama_mesin_cuci['antek_antek_asing'])
else:
    print('tidak ada')

# contoh penggunaan try except dalam error handling
nama_mesin_cuci = {'artis': 'rapi amat', 'influencer': 'widih salim'}
try: 
    print(nama_mesin_cuci['antek_antek_asing'])
except KeyError:
    print('tidak ada')
