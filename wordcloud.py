#ENTER LOCATION OF INPUT TEXT FILE in line 9


#import required libraries
import wordcloud
from matplotlib import pyplot as plt

#open the .txt file to be used to generate the word-cloud
file_contents=open(" ").read() #enter location of text file

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i","for","he","she", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at","us", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor","in","on", "too", "very", "can", "will", "just"]
    
    ns=""
    nl=[]
    for i in file_contents:
        if i in punctuations:
            continue
        ns=ns+i #string without punctuations
    l=ns.split() #list of all words 
    
    for i in l: 
        i=i.lower()  
        nl.append(i) #nl is a list with all lowercase words.
        
    final_list=[]
    
    for i in nl:
        if i in uninteresting_words:  #skip uninteresting words
            continue
        if i.isnumeric():  #skip numbers
            continue
        final_list.append(i)
    
    
    freq={}
    for j in final_list:
        freq[j]=freq.get(j,0)+1   #create dictionary of word-frequencies
    

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.figure(figsize=(50,80))
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()