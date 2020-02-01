import math



#TODO: Consider whether adding punctuation removal will help
def preprocess(text):
    """
    Takes in a piece of text and eliminates unnecessary features such as capitalization, trailing + leading whitespaces,
    and spaces. This is the first step in the winnowing algorithm.

    Parameters
    ----------
    text : str
        String that we want to clean up. In practice, this is source code. 
    
    Returns
    -------
    cleaned_text : str
        String that is the same as the input text but with the unnecessary features removed.
    """

    cleaned_text = text.lower()
    cleaned_text= cleaned_text.replace(" ", "") #remove whitespace
    cleaned_text= cleaned_text.replace("\n", "") #remove the newline character
    return cleaned_text

def return_k_grams(text, k):
    """
    Takes in a string and returns the list of k grams that can be derived from that text. 
    
    Ex: If the text is HelloWorld and we want to derive the various 5-grams, we end up with:

    [Hello, elloW, lloWo, loWor, oWorl, World] 

    Parameters
    ----------
    k : int
        This represents how big our k gram is 

    text : str
        This is the string that we want to derive k-grams for
    
    Returns
    -------
    k-grams : list of str
        This is a list of a strings where each string in the array is a k-gram
    """

    #start and end index give us a handle of what character from the text to start and end slicing
    k = math.floor(k)
    start_index = 0
    end_index = k
    k_grams = []
    while(end_index != len(text) + 1):
        k_grams.append(text[start_index: end_index])
        start_index += 1
        end_index += 1
    return k_grams


    # while(end_index != len(text)):




# function that will acts as a playground to see if my functions are working
def main():
    some_text = "A do run run run a do run run"
    print(some_text)
    cleaned = preprocess(some_text)
    print(cleaned)
    k_grams = return_k_grams(cleaned, 5)
    print(k_grams)
main()