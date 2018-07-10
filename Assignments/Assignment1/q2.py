#Reading the input document
document_text = open('input.txt', 'r').read()
#List of all the words in the document
words = document_text.split()
count = {}
#counting the unique words from the word list
for word in words:
	if word in count:
		count[word.lower()] += 1
	else:
		count[word.lower()] = 1
#Creating a output file and add the content
output_file = open("output.txt","w")
for key in sorted(count):
	output_file.write("%s %d\n" % (key,count[key]))
output_file.close()
