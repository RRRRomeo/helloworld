'''my name's RRRRomeo
接下来的时间我希望我能多学点东西快速成长
要学的东西很多
可以慢慢来
flutter
Django
JavaScript
TensorFlow
慢慢来别急'''

class Hero:
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __str__(self):
        return (self.name + self.hobby )


RRRRomeo = Hero('RRRRomeo',25,'做梦思考')

print(RRRRomeo)