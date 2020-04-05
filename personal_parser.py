import argparse
import sys


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

    # the default status on the parent class is 0, we're
    # changing it to be 1 here ...
    def exit(self, status=1, message=None):
        if message:
            self._print_message(message, sys.stderr)
        self.problem = True
        return

    def parse_args(self, args=None, namespace=None):
        if self.parse_known_args(args, namespace) is None:
            return
        else:
            return super().parse_args(args, namespace)
