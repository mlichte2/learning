import requests
import random
import time
import threading


attack_endpoint = 'https://www.conv.conbzres.com/13/con.php'

# site for list of words used in the bitcoin phrase
word_site = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"

response = requests.get(word_site)
words = response.content.decode()
words = words.split()

headers = {
    'authority': 'www.conv.conbzres.com',
    'method': 'POST',
    'path': '/13/con.php',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://half-strong-scapula.glitch.me',
    'referer': 'https://half-strong-scapula.glitch.me/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


def make_random_phrase(words):
    phrase = []
    length_decider = random.randrange(0, 3)
    if length_decider == 0:
        length = 12
    elif length_decider == 1:
        length = 18
    else:
        length = 24
    while len(phrase) < length:
        random_word = random.choice(words)
        # code below was to prevent duplicates in the bitcoin phrase but BIP39 doesnt actually avoid repeating words
        # https://bitcoin.stackexchange.com/questions/59904/does-bip39-mnemonic-construction-avoid-repeating-words
        # check = phrase.count(random_word)
        # if check > 0:
        #     continue
        # else:
        phrase.append(random_word)
    phrase = " ".join(phrase)
    phrase = phrase.lstrip()
    return phrase


def send_request():
    # count = 0
    while True:
        word_data = make_random_phrase(words)
        body = ({'ai': f'{word_data}'})
        res = requests.post(attack_endpoint, headers=headers,
                            data=body, allow_redirects=True)
        print(res.request.body)
        # count += 1
        # print(f'count: {count}')
        print(res.status_code)
        time.sleep(random.randrange(0, 2))


send_request()

# threads = []

# for i in range(50):
#     t = threading.Thread(target=send_request)
#     t.daemon = True
#     threads.append(t)

# for i in range(50):
#     threads[i].start()

# for i in range(50):
#     threads[i].join()
