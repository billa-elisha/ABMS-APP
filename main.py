from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from Model.database import DataBase
import os
import View.screens


class MyApp(MDApp):
    KV_DIRS = [os.path.join(os.getcwd(), "View")]
    DEBUG = 1

    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)

    def build_app(self):
        self.screen_manager = MDScreenManager()
        screens = View.screens.screens
        self.database = DataBase().get_database_connection()

        for i, screen_name in enumerate(screens.keys()):
            model = screens[screen_name]["model"](self.database)
            controller = screens[screen_name]["controller"](model)
            view = controller.get_view()
            view.manager_screen = self.screen_manager
            view.name = screen_name
            self.screen_manager.add_widget(view)
        # return MDScreenManager()
        print(self.screen_manager.screens)
        return self.screen_manager


MyApp().run()
