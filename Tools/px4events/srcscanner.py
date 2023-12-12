import os
import re
import codecs
import sys

class SourceScanner(object):
    """
    Traverses directory tree, reads all source files, and passes their contents
    to the Parser.
    """

    def ScanDir(self, srcdirs, parser):
        """
        Scans provided path and passes all found contents to the parser using
        parser.Parse method.
        """
        extensions = (".cpp", )
        for srcdir in srcdirs:
            if os.path.isfile(srcdir):
                if not self.ScanFile(srcdir, parser):
                    return False
            else:
                for dirname, dirnames, filenames in os.walk(srcdir):
                    for filename in filenames:
                        if filename.endswith(extensions):
                            path = os.path.join(dirname, filename)
                            try:
                                if not self.ScanFile(path, parser):
                                    return False
                            except:
                                print(f"Exception in file {path}")
                                raise
        return True

    def ScanFile(self, path, parser):
        """
        Scans provided file and passes its contents to the parser using
        parser.Parse method.
        """

        with codecs.open(path, 'r', 'utf-8') as f:
            try:
                contents = f.read()
            except:
                contents = ''
                print(f'Failed reading file: {path}, skipping content.')
        try:
            return parser.Parse(contents, path)
        except Exception as e:
            print(f"Exception while parsing file {path}")
            raise
