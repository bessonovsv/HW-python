from address import Address
from mailing import Mailing

to_address = Address("173009", "Великий Новгород", "Псковская", "44", "1")
from_address = Address("173009", "Великий Новгород", "Псковская", "48", "135")
track = "1"
cost = 150
mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
