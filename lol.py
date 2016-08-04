import string


def thisIsInput():
	i = "2" + '\n' "hello my world" + '\n' + "amazing code"
	return i

def palindrome(inputString):
	arrayOfLines = inputString.splitlines()

	totalLines = arrayOfLines[0]
	word = ""
	for line in arrayOfLines[1:]:
		noSpaces = line.replace(" ", "")
		totalLength = len(noSpaces)
		palLength = createPalindromeNum(line)
		leftover = totalLength - palLength
		ascii = leftover + 65

		word += chr(ascii)

	return word



def createPalindromeNum(istring):
	newString = ""

	alpha = "abcdefghijklmnopqrstuvwxyz"
	for char in alpha:
		count = istring.count(char)
		if count > 1:
			newString += char*count
	
	#print newString		# "llloo"
	if len(newString)%2 == 0:
		num = len(newString) + 1
		return num
	else:
		num = len(newString)
		return num


def main():
	inputString = thisIsInput()
	finalWord = palindrome(inputString)
	print finalWord



if __name__ == "__main__":
    main()

