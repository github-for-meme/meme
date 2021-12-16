from typing import Any


class MsgTypeError(Exception):
    """
    Description
    ----------
        Someone might enter the message in as something other than a string of integers

    Inputs
    ----------
        msg : not a str
            The input that should be a string from the meme needed to get to the correct url

    Static Parameters
    ----------
        message : str
            The string error message this Except will display
    """
    def __init__(self, msg: Any):
        self.msg = str(msg)
        self.message = f"""
        Meme msg variable must be a string of numbers. Please fix this variable
        Current msg input is {self.msg}.
        Current msg input type is {type(msg)}.
        """
        super().__init__(self.message)
