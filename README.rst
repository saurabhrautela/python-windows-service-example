======================
Python Windows Service
======================

Sample application to demonstrate how to create a Windows service using Python.

Setup
=====

* Install dependencies: ``poetry install``
* Activate virtual environment: ``poetry shell``
* Install service: ``python dev\main.py install``

::

    D:\python_windows_service_sample>python dev\main.py install
    Installing service TestService
    Changing service configuration
    Service updated

* Start service in debug mode: ``python dev\main.py debug`` (press Ctrl+C to stop)

::

    D:\python_windows_service_sample>python dev\main.py debug
    Debugging service TestService - press Ctrl+C to stop.
    Info 0x40001002 - The TestService service has started.
    Info 0x400000FF - TestService started at 2020-02-26 15:56:44.405755
    Info 0x400000FF - TestService running at 2020-02-26 15:56:44.406697
    Info 0x400000FF - TestService running at 2020-02-26 15:56:49.410124
    Info 0x400000FF - TestService running at 2020-02-26 15:56:54.411487
    Stopping debug service.
    Info 0x400000FF - TestService stopped at 2020-02-26 15:56:55.753119

* Remove service: ``python dev\main.py remove``

::

    D:\python_windows_service_sample>python dev\main.py remove
    Removing service TestService
    Service removed

Generate executable using Pyinstaller
=====================================

* Generate executable: ``pyinstaller --onefile --hiddenimport win32timezone dev\main.py``

Run service using executable
----------------------------
* Install service: ``main.exe install``
* Start service: ``main.exe start``
* Stop service: ``main.exe stop``

::

    D:\python_windows_service_sample>cd dist

    D:\python_windows_service_sample\dist>main.exe install
    Installing service TestService
    Service installed

    D:\python_windows_service_sample\dist>main.exe start
    Starting service TestService

    D:\python_windows_service_sample\dist>main.exe stop
    Stopping service TestService

.. note::
    You can also start and stop `TestService` using `services.msc`.
