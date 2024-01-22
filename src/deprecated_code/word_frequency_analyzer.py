import json


# unstructured_word_list = []


# def list_unpacker():
# with open('five_lecture_json.json', 'r') as f:
#     texts = json.load(f)
# for sentence in texts:
#     for token in sentence:
#         unstructured_word_list.append(token)


# list_unpacker()

# json_data = json.dumps(unstructured_word_list, ensure_ascii=False, indent=4)
# with open('UNSTRUCTURED_five_lecture_json.json', 'w') as json_file:
#     json_file.write(json_data)


def word_locator():
    # Load data
    with open('UNSTRUCTURED_five_lecture_json.json', 'r') as f:
        texts = json.load(f)

    # Gather Input
    target_word = input('What word would you like to search for? ')
    print(f'Searching for {target_word}')

    # Search in data
    scanning_position = 0
    tw_positions = []

    for word in texts:
        scanning_position += 1
        word = word.lower()
        if word == target_word:
            tw_positions.append(scanning_position)

    # Return to user

    newline = "\n"
    print(
        f'Out of a total of {len(texts)} words, {target_word} appears {len(tw_positions)} times.')
    position_response = input(
        'Would you like you like to see all positions? Type Y or N ')
    if position_response == 'Y':
        for position in tw_positions:
            if position <= 4758:
                print(f'Word #: {position} {newline} (Lecture 1)')
            elif 4759 <= position <= 10332:
                print(f'Word #: {position} {newline} (Lecture 2)')
            elif 10333 <= position <= 16237:
                print(f'Word #: {position} {newline} (Lecture 3)')
            else:
                print(f'Word #: {position} {newline} (Lecture 4)')

    if position_response == 'N':
        print('Okay then!')


word_locator()
