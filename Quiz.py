import pandas as pd

df = pd.read_csv('Questions.csv')

print(df.head())

#All functions here
def show_quiz(quiz_data):
  user_answers = []
  i = 0
  for i in range(len(quiz_data)):
    num = i + 1
    question = quiz_data.loc[i]['Question']
    print(f'{num}.{question}')
    choice_a = quiz_data.loc[i]['A']
    choice_b = quiz_data.loc[i]['B']
    choice_c = quiz_data.loc[i]['C']
    print(f'A.{choice_a}')
    print(f'B.{choice_b}')
    print(f'C.{choice_c}')
    answer = (input("Enter answer: ")).upper()
    print(f'Your answer is: {answer} \n')
    user_answers.append(answer)
    i = i + 1
  
  return (user_answers)

#Try running show_quiz here
show_quiz(df)

def calculate_score(user_answers, correct_answer):
  correct = 0
  wrong = 0
  
  for i in range(len(user_answers)):
    if user_answers[i] == correct_answer[i]:
      correct = correct + 1
    else:
      wrong = wrong + 1

  score = ((correct)/(correct + wrong)) * 100
  return (score)
 

def show_status(score, passing_score):
  if score >= passing_score:
    print(f'Your score is {int(score)}%. You are really friends! \n')
  else:
    print(f'Your score is {int(score)}%. Are we really friends? \n')
 
 
def game_on(quiz_data, passing_score):
  quiz_Data = quiz_data
  passing_Score = passing_score
  user_Answers = show_quiz(quiz_Data)
  correct_Answers = quiz_Data['Answer']
  user_Score = calculate_score(user_Answers, correct_Answers)
  show_status(user_Score, passing_Score)
 

def start_game(quiz_data, passing_score):
  quiz_data = quiz_data
  passing_score = passing_score
  start_answer = input(f'Do you wanna play?Y/N: \n').upper()
  print(start_answer)
  while start_answer == 'Y':
    game_on(quiz_data, passing_score)
    start_answer = input(f'Do you wanna play?Y/N: \n').upper()
  print(f'Thank you for playing')
  
# Start the game here
start_game(df, 80)


