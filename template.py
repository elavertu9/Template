import sys, os

def printUsage():
    print("\n\tusage: template <language> <file name> \n\tusage: template <file name>\n\tnote: file extension will be added for you\n")


def createJava(filename):
    className = filename[0].upper() + filename[1:].lower()
    filename = filename[0].upper() + filename[1:].lower() + ".java"
    file = open(filename, "w+")
    file.write("public class " + className + " { \n\tpublic static void main(String[] args) {\n\n\t}\n}\n")
    file.close()
    print("Created Java file: " + filename)


def createPython(filename):
    filename = filename + ".py"
    file = open(filename, "w+")
    file.write("import sys \n\ndef main():\n\n\nif __name__ == '__main__':\n\tmain()\n")
    file.close()
    print("Created Python file: " + filename)


def createBash(filename):
    filename = filename + ".sh"
    file = open(filename, "w+")
    file.write("#!/bin/bash\n\n")
    file.close()
    os.system("chmod +x " + filename)
    print("Created Bash Script: " + filename)


def createHTML(filename):
    filename = filename + ".html"
    file = open(filename, "w+")
    file.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title></title>\n\t</head>\n\n\t<body>\n\n\t</body>\n</html>\n")
    file.close()
    os.system("chmod 644 " + filename)
    print("Created HTML file: " + filename)


def createC(filename):
    filename = filename + ".c"
    file = open(filename, "w+")
    file.write("#include <stdio.h>\n#include <stdlib.h>\n\nint main(int argc, char** argv) {\n\n}\n")
    file.close()
    print("Created C file: " + filename)


def createCC(filename):
    filename = filename + ".cc"
    file = open(filename, "w+")
    file.write("#include <iostream>\n\nusing namespace std;\n\nint main(int argc, char** argv) {\n\n}\n")
    file.close()
    print("Created C++ file: " + filename)


def touch(filename):
    cmd = "touch " + filename
    os.system(cmd)
    print("Created file using touch command: " + filename)


def checkArgs(arguments):
    language = arguments[0].lower()
    filename = arguments[1]
    if language == "java":
        createJava(filename)
    elif language == "python":
        createPython(filename)
    elif language == "bash":
        createBash(filename)
    elif language == "html":
        createHTML(filename)
    elif language == "c":
        createC(filename)
    elif language == "c++":
        createCC(filename)
    else:
        print("Language \"" + arguments[0] + "\" is not a valid option")
        exit(1)


def main():
    # vue, react, angular
    arguments = sys.argv[1:]
    numArgs = len(arguments)

    if numArgs == 1:
        touch(arguments[0])
    elif numArgs == 2:
        checkArgs(arguments)
    else:
        printUsage()

if __name__ == '__main__':
    main()
