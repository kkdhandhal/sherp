from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.utils.fitimage import FitImage
from kivymd.uix.button import MDIconButton

class NavMenu(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__()
        self.orientation = "vertical"
        self.padding = "8dp"
        self.spacing ="8dp"

        self.ToolIcon = MDIconButton()
        self.ToolIcon.icon = "images/user.png"
        self.ToolIcon.pos_hint = {"center_x": .05, "center_y": .5}
        self.ToolIcon.user_font_size = "64sp"
        self.ToolIcon.radius = [36, 36, 0, 0, ]

        self.UsrAreaLayout= MDBoxLayout()
        self.UsrAreaLayout.orientation = "horizontal"
        self.UsrAreaLayout.size_hint_y = 0.1

        self.UsrAreaDescrLayout = MDBoxLayout()
        self.UsrAreaDescrLayout.orientation ="vertical"
        self.UsrAreaDescrLayout.add_widget(MDLabel(text="User1", halign="left"))
        self.UsrAreaDescrLayout.add_widget(MDLabel(text="xxxxxx-x-x-x-xxx-x", halign="left"))
        self.UsrAreaDescrLayout.add_widget(MDLabel(text="YyYYYYY-YYYYY0YYYY", halign="left"))

        self.UsrAreaLayout.add_widget(self.ToolIcon)
        self.UsrAreaLayout.add_widget(self.UsrAreaDescrLayout)

        self.add_widget(self.UsrAreaLayout)
        self.add_widget(MDLabel(text="Menu list", halign="center"))