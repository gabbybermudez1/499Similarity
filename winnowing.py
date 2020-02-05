
#TODO: Consider whether adding punctuation removal will help
def clean_text(text):
    """
    Takes in a piece of text and eliminates unnecessary features such as capitalization, trailing or leading 
    whitespaces, and spaces between words. 

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



# TODO: give this a new name
def revised_k_gram(text, k):
    '''
    This is the k-gram generator algorithm described in the Extended Winnowing Algorithm paper that accompanies this
    source code. This takes in a piece of text and an integer k that represents how long each K-gram is. This outputs
    the various k-grams as well as their location in the original text. 

    Sample input: "helloworld" , 5 

    Sample Output: [("hello",0) , ("ellow", 1), ("llowo",2), ("lowor",3), ("oworl",4), ("world", 5) ]

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


# TODO: Decide if you want to deprecate this
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


# TODO: check to see you are not off by one 
def select_fingerprints(hash_list, w):
    '''
    Parameters
    ----------
    hash_list : list of (int, int)
    
    w : int
        w represents the window size for which we select a rightmost minimum
    
    Returns
    -------
    fingerprints : list of (int, int)
    '''
    fingerprints = []
    min_index = -1
    prev_min_index = -1
    # traverse over the hash_list
    for hash_index in range(len(hash_list) - w +1):
        min_value =  float("inf")
        #traverse over each window
        for window_index in range(hash_index, hash_index + w ):
            if hash_list[window_index][0] <= min_value:
                min_index = window_index
                min_value = hash_list[window_index][0]
        # If the minimum value of the previous window is no longer the minimum value
        if min_index != prev_min_index:
            prev_min_index = min_index
            fingerprints.append(hash_list[min_index])
    return fingerprints


def winnow(some_text):


    print(some_text)
    k_grams = revised_k_gram(some_text, 6)
    print(k_grams)
    print(len(k_grams))
    test_fingerprints = select_fingerprints(k_grams, 4)
    print(test_fingerprints)

winnow("This is an example of all to all matching")

