import time
import os

def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            questions.append({
                'question': parts[0],
                'options': parts[1:5],
                'correct': parts[5]
            })
    return questions

def load_scores(filename):
    scores = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                scores.append(line.strip())
    return scores

def save_score(filename, username, score):
    with open(filename, 'a') as file:
        file.write(f"{username},{score}\n")

def display_leaderboard(scores):
    print("\nLeaderboard:")
    for score in sorted(scores, key=lambda x: int(x.split(',')[1].split('/')[0]), reverse=True)[:5]:
        print(score)

def quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{chr(65 + j)}. {option}")
        
        start_time = time.time()
        answer = input("Your Answer: ").strip().upper()
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 30:
            print("Time's up! You did not answer in time.")
            continue
        
        if answer == q['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['correct']}.")
    
    return score

def main():
    print("Welcome to the Quiz Application!")
    print("Rules:")
    print("- Each question has 4 options.")
    print("- Enter the option (A, B, C, D) as your answer.")
    print('''- You will have only 30 seconds to answer one question;
           after that, the question's marks will not be counted.''')
    print("Press Enter to Start!")
    input()

    questions = load_questions('questions.txt')
    score = quiz(questions)
    
    print(f"\nQuiz Complete! Your Score: {score}/{len(questions)}")
    
    username = input("Enter your name to record your score: ")
    save_score('scores.txt', username, f"{score}/{len(questions)}")
    
    scores = load_scores('scores.txt')
    display_leaderboard(scores)

if __name__ == "__main__":
    main()