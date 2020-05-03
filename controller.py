from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivymd.uix.dialog import MDInputDialog, MDDialog
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.list import ThreeLineListItem
# from kivy.properties import StringProperty, ObjectProperty
# from kivymd.theming import ThemableBehavior
from kivymd.uix.menu import MDDropdownMenu
# from kivymd.icon_definitions import md_icons
from kivymd import images_path
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import m_panen
import m_produksi

Window.size = (350, 650)

Builder.load_file('kv/InputPanen.kv')
Builder.load_file('kv/HasilInput.kv')  
Builder.load_file('kv/Dashboard.kv') 
Builder.load_file('kv/Cherry.kv')
Builder.load_file('kv/GB_Transport.kv')
Builder.load_file('kv/GB_Bongkar.kv') 
Builder.load_file('kv/GB_Jemur.kv') 
Builder.load_file('kv/GK_Hull.kv') 
Builder.load_file('kv/GK_Jemur.kv') 
Builder.load_file('kv/Green_Suton.kv') 
Builder.load_file('kv/Green_Grading.kv')
Builder.load_file('kv/Green_Color.kv')
Builder.load_file('kv/Green_HandPick.kv')
Builder.load_file('kv/HasilAkhir.kv')
Builder.load_file('kv/Search.kv')
Builder.load_file('kv/Laporan.kv')

class Content(ThreeLineListItem):
    pass

class Laporan(Screen):
    pass
    
class InputPanen(Screen):
    pass
  
class GB_Transport(Screen):
    pass

class HasilAkhir(Screen):
    pass

class Cherry(Screen):
    pass

class Search(Screen):
    pass

class InputProduksi(Screen):
    pass

class Dashboard(Screen):
    pass

