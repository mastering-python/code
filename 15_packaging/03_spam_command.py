import setuptools


class SpamCommand(setuptools.Command):
    description = 'Make some spam!'
    # Specify the commandline arguments for this command here. This parameter
    # uses the getopt module for parsing'
    user_options = [
        ('spam=', 's', 'Set the amount of spams'),
    ]

    def initialize_options(self):
        # This method can be used to set default values for the options.
        # These defaults can be overridden by command-line, configuration files
        # and the setup script itself.
        self.spam = 3

    def finalize_options(self):
        # This method allows you to override the values for the options, useful
        # for automatically disabling incompatible options and for validation.
        self.spam = max(0, int(self.spam))

    def run(self):
        # The actual running of the command.
        print('spam' * self.spam)
