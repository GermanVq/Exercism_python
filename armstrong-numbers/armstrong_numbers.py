def is_armstrong_number(number):
    n=len(str(number))
    numb=str(number)
    numbers = [int(i) ** n for i in numb]   
    return sum(numbers) == number