class Hasilpanen(Screen):
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
    def __init__(self, **kwargs):
        self.title = "Frinsa"
        self.theme_cls.primary_palette = "LightGreen"
        super().__init__(**kwargs)
        
        ##### DROPDOWN
        self.VARIABLE = ""
        self.varietas_labels = [
            {"viewclass": "MDMenuItem",
            "text": "Kopi Robusta","callback": self.callback_for_varietas_items,},
            {"viewclass": "MDMenuItem",
            "text": "Kopi Arabica","callback": self.callback_for_varietas_items,},
        ]
        # Dropdown Proses
        self.Process = ""
        self.proses_labels = [
            {"viewclass": "MDMenuItem",
            "text": "Full Wash","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Wet Hull","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Natural","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Honey","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Lactic Full Wash","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Natural Wet Hull","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Honey Wet Hull","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Natural Lactic","callback": self.callback_for_proses_items,},
            {"viewclass": "MDMenuItem",
            "text": "Honey Lactic","callback": self.callback_for_proses_items,},
        ]
        
        self.varietas_labels_search = [
            {"viewclass": "MDMenuItem",
            "text": "Kopi Robusta","callback": self.callback_for_varietas_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Kopi Arabica","callback": self.callback_for_varietas_items_search,},
        ]
        # Dropdown Search Proses
        self.Process = ""
        self.proses_labels_search = [
            {"viewclass": "MDMenuItem",
            "text": "Full Wash","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Wet Hull","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Natural","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Honey","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Lactic Full Wash","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Natural Wet Hull","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Honey Wet Hull","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Natural Lactic","callback": self.callback_for_proses_items_search,},
            {"viewclass": "MDMenuItem",
            "text": "Honey Lactic","callback": self.callback_for_proses_items_search,},
        ]
        
        
    def callback_for_proses_items(self, *args):
        toast(args[0])
        self.root.ids.screen_manager.get_screen("inputpanen").ids.proses.text = args[0]
    def callback_for_varietas_items(self, *args):
        toast(args[0])
        self.root.ids.screen_manager.get_screen("inputpanen").ids.varietas.text = args[0]
    
    def change_variable_varietas(self, value):
        
        print("dipilih > ",value)
        #####
    def change_variable_proses(self, value):
        
        self.root.ids.screen_manager.get_screen("inputpanen").ids.proses.text = value
        #####
           
    ##search part
    def callback_for_proses_items_search(self, *args):
        toast(args[0])
        self.root.ids.screen_manager.get_screen("search").ids.search_proses.text = args[0]
    def callback_for_varietas_items_search(self, *args):
        toast(args[0])
        self.root.ids.screen_manager.get_screen("search").ids.search_varietas.text = args[0]
        
    def set_item(self, instance):
        self.screen.ids.dropdown_item.set_item(instance.text)
        
    def build(self):
        return Builder.load_file("kv/Main.kv")
    
    def delete(self, *args):
        print("MASOK", args[0])
        m_panen.deletePanen(self.arrayPanen[int(args[0])][8])
        self.refresh_dashboard()
        
    def refresh_dashboard(self):
        self.root.ids.screen_manager.get_screen("dashboard").ids.box.clear_widgets()
        self.on_start()
    
    def on_start(self):
        result = m_panen.getAllPanen()
        j = 0
        self.arrayPanen = []
        for i in result:
            update = "On Progress"
            print(i)
            result = m_produksi.getDataSubProcess(i[4],i[3],i[8],False)
            
            try :
                hpp = result[1]//result[0]
            except:
                hpp = "Error Data"
            #x.insert(len(x),hpp)
            x = i + (hpp,)
            
            self.arrayPanen.append(x)
            #self.arrayPanen[j] = x
            if i[4] == "green_hand_pick":
                result = m_produksi.getTanggalTerakhir(i[8])
                update = 'Tanggal Produksi Terakhir : {}'.format(result[0])
            self.root.ids.screen_manager.get_screen("dashboard").ids.box.add_widget(
                MDExpansionPanel(
                    icon=f"kv/assets/frinsa.png",
                    content=Content(id="{}".format(j),text="Biaya (Hpp) /Kg : Rp. {}".format(hpp), 
                                    secondary_text="Tanggal Panen : {}".format(i[0]),
                                    tertiary_text=update),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Proses : {}".format(i[3]),
                        secondary_text="Blok : {}".format(i[1]),
                        tertiary_text="Varietas : {}".format(i[2]),
                    )
                )
            )
            j+=1
    
    def test_toast(self,*args):
        toast(args[0])
        print(args[0])    
        print(self.arrayPanen[int(args[0])][0])
        tanggal = self.arrayPanen[int(args[0])][0]
        blok = self.arrayPanen[int(args[0])][1]
        varietas = self.arrayPanen[int(args[0])][2]
        proses = self.arrayPanen[int(args[0])][3] 
        status = self.arrayPanen[int(args[0])][4]
        biaya = str(self.arrayPanen[int(args[0])][9]) 
        id_panen = self.arrayPanen[int(args[0])][8]
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.hasilakhir_date.text = tanggal
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.hasilakhir_blok.text = blok
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.hasilakhir_varietas.text = varietas 
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.hasilakhir_proses.text = proses
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.hasilakhir_biaya.text = biaya   
        ###
        if proses == "Wet Hull" or proses == "Natural Wet Hull" or proses == "Honey Wet Hull":
            subprocess = ["Panen","Cherry Wet Mill","Gabah Basah Transport","Gabah Basah Bongkar","Gabah Basah Jemur","Gabah Kering Hull","Gabah Kering Jemur","Green Bean Suton","Green Bean Grading","Green Bean Sorter","Green Bean Hand Pick"]
        else:
            subprocess = ["Panen","Cherry Wet Mill","Gabah Basah Transport","Gabah Basah Bongkar","Gabah Basah Jemur","Gabah Kering Hull","Green Bean Suton","Green Bean Grading","Green Bean Sorter","Green Bean Hand Pick"]
        print(self.arrayPanen[int(args[0])])
        result = m_produksi.getDataSubProcess(status,proses,id_panen,True)
        beratSubProcess = []
        for i in result:
            beratSubProcess.append(i[0])
        
        subprocess = subprocess[0:len(beratSubProcess)]
        print(beratSubProcess)
        print(subprocess)
        #result = m_produksi.getDataSubProcess(i[4],i[3],i[8],False)
        # beratSubProcess = []
        # beratSubProcess.append(data_cherry[3])
        # beratSubProcess.append(m_produksi.getDataWetMill(id_cherry)[0])
        # beratSubProcess.append(m_produksi.getDataTransport(id_cherry)[0])
        # beratSubProcess.append(m_produksi.getDataBongkar(id_cherry)[0])
        # beratSubProcess.append(m_produksi.getDataGabahBasahJemur(id_cherry)[0])
        # beratSubProcess.append(m_produksi.getDataGabahKeringHull(id_gabahB)[0])
        # if self.tipe_proses != "Wet Hull" or self.tipe_proses != "Natural Wet Hull" or self.tipe_proses != "Honey Wet Hull":
        #     beratSubProcess.append(m_produksi.getDataGabahKeringJemur(id_gabahB)[0])
        # else:
        #     del subprocess[6]
        # beratSubProcess.append(m_produksi.getDataGreenBeanSuton(id_gabahK)[0])
        # beratSubProcess.append(m_produksi.getDataGreenBeanGrading(id_gabahK)[0])
        # beratSubProcess.append(m_produksi.getDataGreenBeanSorter(id_gabahK)[0])
        # beratSubProcess.append(m_produksi.getDataGreenBeanHandPick(id_gabahK)[0])
        
        
        print("FINAL")
        self.root.ids.screen_manager.current = "hasilakhir"
        plt.plot((subprocess),(beratSubProcess)) # ((Subproses),(Berat)) 
        plt.title("Berat Per Subproses", fontsize=10)
        plt.yticks(fontsize=7)
        plt.xticks(fontsize=6)
        # plt.xticks(rotation=90, fontsize=6)
        # plt.tight_layout()
        # box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.root.ids.screen_manager.transition.direction = "left"
        ###
    def afterInput(self):
        self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_tgl_panen.text = self.tanggal
        self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_varietas.text = self.varietas
        self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_blok = self.blok
        self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_berat = self.berat
        self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_biaya = self.biaya
        self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_proses = self.tipe_proses
    def finalReport(self):   
        # TAROH DI FUNCTION SEBELUM PINDAH KE PAGE HASILTERAKHIR
        print("FINAL")
        self.root.ids.screen_manager.current = "hasilakhir"
        self.root.ids.toolbar.title = "Produksi"
        plt.plot(("tttttttttttttttt","inxi","indi","inai","iniFFF","invgi","inqi","inri","inei","izni"),(1,5,1,2,9,2,1,2,1,2)) # ((Subproses),(Berat)) 
        plt.title("Berat Per Subproses", fontsize=10)
        plt.yticks(fontsize=7)
        plt.xticks(fontsize=6)
        # plt.xticks(rotation=90, fontsize=6)
        # plt.tight_layout()
        # box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    
    # def graph(self):
    #     plt.plot([1, 23, 2, 4])
    #     plt.ylabel('some numbers')
    #     self.box = BoxLayout()
    #     self.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    
    
    def show_date_mdm(self,*args):
        self.tgl_screen = args[0]
        MDDatePicker(self.set_date_mdm).open()
    
    def set_date_mdm(self, date_obj):
        self.previous_date2 = date_obj
        self.root.ids.screen_manager.get_screen(self.tgl_screen).ids.date_picker_label.text = str(date_obj)
        
    def show_date_laporan(self,*args):
        self.tgl_screen = args[0]
        MDDatePicker(self.set_date_laporan).open()

    def set_date_laporan(self, date_obj):
        self.previous_date2 = date_obj
        if self.tgl_screen == "awal":
            self.root.ids.screen_manager.get_screen("laporan").ids.date_picker_tgl_awal.text = str(date_obj)
        elif self.tgl_screen == "akhir":
            self.root.ids.screen_manager.get_screen("laporan").ids.date_picker_tgl_akhir.text = str(date_obj)
            
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        self.root.ids.screen_manager.get_screen("inputpanen").ids.time_picker_label.text = str(time)
        
    def panen(self):
        tanggal = self.root.ids.screen_manager.get_screen("inputpanen").ids.date_picker_label.text
        blok = self.root.ids.screen_manager.get_screen("inputpanen").ids.blok.text
        varietas = self.root.ids.screen_manager.get_screen("inputpanen").ids.varietas.text
        tipe_proses = self.root.ids.screen_manager.get_screen("inputpanen").ids.proses.text
        berat = self.root.ids.screen_manager.get_screen("inputpanen").ids.berat.text
        biaya = self.root.ids.screen_manager.get_screen("inputpanen").ids.biayacherry.text
        try:
            m_panen.inputPanen(tanggal,blok,varietas,tipe_proses,berat,biaya)
            self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_tgl_panen.text = tanggal
            self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_varietas.text = varietas
            self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_blok.text = blok
            self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_berat.text = berat
            self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_biaya.text = biaya
            self.root.ids.screen_manager.get_screen("hasilpanen").ids.hsl_proses.text = tipe_proses
            self.refresh_dashboard()
            self.root.ids.screen_manager.current = "hasilpanen"
            root.manager.transition.direction = "left"
        except:
            print("ERROR : ",tanggal,blok,varietas,tipe_proses)
        finally:
            self.root.ids.screen_manager.get_screen("inputpanen").ids.date_picker_label.text = ""
            self.root.ids.screen_manager.get_screen("inputpanen").ids.blok.text = ""
            self.root.ids.screen_manager.get_screen("inputpanen").ids.varietas.text = ""
            self.root.ids.screen_manager.get_screen("inputpanen").ids.proses.text = ""
            self.root.ids.screen_manager.get_screen("inputpanen").ids.berat.text = ""
            self.root.ids.screen_manager.get_screen("inputpanen").ids.biayacherry.text = ""
            
    def refresh_callback(self, *args):
        pass
            
    def dataPanen(self):
        self.tanggal = self.root.ids.screen_manager.get_screen("search").ids.date_picker_label.text
        self.blok = self.root.ids.screen_manager.get_screen("search").ids.search_blok.text
        self.varietas = self.root.ids.screen_manager.get_screen("search").ids.search_varietas.text
        self.tipe_proses = self.root.ids.screen_manager.get_screen("search").ids.search_proses.text
        try :
            data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
            status = data_cherry[2]
            print(data_cherry)
            if status == "cherry":
                ##panggil halaman wetmill  
                self.root.ids.screen_manager.current = "cheri"
                self.root.ids.toolbar.title = "Cherry-Wett Mill"
            elif status == "wetmill": 
                ##panggil halaman transport
                self.root.ids.screen_manager.current = "gb_transport"
                self.root.ids.toolbar.title = "GB-Transport Ke Pabrik"
            elif status == "transport":
                ##panggil halaman bongkar
                self.root.ids.screen_manager.current = "gb_bongkar"
                self.root.ids.toolbar.title = "GB-Bongkar"
            elif status == "bongkar":
                ##panggil halaman jemur
                self.root.ids.screen_manager.current = "gb_jemur"
                self.root.ids.toolbar.title = "GB-Jemur"
            elif status == "gb_jemur":
                ##panggil halaman gk hull
                self.root.ids.screen_manager.current = "gk_hull"
                self.root.ids.toolbar.title = "GK-Hull"
            elif status == "gk_hull" :
                if self.tipe_proses == "Wet Hull" or self.tipe_proses == "Natural Wet Hull" or self.tipe_proses == "Honey Wet Hull":
                    ##panggil gk_jemur
                    print("GK JEMUR")
                    self.root.ids.screen_manager.current = "gk_jemur"
                    self.root.ids.toolbar.title = "GK-Jemur"
                else:
                    ##panggil GreenSuton
                    print("GREEN SUTON")
                    self.root.ids.screen_manager.current = "green_suton"
                    self.root.ids.toolbar.title = "Green Bean-Suton"
            elif status == "gk_jemur" :
                ##panggil GreenSuton 
                #print("GREEN SUTON")
                self.root.ids.screen_manager.current = "green_suton"
                self.root.ids.toolbar.title = "Green Bean-Suton"
            elif status == "green_suton":
                ##panggil GreenGrading
                #print("GRADING")
                self.root.ids.screen_manager.current = "green_grading"
                self.root.ids.toolbar.title = "Green Bean-Grading"
            elif status == "green_grading":
                ##panggil Green Color
                self.root.ids.screen_manager.current = "green_color"
                self.root.ids.toolbar.title = "Green Bean-Color Sorter"
            elif status == "green_color":
                ##panggil Green HandPick
                #finalReport(self)
                self.root.ids.screen_manager.current = "green_hand_pick"
                self.root.ids.toolbar.title = "Green Bean-Hand Pick"      
        except:
            print("ERROR :",self.tanggal,self.blok,self.varietas,self.tipe_proses)
            
    def test(self):
        print(self.root.ids.toolbar.title)

    def wetmill(self):
        
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("cheri").ids.berat_cherry_wet_mill.text
        harga = self.root.ids.screen_manager.get_screen("cheri").ids.biaya_cherry_wet_mill.text
        tanggal = self.root.ids.screen_manager.get_screen("cheri").ids.date_picker_label.text  
        m_produksi.inputWetMill(id_cherry,berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("cheri").ids.berat_cherry_wet_mill.text = ""
        self.root.ids.screen_manager.get_screen("cheri").ids.biaya_cherry_wet_mill.text = ""
        self.root.ids.screen_manager.get_screen("cheri").ids.date_picker_label.text = ""
    
    def transport(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("gb_transport").ids.berat_gb_transport.text
        harga = self.root.ids.screen_manager.get_screen("gb_transport").ids.biaya_gb_transport.text
        tanggal = self.root.ids.screen_manager.get_screen("gb_transport").ids.date_picker_label.text
        m_produksi.inputTransport(id_cherry,berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("gb_transport").ids.berat_gb_transport.text = ""
        self.root.ids.screen_manager.get_screen("gb_transport").ids.biaya_gb_transport.text = ""
        self.root.ids.screen_manager.get_screen("gb_transport").ids.date_picker_label.text = ""
    
    def bongkar(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("gb_bongkar").ids.berat_gb_bongkar.text
        harga = self.root.ids.screen_manager.get_screen("gb_bongkar").ids.biaya_gb_bongkar.text
        tanggal = self.root.ids.screen_manager.get_screen("gb_bongkar").ids.date_picker_label.text
        result = m_produksi.getGabahBasah(id_cherry)
        m_produksi.inputBongkar(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("gb_bongkar").ids.berat_gb_bongkar.text = ""
        self.root.ids.screen_manager.get_screen("gb_bongkar").ids.biaya_gb_bongkar.text = ""
        self.root.ids.screen_manager.get_screen("gb_bongkar").ids.date_picker_label.text = ""
        
    def gbJemur(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("gb_jemur").ids.berat_gb_jemur.text
        harga = self.root.ids.screen_manager.get_screen("gb_jemur").ids.biaya_gb_jemur.text
        tanggal = self.root.ids.screen_manager.get_screen("gb_jemur").ids.date_picker_label.text
        result = m_produksi.getGabahBasah(id_cherry)
        m_produksi.inputGabahBasahJemur(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("gb_jemur").ids.berat_gb_jemur.text = ""
        self.root.ids.screen_manager.get_screen("gb_jemur").ids.biaya_gb_jemur.text = ""
        self.root.ids.screen_manager.get_screen("gb_jemur").ids.date_picker_label.text = ""
    
    def gkHull(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("gk_hull").ids.berat_gk_hull.text
        harga = self.root.ids.screen_manager.get_screen("gk_hull").ids.biaya_gk_hull.text
        tanggal = self.root.ids.screen_manager.get_screen("gk_hull").ids.date_picker_label.text
        result = m_produksi.getGabahBasah(id_cherry)
        m_produksi.inputGabahKeringHull(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("gk_hull").ids.berat_gk_hull.text = ""
        self.root.ids.screen_manager.get_screen("gk_hull").ids.biaya_gk_hull.text = ""
        self.root.ids.screen_manager.get_screen("gk_hull").ids.date_picker_label.text = ""
    
    def gkJemur(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("gk_jemur").ids.berat_gk_jemur.text
        harga = self.root.ids.screen_manager.get_screen("gk_jemur").ids.biaya_gk_jemur.text
        tanggal = self.root.ids.screen_manager.get_screen("gk_jemur").ids.date_picker_label.text
        result = m_produksi.getGabahKering(id_cherry)
        m_produksi.inputGabahKeringJemur(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("gk_jemur").ids.berat_gk_jemur.text = ""
        self.root.ids.screen_manager.get_screen("gk_jemur").ids.biaya_gk_jemur.text = ""
        self.root.ids.screen_manager.get_screen("gk_jemur").ids.date_picker_label.text = ""
        
    def suton(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("green_suton").ids.berat_green_suton.text
        harga = self.root.ids.screen_manager.get_screen("green_suton").ids.biaya_green_suton.text
        tanggal = self.root.ids.screen_manager.get_screen("green_suton").ids.date_picker_label.text
        result = m_produksi.getGabahKering(id_cherry)
        m_produksi.inputSuton(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("green_suton").ids.berat_green_suton.text = ""
        self.root.ids.screen_manager.get_screen("green_suton").ids.biaya_green_suton.text = ""
        self.root.ids.screen_manager.get_screen("green_suton").ids.date_picker_label.text = ""
        
    def grading(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("green_grading").ids.berat_green_grading.text
        harga = self.root.ids.screen_manager.get_screen("green_grading").ids.biaya_green_grading.text
        tanggal = self.root.ids.screen_manager.get_screen("green_grading").ids.date_picker_label.text
        result = m_produksi.getGabahKering(id_cherry)
        m_produksi.inputGrading(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("green_grading").ids.berat_green_grading.text = ""
        self.root.ids.screen_manager.get_screen("green_grading").ids.biaya_green_grading.text = ""
        self.root.ids.screen_manager.get_screen("green_grading").ids.date_picker_label.text = ""
        
    def color(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        berat = self.root.ids.screen_manager.get_screen("green_color").ids.berat_green_color.text
        harga = self.root.ids.screen_manager.get_screen("green_color").ids.biaya_green_color.text
        tanggal = self.root.ids.screen_manager.get_screen("green_color").ids.date_picker_label.text
        result = m_produksi.getGabahKering(id_cherry)
        m_produksi.inputColor(result[0],berat,harga,tanggal,id_panen)
        self.root.ids.screen_manager.get_screen("green_color").ids.berat_green_color.text = ""
        self.root.ids.screen_manager.get_screen("green_color").ids.biaya_green_color.text = ""
        self.root.ids.screen_manager.get_screen("green_color").ids.date_picker_label.text = ""
        
    def handPick(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        status = data_cherry[2]
        self.root.ids.screen_manager.get_screen("green_hand_pick").ids.berat_green_hand_pick.text = ""
        self.root.ids.screen_manager.get_screen("green_hand_pick").ids.biaya_green_hand_pick.text = ""
        self.root.ids.screen_manager.get_screen("green_hand_pick").ids.date_picker_label.text = ""
        id_gabahK = m_produksi.getGabahKering(id_cherry)[0]
        m_produksi.inputHandPick(id_gabahK,self.berat,self.harga,self.tanggal,id_panen)
        id_gabahB = m_produksi.getGabahBasah(id_cherry)[0]
        #id_bean = m_produksi.getGreenBean(id_cherry)[0]
        berat = self.root.ids.screen_manager.get_screen("green_hand_pick").ids.berat_green_hand_pick.text
        harga = self.root.ids.screen_manager.get_screen("green_hand_pick").ids.biaya_green_hand_pick.text
        tanggal = self.root.ids.screen_manager.get_screen("green_hand_pick").ids.date_picker_label.text
        subprocess = ["Panen","Cherry Wet Mill","Gabah Basah Transport","Gabah Basah Bongkar","Gabah Basah Jemur","Gabah Kering Hull","Gabah Kering Jemur","Green Bean Suton","Green Bean Grading","Green Bean Sorter","Green Bean Hand Pick"]
        beratSubProcess = []
        beratSubProcess.append(data_cherry[3])
        beratSubProcess.append(m_produksi.getDataWetMill(id_cherry)[0])
        beratSubProcess.append(m_produksi.getDataTransport(id_cherry)[0])
        beratSubProcess.append(m_produksi.getDataBongkar(id_cherry)[0])
        beratSubProcess.append(m_produksi.getDataGabahBasahJemur(id_cherry)[0])
        beratSubProcess.append(m_produksi.getDataGabahKeringHull(id_gabahB)[0])
        if self.tipe_proses != "Wet Hull" or self.tipe_proses != "Natural Wet Hull" or self.tipe_proses != "Honey Wet Hull":
            beratSubProcess.append(m_produksi.getDataGabahKeringJemur(id_gabahB)[0])
        else:
            del subprocess[6]
        beratSubProcess.append(m_produksi.getDataGreenBeanSuton(id_gabahK)[0])
        beratSubProcess.append(m_produksi.getDataGreenBeanGrading(id_gabahK)[0])
        beratSubProcess.append(m_produksi.getDataGreenBeanSorter(id_gabahK)[0])
        beratSubProcess.append(m_produksi.getDataGreenBeanHandPick(id_gabahK)[0])
        
        
        print("FINAL")
        self.root.ids.screen_manager.current = "hasilakhir"
        plt.plot((subprocess),(beratSubProcess)) # ((Subproses),(Berat)) 
        plt.title("Berat Per Subproses", fontsize=10)
        plt.yticks(fontsize=7)
        plt.xticks(fontsize=6)
        # plt.xticks(rotation=90, fontsize=6)
        # plt.tight_layout()
        # box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.root.ids.screen_manager.get_screen("hasilakhir").ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    def getAllSubProcess(self):
        data_cherry = m_panen.getPanen(self.tanggal,self.blok,self.varietas,self.tipe_proses)
        id_cherry = data_cherry[0]
        id_panen = data_cherry[1]
        id_gabahB = m_produksi.getGabahBasah(id_cherry)[0]
        id_gabahK = m_produksi.getGabahKering(id_cherry)[0]
        id_bean = m_produksi.getGreenBean(id_cherry)[0]
       
    
        
if __name__ == "__main__":
    Main().run()