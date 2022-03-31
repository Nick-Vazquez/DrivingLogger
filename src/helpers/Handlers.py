"""
Contains default handlers that can be used to control direct logging output.

:author: Nick Vazquez (nmv)
:created: 2022/03/07
"""
import logging


class QueueHandler(logging.Handler):
    """Send logging records to a queue.
    It can be used from different threads
    """

    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        """
        Adds a log to the QueueHandler's queue. Objects that are monitoring
        this queue can then ready off and process queue items accordingly.

        :param record: Object to add to the queue.
        """
        self.log_queue.put(record)
