# @title: Explain Log
# @description: Explains error messages and log entries in plain language.
# @author: Scryptian

import bridge


def prompt(text):
    return (
        "Explain the following error or log message in plain language. "
        "What happened, why, and how to fix it:\n\n"
        f"{text}"
    )


def run(text):
    """
    text: log or error message from clipboard
    """
    return bridge.generate(prompt(text))
