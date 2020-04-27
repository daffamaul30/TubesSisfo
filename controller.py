from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty, ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.icon_definitions import md_icons
import m_panen

# Window.size = (350, 550)

class InputPanen(Screen):
    pass

class InputProduksi(Screen):
    pass

class Dashboard(Screen):
    pass

class HasilInput(Screen):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

# class ItemDrawer(OneLineIconListItem):
#     icon = StringProperty()

# class DrawerList(ThemableBehavior, MDList):
#     def set_color_item(self, instance_item):
#         """Called when tap on a menu item."""

#         # Set the color of the icon and text for the menu item.
#         for item in self.children:
#             if item.text_color == self.theme_cls.primary_color:
#                 item.text_color = self.theme_cls.text_color
#                 break
#         instance_item.text_color = self.theme_cls.primary_color
def toast(text):
    from kivymd.toast.kivytoast import toast
    toast(text)
    
class Main(MDApp):
    icons = list(md_icons.keys())[15:30]
    def __init__(self, **kwargs):
        self.title = "Frinsa"
        self.theme_cls.primary_palette = "LightGreen"
        super().__init__(**kwargs)
        #print(self.root.ids.screen_manager.get_screen("inputpanen").ids.time_picker_label.text)
        ##### DROPDOWN
        self.VARIABLE = ""
        self.menu_labels = [
            {"viewclass": "MDMenuItem",
            "text": "Kopi Robussa","callback": self.callback_for_menu_items,},
            {"viewclass": "MDMenuItem",
            "text": "Kopi Luwak","callback": self.callback_for_menu_items,},
            {"viewclass": "MDMenuItem",
            "text": "Kopi Sawit","callback": self.callback_for_menu_items,},
        ]
        
    def callback_for_menu_items(self, *args):
        toast(args[0])
    def change_variable(self, value):
        print("value=", value)
        self.VARIABLE = value
        print("self.VARIABLE=", self.VARIABLE)
        self.root.ids.screen_manager.get_screen("inputpanen").ids.jenis.text = value
        #####
        
    
        
    def set_item(self, instance):
        self.screen.ids.dropdown_item.set_item(instance.text)
        
    def build(self):
        return Builder.load_file("kv/Main.kv")
    
    # def on_start(self):
    #     icons_item = {
    #         "home": "Home",
    #         "leaf": "Input Hasil Panen",
    #         "factory": "Input Produksi",
    #         # "history": "Recent",
    #         # "checkbox-marked": "Shared with me",
    #         # "upload": "Upload",
    #     }
    #     for icon_name in icons_item.keys():
    #         self.root.ids.content_drawer.ids.md_list.add_widget(
    #             ItemDrawer(icon=icon_name, text=icons_item[icon_name])
    #         )

    def show_date_picker(self, *args):
        # print('AAA')
        MDDatePicker(self.set_date).open()
    
    def change_screen(self):
        # print(self.root.ids)
        pass

    def set_date(self, date_obj):
        self.previous_date = date_obj
        # print(self.root.ids.screen_manager)
        
        self.root.ids.screen_manager.get_screen("inputpanen").ids.date_picker_label.text = str(date_obj)
    
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)

        time_dialog.open()

    def get_time(self, instance, time):
        
        self.root.ids.screen_manager.get_screen("inputpanen").ids.time_picker_label.text = str(time)
        
    def panen(self):
        jenis = self.root.ids.screen_manager.get_screen("inputpanen").ids.jenis.text
        
        berat = self.root.ids.screen_manager.get_screen("inputpanen").ids.berat.text
        waktu = self.root.ids.screen_manager.get_screen("inputpanen").ids.time_picker_label.text
        tanggal = self.root.ids.screen_manager.get_screen("inputpanen").ids.date_picker_label.text
        try:
            m_panen.inputPanen(jenis,berat,waktu,tanggal)
        except:
            print("ERROR : ",jenis,berat,waktu,tanggal)
    def dataPanen(self):
        try :
            m_panen.getPanen()    
        except:
            print("ERROR :")
    def test(self):
        print(self.root.ids.toolbar.title)
        
    # def show_dialog_submit_panen(self):
        
    
if __name__ == "__main__":
    Main().run()