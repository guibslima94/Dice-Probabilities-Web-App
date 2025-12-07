document.addEventListener('DOMContentLoaded', function() {
    const calculateBtn = document.getElementById('calculate-btn');
    const resultContainer = document.getElementById('result-container');
    const probabilityDisplay = document.getElementById('probability-display');
    const lastRunValue = document.getElementById('last-run-value');
    const errorMessage = document.getElementById('error-message');
    
    calculateBtn.addEventListener('click', async function() {
        // Hide previous results and errors
        resultContainer.classList.add('hidden');
        errorMessage.classList.add('hidden');
        
        // Get input values
        const numDices = parseInt(document.getElementById('num_dices').value);
        const targetValue = parseInt(document.getElementById('target_value').value);
        const numDicesReachingTarget = parseInt(document.getElementById('num_dices_reaching_target').value);
        
        // Basic client-side validation
        if (!numDices || !targetValue || numDicesReachingTarget === undefined) {
            showError('Please fill in all fields');
            return;
        }
        
        // Disable button and show loading state
        calculateBtn.disabled = true;
        calculateBtn.textContent = 'Calculating...';
        
        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    num_dices: numDices,
                    target_value: targetValue,
                    num_dices_reaching_target: numDicesReachingTarget
                })
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'An error occurred');
            }
            
            // Display result
            const probability = parseFloat(data.probability);
            const percentage = (probability * 100).toFixed(2);
            
            probabilityDisplay.textContent = `${data.probability_formatted} (${percentage}%)`;
            resultContainer.classList.remove('hidden');
            
            // Update last run
            lastRunValue.textContent = `Probability = ${data.probability_formatted}`;
            
        } catch (error) {
            showError(error.message);
        } finally {
            // Re-enable button
            calculateBtn.disabled = false;
            calculateBtn.textContent = 'Calculate Probability';
        }
    });
    
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
    }
    
    // Allow Enter key to submit
    const inputs = document.querySelectorAll('input[type="number"]');
    inputs.forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                calculateBtn.click();
            }
        });
    });
});

