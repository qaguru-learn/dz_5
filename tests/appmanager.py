from tests.pages.left_panel import LeftPanel


class ApplicationManager:
    def __init__(self):
        self.left_panel = LeftPanel()


app = ApplicationManager()
