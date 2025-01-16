from View.base_screen import BaseScreen


class LoginScreenView(BaseScreen):
    """
    The login screen of the app
    attr:
        1. self.model: Model.login_model.LoginScreenModel
            (to help you intereact with the database)
        2. self.controller : Controller.login_controller.LoginScreenController
            (where the logic of the login screen is found)
    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def clickme(self):
        self.controller.me()
