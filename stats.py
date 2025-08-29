
def word_count(text):
    words = text.split()
    words_count = len(words)
    return  words_count 
def dictionary(text):
    word_dict = {}
    text = text.lower()
    for ch in text:
        if ch not in  word_dict:
            word_dict[ch] = 1
        else:
            word_dict[ch] += 1

    return word_dict    
def report(chars_dict):
    
    char_list = []
    for key in chars_dict:
        if key.isalpha():
            char_list.append({"char": key, "num": chars_dict[key]})

    def get_count(entry):
        return entry["num"] 
    

         
    char_list.sort(key=get_count, reverse=True ) 
    return char_list


    
     
    
    
