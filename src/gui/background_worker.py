from gi.overrides import GObject
from threading import Thread

class BackgroundWorker(Thread):
    """Helps synchronizing background activities with the GUI thread"""

    def __init__(self, work_delegate, finished_cb, progress_cb):
        """
            work_delegate(worker): The function to execute on a background thread.
                                   Its only parameter is the current BackgroundWorker instance.
            finished_cb(result): A callback fired after the work finished. 
                                 Gets the work_delegate's result as parameter.
            progress_cb(status): A callback defining the way of graphical progress reporting.
                                 Gets a status object as parameter.
                                 Can be fired manually via the report(status) method.
        """
        super(BackgroundWorker, self).__init__()
        self._work = work_delegate
        self._finished = finished_cb
        self._progress = progress_cb
        
    
    #TODO: Ezt nem lehetne normális delegálással öröklés helyett?? Hogy relytsük el?
    def run(self):
        result = self._work(self)
        GObject.idle_add(self._finished, result)

    #def start(self):
    #    self._thread = Thread()

    def report(self, status):
        GObject.idle_add(self._progress, status)

