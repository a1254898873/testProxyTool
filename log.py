import sys
import traceback
import datetime





def getnowtime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def success(content, *args):
    content = "%s - %s\n" % (getnowtime(), content)
    sys.stdout.write("\033[32m{}\033[0m".format(content))
    for arg in args:
        sys.stdout.write("%s\n" % arg)


def error(content, *args):
    content = "%s - %s\n" % (getnowtime(), content)
    sys.stdout.write("\033[31m{}\033[0m".format(content))
    for arg in args:
        sys.stdout.write("%s\n" % arg)

def info(content, *args):
    content = "%s - %s\n" % (getnowtime(), content)
    sys.stdout.write("\033[39m{}\033[0m".format(content))
    for arg in args:
        sys.stdout.write("%s\n" % arg)



def exception(content):
    sys.stdout.write("%s - %s\n" % (getnowtime(), content))
    traceback.print_exc(file=sys.stdout)



