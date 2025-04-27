// Function to roll the dice and update the value
function rollDice() {
    const diceValue = Math.floor(Math.random() * 6) + 1; // Random number between 1-6
    document.getElementById('diceValue').textContent = diceValue;
}

// Attach event listener to the button
document.getElementById('rollDice').addEventListener('click', rollDice);
