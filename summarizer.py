# Import necessary libraries
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from heapq import nlargest

def summarize_text(text, num_sentences=5):
    """
    Summarizes a given text by extracting the most important sentences.

    Args:
        text (str): The input text to be summarized.
        num_sentences (int): The desired number of sentences in the summary.

    Returns:
        str: A concise summary of the input text.
    """
    
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    word_freq = defaultdict(int)
    for word in filtered_words:
        word_freq[word] += 1

    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] += word_freq[word]


    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summary

if __name__ == "__main__":
    # Sample long text
    long_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals and humans. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving".

    As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. A quip in Tesler's Theorem says "AI is whatever hasn't been done yet." For instance, optical character recognition is frequently excluded from things considered to be "AI", having become a routine technology. Modern machine capabilities generally classified as AI include successfully understanding human speech, competing at the highest level in strategic game systems (such as chess and Go), autonomous cars, intelligent routing in content delivery networks and military simulations.
    """

    print("--- Original Text ---")
    print(long_text)
    print("\n" + "="*50 + "\n")
    
    summary = summarize_text(long_text, num_sentences=2)
    print("--- Concise Summary ---")
    print(summary)