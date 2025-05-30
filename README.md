<h1 align="center">🎮 Tic-Tac-Toe (Python CLI)</h1>

<p align="center">
  A simple, interactive, command-line Tic-Tac-Toe game built in Python for two players.
</p>

---

## 🧠 Features

- Two-player turn-based gameplay  
- Smart input validation  
- Win/tie detection  
- Modular code with function imports  

---

## 📂 Project Structure

<pre>
📦 <b>tic-tac-toe-python</b>
├── <a href="Main.py">Main.py</a>            # Main game loop and player input
├── <a href="Functions.py">Functions.py</a>       # Win-check and board display
└── <a href="README.md">README.md</a>          # Project documentation
</pre>

---

## 🚀 Installation & Usage

<div align="center">
  <img src="https://img.shields.io/badge/python-3.6+-blue?logo=python&logoColor=white" alt="Python version">
  <img src="https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macOS-lightgrey" alt="Platforms">
</div>

### Requirements
- Python 3.6 or higher
- No additional dependencies
```bash
# Clone the repository
git clone https://github.com/your-username/tic-tac-toe-python.git

# Navigate to project directory
cd tic-tac-toe-python

# Run the game
python Main.py

```
---

## 🎮 How to Play
```
Players take turns entering numbers 1-9 corresponding to board positions:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
Player 1 is X, Player 2 is O

First to get 3 marks in a row (horizontal/vertical/diagonal) wins!

```
---
## 🛠️ Key Features
<table border="1" style="width:100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th>Feature</th>
            <th>Implementation</th>
            <th>File</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Turn Management</td>
            <td>player_number % 2 alternates between 0 (X) and 1 (O)</td>
            <td>Main.py</td>
        </tr>
        <tr>
            <td>Input Validation</td>
            <td>Checks for integers 1-9 and empty cells</td>
            <td>Main.py</td>
        </tr>
        <tr>
            <td>Board Display</td>
            <td>Dynamic ASCII rendering with list_Display()</td>
            <td>Functions.py</td>
        </tr>
        <tr>
            <td>Win Detection</td>
            <td>8-combination check including diagonals</td>
            <td>Functions.py</td>
        </tr>
        <tr>
            <td>Draw Detection</td>
            <td>player_number == 9 condition</td>
            <td>Main.py</td>
        </tr>
    </tbody>
</table>

---

## 📊 Board Mapping Logic
```
Input to Grid Conversion:
1(0,0) | 2(0,1) | 3(0,2)
-------|--------|-------
4(1,0) | 5(1,1) | 6(1,2)
-------|--------|-------
7(2,0) | 8(2,1) | 9(2,2)

Calculation:
row = (move-1) // 3 
col = (move-1) % 3
```
--- 

## 🔮 Future Improvements

### 🧠 AI Opponent
- Implement minimax algorithm for unbeatable AI
- Add difficulty settings (Easy/Medium/Hard)
  
### ⚙️ Advanced Features
- Game history tracking
- Player statistics and win ratios
- Tournament mode with multiple rounds

--- 

## 🤝 Contributing

<div align="center">
  <a href="https://github.com/your-username/tic-tac-toe-python/fork">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome">
  </a>
</div>

<ol>
  <li><b>Fork</b> the project</li>
  <li><b>Create</b> your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li><b>Commit</b> your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li><b>Push</b> to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
  <li><b>Open</b> a Pull Request</li>
</ol>

--- 

## 📜 License

<div align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License">
  </a>
</div>

<p align="center">
  Distributed under the MIT License. See <a href="LICENSE">LICENSE</a> for more information.
</p>
