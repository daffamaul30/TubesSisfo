from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker

Window.size = (350, 550)


Builder.load_file("panen.kv")

class Panen(MDApp):
    def __init__(self, **kwargs):
        self.title = "Hasil Panen"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.sm = ScreenManager()
        super().__init__(**kwargs)
    
    def build(self):
        self.root = Factory.InputPanen()
        # self.sm.add_widget()
        # return self.sm

    def show_date_picker(self, *args):
            # print('AAA')
            MDDatePicker(self.set_date).open()

    def set_date(self, date_obj):
        self.previous_date = date_obj
        # print(self.root.ids)
        self.root.ids.date_picker_label.text = str(date_obj)
    
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)

        time_dialog.open()

    def get_time(self, instance, time):
        self.root.ids.time_picker_label.text = str(time)
    
if __name__ == "__main__":
    Panen().run()