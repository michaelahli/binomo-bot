from random import seed
from random import gauss
from random import randint
from datetime import datetime

i = randint(0, 1)
balance = 'Rp19,000,000.00'
balance = balance.replace('Rp', '')
balance = balance.replace(',', '')
balance = balance[:-3]

current_time = datetime.now()
# selisih 25 detik lebih lambat
print(current_time.second)
