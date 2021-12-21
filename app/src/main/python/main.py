import sys

from fbs_runtime.application_context import cached_property
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QApplication

import src.main.python.config.colors as b_color
from src.main.python.views.MainWindow import MainWindow


class App(QApplication):
    """Main application MVC instantiations"""

    def __init__(self, appctxt: ApplicationContext, sys_argv: list) -> None:
        super(App, self).__init__(sys_argv)

        print("|================================|")
        print(f"|          {b_color.BOLD}MassCreator{b_color.END}           |")
        print("|================================|")

        self.main_view = MainWindow(appctxt)
        self.main_view.showMaximized()


class AppContext(ApplicationContext):
    """Application context to build on all os and give resource managment (fbs structure)"""

    @cached_property
    def app(self) -> App:
        return App(self, sys.argv)


if __name__ == "__main__":
    # Launch application
    appctxt = AppContext()
    sys.exit(appctxt.app.exec_())
