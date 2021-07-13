from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.button import MDIconButton

class UserDetail(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.orientation = "horizontal"

        self.ToolIcon = MDIconButton()
        self.ToolIcon.icon = "images/user.png"
        self.ToolIcon.pos_hint = {"center_x": .05, "center_y": .5}
        self.ToolIcon.user_font_size = 40
        self.size_hint_y = 0.3
        self.ToolIcon.radius = [36, 36, 0, 0, ]

        self.UsrAreaDescrLayout = MDBoxLayout()
        self.UsrAreaDescrLayout.orientation = "vertical"
        self.UsrAreaDescrLayout.add_widget(MDLabel(text="User1", halign="left"))
        self.UsrAreaDescrLayout.add_widget(MDLabel(text="xxxxxx-x-x-x-xxx-x", halign="left"))
        self.UsrAreaDescrLayout.add_widget(MDLabel(text="YyYYYYY-YYYYY0YYYY", halign="left"))

        self.add_widget(self.ToolIcon)
        self.add_widget(self.UsrAreaDescrLayout)

class MenuList(MDList):
    def __init__(self, **kwargs):
        super().__init__()
        self.size_hint_y = 3.5
        self.home_link = TwoLineAvatarListItem()
        self.home_link.text="Dashbord"
        self.home_link.secondary_text="your home page"
        self.home_link.add_widget(ImageLeftWidget(source="images/home.png"))
        self.add_widget(self.home_link)

        self.report_link = TwoLineAvatarListItem()
        self.report_link.text = "Report"
        self.report_link.secondary_text = "Analyze your data by report."
        self.report_link.add_widget(ImageLeftWidget(source="images/home.png"))
        self.add_widget(self.report_link)

        self.masterlink = TwoLineAvatarListItem()
        self.masterlink.text = "Master"
        self.masterlink.secondary_text = "Add Edit your Master Record."
        self.masterlink.add_widget(ImageLeftWidget(source="images/home.png"))
        self.add_widget(self.masterlink)

        self.report1_link = TwoLineAvatarListItem()
        self.report1_link.text = "Report1"
        self.report1_link.secondary_text = "Analyze your data by report."
        self.report1_link.add_widget(ImageLeftWidget(source="images/home.png"))
        self.add_widget(self.report1_link)

        self.report2_link = TwoLineAvatarListItem()
        self.report2_link.text = "Report2"
        self.report2_link.secondary_text = "Analyze your data by report."
        self.report2_link.add_widget(ImageLeftWidget(source="images/home.png"))
        self.add_widget(self.report2_link)



class NavMenu(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__()
        self.orientation = "vertical"
        self.size_hint_X=None
        self.padding = "8dp"
        self.spacing ="8dp"
        self.add_widget(UserDetail())
        self.add_widget(MenuList())