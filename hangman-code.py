import random
with open('words.txt','r') as f:
    words=f.readlines()
word="programming"
allowed_Errors=7
guesses=[]
done=False
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print("")
    guess=input(f"allowed errors left {allowed_Errors},next guess:")
    guesses.append(guess.lower())
    if guess.lower() not in  word.lower():
        allowed_Errors-=1
        if allowed_Errors==0:
            break
    done=True
    for letter in word:
        if letter.lower() not in guesses:
            done=False
if done:
    print(f"you found the word it was {word}!:")
else:
    print(f"Game over! the word was {word}")
