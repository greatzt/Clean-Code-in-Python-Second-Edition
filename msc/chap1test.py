from __future__ import annotations
from typing import Iterable


def broadcast_notification(
    message: str,
    relevant_user_emails: Iterable[str]
) -> None:
    for email in relevant_user_emails:
        print("Sending %r to %r", message, email)


broadcast_notification("welcome", "user1@domain.com")
