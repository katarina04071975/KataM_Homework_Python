class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"

        from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Apple", "iPhone 14", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79007654321"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79009876543"))
catalog.append(Smartphone("Google", "Pixel 6", "+79005432123"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79006789012"))

for smartphone in catalog:
    print(smartphone)