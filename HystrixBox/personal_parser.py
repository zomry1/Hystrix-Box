import argparse
import sys

# Create parserException
class ParserException(Exception):
    pass

# Override ArgumentParser to raise an ParseException instead of exiting
class MyParser(argparse.ArgumentParser):
    def __init__(self,
                 prog=None,
                 usage=None,
                 description=None,
                 epilog=None,
                 parents=[],
                 formatter_class=argparse.HelpFormatter,
                 prefix_chars='-',
                 fromfile_prefix_chars=None,
                 argument_default=None,
                 conflict_handler='error',
                 add_help=True,
                 allow_abbrev=True):
        super().__init__(prog, usage, description, epilog, parents, formatter_class, prefix_chars,
                         fromfile_prefix_chars,
                         argument_default, conflict_handler, add_help, allow_abbrev)
        self.problem = False

    # Change exit call default to raise an ParseException instead of exiting
    def exit(self, status=1, message=None):
        if message:
            self._print_message(message, sys.stderr)
        self.problem = True
        raise ParserException
        return

