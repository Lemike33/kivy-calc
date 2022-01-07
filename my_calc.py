from kivy.uix.gridlayout import GridLayout  # импорт класса слоя в который можно помещать объекты (кнопки, текст и др.)
from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (500, 700)


class Container(GridLayout):
    operand1 = []
    operand2 = []
    operand_1 = ''
    operand_2 = ''
    numeric = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    operations = ('+', '-', '*', '/')
    my_operations = ''
    result = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def numeration(self, num):
        while num in Container.numeric:
            if Container.my_operations == '':
                Container.operand1.append(num)
                self.printNum()
                break
            else:
                Container.operand2.append(num)
                self.printNum2()
                break

    def printNum(self):
        oper1 = ''
        for i in Container.operand1:
            oper1 += str(i)
            if oper1[-1] == '.' and oper1[-2] == '.':
                Container.operand1.pop(-1)
            self.number.text = oper1
        Container.operand_1 = oper1

    def printNum2(self):
        oper2 = ''
        for i in Container.operand2:
            oper2 += str(i)
            if oper2[-1] == '.' and oper2[-2] == '.':
                Container.operand2.pop(-1)
            self.number.text = oper2
        Container.operand_2 = oper2

    def operation(self, oper):
        if oper in Container.operations:
            if oper == '+':
                Container.my_operations = '+'
            elif oper == '-':
                Container.my_operations = '-'
            elif oper == '*':
                Container.my_operations = '*'
            else:
                Container.my_operations = '/'

    def equal(self, equal):
        if equal == '=':
            if Container.my_operations == '+':
                res = float(Container.operand_1) + float(Container.operand_2)
                self.number.text = str(res)
                Container.my_operations = ''
                Container.operand2.clear()
                Container.operand_1 = float(res)

            elif Container.my_operations == '-':
                res = float(Container.operand_1) - float(Container.operand_2)
                self.number.text = str(res)
                Container.my_operations = ''
                Container.operand2.clear()
                Container.operand_1 = float(res)

            elif Container.my_operations == '*':
                res = float(Container.operand_1) * float(Container.operand_2)
                self.number.text = str(res)
                Container.my_operations = ''
                Container.operand2.clear()
                Container.operand_1 = float(res)

            elif Container.my_operations == '/':
                if Container.operand_2 == '0':
                    self.number.text = 'Ошибка - нельзя делить на 0!'
                else:
                    res = float(Container.operand_1) / float(Container.operand_2)
                    self.number.text = str(res)
                    Container.my_operations = ''
                    Container.operand2.clear()
                    Container.operand_1 = float(res)

    def cleaner(self, ac):
        if ac == 'AC':
            Container.operand1.clear()
            Container.operand2.clear()
            Container.my_operations = ''
            self.number.text = ''


class CalcApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "LeMike33 CORP"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == '__main__':
    CalcApp().run()
