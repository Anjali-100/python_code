import random
data = [{'name': 'Instagram','follower_count': 346,'description': 'Social media platform','country': 'United States' },
        {'name': 'Cristiano Ronaldo','follower_count': 215,'description': 'Footballer','country': 'Portugal'},
        {'name': 'Ariana Grande','follower_count': 183,'description': 'Musician and actress','country': 'United States'},
        {'name': 'Dwayne Johnson','follower_count': 181,'description': 'Actor and professional wrestler','country': 'United States'},
        {'name': 'Selena Gomez','follower_count': 174,'description': 'Musician and actress','country': 'United States'},
        {'name': 'Kylie Jenner','follower_count': 172,'description': 'Reality TV personality and businesswoman and Self-Made Billionaire','country': 'United States'},
        {'name': 'Kim Kardashian','follower_count': 167,'description': 'Reality TV personality and businesswoman','country': 'United States' },
        {'name': 'Lionel Messi', 'follower_count': 149, 'description': 'Footballer','country': 'Argentina'},
        {'name': 'Beyoncé','follower_count': 145,'description': 'Musician','country': 'United States'},
        {'name': 'Neymar','follower_count': 138,'description': 'Footballer','country': 'Brasil'},
        {'name': 'National Geographic', 'follower_count': 135,'description': 'Magazine','country': 'United States'},
        {'name': 'Justin Bieber','follower_count': 133,'description': 'Musician','country': 'Canada'},
        {'name': 'Taylor Swift','follower_count': 131,'description': 'Musician','country': 'United States' },
        {'name': 'Kendall Jenner','follower_count': 127,'description': 'Reality TV personality and Model','country': 'United States'}
        ]
import random,os,time
def get_random_account():
  return random.choice(data)
def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"
def check_answer(guess, a_followers, b_followers):
   if a_followers > b_followers:
    return guess == "a"
   else:
    return guess == "b"
def game():
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()
  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()
    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    time.sleep(1)
    os.system("clear")
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")
game()


