from random import randint

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class GoButton(Button):
    pass


class LotoScreen(BoxLayout):

    liste_des_numeros_tires = ObjectProperty()
    tirage = ObjectProperty()

    def __init__(self, **kwargs):
        super(LotoScreen, self).__init__(**kwargs)

        self.numeros_restants = list(range(1, 100))
        self.numeros_tires = ['' for i in range(1, 100)]
        

    def nouveau_tirage(self):
               
        if len(self.numeros_restants) > 0:
            i = randint(0, len(self.numeros_restants)-1)
            nouveau_numero_tire = self.numeros_restants.pop(i)
            self.numeros_tires[nouveau_numero_tire-1] = str(nouveau_numero_tire)
            self.tirage.text = str(nouveau_numero_tire)
            self.liste_des_numeros_tires.text = '-'.join(s for s in self.numeros_tires if s != '')
        else:
            self.tirage.text = 'Fin'


class MainApp(App):

    def build(self):
        self.title = 'Loto'
        return LotoScreen()


if __name__ == '__main__':
    MainApp().run()