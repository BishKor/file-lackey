from datetime import datetime as dt


class BossFile:
    def __init__(self, filename, mode, script, purpose):
        self.filename = filename
        self.script = script
        self.f = open(filename, mode)
        self.purpose = purpose

    def lwrite(self, string):
        self.f.write(string)

    def lclose(self):
        self.f.close()
        lackey = open(self.filename + ".lackey", 'w')
        date = dt.now()
        lackey.write(self.filename + '\n')
        lackey.write('Generation Date: ' + str(date.month) + '/' + str(date.day) + '/' + str(date.year) + ' at ' +
                     str(date.hour) + ':' + str(date.minute) + '\n')
        lackey.write('Generator Module: ' + self.script + '\n')
        lackey.write('File Purpose: ' + self.purpose)
