# Coddy.Tech Daily Challenge Exam Concentration Simulator
# Coddy.tech DC 21/06/2025
# Today we are trying a medium challenge question. It wasn't the hardest to contextually however a lot of fine tuning required in order to make it work.

def is_prime(num):
  for i in range(2, int(num / 2)):
    if (num % i == 0):
      return False
  return True

def exam_concentration_simulator(questions, difficulty_levels):
  for i in range(len(questions)):
    # 1. If a question's difficulty level is greater than 7, reverse the entire question string.
    if difficulty_levels[i] > 7:
      questions[i] = questions[i][::-1]
      
    # 2. If a question contains the word "explain" (case-insensitive), skip processing that question and move to the next one.
    if 'explain' in questions[i].lower():
      break
    
    # 3. If a question's length is a prime number, reverse the order of words in the question.
    if is_prime(len(questions[i])):
      str_list = ''
      
      str_list = questions[i].rsplit()
      str_list.reverse()
      questions[i] = ' '.join(str_list)
    
    # 4. If a question's difficulty level is a multiple of 3, convert every third character to uppercase.
    if difficulty_levels[i] % 3 == 0:
      string = questions[i]
      string.rsplit()
      str_list = string.rsplit()
      str_list = list(' '.join(str_list))
      for j in range(2, len(str_list), 3):
        str_list[j] = str_list[j].upper()
      questions[i] = ''.join(str_list)
      
    # 5. If a question starts with "What" or "How", continue to the next question without processing it.
    if questions[i].startswith('What') or questions[i].startswith('How'):
      continue
  return questions
    
    