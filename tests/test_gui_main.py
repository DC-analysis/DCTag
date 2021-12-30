import io
import pathlib
from unittest import mock

import pytest
from PyQt5 import QtCore, QtWidgets

import dctag
from dctag.gui.main import DCTag
from dctag import session
from helper import get_clean_data_path


data_dir = pathlib.Path(__file__).parent / "data"


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    pass
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    # restore dctag-tester for other tests
    QtCore.QCoreApplication.setOrganizationName("MPL")
    QtCore.QCoreApplication.setOrganizationDomain("mpl.mpg.de")
    QtCore.QCoreApplication.setApplicationName("dctag")
    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.IniFormat)
    settings = QtCore.QSettings()
    settings.setValue("user/name", "dctag-tester")


def test_basic(qtbot):
    """Run the program and exit"""
    mw = DCTag()
    mw.close()


def test_clear_session(qtbot):
    """Clearing the session should not cause any trouble"""
    path = get_clean_data_path()
    mw = DCTag()
    QtWidgets.QApplication.setActiveWindow(mw)
    # claim session
    with session.DCTagSession(path, "dctag-tester"):
        pass
    # open session
    mw.on_action_open(path)
    # go through the tabs
    mw.tabWidget.setCurrentIndex(1)
    mw.tabWidget.setCurrentIndex(2)

    # Now clear the session
    mw.on_action_close()
    assert not mw.session
    # go through the tabs
    mw.tabWidget.setCurrentIndex(1)
    assert not mw.tab_binary.session
    assert not mw.tab_binary.widget_vis.session
    mw.tabWidget.setCurrentIndex(2)


def test_init_get_username(qtbot):
    # first reset the username
    # (undo what was done in conftest.py)
    QtCore.QCoreApplication.setOrganizationName("MPL")
    QtCore.QCoreApplication.setOrganizationDomain("mpl.mpg.de")
    QtCore.QCoreApplication.setApplicationName("dctag")
    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.IniFormat)
    settings = QtCore.QSettings()
    settings.remove("user/name")

    with mock.patch.object(QtWidgets.QInputDialog, "getText",
                           return_value=("peter", True)):
        DCTag()

    assert settings.value("user/name") == "peter"


def test_init_get_username_abort(qtbot):
    # first reset the username
    # (undo what was done in conftest.py)
    QtCore.QCoreApplication.setOrganizationName("MPL")
    QtCore.QCoreApplication.setOrganizationDomain("mpl.mpg.de")
    QtCore.QCoreApplication.setApplicationName("dctag")
    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.IniFormat)
    settings = QtCore.QSettings()
    settings.remove("user/name")

    with mock.patch.object(QtWidgets.QInputDialog, "getText",
                           return_value=("hans", False)):
        with pytest.raises(SystemExit):
            DCTag()

    assert settings.value("user/name") is None


def test_init_print_version(qtbot):
    mock_stdout = io.StringIO()
    mock_exit = mock.Mock()

    with mock.patch("sys.argv", ["--version"]):
        with mock.patch("sys.exit", mock_exit):
            with mock.patch('sys.stdout', mock_stdout):
                mw = DCTag("--version")
                mw.close()

    assert mock_exit.call_args.args[0] == 0
    assert mock_stdout.getvalue().strip() == dctag.__version__
