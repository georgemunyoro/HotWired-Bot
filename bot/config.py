import os
from enum import Enum

from discord import Color
from yaml import safe_load

DATABASE = {
    "host": "127.0.0.1",
    "database": os.getenv("DATABASE_NAME"),
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "min_size": int(os.getenv("POOL_MIN", "20")),
    "max_size": int(os.getenv("POOL_MAX", "100")),
}

DEV_MODE = True

log_channel = 728570503169704014
contact_channel = 728570526443896934
support_channel = 728570540998262834
bug_report_channel = 728570578507923526
suggestions_channel = 728570594899132456
complaints_channel = 728570619985264650

creator = "The-Codin-Hole team"
devs = [688275913535914014, 306876636526280705, 710400991761137666, 711194921683648523]

youtube_url = "https://www.youtube.com/channel/UC3S4lcSvaSIiT3uSRSi7uCQ"
ig_url = "https://instagram.com/the.codin.hole/"

github_repo_link = "https://github.com/The-Codin-Hole/HotWired-Bot"
discord_server = "https://discord.gg/CgH6Sj6"

invite_link = (
    "https://discord.com/api/oauth2/authorize?client_id=742983334564462673&permissions=1610608374&scope=bot"
)

admin_invite_link = (
    "https://discord.com/api/oauth2/authorize?client_id=742983334564462673&permissions=8&scope=bot"
)

SUPPORT_SERVER = "https://discord.gg/7e9zKFr"


COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", ">>")

paste_link = "https://pastebin.com"
paste_link_2 = "https://hasteb.in"

line_img_url = "https://cdn.discordapp.com/attachments/581139962611892229/692712698487767080/animated_line.gif"


WEATHER_ICONS = {
    "wind": "https://cdn.discordapp.com/attachments/728569086174298112/735550169222873118/windy.png",
    "rain": "https://cdn.discordapp.com/attachments/728569086174298112/735550164458274947/raining.png",
    "sun": "https://cdn.discordapp.com/attachments/728569086174298112/735550167859593306/sunny.png",
    "cloud": "https://cdn.discordapp.com/attachments/728569086174298112/735550159781494865/cloudy.png",
    "partly": "https://cdn.discordapp.com/attachments/728569086174298112/735550162721701979/partly.png",
    "snow": "https://cdn.discordapp.com/attachments/728569086174298112/735550166563684474/snowy.png"
}


# Magic 8-Ball responses
NEGATIVE_REPLIES = [
    "Noooooo!!",
    "Nope.",
    "I'm sorry Dave, I'm afraid I can't do that.",
    "I don't think so.",
    "Not gonna happen.",
    "Out of the question.",
    "Huh? No.",
    "Nah.",
    "Naw.",
    "Not likely.",
    "No way, José.",
    "Not in a million years.",
    "Fat chance.",
    "Certainly not.",
    "NEGATORY.",
    "Nuh-uh.",
    "Not in my house!",
]

POSITIVE_REPLIES = [
    "Yep.",
    "Absolutely!",
    "Can do!",
    "Affirmative!",
    "Yeah okay.",
    "Sure.",
    "Sure thing!",
    "You're the boss!",
    "Okay.",
    "No problem.",
    "I got you.",
    "Alright.",
    "You got it!",
    "ROGER THAT",
    "Of course!",
    "Aye aye, cap'n!",
    "I'll allow it.",
]

ERROR_REPLIES = [
    "Please don't do that.",
    "You have to stop.",
    "Do you mind?",
    "In the future, don't do that.",
    "That was a mistake.",
    "You blew it.",
    "You're bad at computers.",
    "Are you trying to kill me?",
    "Noooooo!!",
    "I can't believe you've done this",
]

# NSFW Command Possible types
nsfw_possible = [
    "feet", "yuri", "trap", "futanari", "hololewd", "lewdkemo",
    "solog", "feetg", "cum", "erokemo", "les", "wallpaper",
    "lewdk", "ngif", "tickle", "lewd", "feed", "gecg",
    "eroyuri", "eron", "cum_jpg", "bj", "nsfw_neko_gif", "solo",
    "kemonomimi", "nsfw_avatar", "gasm", "poke", "anal", "slap",
    "hentai", "avatar", "erofeet", "holo", "keta", "blowjob",
    "pussy", "tits", "holoero", "lizard", "pussy_jpg", "pwankg",
    "classic", "kuni", "waifu", "pat", "8ball", "kiss",
    "femdom", "neko", "spank", "cuddle", "erok", "fox_girl",
    "boobs", "random_hentai_gif", "smallboobs", "hug", "ero", "smug",
    "goose", "baka", "woof",
]

# Possible HTTP Codes for HttpCat
http_codes = [
    100, 101, 200, 201, 202, 204, 206, 207, 300, 301,
    302, 303, 304, 305, 307, 400, 401, 402, 403, 404,
    405, 406, 408, 409, 410, 411, 412, 413, 414, 416,
    417, 418, 420, 421, 422, 423, 424, 425, 426, 429,
    444, 450, 451, 500, 502, 503, 504, 506, 507, 508,
    509, 511, 599,
]

# Search Engine categories
basic_search_categories = [
    "web",
    "videos",
    "music",
    "files",
    "images",
    "it",
    "maps",
]

nekos = {
    "sfw": "https://nekos.life/api/neko",
}


with open("bot/assets/languages.yml", "r") as file:
    default_languages = safe_load(file)


# Emojis class
class Emojis:
    issue = "<:IssueOpen:725770366714380410>"
    issue_closed = "<:IssueClosed:725770497039663114>"
    pull_request = "<:PROpen:725770558582554744>"
    pull_request_closed = "<:PRClosed:725770652354609234>"
    merge = "<:PRMerged:725770703600615435>"


