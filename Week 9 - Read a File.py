"""
Created on Sun Apr 20 20:43:18 2025

@author: Mateusz
"""

#Counts how many times a word appears in the story
def count_word(story, word):
    story = story.lower()
    word = word.lower()
    words = story.split()
    count = 0
    for w in words:
        clean = w.strip(".,!?:;\"'")
        if clean == word or clean == word + "'s":
            count += 1
    return count

#Finds all words in the story that are a specific length
def words_of_length(story, length):
    words = story.split()
    result = []
    for word in words:
        clean = word.strip(".,!?:;\"'")
        if len(clean) == length:
            result.append(clean)
    return result

#Finds the average word length
def average_length(story):
    words = story.split()
    clean_words = [word.strip(".,!?:;\"'") for word in words if word.strip(".,!?:;\"'")]
    total_length = sum(len(word) for word in clean_words)
    return total_length / len(clean_words)

def main():
    # Read the story
    file = open("story.txt", "r")
    lines = file.readlines()
    story = "".join(lines)
    file.close()

    # 1 & 2) Count Ginger and Pumpkin
    ginger_count = count_word(story, "ginger")
    pumpkin_count = count_word(story, "pumpkin")

    # 3) Longest word
    words = story.split()
    longest_word = ""
    for word in words:
        clean = word.strip(".,!?")
        if len(clean) > len(longest_word):
            longest_word = clean
    longest_length = len(longest_word)

    # 4) Average word length
    avg_length = average_length(story)

    # 5) Words of length 6
    words_len6 = words_of_length(story, 6)

    # 6) First line with "kitten"
    kitten_line = -1
    for i in range(len(lines)):
        if "kitten" in lines[i].lower():
            kitten_line = i + 1
            break

    # Write answers to file
    out = open("output.txt", "w")
    out.write("1) How many times is the name ginger mentioned?: " + str(ginger_count) + "\n")
    out.write("2) How many times is the name pumpkin mentioned?: " + str(pumpkin_count) + "\n")
    out.write("3) What is the length of the longest word in the story and what is the word(may be multiple only need one)?: " + "The length is " + str(longest_length) + " and the word is " + longest_word + "\n")
    out.write("4) What is the average length of words in the story? " + str(round(avg_length, 2)) + "\n")
    out.write("5) How many words are length 6?: " + str(len(words_len6)) + "\n")
    out.write("6) On which line do they first use the word kitten?: " + str(kitten_line) + "\n")
    out.close()

main()