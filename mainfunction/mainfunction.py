#!/usr/bin/env python

import inspect
import warnings

def mainfunction(fn):
    mainfunction._last_registered = getattr(mainfunction, '_last_registered', [])
    
    module = inspect.getmodule(fn)
    if module.__name__ == '__main__':
        try:
            lineno = fn.func_code.co_firstlineno # should always exist
            source_id = "%s:%s" % (fn.__name__, lineno)
        except:
            # but don't fail if lineno isn't there
            source_id = fn.__name__

        if mainfunction._last_registered:
            toissue = list(mainfunction._last_registered)
            toissue.append(source_id)
            fname = getattr(module, '__file__', '__main__') #cli doesn't have __file__
            warnings.warn("Multiple main functions defined in %s: %s" % (fname, toissue), stacklevel=2)
        mainfunction._last_registered.append(source_id)

        fn()
    return fn
