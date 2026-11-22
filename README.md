# 📊 Survey Feedback Analyzer

A Python-based text analysis tool built to process, clean, and extract actionable insights from user survey data. This project demonstrates core Python programming fundamentals including dictionaries of lists, loops, conditionals, string manipulation, and user-defined functions.

---

## 🚀 Features

* **Preloaded Dataset:** Starts with 10 sample customer feedback records stored in a structured dictionary of lists (`S_No`, `Name`, `Feedback`, `Rating`).
* **Interactive Data Entry:** Prompts users to dynamically add new feedback entries with input validation for ratings (`1–5`) and automatic `S_No` incrementing.
* **Automated Text Cleaning:** Standardizes feedback strings by removing punctuation (`.`, `,`, `!`, `?`), stripping extra whitespace, and converting text to lowercase.
* **Keyword Frequency Analysis:** Includes a custom `count_word_in_feedbacks(word)` function to perform case-insensitive, exact word searches across all entries.
* **Summary Insights & Sorting:**
  * Calculates the overall average customer rating.
  * Identifies the longest feedback comment based on word count.
  * Extracts a sorted list of all unique words used across the dataset.
  * Sorts and displays all feedback entries from highest to lowest rating using `zip()` and `sorted()`.

---

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Concepts Applied:** Dictionaries & Lists, `while`/`for` Loops, Exception Handling (`try-except`), String Methods (`.replace()`, `.split()`, `.join()`, `.lower()`), Sets, `zip()`, and `lambda` sorting.

---

## 📂 Project Structure

```text
survey-feedback-analyzer/
│
├── feedback_analyzer.py   # Main Python script containing the analyzer logic
└── README.md              # Project documentation
```

---

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/survey-feedback-analyzer.git
   cd survey-feedback-analyzer
   ```

2. **Run the Python script:**
   ```bash
   python feedback_analyzer.py
   ```

3. **Follow the on-screen prompts:**
   * Enter `0` to analyze the 10 preloaded entries immediately, or enter a positive integer to add your own survey responses.

---

## 📋 Sample Output

```text
=============================================
WORD COUNT INSIGHTS
=============================================
Number of feedbacks containing 'good': 3
Number of feedbacks containing 'poor': 2
Number of feedbacks containing 'excellent': 1

=============================================
FINAL SUMMARY
=============================================
Average Rating: 3.40

Longest Feedback (by word count):
  S_No: 8 | Name: Kiran | Rating: 1 | Words: 7
  Comment: 'poor response and poor handling of issue'
```

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests if you'd like to expand the tool with sentiment scoring, CSV export, or visualization features!