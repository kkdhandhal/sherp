from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivy.uix.image import Image


MenuDrawer = """
BoxLayout:
    orientation:"vertical"
    MDLabel:
        text:"User Detail"
        font_style:"Subtitle1"
    
    MDLabel:
        text:"User Description"
        font_style:"Caption"    
        
"""
# class UserDetail(MDBoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__()
#         self.orientation = "horizontal"
#         self.size_hint_y=0.33
#
#         self.lbl_uname = MDLabel()
#         self.lbl_uname.text = "UserNmae"
#         self.lbl_uname.halign = "left"
#         self.lbl_uname.font_style = "Subtitle2"
#
#         self.lbl_udecr1 = MDLabel()
#         self.lbl_udecr1.text = "User Description 1"
#         self.lbl_udecr1.halign = "left"
#         self.lbl_udecr1.font_style = "Caption"
#
#         self.lbl_udecr2 = MDLabel()
#         self.lbl_udecr2.text = "User Description 1"
#         self.lbl_udecr2.halign = "left"
#         self.lbl_udecr2.font_style = "Caption"
#
#
#         self.ToolIcon = Image()
#         self.ToolIcon.source= "images/user.png"
#         self.ToolIcon.size_hint= [1,1]
#         self.ToolIcon.md_bg_color = [1, 0.7, 0.4, 0.5]
#
#         #self.ToolIcon.pos_hint = {"center_x": .05, "center_y": .5}
#         #self.ToolIcon.user_font_size = 36
#
#         #self.size_hint_x =None
#         #self.ToolIcon.radius = [36, 36, 0, 0, ]
#
#
#         self.UsrAreaDescrLayout = MDBoxLayout()
#         self.UsrAreaDescrLayout.orientation = "vertical"
#         #self.UsrAreaDescrLayout.md_bg_color = [0.9, 0.7, 0.2, 0.5]
#         #self.UsrAreaDescrLayout.size_hint_x=2.5
#         self.UsrAreaDescrLayout.size_hint = [2.5, 1]
#         self.UsrAreaDescrLayout.add_widget(self.lbl_uname)
#         self.UsrAreaDescrLayout.add_widget(self.lbl_udecr1)
#         self.UsrAreaDescrLayout.add_widget(self.lbl_udecr2)
#
#         self.add_widget(self.ToolIcon)
#         self.add_widget(self.UsrAreaDescrLayout)
#
#     def Click_userDetail(self):
#         print("Click On User Detail.")
#
#
# class MenuList(MDList):
#     def __init__(self, **kwargs):
#         super().__init__()
#
#         self.size_hint_y = 3.5
#         self.home_link = TwoLineAvatarListItem()
#         self.home_link.text="Dashbord"
#         self.home_link.secondary_text="your home page"
#         self.home_link.font_style="Subtitle2"
#         self.home_link.secondary_font_style ="Caption"
#         self.leftimgicon = ImageLeftWidget()
#         self.leftimgicon.icon = "android"
#         self.home_link.add_widget(self.leftimgicon)
#         self.add_widget(self.home_link)
#
#         self.report_link = TwoLineAvatarListItem()
#         self.report_link.text = "Report"
#         self.report_link.secondary_text = "Analyze your data by report."
#         self.report_link.add_widget(ImageLeftWidget(source="images/home.png"))
#         self.add_widget(self.report_link)
#
#         self.masterlink = TwoLineAvatarListItem()
#         self.masterlink.text = "Master"
#         self.masterlink.secondary_text = "Add Edit your Master Record."
#         self.masterlink.add_widget(ImageLeftWidget(source="images/home.png"))
#         self.add_widget(self.masterlink)
#
#         self.report1_link = TwoLineAvatarListItem()
#         self.report1_link.text = "Report1"
#         self.report1_link.secondary_text = "Analyze your data by report."
#         self.report1_link.add_widget(ImageLeftWidget(source="images/home.png"))
#         self.add_widget(self.report1_link)
#
#         self.report2_link = TwoLineAvatarListItem()
#         self.report2_link.text = "Report2"
#         self.report2_link.secondary_text = "Analyze your data by report."
#         self.report2_link.add_widget(ImageLeftWidget(source="images/home.png"))
#         self.add_widget(self.report2_link)


class NavMenu(MDBoxLayout):
   def __new__(cls, *args, **kwargs):
        return Builder.load_string(MenuDrawer)

    # def __init__(self,**kwargs):
    #     super().__init__()
    #     self.orientation = "vertical"
    #     self.size_hint_X=None
    #     #self.padding = "8dp"
    #     #self.spacing ="8dp"
    #     self.add_widget(UserDetail())
    #     self.add_widget(MenuList())