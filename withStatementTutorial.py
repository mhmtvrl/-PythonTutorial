def openFile():
	with open('output.txt', 'w') as f:
		f.write('Hi there!')

def main():
	openFile()

if __name__ == '__main__':
	main()