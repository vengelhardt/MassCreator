import typing

# PySide2 import
from PySide2.QtWidgets import QWidget

import src.main.python.config.version as version
from src.main.python.views.ui.Ui_MainWindow import Ui_MainWindow

if typing.TYPE_CHECKING:
    from src.main.python.main import AppContext


class MainWindow(QWidget):
    """Class MainWindow intialisation of main view with menu and content"""

    def __init__(self, appctxt: "AppContext"):
        super(MainWindow, self).__init__()
        self.appctxt = appctxt
        self.setupUi()

    def setupUi(self) -> None:
        """Load Ui component and signal"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.version.setText(version.VERSION)
        self.setWindowTitle("MassCreator")
        self.connect_signal_main_ui()

    def delete_ui(self, widget: QWidget, ui_name: str) -> None:
        """Delete ui and attribut"""
        widget.deleteLater()
        delattr(self, ui_name)

    def test_push_button_test(self) -> None:
        self.ui.textEdit.setText("ON EST DES CRACK")

    # Connect signal/slot
    def connect_signal_main_ui(self) -> None:
        self.ui.pushButtonTest.clicked.connect(self.test_push_button_test)
