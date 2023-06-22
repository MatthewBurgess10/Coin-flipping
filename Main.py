import random
coin = ['heads', 'tails']
total_flips = []
def coin_flip():
    answer = random.choice(coin)
    return answer
def flip_percentage():
    counter = 0
    for i in total_flips:
        if i == 'heads':
            counter = counter + 1
    percentage = counter/len(total_flips)
    return percentage


choice = int(input("Pick the number of times you want the coin flipped: "))
for i in range(0, choice):
    toss = coin_flip()
    total_flips.append(toss)
    
print(', '.join(total_flips))

percent_print = input("would you like to see the percentage of heads to tails? \ny/n: ")
if percent_print == 'y':
    print(f'The percentage of heads is:', {percentage})       
else: 
    print("okay")