from smartphone import Smartphone

catalog = [
    Smartphone("Doogee", "Max 41", "+79814567556"),
    Smartphone("Samsung", "A30", "+79824567893"),
    Smartphone("Prestigio", "L51", "+79835673478")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")
