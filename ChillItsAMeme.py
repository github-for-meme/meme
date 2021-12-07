import webbrowser


class ChillItsAMeme:
    """
    Description
    ----------
        A class to demonstrate proper meme etiquette.

    Inputs
    ----------
        url : str
            The url from the meme
        msg : str
            The string from the meme needed to get to the correct url

    Static Parameters
    ----------
        decoded_url : str
            a full url to go see the Congratulation page from the meme
            will always decode based on meme_decoder function
        referenced_meme_url: str
            the url to the meme being referenced
            which happens to be the top post currently

    Static Methods
    ----------
        meme_decoder() -> str
            A function to get the full url to go see the Congratulation page from the meme
        go_to_decoded_url() -> None
            A function to open the congratulations page in your web browser
        go_to_original_meme() -> None
            A function to open the original meme in your web browser
    """

    def __init__(self, url: str, msg: str) -> None:
        self.url: str = url
        self.msg: str = msg
        self.decoded_url: str = self.meme_decoder()
        self.referenced_meme_url: str = "https://www.reddit.com/r/ProgrammerHumor/comments/ratv6p" \
                                        "/in_a_train_in_stockholm_sweden/?utm_source=share&utm_medium=web2x&context=3"

    def meme_decoder(self) -> str:
        """
        Description
        ----------
            A function to get the full url to go see the Congratulation page from the meme

        Parameters
        ----------
            self : represents the instance of the class
                self is always pointing to Current Object.
        
        Returns
        -------
            decoded_url : str
                a full url to go see the Congratulation page from the meme
        """
        # string to append to the end of the base url
        url_end: str = ''
        # conversion to a list of integers
        msg_l: list[int] = [int(i) for i in self.msg]
        # start at 1 because the first iteration 0-1 would give the last index and that is not the behavior we want
        for i in range(1, len(msg_l)):
            # if numbers from message string are both even or odd in the current iteration
            if msg_l[i] % 2 == msg_l[i - 1] % 2:
                # find the maximum of those two numbers
                i_max: int = max(msg_l[i], msg_l[i - 1])
                # build the url
                url_end += str(i_max)

        decoded_url: str = f"https://{self.url}/{url_end}/"  # properly format the url to return
        return decoded_url

    def go_to_decoded_url(self) -> None:
        """
        Description
        ----------
            A function to open the congratulations page in your web browser

        Parameters
        ----------
            self : represents the instance of the class
                self is always pointing to Current Object.
        """
        webbrowser.open(self.decoded_url)

    def go_to_original_meme(self) -> None:
        """
        Description
        ----------
            A function to open the original meme in your web browser

        Parameters
        ----------
            self : represents the instance of the class
                self is always pointing to Current Object.
        """
        webbrowser.open(self.referenced_meme_url)


if __name__ == '__main__':
    meme = ChillItsAMeme(url="www.multisoft.se", msg="1112031584")
    print("decoded_url: ", meme.decoded_url)
