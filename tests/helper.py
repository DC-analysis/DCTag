import pathlib
import shutil
import tempfile

from dctag.gui.main import DCTag

import pytest
from PyQt5 import QtCore, QtWidgets

data_path = pathlib.Path(__file__).parent / "data"


def get_clean_data_path():
    """Return .rtdc file in a temp dir for modification"""
    tdir = tempfile.mkdtemp(prefix="dctag_data_")
    orig = data_path / "blood_rbc_leukocytes.rtdc"
    new = pathlib.Path(tdir) / orig.name
    shutil.copy2(orig, new)
    return new


@pytest.fixture
def mw(qtbot):
    # Always set server correctly, because there is a test that
    # makes sure DCOR-Aid starts with a wrong server.
    QtWidgets.QApplication.processEvents(
        QtCore.QEventLoop.ProcessEventsFlag.AllEvents, 200)
    # Code that will run before your test
    mw = DCTag()
    qtbot.addWidget(mw)
    QtWidgets.QApplication.setActiveWindow(mw)
    QtWidgets.QApplication.processEvents(
        QtCore.QEventLoop.ProcessEventsFlag.AllEvents, 200)
    # Run test
    yield mw
    # Make sure that all daemons are gone
    mw.close()
    # It is extremely weird, but this seems to be important to avoid segfaults!
    QtWidgets.QApplication.processEvents(
        QtCore.QEventLoop.ProcessEventsFlag.AllEvents, 200)
