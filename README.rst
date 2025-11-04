DCTag
=====

|PyPI Version| |Build Status| |Coverage Status|

**DCTag** is a graphical toolkit for manually annotating RT-DC events
for machine-learning purposes.


Installing DCTag
----------------
This section is only for users. If you are a developer and want to contribute to DCTag, you have
to clone the repository and install in editable mode (see further below).

There are no graphical installers. You must install Python 3.10 or later and
install DCTag via pip::

    pip install dctag

To **upgrade** to a new version, use the ``--upgrade`` argument::

    pip install --upgrade dctag

Running DCTag
-------------
If installed properly, a simple ``dctag`` should work. Otherwise (make sure
the virtual environment is active)::

    python -m dctag


For Developers
--------------
Here is how to work on contributions:

1. Fork this repository, create your virtual environment and install in editable mode via
   ``pip install -e .`` in the repository root.
2. Create an issue or open the issue that you want to address.
3. Assign yourself to that issue so nobody else is working on it.
4. Verify that nobody else is currently working an an issue that might
   interfere with your issue (e.g. editing same part of a file)
5. Activate your virtual environment and install dctag in editable mode::

      pip install -e .

7. Create a new branch that starts with your issue number and short description::

      git branch 15-keyboard-control
      git checkout 15-keyboard-control

8. Make your changes and commit::

      git commit -a -m "feat: introduced keyboard control"
      # for the first push
      git push --set-upstream origin 15-keyboard-control
      # for consecutive changes
      git commit -a -m "fix: layout reversed"
      git push

9. After making your changes, create your pull request.

Testing
-------
To run all tests, install the requirements and run pytest::

    pip install -r tests/requirements.txt
    pytest tests

.. |PyPI Version| image:: https://img.shields.io/pypi/v/DCTag.svg
   :target: https://pypi.python.org/pypi/DCTag
.. |Build Status| image:: https://img.shields.io/github/actions/workflow/status/DC-analysis/DCTag/check.yml?branch=main
   :target: https://github.com/DC-analysis/DCTag/actions?query=workflow%3AChecks
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/DC-analysis/DCTag/main.svg
   :target: https://codecov.io/gh/DC-analysis/DCTag
