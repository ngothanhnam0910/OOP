class Phone:
    def __init__(self, model, color, size):
        self.model = model
        self.color = color
        self.size = size

    def call(self, number):
        print(f"Calling {number}")

    def send_sms(self, number, message):
        print(f"Sending SMS to {number}, message: {message}")

    def play_music(self, song):
        print(f"Now playing {song}")

# Creating instances (objects) of the Phone class
iphone = Phone("iPhone 12", "Black", "Medium")
samsung = Phone("Galaxy S21", "Blue", "Large")

iphone.send_sms("kdkdkdk1", "Hello")