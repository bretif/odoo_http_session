# -*- coding: utf-8 -*-
import logging

from openerp import http

def session_gc(session_store):
    """
    Global cleaning of sessions using either the standard way (delete session files),
    Or the DB way.
    """
    pass

# Monkey patch of standard methods
_logger.debug("Monkey patching sessions")
http.session_gc = session_gc