class Infraction(Enum):
    warning = Color.gold()
    kick = Color.gold()
    ban = Color.red()


class SuggestionStatus(Enum):
    under_review = "Under review"
    denied = "Denied"
    approved = "Approved"


talk_games = {
    "wyr": [
        ".always be 10 minutes late or always be 20 minutes early?",
        ".lose all of your money and valuables or all of the pictures you have ever taken?",
        ".be able to see 10 minutes into your own future or 10 minutes into the future of anyone but yourself?",
        ".be famous when you are alive and forgotten when you die or unknown when you are alive but famous after you die?",
        ".go to jail for 4 years for something you didn’t do or get away with something horrible you did but always live in fear of being caught?",
        ".accidentally be responsible for the death of a child or accidentally be responsible for the deaths of three adults?",
        ".your shirts be always two sizes too big or one size too small?",
        ".live in the wilderness far from civilization or live on the streets of a city as a homeless person?",
        ".the general public think you are a horrible person but your family be very proud of you or your family think you are a "
        "horrible person but the general public be very proud of you?",
        ".live your entire life in a virtual reality where all your wishes are granted or in the real world?",
        ".be alone for the rest of your life or always be surrounded by annoying people?",
        ".never use social media sites / apps again or never watch another movie or TV show?",
        ".have an easy job working for someone else or work for yourself but work incredibly hard?",
        ".be the first person to explore a planet or be the inventor of a drug that cures a deadly disease?",
        ".have a horrible short term memory or a horrible long term memory?",
        ".be completely invisible for one day or be able to fly for one day?",
        ".be locked in a room that is constantly dark for a week or a room that is constantly bright for a week?",
        ".be poor but help people or become incredibly rich by hurting people?",
        ".live without the internet or live without AC and heating?",
        ".have a horrible job, but be able to retire comfortably in 10 years or have your dream job, but have to work until the day you die?",
        ".find your true love or a suitcase with five million dollars inside?",
        ".be able to teleport anywhere or be able to read minds?",
        ".die in 20 years with no regrets or die in 50 years with many regrets?",
        ".be feared by all or loved by all?",
        ".be transported permanently 500 years into the future or 500 years into the past?",
        ".never be able to use a touchscreen or never be able to use a keyboard and mouse?",
        ".be able to control fire or water?",
        ".have everything you eat be too salty or not salty enough no matter how much salt you add?",
        ".have hands that kept growing as you got older or feet that kept growing as you got older?",
        ".be unable to use search engines or unable to use social media?",
        ".give up bathing for a month or give up the internet for a month?",
        ".donate your body to science or donate your organs to people who need them?",
        ".go back to age 5 with everything you know now or know now everything your future self will learn?",
        ".relive the same day for 365 days or lose a year of your life?",
        ".have a golden voice or a silver tongue?",
        ".be able to control animals (but not humans) with your mind or control electronics with your mind?",
        ".sell all of your possessions or sell one of your organs?",
        ".lose all of your memories from birth to now or lose your ability to make new long term memories?",
        ".be infamous in history books or be forgotten after your death?",
        ".never have to work again or never have to sleep again (you won’t feel tired or suffer negative health effects)?",
        ".be beautiful / handsome but stupid or intelligent but ugly?",
        ".get one free round trip international plane ticket every year or be able to fly domestic anytime for free?",
        ".be balding but fit or overweight with a full head of hair?",
        ".be able to be free from junk mail or free from email spam for the rest of your life?",
        ".be fluent in all languages and never be able to travel or be able to travel anywhere for a year but never be able to "
        "learn a word of a different language?",
        ".have an unlimited international first class ticket or never have to pay for food at restaurants?",
        ".see what was behind every closed door or be able to guess the combination of every safe on the first try?",
        ".live in virtual reality where you are all powerful or live in the real world and be able to go anywhere but not "
        "be able to interact with anyone or anything?",
        ".never be able to eat meat or never be able to eat vegetables?",
        ".give up watching TV / movies for a year or give up playing games for a year?",
        ".always be able to see 5 minutes into the future or always be able to see 100 years into the future?",
        ".super sensitive taste or super sensitive hearing?",
        ".be a practicing doctor or a medical researcher?",
        ".be married to a 10 with a bad personality or a 6 with an amazing personality?",
        ".never be able to drink sodas like coke again or only be able to drink sodas and nothing else?",
        ".be a reverse centaur or a reverse mermaid/merman?",
        ".have constantly dry eyes or a constant runny nose?",
        ".be a famous director or a famous actor?",
        ".not be able to open any closed doors (locked or unlocked) or not be able to close any open doors?",
        ".give up all drinks except for water or give up eating anything that was cooked in an oven?",
        ".have to read aloud every word you read or sing everything you say out loud?",
        ".have whatever you are thinking appear above your head for everyone to see or have absolutely everything you do live streamed "
        "for anyone to see?",
        ".be put in a maximum security federal prison with the hardest of the hardened criminals for one year or be put in a relatively "
        "relaxed prison where wall street types are held for ten years?",
        ".have a clown only you can see that follows you everywhere and just stands silently in a corner watching you without doing or "
        "saying anything or have a real life stalker who dresses like the Easter bunny that everyone can see?",
        ".kill one innocent person or five people who committed minor crimes?",
        ".have a completely automated home or a self-driving car?",
        ".work very hard at a rewarding job or hardly have to work at a job that isn’t rewarding?",
        ".be held in high regard by your parents or your friends?",
        ".be an amazing painter or a brilliant mathematician?",
        ".be reincarnated as a fly or just cease to exist after you die?",
        ".be able to go to any theme park in the world for free for the rest of your life or eat for free at any drive through restaurant "
        "for the rest of your life?",
        ".be only able to watch the few movies with a rotten tomatoes score of 95-100% or only be able to watch the majority of movies with a"
        " rotten tomatoes score of 94% and lower?",
        ".never lose your phone again or never lose your keys again?",
        ".have one real get out of jail free card or a key that opens any door?",
        ".have a criminal justice system that actually works and is fair or an administrative government that is free of corruption?",
        ".have real political power but be relatively poor or be ridiculously rich and have no political power?",
        ".have the power to gently nudge anyone’s decisions or have complete puppet master control of five people?",
        ".have everyone laugh at your jokes but not find anyone else’s jokes funny or have no one laugh at your jokes but you still find "
        "other people’s jokes funny?",
        ".be the absolute best at something that no one takes seriously or be well above average but not anywhere near the best at something "
        "well respected?",
        ".lose the ability to read or lose the ability to speak?",
        ".live under a sky with no stars at night or live under a sky with no clouds during the day?",
        ".humans go to the moon again or go to mars?",
        ".never get angry or never be envious?",
        ".have free Wi-Fi wherever you go or be able to drink unlimited free coffee at any coffee shop?",
        ".be compelled to high five everyone you meet or be compelled to give wedgies to anyone in a green shirt?",
        ".live in a house with see-through walls in a city or in the same see-though house but in the middle of a forest far from civilization?",
        ".take amazing selfies but all of your other pictures are horrible or take breathtaking photographs of anything but yourself?",
        ".use a push lawn mower with a bar that is far too high or far too low?",
        ".be able to dodge anything no matter how fast it’s moving or be able ask any three questions and have them answered accurately?",
    ],
    "nhie": [
        ".watched the Ghostbusters remake.",
        ".wanted to be one of the Kardashians.",
        ".dressed as the opposite sex.",
        ".watched Spongebob Squarepants.",
        ".cried during a Pixar movie.",
        ".had a crush, or man crush, on Ron Swanson.",
        ".'cleaned up' by piling everything into a closet.",
        ".sung karaoke.",
        ".watched the 'Gangnam Style' music video.",
        ".had a crush on someone from 'Full House'.",
        ".watched an episode of 'Gilmore Girls'.",
        ".pretended to know a stranger.",
        ".worn sleepwear and pretended it was clothing.",
        ".said 'excuse me' when there was no one around.",
        ".scared myself in a mirror.",
        ".missed a high five.",
        ".heard someone else doing it.",
        ".sang in the shower.",
        ".blamed farts on an animal.",
        ".secretly wished I were a wizard at Hogwarts.",
        ".slept in regular clothing.",
        ".had a nightmare about zombies chasing me.",
        ".pretended to laugh at a joke I didn't get.",
        ".been scared of clowns.",
        ".thought a cartoon character was hot.",
        ".faked being sick so I could play video games.",
        ".liked Star Wars more than Star Trek.",
        ".tried out to be an extra in a movie.",
        ".scored over 100 while bowling.",
        ".used an Instant Pot.",
        ".played Candy Crush.",
        ".won a game of Scrabble.",
        ".made a duck face when taking a selfie.",
        ".looked out the car's passenger seat window and imagined it was a scene from a music video.",
        ".actually laughed out loud when typing 'lol'.",
        ".reread an email immediately after sending it.",
        ".daydreamed about being on a talk show and what I'd talk about.",
        ".Googled my own name to see what comes up.",
        ".pretended I was running from zombies while on a run.",
        ".sat in the shower.",
        ".tried something I saw on Pinterest.",
        ".ugly cried for no reason.",
        ".creeped on someone I just met on social media.",
        ".thought about how a loved one could identify me if my face was horribly disfigured in an accident.",
        ".answered someone 'left' or 'right' without thinking, because I have a 50/50 chance of being right.",
        ".been out of the country.",
        ".regifted a gift card.",
        ".traveled out of state by myself.",
        ".flown in a helicopter.",
        ".been on stage in front of a crowd.",
        ".lied in a job interview.",
        ".stalked a crush.",
        ".sung karaoke.",
        ".agreed with something Donald Trump said.",
        ".thought about what type of dog I would be.",
        ".watched children's cartoons I'm too old for.",
        ".lost sunglasses that I was already wearing.",
        ".locked my keys in my car.",
        ".not tipped at a restaurant.",
        ".given money to a homeless person.",
        ".tried to look at the sun.",
        ".bungee-jumped.",
        ".had surgery.",
        ".jumped out of a plane.",
        ".made a wish at a fountain.",
        ".accidentally eaten a bug.",
        ".cut someone in line.",
        ".stayed up all night.",
        ".read a single Harry Potter book.",
        ".been inside of a library.",
        ".lied about my age.",
        ".shot a gun.",
        ".had a cavity.",
        ".been mini golfing.",
        ".seen an elephant in real life.",
        ".been to Disney World.",
        ".bought clothing online.",
        ".had someone draw a caricature of me.",
        ".owned an Xbox.",
        ".spent hours watching funny videos on Youtube.",
        ".seen Titanic.",
        ".met a celebrity.",
        ".thought a movie was better than the book.",
        ".voted.",
        ".owned a watch.",
        ".ridden a skateboard.",
        ".learned how to play a musical instrument.",
        ".seen snow.",
        ".finished a Sudoku puzzle.",
        ".Googled something so I'd know how to spell it.",
        ".cheated on a test.",
        ".cried watching Homeward Bound.",
        ".licked a frozen pole.",
        ".had gum in my hair.",
        ".taken a horrible picture on picture day.",
        ".been a bully.",
        ".wanted to be a superhero.",
        ".been scared of the dark.",
        ".had trouble sleeping after watching a scary movie.",
        ".stayed up all night.",
        ".been to a sleepover.",
        ".had a birthday party.",
        ".cried at school.",
        ".sang on a stage.",
        ".performed in a talent show.",
        ".killed ants with a magnifying glass.",
        ".dropped Mentos into Coke or Pepsi.",
        ".eaten something on a dare.",
        ".used the excuse 'my dog ate my homework'.",
        ".sucked my thumb.",
        ".believed my toys had feelings.",
        ".watched Blue's Clues.",
        ".been terrified of a theme park ride.",
        ".been to a haunted house.",
        ".dressed up as a zombie for Halloween.",
        ".been sent to the principle's office.",
        ".done an Easter Egg Hunt.",
        ".built a fort with blankets.",
        ".fallen off a bike.",
        ".played video games all day.",
        ".stolen money from a sibling's piggy bank.",
        ".wished I had bunk beds.",
        ".played Pokemon.",
        ".been on a family road trip.",
        ".named a stuffed animal.",
        ".used training wheels.",
        ".eaten only candy for dinner.",
        ".stayed in character all day.",
        ".lied about being related to someone on tv.",
        ".written notes on the desk to use during a test.",
        ".tried to sign a permission slip for my parents.",
        ".stolen a friend's story and pretend it happened to me.",
        ".thrown something out of the school bus window.",
        ".lied about staying after school and went somewhere else.",
        ".hopped seats on the school bus.",
        ".accidentally sharted.",
        ".forgotten the punchline of a joke.",
        ".sang a song out loud and messed the lyrics.",
        ".walked in on someone in the bathroom.",
        ".had someone walk in on me in the bathroom.",
        ".sent a text to the wrong person.",
        ".tried to pass a silent fart, but it came out loud instead.",
        ".tripped in public.",
        ".wet the bed after childhood.",
        ".accidentally pooped my pants.",
        ".attempted martial arts moves while by myself.",
        ".drove over a curb.",
        ".mistaken a man for a women or vice versa.",
        ".laughed so hard, I peed my pants.",
        ".picked a wedgie in public.",
        ".called the wrong person, but pretended I meant to call them.",
        ".gone into the wrong restroom.",
        ".been so freaked to be outside at night, that I ran back in.",
        ".lost my swimwear bottoms.",
        ".had diarrhea at a friend's house.",
        ".broken a piece of furniture by sitting on it.",
        ".arrived somewhere late and had everyone staring at me.",
        ".had food stuck in my teeth all day.",
        ".walked around with my zipper down.",
        ".bought a children's toy for myself, as an adult.",
        ".recorded video of myself singing or dancing.",
        ".been caught picking my nose.",
        ".gotten something stuck in my nose.",
        ".greeted someone I thought was someone else.",
    ],
    "truths": [
        "What was the last thing you searched for on your phone?",
        "If you had to choose between going naked or having your thoughts appear in thought bubbles above your head for everyone to read, "
        "which would you choose?",
        "After you've dropped a piece of food, what's the longest time you've left it on the ground and then ate it?",
        "Have you ever played Cards Against Humanity with your parents?",
        "What's the first thing you would do if you woke up one day as the opposite sex?",
        "Have you ever peed in the pool?",
        "Who do you think is the worst dressed person here?",
        "True or false? You have a crush on {name}.",
        "Of the people here, who do you want to trade lives with?",
        "Did you have an imaginary friend growing up?",
        "Do you cover your eyes during a scary parts of a movie?",
        "Have you ever practiced kissing in a mirror?",
        "Did your parents ever give you the “birds and the bees” talk?",
        "What is your worst habit?",
        "Have you ever walked into a wall?",
        "Do you ever talk to yourself in the mirror?",
        "You’re in a public restroom and just went #2, then you realized your stall has no toilet paper. What do you do?",
        "What would be in your web history that you’d be embarrassed if someone saw?",
        "Do you sleep with a stuffed animal?",
        "Do you drool in your sleep?",
        "Do you talk in your sleep?",
        "Who is your secret crush?",
        "Who do you like the least here and why?",
        "What is your go-to song for the shower?",
        "Who is the sexiest person in this room?",
        "How would you rate your looks on a scale of 1 to 10?",
        "Would you rather have sex with {name} in secret or not have sex with that person but everyone thinks you did?",
        "What don't you like about me?",
        "What color underwear are you wearing right now?",
        "If you were rescuing people from a burning building and you had to leave one person behind from here, who would it be?",
        "Do you ever try to solve the problems between your best friend and his/her crush?",
        "Do you ever apply makeup without using the mirror?",
        "Have you ever admired your best friend if he/she get good marks in the examination?",
        "Have you ever tried to sing a tongue twister in a musical way?",
        "Tell me your weirdest habit.",
        "Do you like parties?",
        "Do you have crush on any of your school teachers?",
        "Who is the most annoying person among your friends?",
        "Do you go directly to your home after college in the evening?",
        "How many partners have you had?",
        "Suppose you were a billionaire, how would you spend your time?",
        "If your parents forced you to leave home, where would you go?",
        "If you wanted to start your own business, what it would be?",
        "Have you ever had the crush on someone much younger or older than you? What’s the biggest age difference?",
        "When was the last time you touched yourself?",
        "How many hours do you exercise a day?",
        "Have you ever farted in an elevator and get caught?",
        "Who is the worst kisser you have ever kissed and why?",
        "What is your favorite villain character?",
        "Have you ever wanted to try BDSM?",
        "Do you like when I act or talk dirty to you?",
        "Do you like having it in the morning or evening?",
        "Have you ever done it with your teacher?",
        "Have you ever flirted with your teacher in the school for good marks and grades?",
        "Have you ever laughed out when doing it and what is the reason?",
        "Whom would you love to date amongst the people in this room?",
        "When was the first time you fell in love and with whom?",
        "What has been the most embarrassing moment you've experienced so far?",
        "Tell us about your secret fantasy.",
        "Would you kiss {name}?",
        "What turns you on the most?",
        "Have you ever cheated on your partner?",
        "What is the most sensual piece of clothing you own?",
        "What attracts you to a person of the opposite sex?",
        "Have you ever gone skinny dipping?",
        "When was the first time you kissed someone? Who was it?",
        "Have you got a secret talent?",
        "Pick one person from this room you'd like to exchange your partners with!",
        "What is the wildest thing you have ever done in your life so far?",
        "What was your best sexual experience?",
        "What is the longest you’ve ever given head?",
        "Would you ever do a threesome?",
        "How do you feel about sex in groups?",
        "Would you ever watch your partner have sex with someone else?",
        "How many partners have you had at one time?",
        "Describe how your orgasms feel?",
        "Where is your favourite place to be kissed?",
        "Have you ever taken it in the butt or would you?",
        "What is the longest time you’ve gone without sex?",
        "Do you enjoy rough or slow sex?",
        "Do you prefer to be on top or bottom?",
        "What is your favourite position?",
        "What is your least favourite position?",
        "What is the worst sexual experience you’ve ever had?",
        "Have you ever had sex outside?",
        "Where is the strangest place you’ve ever had sex?",
        "Have you ever performed oral on someone of the same sex?",
        "Have you ever paid for sex?",
        "Who was your first partner?",
        "Have you ever made a video of yourself?",
        "Who is your favourite porn star?",
        "What is your favourite type of porn?",
        "What is your favourite strip club?",
        "Have you ever thought about being a stripper?",
        "Do you prefer the lights on or off (during sex)?",
        "Does size matter?",
        "Do you prefer to have music in the background, or for it to be be quiet?",
        "Do you prefer for your partner to be silent, or do you like moans?",
        "Do you like a lot of foreplay?",
        "What is your favourite type of foreplay?",
        "Have you done role-playing?",
        "What is your role-playing fantasy?",
        "What is your “sweet spot”?",
        "What is your strangest sexual fantasy?",
        "Would you ever have sex for money?",
        "How flexible are you?",
        "How many orgasms have you had in one sexual encounter?",
        "Spit or swallow?",
        "Who is your best looking teacher that you have ever had?",
        "Have you ever cheated on any test?",
        "Who is your crush?",
        "Who is the most annoying person you know?",
        "Have you ever pulled a prank on your teacher?",
        "Have you ever lied to your parents about what you were doing after school?",
        "Have you ever blamed something that you have done on one of your siblings?",
        "What college do you plan on going to?",
        "Are you still a virgin?",
        "How many partners have you had?",
        "Have you ever been kissed yet?, If so, who was your best kiss?",
        "What is your biggest pet peeve?",
        "What is the best vacation you’ve ever been on?",
        "Have you ever told one of your best friend’s secrets, even if you said you wouldn’t?",
        "Have you ever had a crush on someone that your best friend has dated?",
        "What is the most annoying thing that one of your siblings has done?",
        "Do you have a job? If so, what is your favourite thing about it?",
        "If you were a billionaire, what would you spend your time doing?",
        "What is the longest time you have ever been grounded?",
        "What is the longest time that you think you could go without your cell phone?",
        "What is the most expensive thing you own?",
        "If you had the choice to live on your own right now, would you do it?",
        "Would you ever get on a dating website?",
        "If you could own your own business one day, what would it be?",
        "What is your favourite kind of clothing?",
        "What celebrity are you obsessed with?",
        "What is the funniest youtube video you have ever seen?",
        "Who is the worst teacher you have ever had, why?",
        "What is your favourite sports team?",
        "What's the craziest thing that you have ever done without your parents knowing?",
        "What would you do if your parents left the house to you for a whole week?",
        "What is your favourite song that is out right now?",
        "Could you go two months without talking to your friends?",
        "Have you ever walked in on your parents doing it?",
        "Have you ever tasted a booger?",
        "What are some things you think about when sitting on the toilet?",
        "Do you cover your eyes during a scary part in a movie?",
        "What is your guilty pleasure?",
        "Has anyone ever walked in on you when taking a shit in the bathroom?",
        "Do you pick your nose?",
        "Do you sing in the shower?",
        "Have you ever peed yourself?",
        "What was your most embarrassing moment in public?",
        "Have you ever farted loudly in public?",
        "Have you ever tried to take a sexy picture of yourself?",
        "Do you think {name} is cute?",
        "What does your dream boy or girl look like?",
        "What was the last thing you texted?",
        "Do you think you'll marry your current partner?",
        "How often do you wash your undergarments?",
        "Have you ever tasted ear wax?",
        "Have you ever farted and then blamed someone else?",
        "Have you ever tasted your sweat?",
        "What is the most illegal thing you have ever done?",
        "Who is your favourite? Mom or Dad?",
        "Would you trade in your dog for a million dollars?",
        "If you were allowed to marry more than one person, would you? Who would you choose to marry?",
        "Would you rather lose your sex organs forever or gain 200 pounds?",
        "Would you choose to save 100 people without anyone knowing about it or not save them but have everyone praise you for it?",
        "If you could only hear one song for the rest of your life, what would it be?",
        "If you lost one day of your life every time you said a swear word, would you try not to do it?",
        "Who in this room would be the worst person to date? Why?",
        "Would you rather live with no internet or no A/C or heating?",
        "If someone offered you $1 million dollars to break up with your partner, would you do it?",
        "If you were reborn, what decade would you want to be born in?",
        "If you could go back in time in erase one thing you said or did, what would it be?",
        "Has your partner ever embarrassed you?",
        "Have you ever thought about cheating on your partner?",
        "If you could suddenly become invisible, what would you do?",
        "Have you ever been caught checking someone out?",
        "Have you ever waved at someone thinking they saw you when really they didn't? What did you do when you realized it?",
        "What's the longest time you've stayed in the bathroom, and why did you stay for that long?",
        "What's the most unflattering school picture of you?",
        "Have you ever cried because you missed your parents so much?",
        "Describe the strangest dream you've ever had. Did you like it?",
        "Have you ever posted something on social media that you regret?",
        "What is your biggest fear?",
        "Do you pee in the shower?",
        "Have you ever ding dong ditched someone?",
        "The world ends next week and you can do anything you want. What would you do?",
        "Would you wear your shirt inside out for a whole day if someone paid you $100?",
        "What is the most childish thing that you still do?",
        "How far would you go to land the guy or girl of your dreams?",
        "Tell us about a time you embarrassed yourself in front of a crush.",
        "Have you ever kept a library book?",
        "Who is one person you pretend to like, but actually don’t?",
        "What children’s movie could you watch over and over again?",
        "Do you have bad foot odor?",
        "Do you have any silly nicknames?",
        "When was the last time you wet the bed?",
        "How many pancakes have you eaten in a single sitting?",
        "Have you ever accidentally hit something with your car?",
        "If you had to make out with any Disney character, who would it be?",
        "Have you ever watched a movie you knew you shouldn’t?",
        "Have you ever wanted to try LARP (Live Action Role-Play)?",
        "What app on your phone do you waste the most time on?",
        "Have you ever pretended to be sick to get out of something? If so, what was it?",
        "What is the most food you’ve eaten in a single sitting?",
        "Do you dance when you’re by yourself?",
        "Would you have voted for or against Trump?",
        "What song on the radio do you sing with every time it comes on?",
        "Do you own a pair of footie pajamas?",
        "Are you scared of the dark?",
        "What ‘As seen on TV’ product do you secretly want to buy?",
        "Do you still take bubble baths?",
        "If you were home by yourself all day, what would you do?",
        "How many selfies do you take a day?",
        "What is something you’ve done to try to be ‘cooler’?",
        "When was the last time you brushed your teeth?",
        "Have you ever used self tanner?",
        "What does your favorite pajamas look like?",
        "Do you have a security blanket?",
        "Have you ever eaten something off the floor?",
        "Have you ever butt-dialed someone?",
        "Do you like hanging out with your parents?",
        "Have you ever got caught doing something you shouldn’t?",
        "What part of your body do you love and which part do you hate?",
        "Have you ever had lice?",
        "Have you ever pooped your pants?",
        "What was the last rate-R movie you watched?",
        "Do you lick your plate?",
        "What is something that no one else knows about you?",
        "Do you write in a diary?",
        "Who would you hate to see naked?",
        "How long have you gone without a shower?",
        "If you could only text one person for the rest of your life, but you could never talk to that person face to face, "
        "who would that be?",
        "How long have you gone without brushing your teeth?",
        "What's one thing you would never eat on a first date?",
        "What have you seen that you wish you could unsee?",
        "If you could be reincarnated into anyone's body, who would you want to become?",
        "If you switched genders for the day, what would you do?",
        "What's one food that you will never order at a restaurant?",
        "What's the worst weather to be stuck outside in if all you could wear was a bathing suit?",
        "If your car broke down in the middle of the road, who in this room would be the last person you would call? Why?",
        "What's the most useless piece of knowledge you know?",
        "What did you learn in school that you wish you could forget?",
        "Is it better to use shampoo as soap or soap as shampoo?",
        "If you ran out of toilet paper, would you consider wiping with the empty roll?",
        "What would be the worst part about getting pantsed in front of your crush?",
        "If you could only use one swear word for the rest of your life, which one would you choose?",
        "What's the best thing to say to your friend that would be the worst thing to say to your crush?",
        "Who do you think is the Beyonce of the group?",
        "Would you rather eat dog food or cat food?",
        "If you had nine lives, what would you do that you wouldn't do now?",
        "If you could play a prank on anyone without getting caught, who would you play it on?",
        "Have you ever pretended to like a gift? How did you pretend?",
        "Would you rather not shower for a month, or eat the same meal everyday for a month?",
        "What animal most closely resembles your eating style?",
        "If you could choose to never sweat for the rest of your life or never have to use the bathroom, which would you choose?",
        "If you could spend every waking moment with your partner, would you?",
        "What's your biggest pet peeve?",
        "If you could date anyone in the world, who would you date?",
        "Would you rather be skinny and hairy or fat and smooth?",
        "Who would you ask to prom if you could choose anyone?",
        "Describe your perfect date.",
        "Would you ever date two people at once if you could get away with it?",
        "You have to delete every app on your except for five. Name the five you would keep.",
        "Have you ever sent out a nude?",
        "Have you ever received a nude? Who was it from?",
        "What was your reaction? Like or dislike?",
        "Have you ever gotten mad at a friend for posting an unflattering picture of you?",
        "Have you ever had a crush on a teacher?",
        "Who do you think would make the best kisser? (List a few people for them to choose.)",
        "Have you ever sent someone the wrong text?",
        "Have you ever cursed at your parents? Why?",
        "Who do you think is the cutest person in our class?",
        "What is the most attractive feature on a person?",
        "What the biggest deal breaker for you?",
        "How far would you go on a first date?",
        "Have you ever regretted something you did to get a crush's attention?",
        "Would you ever be mean to someone if it meant you could save your close friend from embarrassment?",
        "Of the people at our school, who do you think would make the best president?",
        "If we didn't have a dress code, what would you wear to school that you can't wear now?",
        "Describe what makes someone husband or wife material.",
        "If you could make $1 million, would you drop out of school?",
        "What's one thing you do that you don't want anyone to know about?",
        "Do you frequently stalk anyone on social media? Who?",
        "Who do you want to make out with the most?",
        "If you had to flash just one person in this room, who would it be?",
        "If you haven't had your first kiss yet, who in this room do you want to have your first kiss with?",
        "Of the people in this room, who would you go out with?",
        "Describe the most attractive thing about each person in this room.",
        "Who here do you think is the best flirt?",
        "Who has the best smile?",
        "Who has the cutest nose?",
        "How about prettiest eyes?",
        "Who's the funniest in this room?",
        "What's one thing you would never do in front of someone you had a crush on?",
        "How often do you check yourself out in the mirror when you're on a date?",
        "Who here do you think would be the best kisser?",
        "Who has the best dance moves?",
        "If you could have one physical feature of someone in this room, what would that be?",
        "What is your wildest fantasy?",
        "How far would you go with someone you just met and will never see again?",
        "Rate me on a scale of 1 to 10, with 10 being the hottest.",
        "If I was a food, what would I be, and how would you eat me?",
        "Would you choose a wild, hot relationship or a calm and stable one?",
        "If you had one week to live and you had to marry someone in this room, who would it be?",
        "If you only had 24 hours to live and you could do anything with anyone in this room, who would it be and what would "
        "you do with that person?",
        "What's your biggest turn-on?",
        "And biggest turn-off?",
        "Would you go out with me if I was the last person on earth?",
        "What's the most flirtatious thing you've ever done?",
        "What's the sexiest thing about [fill in the name of a person in the room]?",
        "If you could go on a romantic date with anyone in this room, who would you pick?",
        "If you had to delete one app from your phone, what would it be?",
        "What is your greatest fear in a relationship?",
        "Say one positive and one negative thing about each person here.",
        "What is one disturbing fact I should know about you?",
        "Have you ever smoked?",
        "Have you ever tried drugs?",
        "What about alcohol?",
        "What's the craziest thing you've done while under the influence?",
        "If you were trapped for three days on an island, who are three people in this room you would bring with you and why?",
        "Would you go to a nude beach?",
        "Who's the most annoying person in this room?",
        "If you had to marry someone in this room, who would it be?",
        "Do you have hidden piercings or tattoos?",
        "How long was your longest relationship?",
        "If you could have one celebrity follow you on Instagram, who would that be?",
        "You have to delete 5 people on Instagram. Name them.",
        "Do you want to get married one day?",
        "Do you want to have kids? How many?",
        "Would you ever get into a long distance relationship?",
        "Describe the person of your dreams.",
        "What would you do if you found out you flunked school?",
        "If your partner broke up with you at school, what would you do?",
        "If you had the power to fire one teacher, who would it be?",
        "Basketball, baseball, or football?",
        "What was your first job?",
        "If you don't have one yet, where would you want to work?",
        "How many hours would you spend online if you didn't have school or homework?",
        "How tall do you want to be?",
        "What's your biggest fear about college?",
        "What are you most excited about?",
        "Would you want your best friend to go to the same college as you?",
        "Would you want your current partner to go to the same college as you?",
        "Who do you think is the hottest celebrity?",
        "What's you dream job?",
        "What was a rumor that went around about you?",
        "Have you ever failed a class?",
        "If you had the power to fire one teacher, who would that be?",
        "If you could plan a class prank knowing you'll never get caught, what would the prank be?",
        "Have you ever cheated on a test?",
        "Have you ever had a crush on a teacher? Who?",
        "Who would you take to prom?",
        "Have you ever made out at school?",
        "Who would you never ever want to sit next to in class?",
        "Have you ever been late to class?",
        "What's the most embarrassing thing you've ever done in front of a teacher?",
        "Have you ever stuck gum under a desk?",
        "What do you think is better: tests or essays?",
        "Have you ever eaten lunch by yourself? Why?",
        "If you had to take one class for the rest of your life, what class would it be and who would the teacher be?",
        "If you wanted to make out on campus, where would you do it?",
        "Have you ever gotten into a fight on school grounds?",
        "What was the worst score you’ve ever gotten on a test?",
        "Have you ever fallen asleep in class?",
        "Have you ever gotten detention or been suspended?",
        "If you were invisible, would you sneak a peak in the other locker room?",
        "If so, who would you be hoping to see?",
        "Who's the hottest teacher at our school?",
        "What's the worst class to have first period?",
        "If you had to take a person from another grade to prom, who would that be?",
        "Have you ever flashed someone?",
        "Have you ever sexted anyone?",
        "Have you ever been to a nudist beach? Would you consider going?",
        "Would you ever consider posing for Playboy?",
        "Who has seen you without clothes on?",
        "Have you ever seen a naughty magazine?",
        "Have you ever sent a nude selfie? Who would you send it to?",
        "Have you ever searched for something dirty on the internet?",
        "Who do you most want to sleep with, out of everyone here?",
        "What's your favorite body part on your partner?",
        "How many people have you kissed?",
        "Have you ever been attracted to the same sex?",
        "When and where was your first kiss? Who was it with?",
        "When did you lose your virginity and who did you lose it with?",
        "What's your ultimate sexual fantasy?",
        "Would you go out with an older guy? How old is too old?",
        "Do you sleep in the nude?",
        "How much money would we have to pay you for you to agree to flash your boobs?",
        "Have you ever been in a friends with benefits situation?",
        "If you had to go skinny dipping with someone, who in this room would you choose?",
        "If I paid you $100, would you wear your sexiest clothes to class?",
    ],
    "dares": [
        "Set your crush's profile picture as your profile picture.",
        "Flirt with {name} poorly in text and send screenshots of it to you.",
        "Send a screenshot of your search history of last 2 days.",
        "Send the most recent photo of your gallery.",
        "Send your ugliest selfie.",
        "Text flirt and then send “I love you” to a someone already in a relationship (not married) and screenshot his/her reaction",
        "Send a romantic message to someone of your own gender and screenshot their response",
        "Send a video of you dancing.",
        "Call me and sing a song for me.",
        "Send a voice message saying that you love me in 3 romantic ways.",
        "Send me a pic of you wearing the least clothes on you.",
        "Be my one day boyfriend or girlfriend.",
        "Write your and my name in your status for 1 day.",
        "Propose to me in the most sensual way possible.",
        "Send love letter through email to your class teacher.",
        "Select one mobile number blindfolded from your contacts and send one breakup message to him/her. Screenshot the response.",
        "Give a deep explanation of one item in front of you.",
        "Paint your fingernails blindfolded with a pencil. Show us the result.",
        "Do a prank call to your mother and tell “I’m expecting a baby soon”. Screenshot the response.",
        "Send me the last message you received from your crush.",
        "Make a voice call to me and sing rhymes.",
        "Make a video call to me and perform belly dance.",
        "Open your gallery, close your eyes, scroll randomly and select one picture and send it to me.",
        "Send a text message to your crush blindfolded.",
        "Put my picture as your mobile wallpaper for three days.",
        "Send a selfie of yours while keeping your finger in your nose.",
        "Call to any random number and do non-stop conversation for 2 minutes.",
        "Send me the message of your first message that sends to me.",
        "Make a video call to me and do 20 situps continuously.",
        "Send next five text messages to your friends using your elbow only.",
        "Wear your dress upside down and send that picture to me.",
        "Send any message using only emojis.",
        "Call someone and say nothing.",
        "Send a message to your crush saying I’ve lost my condoms in your home please find them.",
        "Send five photo from your gallery.",
        "I’ll give you a person's contact information and send a romantic message to that person.",
    ],
}

