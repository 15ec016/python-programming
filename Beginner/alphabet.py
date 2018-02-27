m = input("Input a letter of the alphabet: ")

if m in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % m)
elif m == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % m) 
	
