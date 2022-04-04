import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')


def summarize(text):
    # print(text)
    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    return(summary)


# text = '''
# The fire spread to the nearby Vassilikou power station - which provides 50% of the country's electricity - knocking out the electricity supply to many homes and businesses.

# State television said the blasts caused extensive damage to property in the area and sparked wildfires in nearby scrubland in the tinder-dry summer conditions.


# A massive blast at a munitions dump in southern Cyprus has killed 12 people, including the commander of the country's navy, officials say.

# Alexandra Dimitriou, who was at nearby Governor's Beach at the time of the explosion, said all the hotels in the area had their glass blown out.

# A fire reportedly ignited about 100 containers holding confiscated Iranian explosives at the naval base at Zygi.

# Officials say all 98 containers of explosive stored in the munitions dump at the base had exploded.

# State radio said the dead included two sailors from the Cyprus navy, two soldiers and five firefighters.

# The blast, which occurred at 0600 (0300 GMT), was "rather like a sonic boom", eyewitness Hermes Solomon told the BBC.

# Six of the eight transmitters in the BBC's relay station at Zygi are without power, interrupting direct English-language broadcasts to the Middle East.

# I fell out of bed and ran to check on the kids," nearby resident Eleni Toubi told Reuters.

# President Dimitris Christopfias, who went to the area, described the explosion as "a catastrophe of biblical proportions".

# It has been knocked out, resulting in widespread power cuts.

# Government spokesman Stefanos Stefanou said sabotage had been ruled out.

# Cyprus said the shipment violated UN sanctions against Iran.

# The fire has also had a knock-on effect on the BBC's broadcasts to the eastern Mediterranean.

# About 60 people were wounded in the blast.

# '''
# print(summarize(text))
# print("\nfunc call done")
