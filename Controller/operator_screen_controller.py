import View
import View.OperatorScreen
import View.OperatorScreen.operator_screen


class OperatorScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.OperatorScreen.operator_screen.OperatorScreenView(
            controller=self, model=self.model
        )

    def get_view(self):
        return self.view
