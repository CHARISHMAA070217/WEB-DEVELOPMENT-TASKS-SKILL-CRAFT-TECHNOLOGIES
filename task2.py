                                                            TASK-2
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Stopwatch App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      height: 100vh;
      margin: 0;
    }

    .stopwatch {
      background: #fff;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    .time-display {
      font-size: 3rem;
      margin-bottom: 1rem;
    }

    .controls button {
      padding: 10px 20px;
      margin: 0 5px;
      font-size: 1rem;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.3s ease;
    }

    .start { background: #28a745; color: white; }
    .pause { background: #ffc107; color: white; }
    .reset { background: #dc3545; color: white; }
    .lap { background: #007bff; color: white; }

    .controls button:hover {
      opacity: 0.9;
    }

    .laps {
      margin-top: 1rem;
      max-height: 150px;
      overflow-y: auto;
      text-align: left;
    }

    .lap-item {
      background: #eee;
      margin: 5px 0;
      padding: 5px 10px;
      border-radius: 6px;
    }
  </style>
</head>
<body>

  <div class="stopwatch">
    <div class="time-display" id="display">00:00:00.00</div>
    <div class="controls">
      <button class="start" onclick="start()">Start</button>
      <button class="pause" onclick="pause()">Pause</button>
      <button class="reset" onclick="reset()">Reset</button>
      <button class="lap" onclick="lap()">Lap</button>
    </div>
    <div class="laps" id="laps"></div>
  </div>

  <script>
    let startTime = 0;
    let elapsed = 0;
    let interval;
    let running = false;

    function formatTime(ms) {
      const date = new Date(ms);
      const min = String(date.getUTCMinutes()).padStart(2, '0');
      const sec = String(date.getUTCSeconds()).padStart(2, '0');
      const centis = String(Math.floor(date.getUTCMilliseconds() / 10)).padStart(2, '0');
      return `${min}:${sec}:${centis}`;
    }

    function updateDisplay() {
      const display = document.getElementById('display');
      const now = Date.now();
      const time = running ? now - startTime + elapsed : elapsed;
      display.textContent = formatTime(time);
    }

    function start() {
      if (!running) {
        startTime = Date.now();
        interval = setInterval(updateDisplay, 10);
        running = true;
      }
    }

    function pause() {
      if (running) {
        elapsed += Date.now() - startTime;
        clearInterval(interval);
        running = false;
      }
    }

    function reset() {
      clearInterval(interval);
      startTime = 0;
      elapsed = 0;
      running = false;
      document.getElementById('display').textContent = '00:00:00.00';
      document.getElementById('laps').innerHTML = '';
    }

    function lap() {
      if (running) {
        const laps = document.getElementById('laps');
        const now = Date.now();
        const time = now - startTime + elapsed;
        const lapItem = document.createElement('div');
        lapItem.className = 'lap-item';
        lapItem.textContent = `Lap: ${formatTime(time)}`;
        laps.prepend(lapItem);
      }
    }
  </script>

</body>
</html>

                                                                   Task-2[Alternative]
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Calculator</title>
  <style>
    body {
      background: #f0f0f0;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .calculator {
      background: #fff;
      padding: 2rem;
      border-radius: 16px;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
      width: 300px;
    }

    .display {
      width: 100%;
      height: 60px;
      font-size: 1.8rem;
      text-align: right;
      padding: 0.5rem;
      border: none;
      border-radius: 8px;
      margin-bottom: 1rem;
      background: #f9f9f9;
    }

    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }

    button {
      padding: 20px;
      font-size: 1.2rem;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: #e0e0e0;
      transition: background 0.2s;
    }

    button:hover {
      background: #ccc;
    }

    .equal {
      background: #007bff;
      color: white;
    }

    .clear {
      background: #dc3545;
      color: white;
    }

    .operator {
      background: #ffc107;
      color: black;
    }
  </style>
</head>
<body>

  <div class="calculator">
    <input type="text" id="display" class="display" disabled />
    <div class="buttons">
      <button onclick="clearDisplay()" class="clear">C</button>
      <button onclick="append('%')" class="operator">%</button>
      <button onclick="append('/')" class="operator">÷</button>
      <button onclick="append('*')" class="operator">×</button>

      <button onclick="append('7')">7</button>
      <button onclick="append('8')">8</button>
      <button onclick="append('9')">9</button>
      <button onclick="append('-')" class="operator">−</button>

      <button onclick="append('4')">4</button>
      <button onclick="append('5')">5</button>
      <button onclick="append('6')">6</button>
      <button onclick="append('+')" class="operator">+</button>

      <button onclick="append('1')">1</button>
      <button onclick="append('2')">2</button>
      <button onclick="append('3')">3</button>
      <button onclick="calculate()" class="equal">=</button>

      <button onclick="append('0')">0</button>
      <button onclick="append('.')">.</button>
      <button onclick="backspace()">⌫</button>
    </div>
  </div>

  <script>
    const display = document.getElementById('display');

    function append(value) {
      display.value += value;
    }

    function clearDisplay() {
      display.value = '';
    }

    function backspace() {
      display.value = display.value.slice(0, -1);
    }

    function calculate() {
      try {
        const result = eval(display.value);
        if (!isFinite(result)) throw new Error("Math Error");
        display.value = result;
      } catch (err) {
        display.value = "Error";
        setTimeout(() => display.value = '', 1500);
      }
    }

    // Keyboard input support
    document.addEventListener('keydown', (e) => {
      const key = e.key;
      if (/\d/.test(key) || ['+', '-', '*', '/', '.', '%'].includes(key)) {
        append(key);
      } else if (key === 'Enter') {
        e.preventDefault();
        calculate();
      } else if (key === 'Backspace') {
        backspace();
      } else if (key === 'Escape') {
        clearDisplay();
      }
    });
  </script>

</body>
</html>

