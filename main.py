# List of quiz questions, each with options and the correct answer key
questions = [
    {
        'question': 'Who was the first President of India?',
        'options': ['A. Mahatma Gandhi', 'B. Jawaharlal Nehru', 'C. Rajendra Prasad', 'D. Sardar Vallabhbhai Patel'],
        'answer': 'C'
    },
    {
        'question': 'What is the chemical formula for water?',
        'options': ['A. H2O', 'B. CO2', 'C. O2', 'D. NaCl'],
        'answer': 'A'
    },
    {
        'question': 'Which is the longest river in the world?',
        'options': ['A. Amazon', 'B. Nile', 'C. Yangtze', 'D. Ganges'],
        'answer': 'B'
    },
    {
        'question': 'Which country won the FIFA World Cup in 2018?',
        'options': ['A. Brazil', 'B. Germany', 'C. France', 'D. Argentina'],
        'answer': 'C'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options': ['A. Charles Dickens', 'B. William Shakespeare', 'C. Jane Austen', 'D. Mark Twain'],
        'answer': 'B'
    },
    {
        'question': 'What is 15% of 200?',
        'options': ['A. 20', 'B. 30', 'C. 40', 'D. 50'],
        'answer': 'B'
    },
    {
        'question': 'What is the powerhouse of the cell?',
        'options': ['A. Nucleus', 'B. Mitochondria', 'C. Ribosome', 'D. Endoplasmic Reticulum'],
        'answer': 'B'
    },
    {
        'question': 'What is the capital of Australia?',
        'options': ['A. Sydney', 'B. Melbourne', 'C. Canberra', 'D. Perth'],
        'answer': 'C'
    },
    {
        'question': 'Which movie won the Oscar for Best Picture in 2020?',
        'options': ['A. Parasite', 'B. Joker', 'C. 1917', 'D. Once Upon a Time in Hollywood'],
        'answer': 'A'
    },
    {
        'question': 'What is the currency of Japan?',
        'options': ['A. Yen', 'B. Won', 'C. Ringgit', 'D. Baht'],
        'answer': 'A'
    }
]

# Prize levels for safe exits at milestones
prices = [200000, 500000, 1000000]

# p is a progress counter that increases when the player answers correctly
p = 1

for question in questions:
    # Display the current question and answer choices
    print(f"Question: {question['question']} \nOptions: {question['options']}")
    
    # Get the player's answer and normalize it to uppercase
    user_answer = input('Your answer (A/B/C/D): ')

    # Check if the answer is correct
    if user_answer.upper() == question['answer']:
        print('Correct!')
        p += 1

        # Award prize money when the player reaches a guaranteed milestone
        if p == 5 or p == 9 or p == 11:
            guaranteed_index = ((p - 2) // 3) - 1
            print(f'Congratulations! You have won Rs. {prices[guaranteed_index]}! \n')
    else:
        # Show the correct answer and final prize money on a wrong response
        print(f'Wrong! The correct answer is {question["answer"]}.')
        guaranteed_index = ((p - 2) // 3) - 1
        print(f'You can take home Rs. {prices[guaranteed_index]}!')
        print('Better luck next time!')
        break

print('Quiz completed!')


