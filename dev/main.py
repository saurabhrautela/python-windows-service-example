"""
Demonstrate the way to create windows service using python.

Steps to run without virtual environment:
1. Install pywin: ``pip install pywin32``
2. Install service: ``python main.py install``
3. Update service after changes: ``python main.py update``
4. Debug service: ``python main.py debug``
5. Run service: ``python main.py remove``

Dependencies:
1. python = "^3.7"
2. pywin32 = "^227"
"""
import sys
import socket
from datetime import datetime

import servicemanager
import win32event
import win32service
import win32serviceutil


class TestService(win32serviceutil.ServiceFramework):
    """Windows service to log its state in a file."""

    _svc_name_ = "TestService"
    _svc_display_name_ = "TestService"
    _svc_description_ = "Logs its own state."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(  # pylint: disable=invalid-name
            None, 0, 0, None
        )
        self.timeout_ms = 5000
        self.log_file_path = "C:\\TestService.log"
        socket.setdefaulttimeout(60)

    def SvcStop(self):  # pylint: disable=invalid-name
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):  # pylint: disable=invalid-name
        rc = None

        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )

        self.log("started")

        while rc != win32event.WAIT_OBJECT_0:
            self.log("running")

            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout_ms)

        self.log("stopped")

    def log(self, state):
        """Logs messages to specify the service is in at a time."""
        message = f"TestService {state} at {datetime.now()}"

        servicemanager.LogInfoMsg(message)

        with open(self.log_file_path, "a") as file:
            file.write(message + "\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TestService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TestService)
