#!/usr/bin/env python3
"""Session authentication class
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session id for a user_id
        Args:
            user_id: id to create session for
        Returns:
            enerated session id or None if user_id is None or not a string
        """
        if type(user_id) is not str or user_id is None:
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[str(session_id)] = user_id
        return str(session_id)
