def javascript(content: str) -> None:

    """This is the Javascript/Nodejs language worker."""

    if content.contains(".listen("):

        print(f"${Fore.GREEN}[X] CHANCE OF SERVER BEING RUNNED ON A PORT!")

    if content.contains("process.env."):

        print(f"${Fore.GREEN}[X] CHANCE OF ENV (KEYS) BEING USED!")

def python(content: str) -> None:

    """This is the Python language worker."""

    pass