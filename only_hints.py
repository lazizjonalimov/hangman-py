def hint(word_length, choices_list, characters):
  is_correct = True
  while is_correct:
    if word_length <= 3: 
      for i in range(word_length):
        if i == 0:
          choices_list.append(characters[i])
        else: 
          choices_list.append("_")

    elif 6 >= word_length > 3: 
      for i in range(word_length):
        if i == 0 or i == 3:
          choices_list.append(characters[i])
        else: 
          choices_list.append("_")
    elif 10 >= word_length > 6: 
      for i in range(word_length):
        if i == 0 or i == 3 or i == 6:
          choices_list.append(characters[i])
        else: 
          choices_list.append("_")
    elif word_length >= 11:
      for i in range(word_length):
        if i == 0 or i == 3 or i == 6 or i == 10:
          choices_list.append(characters[i])
        else: 
          choices_list.append("_")

    is_correct = False
  return choices_list