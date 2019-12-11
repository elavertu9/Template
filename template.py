import sys, os

def printUsage():
    print("\n\tusage: template <language> <file name> \n\tusage: template <file name>\n\tnote: file extension will be added for you\n")


def createJava(filename):
    className = filename[0].upper() + filename[1:].lower()
    filename = filename + ".java"
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
    print("Created Bash Script: " + filename)
    os.system("chmod +x " + filename)


def checkArgs(arguments):
    language = arguments[0].lower()
    filename = arguments[1]
    if language == "java":
        createJava(filename)
    elif language == "python":
        createPython(filename)
    elif language == "bash":
        createBash(filename)
    else:
        print("Language \"" + arguments[0] + "\" is not a valid option")
        exit(1)


def main():
    # c, c++, vue, html, react, angular, bash
    arguments = sys.argv[1:]
    numArgs = len(arguments)

    if numArgs == 1:
        # Use touch command
        print("1 arg provided, issuing touch command using filename provided")
    elif numArgs == 2:
        checkArgs(arguments)
    else:
        printUsage()

if __name__ == '__main__':
    main()
