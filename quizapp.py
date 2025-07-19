# Simple Quiz App for Beginners

# Questions, Options, and Answers
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote the Ramayana?",
        "options": ["A. Tulsidas", "B. Valmiki", "C. Ved Vyas", "D. Kalidas"],
        "answer": "B"
    }
]

# Start the quiz
score = 0

print("Welcome to the Quiz App!")
print("-------------------------\n")

for i, q in enumerate(quiz):
    print(f"Q{i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

# Final score
print(f"Your final score: {score} out of {len(quiz)}")
