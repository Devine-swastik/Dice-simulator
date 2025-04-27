async function rollDice() {
    const response = await fetch('/roll');
    const data = await response.json();
    document.getElementById('dice-result').innerText = `You rolled: ${data.result}`;
}
