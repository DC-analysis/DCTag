import pkg_resources

from PyQt5 import QtWidgets, uic


class TabBinaryLabel(QtWidgets.QWidget):
    """Tab for doing binary classification"""
    def __init__(self, *args, **kwargs):
        super(TabBinaryLabel, self).__init__(*args, **kwargs)

        ui_file = pkg_resources.resource_filename(
            'dctag.gui', 'tab_binary.ui')
        uic.loadUi(ui_file, self)

    def update_session(self, session):
        """Update this widget with the session info"""
