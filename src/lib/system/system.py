from os import  get_terminal_size, name, system

def clear() -> None:

    """Clears screen for most operating systems: Windows, Linux & Mac (Posix) """
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

def terminal_width() -> int:

    return get_terminal_size()[0]