import random
import datetime
import time
import json


class Variables:
    game_names = ["uno", "chess"]

    DEADLINE = 1200
    TIMEOUT = 360

    eng_dict = None
    randwords = list()

    history = list()

    games_names_short = ["uno", "chess"]

    colors_uno = {"Blue": "🟦", "Green": "🟩", "Red": "🟥", "Yellow": "🟨"}
    white = {"White": "⬜"}

    SPLIT_EMOJI = "↔️"
    INC_EMOJI1 = "⬆️"
    INC_EMOJI2 = "⏫"
    STOP_EMOJI = "❌"
    BACK_EMOJI = "◀"
    FORWARD_EMOJI = "▶️"
    REPEAT_EMOJI = "🔁"
    NEXT_EMOJI = "➡️"

    DICT_ALFABET = {
        'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩', 'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭',
        'i': '🇮', 'j': '🇯',
        'k': '🇰', 'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵', 'q': '🇶', 'r': '🇷',
        's': '🇸', 't': '🇹',
        'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽', 'y': '🇾', 'z': '🇿'
    }  # letter: emoji

    NUMBERS = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    REACTIONS_CONNECT4 = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]

    GWRULES = f"""
        Guess the word from the given definition.\n
        Press the indicated reactions on the message to make your move.\n
        Press {STOP_EMOJI} to close the game.\n
    """

    SCRULES = f"""
        Try to unscramble the letters that the bot scrambled.\n
        Press the indicated reactions on the message to make your move.\n
        Press {STOP_EMOJI} to close the game.\n
    """

    QZRULES = f"""
        Try to give the correct answer to the questions.\n
        Questions are always multiple choice and have 4 possible answers.\n
        Only one answer is the correct one.\n
        There are different categories available.\n
        You can get a new question after answering the previous one with {NEXT_EMOJI}.\n
        Press the indicated reactions on the message to make your move.\n
        Press {STOP_EMOJI} to close the game.\n
    """

    UNORULES = f"""
        Every message you type in the bot DM will be visible to other players in the "CHAT" message.\n
        Only the person who's turn it is can play.\n
        Playable cards are marked with an emoji.\n
        Match cards by color or value.\n
        Wild cards and Wild Draw 4 cards can be played without matching color or value.\n
        Press {STOP_EMOJI} to draw a card.\n
        If you need to draw multiple cards, use {INC_EMOJI2} to take cards.\n
        After drawn a card, use {NEXT_EMOJI} to end turn.\n
        When you have on card remaining type "uno" in chat.
        Players can type "no uno" in chat to catch someone not saying uno.\n
        The rest of the rules are according to the official Uno rules.\n
    """

    CHESSRULES = "Start a game of chess with 2 players, one game per channel allowed."


def on_startup():
    json1_file = open('bot/assets/dictionary.json')
    json1_str = json1_file.read()
    Variables.eng_dict = json.loads(json1_str)
    json1_file.close()


def get_next_midnight_stamp():
    datenow = datetime.date.today() + datetime.timedelta(days=1)
    unix_next = datetime.datetime(datenow.year, datenow.month, datenow.day, 0)
    unixtime = time.mktime(unix_next.timetuple())
    return unixtime
