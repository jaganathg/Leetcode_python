def Stop_gninnipS_My_sdroW(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])

if __name__ == "__main__":
    # Example 1
    sentence = "Hey fellow warriors"
    print(Stop_gninnipS_My_sdroW(sentence))  # Output: "Hey wollef sroirraw"
    
    # Example 2
    sentence = "This is a test"
    print(Stop_gninnipS_My_sdroW(sentence))  # Output: "This is a test"
    
    # Example 3
    sentence = "This is another test"
    print(Stop_gninnipS_My_sdroW(sentence))  # Output: "This is rehtona test"