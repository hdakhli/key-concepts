class Phone:
    def __init__(self, brand: str, color: str, ram: int, storage: int):
        self._brand = brand
        self._color = color
        self._ram = ram
        self._storage = storage

    def display_features(self):
        print(f"brand: {self._color}, color: {self._color}, "
              f"ram: {self._ram}, storage: {self._storage}")

    def call(self, phone_num: str):
        print(f"I'm calling: {phone_num}")

    def send_sms(self, phone_num: str):
        print(f"I'm sending text message to: {phone_num}")


samsung = Phone("Samsung", "black", 2048, 60)
xiaomi = Phone("Xiaomi", "Red", 4096, 120)
sony = Phone("Sony", "Blue", 4096, 250)
