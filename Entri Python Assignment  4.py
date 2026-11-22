# Step 1: Preloaded Feedbacks
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '  Very   GOOD  Service!!!',
        'poor support,   not happy   ',
        'GREAT experience! will come again.',
        'okay   okay...',
        '  not   BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add More Feedbacks
while True:
    try:
        num_new = int(input("How many more feedbacks do you want to add? "))
        if num_new < 0:
            print("Please enter 0 or a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

next_s_no = len(feedback_data['S_No']) + 1

for i in range(num_new):
    print(f"\n--- Entering Feedback #{next_s_no} ---")
    name = input("Enter Name: ").strip()
    fb_text = input("Enter Written Feedback: ")
    
    # Validate rating between 1 and 5
    while True:
        try:
            rating = int(input("Enter Rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            
    # Append new data into the dictionary
    feedback_data['S_No'].append(next_s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(fb_text)
    feedback_data['Rating'].append(rating)
    next_s_no += 1

# Step 3: Text Cleaning
cleaned_feedbacks = []
for text in feedback_data['Feedback']:
    # Remove punctuation (., ,, !, ?)
    for punct in ['.', ',', '!', '?']:
        text = text.replace(punct, '')
    # Remove leading/trailing spaces, collapse multiple spaces, and convert to lowercase
    cleaned_text = ' '.join(text.split()).lower()
    cleaned_feedbacks.append(cleaned_text)

feedback_data['Feedback'] = cleaned_feedbacks

# Step 4: Word Count Insights
def count_word_in_feedbacks(word):
    target = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        # Split into words so partial matches aren't counted
        if target in fb.split():
            count += 1
    return count

print("\n" + "="*45)
print("WORD COUNT INSIGHTS")
print("="*45)
print(f"Number of feedbacks containing 'good': {count_word_in_feedbacks('good')}")
print(f"Number of feedbacks containing 'poor': {count_word_in_feedbacks('poor')}")
print(f"Number of feedbacks containing 'excellent': {count_word_in_feedbacks('excellent')}")

# Step 5: Final Summary & Insights
print("\n" + "="*45)
print("FINAL CLEANED FEEDBACK DATA")
print("="*45)
print(feedback_data)

# Average rating
avg_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage Rating: {avg_rating:.2f}")

# Feedback with the longest comment (by word count)
max_words = -1
longest_idx = 0
for idx, fb in enumerate(feedback_data['Feedback']):
    word_count = len(fb.split())
    if word_count > max_words:
        max_words = word_count
        longest_idx = idx

print("\nLongest Feedback (by word count):")
print(f"  S_No: {feedback_data['S_No'][longest_idx]} | Name: {feedback_data['Name'][longest_idx]} | "
      f"Rating: {feedback_data['Rating'][longest_idx]} | Words: {max_words}")
print(f"  Comment: '{feedback_data['Feedback'][longest_idx]}'")

# List of unique words across all feedbacks
unique_words = sorted(set(
    word for fb in feedback_data['Feedback'] for word in fb.split()
))
print(f"\nUnique Words ({len(unique_words)} total):")
print(unique_words)

# Optional: Sort feedbacks by rating (highest to lowest) using zip() and sorted()
print("\n" + "="*45)
print("FEEDBACKS SORTED BY RATING (HIGHEST TO LOWEST)")
print("="*45)
zipped_data = zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
)
sorted_feedbacks = sorted(zipped_data, key=lambda x: x[3], reverse=True)

for s_no, name, fb, rating in sorted_feedbacks:
    print(f"Rating: {rating}/5 | S_No: {s_no:<2} | Name: {name:<8} | Feedback: {fb}")