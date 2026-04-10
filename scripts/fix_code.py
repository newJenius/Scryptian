# @title: Fix Code
# @description: Automatically repairs syntax and logical errors in code snippets.
# @author: Scryptian

import bridge


def run(text):
    """
    text: code from clipboard, passed by main.py
    """
    prompt = (
        "Fix the following code. Provide only the corrected version, "
        "no explanations:\n\n"
        f"{text}"
    )
    return bridge.generate(prompt)
