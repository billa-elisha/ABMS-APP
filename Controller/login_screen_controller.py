import View
import View.LoginScreen
import View.LoginScreen.login_screen


class LoginScreenContorller:
    def __init__(self, model):
        self.model = model
        self.view = View.LoginScreen.login_screen.LoginScreenView(
            controller=self, model=self.model
        )

    def get_view(self):
        return self.view

    def me(self):
        self.model.select_all_users()
        self.view.parent.current = "admin screen"
