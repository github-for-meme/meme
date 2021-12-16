class UrlTypeError(Exception):
    """
    Description
    ----------
        Someone might enter the url in a different way

    Inputs
    ----------
        url : str
            The url from the meme.

    Static Parameters
    ----------
        message : str
            The string error message this Exception will display
    """

    def __init__(self, url):
        self.message = f"""
         Meme url variable must start with 'www.' and end with '.se'.
         Please fix this variable
         Current url input is {url}.
         Correct format example 'www.multisoft.se'
         """
        self.url = url
        super().__init__(self.message)
