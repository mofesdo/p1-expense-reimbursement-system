import datetime


def log_regular(aString):
    f = open("project1log.txt", "a")
    f.write(str("R: " + datetime.datetime.now().__str__())+" "+aString+"\n")
    f.close()


def log_warning(aString):
    f = open("project1log.txt", "a")
    f.write(str("W: " + datetime.datetime.now().__str__())+" "+aString+"\n")
    f.close()


def log_error(aString):
    f = open("project1log.txt", "a")
    f.write(str("E: " + datetime.datetime.now().__str__())+" "+aString+"\n")
    f.close()

