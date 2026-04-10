# @title: Explain Log
# @description: Explains error messages and log entries in plain language.
# @author: Scryptian

import bridge


def run(text):
    """
    text: log or error message from clipboard
    """
    prompt = (
        "Explain the following error or log message in plain language. "
        "What happened, why, and how to fix it:\n\n"
        f"{text}"
    )
    return bridge.generate(prompt)
