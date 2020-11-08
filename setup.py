import sys, platform, os

def configureMac():
	path  = os.popen('pwd').readlines()[0].rstrip()
	append = "echo \'alias template=\"python " + path + "/template.py \"\' >> ~/.bash_profile"
	os.system(append)
	print("Refresh your terminal using . ~/.bash_profile for the changes to take effect.")


def configureLinux():
	path = os.popen('pwd').readlines()[0].rstrip()
	append = "echo \'alias template=\"python " + path + "/template.py \"\' >> ~/.bashrc"
	os.system(append)
	print("Refresh your terminal using . ~/.bashrc for the changes to take effect.")


def main():
	os = platform.system()

	if os == 'Darwin':
		print("Mac operating system detected. Adding alias entry to .bash_profile...")
		configureMac()
	elif os == 'Linux':
		print("Linux operating system detected. Adding alias entry to .bashrc...")
		configureLinux()
	else:
		print(os + " is not supported by Template.py")


if __name__ == '__main__':
	main()
