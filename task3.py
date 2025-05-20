                                                                 TASK-3
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Tic Tac Toe</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f0f0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      flex-direction: column;
    }

    h1 {
      margin-bottom: 20px;
    }

    .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-template-rows: repeat(3, 100px);
      gap: 5px;
    }

    .cell {
      width: 100px;
      height: 100px;
      background: white;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 2.5rem;
      cursor: pointer;
      border-radius: 10px;
      box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }

    .cell:hover {
      background: #f9f9f9;
    }

    .status {
      margin: 20px;
      font-size: 1.2rem;
      min-height: 1.5rem;
    }

    .reset-btn {
      padding: 10px 20px;
      font-size: 1rem;
      border: none;
      background: #007bff;
      color: white;
      border-radius: 8px;
      cursor: pointer;
    }

    .reset-btn:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>

  <h1>Tic-Tac-Toe</h1>
  <div class="status" id="status">Player X's Turn</div>
  <div class="board" id="board"></div>
  <button class="reset-btn" onclick="resetGame()">Reset</button>

  <script>
    const boardElement = document.getElementById('board');
    const statusElement = document.getElementById('status');

    let board = ["", "", "", "", "", "", "", "", ""];
    let currentPlayer = "X";
    let gameOver = false;

    const winningCombos = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
      [0, 4, 8], [2, 4, 6]             // Diagonals
    ];

    function createBoard() {
      boardElement.innerHTML = '';
      board.forEach((cell, i) => {
        const cellDiv = document.createElement('div');
        cellDiv.classList.add('cell');
        cellDiv.dataset.index = i;
        cellDiv.textContent = cell;
        cellDiv.addEventListener('click', handleClick);
        boardElement.appendChild(cellDiv);
      });
    }

    function handleClick(e) {
      const index = e.target.dataset.index;
      if (board[index] !== "" || gameOver) return;

      board[index] = currentPlayer;
      e.target.textContent = currentPlayer;

      if (checkWin(currentPlayer)) {
        statusElement.textContent = `🎉 Player ${currentPlayer} Wins!`;
        gameOver = true;
      } else if (board.every(cell => cell !== "")) {
        statusElement.textContent = "It's a Draw!";
        gameOver = true;
      } else {
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        statusElement.textContent = `Player ${currentPlayer}'s Turn`;
      }
    }

    function checkWin(player) {
      return winningCombos.some(combo => {
        return combo.every(index => board[index] === player);
      });
    }

    function resetGame() {
      board = ["", "", "", "", "", "", "", "", ""];
      currentPlayer = "X";
      gameOver = false;
      statusElement.textContent = `Player ${currentPlayer}'s Turn`;
      createBoard();
    }

    // Initialize
    createBoard();
  </script>

</body>
</html>
                                                                            TASK-3[Alternative]
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Quiz Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f2f2f2;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
    }

    .quiz-container {
      background: white;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      max-width: 500px;
      width: 100%;
    }

    .question {
      font-size: 1.2rem;
      margin-bottom: 1rem;
    }

    .options {
      display: flex;
      flex-direction: column;
    }

    .option {
      background: #e7e7e7;
      border: none;
      padding: 0.8rem;
      margin: 0.3rem 0;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.3s;
    }

    .option:hover {
      background: #d3d3d3;
    }

    .result {
      font-size: 1.3rem;
      margin-top: 2rem;
    }

    .next-btn {
      margin-top: 1rem;
      padding: 0.8rem 1.5rem;
      font-size: 1rem;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }

    .next-btn:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>

  <div class="quiz-container" id="quiz">
    <div class="question" id="question">Loading...</div>
    <div class="options" id="options"></div>
    <button class="next-btn" onclick="nextQuestion()">Next</button>
    <div class="result" id="result"></div>
  </div>

  <script>
    const quizData = [
      {
        question: "What is the capital of France?",
        type: "single",
        options: ["Paris", "Madrid", "Rome", "Berlin"],
        answer: "Paris"
      },
      {
        question: "Which language runs in a web browser?",
        type: "single",
        options: ["Python", "Java", "C", "JavaScript"],
        answer: "JavaScript"
      },
      {
        question: "Fill in the blank: The sun ____ in the east.",
        type: "fill",
        answer: "rises"
      },
      {
        question: "Select the prime numbers:",
        type: "multi",
        options: ["2", "3", "4", "6"],
        answer: ["2", "3"]
      }
    ];

    let currentQuestion = 0;
    let score = 0;
    let userAnswer = [];

    const questionEl = document.getElementById("question");
    const optionsEl = document.getElementById("options");
    const resultEl = document.getElementById("result");

    function loadQuestion() {
      resultEl.textContent = '';
      const current = quizData[currentQuestion];
      questionEl.textContent = current.question;
      optionsEl.innerHTML = '';

      if (current.type === "single") {
        current.options.forEach(option => {
          const btn = document.createElement("button");
          btn.classList.add("option");
          btn.textContent = option;
          btn.onclick = () => {
            userAnswer = option;
            validateAnswer();
          };
          optionsEl.appendChild(btn);
        });
      }

      else if (current.type === "multi") {
        userAnswer = [];
        current.options.forEach(option => {
          const btn = document.createElement("button");
          btn.classList.add("option");
          btn.textContent = option;
          btn.onclick = () => {
            btn.classList.toggle("selected");
            if (userAnswer.includes(option)) {
              userAnswer = userAnswer.filter(item => item !== option);
            } else {
              userAnswer.push(option);
            }
          };
          optionsEl.appendChild(btn);
        });
      }

      else if (current.type === "fill") {
        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = "Type your answer";
        input.style.padding = "0.5rem";
        input.style.width = "100%";
        input.style.borderRadius = "6px";
        optionsEl.appendChild(input);

        const submitBtn = document.createElement("button");
        submitBtn.textContent = "Submit";
        submitBtn.classList.add("next-btn");
        submitBtn.onclick = () => {
          userAnswer = input.value.trim().toLowerCase();
          validateAnswer();
        };
        optionsEl.appendChild(submitBtn);
      }
    }

    function validateAnswer() {
      const current = quizData[currentQuestion];
      if (current.type === "single" && userAnswer === current.answer) {
        score++;
      }

      if (current.type === "multi") {
        const correct = current.answer.sort().join(",");
        const selected = userAnswer.sort().join(",");
        if (correct === selected) {
          score++;
        }
      }

      if (current.type === "fill") {
        if (userAnswer === current.answer.toLowerCase()) {
          score++;
        }
      }

      document.querySelectorAll(".option").forEach(btn => btn.disabled = true);
      resultEl.textContent = `Score: ${score}/${quizData.length}`;
    }

    function nextQuestion() {
      currentQuestion++;
      if (currentQuestion < quizData.length) {
        loadQuestion();
      } else {
        questionEl.textContent = "Quiz Completed!";
        optionsEl.innerHTML = "";
        resultEl.textContent = `Final Score: ${score}/${quizData.length}`;
        document.querySelector(".next-btn").style.display = "none";
      }
    }

    loadQuestion();
  </script>

</body>
</html>
