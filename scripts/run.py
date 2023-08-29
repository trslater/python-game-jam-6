import os
import sys

from pyjam import cli


def main():
    # Make sure data relative paths work correctly
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)
    
    cli.run()

if __name__ == "__main__":
    main()
