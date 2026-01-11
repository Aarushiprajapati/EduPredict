document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    // UI Loading State
    const btn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');
    const resultCard = document.getElementById('resultCard');

    btn.disabled = true;
    btnText.style.display = 'none';
    spinner.style.display = 'block';

    // Gather Data
    const formData = {
        Attendance: parseFloat(document.getElementById('Attendance').value),
        Study_Hours: parseFloat(document.getElementById('Study_Hours').value),
        Previous_Scores: parseFloat(document.getElementById('Previous_Scores').value),
        Sleep_Hours: parseFloat(document.getElementById('Sleep_Hours').value),
        Extracurricular: parseInt(document.getElementById('Extracurricular').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        // Update UI with Results
        updateResultUI(data);

        // Show Result Card
        resultCard.classList.add('visible');

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching the prediction. Please make sure the backend server is running.');
    } finally {
        // Reset Button State
        btn.disabled = false;
        btnText.style.display = 'inline';
        spinner.style.display = 'none';
    }
});

function updateResultUI(data) {
    const statusBadge = document.getElementById('statusBadge');
    const suggestionsList = document.getElementById('suggestionsList');

    // Reset classes
    statusBadge.className = 'status-badge';

    // Set Status
    statusBadge.textContent = data.status;

    if (data.status === 'Excellent') {
        statusBadge.classList.add('status-excellent');
    } else if (data.status === 'Average') {
        statusBadge.classList.add('status-average');
    } else {
        statusBadge.classList.add('status-risk');
    }

    // Set Suggestions
    suggestionsList.innerHTML = '';
    data.suggestions.forEach(suggestion => {
        const li = document.createElement('li');
        li.className = 'suggestion-item';
        li.textContent = suggestion;
        suggestionsList.appendChild(li);
    });
}
