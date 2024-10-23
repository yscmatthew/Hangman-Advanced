# Hangman-Advanced
Introduction
Design a word game for vocabulary learning for S1 to S5 students

Users:

During the secondary school education, we would come along with different words in different levels  that we have to learn in order to ace the exams. However, secondary school students often find it difficult and hard to memorize the words in a traditional format. They also have to face the studying stress, so they would be discouraged easily to just memorize the words. Therefore, I come up with the Hangman Advanced Game so as to encourage the students to learn and study and spell the words in a fun and interesting way.

Hangman Advanced is a Python-based word-guessing game built upon the traditional Hangman rules, but with several enhancements. The game incorporates multiple features such as user accounts, score management, streak tracking, word hints, customizable word banks, and more. As such, fabulous and fresh things the students discover while they are playing the game.
Purpose:
The purpose of the game is to make learning new words less of a chore and more of a fun experience. Instead of simply memorizing lists of vocabulary, students get to engage with the words in an interactive way. With the added features like streaks, scores, and hints, the game keeps students motivated and encourages them to improve their spelling and word recognition skills. Plus, being able to customize the word bank means the game can be tailored to different learning levels, ensuring that it's always challenging but not overwhelming. It's all about turning the stress of studying into a playful competition for S1 to S5 students!




Design
Refined details beyond the main game:

Login and Account System:
A login and account system is implemented so as to provide each user (maximum 5) to have their own game progress recorded, like the score, the maximum streak, etc, for each player.
The accounts are stored in the database. This can encourage players to compete with their friends and see each other’s progress for fun.


Custom Encryption Algorithm to Safeguard the Accounts:
An unique encryption and decryption algorithm is integrated in the system. The algorithm , called Erika EncDec, is responsible for the security of the accounts. In partic, during the registration process, the algorithm, encABC.py would use the user’s password to encrypt a particular string, “ABCdef”, and stores it to the database (e.g. “ABCdef” => “7@0cnM” with a password of “qwertyui”). During the login process, the algorithm, decABC.py uses player’s password to decrypt the encrypted string from the database. If the password is incorrect, the string will be failed to decrypted to “ABCdef”, thus denying the login attempt. If a player tries jangling a password on a specific account (someone who is not the account owner attempts to try many passwords to login), the system can detect it and prevent him from logging in. Thus, the system will block any log-in attempts for 5 minutes.

The crux of the matter is that, even though a hacker opens the database from the game files, he is still unable to retrieve any password but an encrypted meaningless string. This further protects all players, especially if their password in game is The same with their accounts on other platforms.


Streak Mode:
The streak mode in Hangman Advanced is a great way to keep players hooked. Each time a player guesses a word correctly without losing all their lives, their streak goes up, which gives them a sense of achievement. The longer the streak, the more rewarding it feels, as players aim to beat their own records. The game enhances this experience with positive feedback and leaderboard rankings to compete with pals, encouraging a sense of accomplishment and friendly competition.

Wordbank customization (add,edit,delete,view):
The Hangman Advanced game boasts an exceptional word bank customization feature accessible directly from the game menu, giving players unparalleled control over their gameplay experience. Players can effortlessly add new words, edit existing ones, or delete any words they choose, creating a highly personalized vocabulary list. This comprehensive functionality doesn't stop at just the words; users can also add or modify the corresponding tips and adjust the level of difficulty for each word, tailoring the game to their specific needs or preferences. Every user-created word is tagged accordingly, allowing for easy filtering and differentiation from the pre-installed words. This is especially valuable in educational settings—secondary school teachers, for example, can input vocabulary that aligns with their current curriculum, making the game an effective learning tool for students at various levels. The ability to customize content ensures the game remains accessible and challenging for a wide range of players in a school environment. Moreover, the option to filter out user-created words is particularly helpful for players who wish to focus solely on syllabus-specific vocabulary, avoiding words that might be irrelevant or outside their course of study. This level of customization ensures that the game remains both engaging and educational, catering to the diverse needs of its users.

Multi-user Support:
 Multiple user profiles (up to 5 slots)
Login via typing the account code first, than the password

Players’ Progress Stored:
 Individual game progress and statistics for each user, including the highest score in a game, the total score in all the games he played, and the highest streak. Progresses are stored even after the game is closed.


Selectable Range for the Level of Difficulty:
The selectable range for difficulty levels in Hangman Advanced lets players tailor the game to match their skill level or learning objectives. With levels from 1 to 5, players can decide how challenging they want their word-guessing experience to be. This feature is great because it allows players to gradually increase the difficulty as they get better, making the game accessible to junior form students while still providing a challenge for senior form players. In particular, S3 students can not only select a word list of level 3, which is the words they are currently learning at school, they can also select level 1-2 to revise what they learnt in previous form, as well as challenge themselves by selecting level 4-5, which is generally for senior form students.

Moreover, the selectable difficulty makes the game more dynamic and replayable, allowing players to try different word categories and gradually tackle tougher challenges. This keeps the game engaging and ensures it remains a valuable learning tool over time.

Unique & unplayed words every time:
As the game mechanics record whether the word has been played by the user before, every time the user plays, the word selector nomination finds the word he never tried before, so as to enhance fun and make sure the player can learn a new word every time.



Leaderboard:
The Leaderboard feature in Hangman Advanced acts as a driving force by inspiring competition and a sense of achievement among players. It offers a detailed ranking system that keeps track of each player's highest score, total score, and longest streak, providing a clear view of their progress and successes. Players can compare themselves to others, which motivates them to enhance their performance and either maintain or rise in the leaderboard standings. This feature is especially appealing because it adds a social and competitive layer to the game, making the learning process more engaging.

Furthermore, the leaderboard establishes a persistent record of achievements, giving players pride in what they've accomplished. It also sets a tangible goal beyond just winning individual rounds, as players aim for a top spot. For those who enjoy pushing their limits, the leaderboard serves as a constant incentive to play more and improve, making the game more addictive and fulfilling. Additionally, the option to reset the leaderboard keeps the competition lively, allowing players to start fresh and compete anew.


