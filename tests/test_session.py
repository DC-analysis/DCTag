from dctag import session

from helper import get_clean_data_path


def test_basic():
    path = get_clean_data_path()
    with session.DCTagSession(path, "Peter") as dts:
        assert dts.event_count == 18
        lock_path = dts.path_lock
        assert lock_path.exists()
    assert not lock_path.exists()
