#Hangman Advanced
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hangman Advanced - Design Overview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2e6da4;
        }
        h1 {
            text-align: center;
        }
        h2 {
            margin-top: 30px;
            border-bottom: 2px solid #2e6da4;
            padding-bottom: 5px;
        }
        h3 {
            margin-top: 20px;
        }
        p {
            margin: 10px 0;
        }
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
    </style>
</head>
<body>

    <h1>Hangman Advanced - Design Overview</h1>

    <h2>Introduction</h2>
    <p><strong>Design a word game for vocabulary learning for S1 to S5 students</strong></p>

    <h3>Users:</h3>
    <p>During secondary school education, students encounter words at different levels that they need to master for exams. However, traditional memorization methods can be difficult and stressful, leading to discouragement. To address this, the Hangman Advanced Game was created to make learning spelling more enjoyable and interactive.</p>
    <p>Hangman Advanced is a Python-based word-guessing game built on traditional Hangman rules, but with several enhancements. The game includes user accounts, score management, streak tracking, word hints, customizable word banks, and more, making learning fresh and engaging for students.</p>

    <h3>Purpose:</h3>
    <p>The purpose of the game is to make learning new words enjoyable rather than burdensome. Instead of rote memorization, students engage with words in an interactive format. Features like streaks, scores, and hints keep students motivated and encourage them to improve their spelling and word recognition skills. The ability to customize the word bank to different learning levels ensures the game is challenging but not overwhelming, turning studying into a playful competition for S1 to S5 students!</p>

    <h2>Design</h2>
    <h3>Refined details beyond the main game:</h3>

    <h3>Login and Account System:</h3>
    <p>A login and account system allows up to 5 users to save their game progress, including scores and streaks. Accounts are stored securely in a database, which fosters friendly competition among players as they track each other's progress.</p>

    <h3>Custom Encryption Algorithm to Safeguard the Accounts:</h3>
    <p>An exclusive encryption and decryption algorithm, Erika EncDec, is used to protect users' accounts. During registration, the algorithm encrypts a specific string using the player's password and stores it in the database. During login, the algorithm decrypts the stored string and verifies the password. If the wrong password is entered, access is denied. Additionally, the system prevents brute-force attempts by blocking logins for 5 minutes after multiple failed attempts. Even if a hacker gains access to the database, the encrypted passwords remain meaningless and secure, providing robust protection for users.</p>

    <h3>Streak Mode:</h3>
    <p>The streak mode in Hangman Advanced keeps players hooked by increasing their streak count every time they guess a word without losing all their lives. The longer the streak, the more rewarding it feels, pushing players to beat their own records. Positive feedback and leaderboard rankings enhance the experience, encouraging friendly competition and a sense of achievement.</p>

    <h3>Wordbank Customization (Add, Edit, Delete, View):</h3>
    <p>The game offers robust word bank customization, allowing players to add, edit, or delete words. Players can also modify tips and difficulty levels for each word, tailoring the game to their preferences. Teachers can input vocabulary aligned with their curriculum, ensuring the game remains a valuable learning tool. Custom words are tagged, making it easy to filter them out if needed, especially for students who want to focus on syllabus-specific vocabulary. This customization ensures the game is both educational and engaging for a wide range of players.</p>

    <h3>Multi-user Support:</h3>
    <ul>
        <li>Supports up to 5 user profiles</li>
        <li>Login by typing the account code followed by the password</li>
    </ul>

    <h3>Players’ Progress Stored:</h3>
    <p>Each user's game progress, including highest score, total score, and longest streak, is stored individually. This ensures that progress is saved even after the game is closed, allowing players to pick up where they left off.</p>

    <h3>Selectable Range for the Level of Difficulty:</h3>
    <p>The game allows players to select a difficulty level between 1 and 5, making it accessible to students of various skill levels. For example, S3 students can practice words from their current syllabus (level 3) or review easier words (levels 1-2) while challenging themselves with harder words (levels 4-5). This dynamic feature keeps the game engaging and ensures continuous learning as players progress.</p>

    <h3>Unique & Unplayed Words Every Time:</h3>
    <p>The game tracks which words a player has already encountered and ensures that each new game presents a word the player has not yet guessed, keeping the experience fresh and educational.</p>

    <h3>Leaderboard:</h3>
    <p>The leaderboard adds a competitive element to the game by tracking each player's highest score, total score, and longest streak. Players can compare their progress to others, which motivates them to improve and climb the leaderboard. The leaderboard provides a persistent record of achievements and can be reset, allowing players to start fresh and compete anew, keeping the game lively and engaging.</p>

</body>
</html>
