class Dog:
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    def speak(self):
        return self.speakText

    def getName(self):
        return self.name

    def birthDate(self):
        return str(self.month)+'/'+str(self.day)+'/'+str(self.year)

    def changeSpeak(self, bark):
        self.speakText = bark

    def __add__(self, otherDog):
        return Dog('Puppy of ' + self.name + ' and ' + otherDog.name, \
                   self.month, self.day, self.year + 1, \
                   self.speakText + otherDog.speakText)
def main():
    boyDog = Dog('Mesa', 05, 15, 2010, 'WOOF')
    girlDog = Dog('Sequio', 06, 20, 2010, 'Bark')
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeSpeak('Woofy Woofy')
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print('Puppy Speak: ', puppy.speak())
    print('Puppy Birthday: ',puppy.birthDate())
    print('Puppy Name: ',puppy.getName())

if __name__ == '__main__':
    main()