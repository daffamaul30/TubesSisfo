from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior

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
        
    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(ItemDrawer(icon=icon_name, text=icons_item[icon_name]))
    
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
    
class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


# class TestNavigationDrawer(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def on_start(self):
#         icons_item = {
#             "folder": "My files",
#             "account-multiple": "Shared with me",
#             "star": "Starred",
#             "history": "Recent",
#             "checkbox-marked": "Shared with me",
#             "upload": "Upload",
#         }
#         for icon_name in icons_item.keys():
#             self.root.ids.content_drawer.ids.md_list.add_widget(
#                 ItemDrawer(icon=icon_name, text=icons_item[icon_name]))
    
if __name__ == "__main__":
    Panen().run()