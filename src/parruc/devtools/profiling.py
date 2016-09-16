# -*- coding: utf-8 -*-
from time import time

import functools
import logging


logger = logging.getLogger(__name__)


# http://stackoverflow.com/questions/3931627/how-to-build-a-python-decorator-with-optional-parameters
def profiled(*args, **kwargs):
    def _profiled(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            func_name = f.__name__
            func_full_name = '%s.%s' % (f.__module__, func_name)
            start = time()
            try:
                return f(*args, **kwargs)
            finally:
                elapsed = int((time() - start) * 1000.0)
                if elapsed > threshold:
                    logger.info('func=%s elapsed=%sms threshold=%sms',
                                func_full_name, elapsed, threshold)
        return wrapper
    if 'threshold' not in kwargs and callable(args[0]):
        # No arguments, this is the decorator
        # Set default values for the arguments
        threshold = -1
        return _profiled(args[0])
    else:
        # This is just returning the decorator
        threshold = kwargs['threshold']
        return _profiled
