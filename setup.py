import sys, platform, os

def printUsage():
	print("Usage: \n\tsetup.py <mac|MAC|linux|Linux>")


def configureMac():
	path  = os.popen('pwd').readlines()[0].rstrip()
	append = "echo \'alias template=\"python " + path + "/template.py \"\' >> ~/.bash_profile"
	os.system(append)


def configureLinux():
	path = os.popen('pwd').readlines()[0].rstrip()
	append = "echo \'alias template=\"python " + path + "/template.py \"\' >> ~/.bashrc"
	os.system(append)


def main():
	os = platform.system()

	if os == 'Darwin':
		print("Mac operating system detected. Adding alias entry to .bash_profile...")
		configureMac()
	elif os == 'Linux':
		print("Linux operating system detected. Adding alias entry to .bashrc...")
	else:
		print(os + " is not supported by Template.py")


if __name__ == '__main__':
	main()
