


        
from address import Address
from mailing import Mailing

to_address = Address("101000", "Кашира", "Новая", "8", "11")
from_address = Address("125009", "Саратов", "Литейный", "5", "5")

mailing = Mailing(to_address, from_address, 520, "TRK89745")


print(mailing)