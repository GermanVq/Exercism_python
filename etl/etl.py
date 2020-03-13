def transform(legacy_data):
  return {text.lower(): points 
          for points,letters in legacy_data.items() 
          for text in letters}
