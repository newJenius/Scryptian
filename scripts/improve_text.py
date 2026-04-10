# @title: Improve Text
# @description: Rewrites text to sound more professional and polished.
# @author: Scryptian

import bridge


def prompt(text):
    return (
        "Rewrite the following text to make it more professional, clear, "
        "and polished. Provide only the improved version:\n\n"
        f"{text}"
    )


def run(text):
    """
    text: text from clipboard to improve
    """
    return bridge.generate(prompt(text))
