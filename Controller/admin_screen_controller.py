import View
import View.AdminScreen
import View.AdminScreen.admin_screen


class AdminScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.AdminScreen.admin_screen.AdminScreenView(
            controller=self, model=self.model
        )

    def get_view(self):
        return self.view
