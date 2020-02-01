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


def main():
    some_text = "A do run run run, a do run run"
    print(some_text)
    cleaned = preprocess(some_text)
    print(cleaned)
main()