from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from logIn.LogInSystem import Deleting_Auto_SignIn_System


class ItemDrawer(OneLineIconListItem):
    pass


class ContentNavigationDrawer(BoxLayout):
    avatar = ObjectProperty(None);
    username = ObjectProperty(None);
    email = ObjectProperty(None);

    def Deleting_Temporary_Database(self):
        Deleting_Auto_SignIn_System()
        self.marketPageDemo.fourthScreen.mainScreen.logInDemo.Hiding_Password_LogInDemo()
        self.marketPageDemo.fourthScreen.manager.current = "main"


'''class DrawerList(ThemableBehavior, MDList):

    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.rimary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color'''


class MarketPageDemo(Screen):
    pass
