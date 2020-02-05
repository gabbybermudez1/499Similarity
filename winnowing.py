import math



#TODO: Consider whether adding punctuation removal will help
def clean_text(text):
    """
    Takes in a piece of text and eliminates unnecessary features such as capitalization, trailing or leading 
    whitespaces, and spaces between woerds. This is the first step in the winnowing algorithm.

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


# DEPRECATED
def return_k_grams(text, k):
    """
    Takes in a string and returns the list of k grams that can be derived from that text. 
    
    Ex: If the text is HelloWorld and we want to derive the various 5-grams, we end up with:

    [Hello, elloW, lloWo, loWor, oWorl, World] 


    Note this will also come in handy when selecting further windows. 

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
    k = math.floor(k) # make sure k is an integer
    #start and end index give us a handle of what character from the text to start and end slicing
    start_index = 0
    end_index = k
    k_grams = []
    while(end_index != len(text) + 1):
        k_grams.append(text[start_index: end_index])
        start_index += 1
        end_index += 1
    return k_grams

# TODO: give this a new name
def revised_k_gram(text, k):
    '''
    This is the k-gram generator algorithm described in the Extended Winnowing Algorithm paper that accompanies this
    source code.

    Parameters
    ----------
    text : str
        This is the string that we want to derive k-grams for

    k : int
        This represents how big our k-gram is 

    Returns
        k_grams : list of typles (String, int)
            This represents a list of tuples.
    -------
    '''
    # Explicit type casting to ensure proper behaviour
    text = str(text)
    k_grams = []
    for start in range(len(text) - k + 1):
        # only perform the work necessary if the current character is not a whitespace
        if text[start] != " ":
            end = k  
            k_gram = text[start:end]
            k_gram = clean_text(k_gram)
            # after cleaning up our k-gram, we can end up with a much smaller string that is below the denoted k-gram length
            # if this is the case, then we will continually add the missing length to the string we are slicing
            while(len(k_gram) < k):
                end = end + (k - len(k_gram)) # we will need to add as many letters as are missing from the k-gram
                k_gram = text[start: end]    
                k_gram = clean_text(k_gram)
            k_grams.append((hash(k_gram), start))
    return k_grams

def generate_hashes(kgram_list, hash_func=None):
    """
    Parameters
    ----------
    kgram_list : list of str 
        This describes a list of different k-grams

    hash_func : function
        This is where we can define a custom hash function. This is here for optimization purposes (we can use
        less expensive hash functions down the line). Default is none. If none, then we will use python's in-built
        hash function 
    
    Returns
    -------
    hash_list : list of int
        A list of integers generated when we apply the hash function to each of the words of the input string list 
    """
    
    if (hash_func is None):
        hash_func = hash
    
    return [hash(kgram) for kgram in kgram_list]

#TODO: Fill this in
def rightmost_min(int_list):
    return


def main():
    some_text = "This is an example of all to all matching"
    print(some_text)
    k_grams = revised_k_gram(some_text, 6)
    print(k_grams)
    print(len(k_grams))
main()