document.addEventListener('DOMContentLoaded', () => {
    // Elements
    const emailInput = document.getElementById('emailInput');
    const classifyBtn = document.getElementById('classifyBtn');
    const clearBtn = document.getElementById('clearBtn');
    const resultsSection = document.getElementById('resultsSection');
    const categoryBadge = document.getElementById('categoryBadge');
    const confidenceValue = document.getElementById('confidenceValue');
    const confidenceBar = document.getElementById('confidenceBar');
    const explanationText = document.getElementById('explanationText');
    const feedbackBtns = document.querySelectorAll('.feedback-btn');
    const correctionArea = document.getElementById('correctionArea');
    const submitFeedbackBtn = document.getElementById('submitFeedbackBtn');
    const correctionSelect = document.getElementById('correctionSelect');
    const toast = document.getElementById('toast');

    // State
    let currentPrediction = null;

    // Event Listeners
    classifyBtn.addEventListener('click', handleClassification);
    clearBtn.addEventListener('click', clearUI);

    feedbackBtns.forEach(btn => {
        btn.addEventListener('click', (e) => handleFeedbackClick(e.target.dataset.type));
    });

    submitFeedbackBtn.addEventListener('click', submitCorrection);

    // Functions
    async function handleClassification() {
        const text = emailInput.value.trim();
        if (!text) return;

        setLoading(true);
        resultsSection.classList.add('hidden');
        correctionArea.classList.add('hidden');

        try {
            const response = await fetch('/classify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });

            if (!response.ok) throw new Error('API Error');

            const data = await response.json();
            displayResults(data);
            currentPrediction = data.category;

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while classifying the email.');
        } finally {
            setLoading(false);
        }
    }

    function displayResults(data) {
        // Category Badge
        categoryBadge.textContent = data.category;
        categoryBadge.className = `badge ${data.category.toLowerCase()}`;

        // Confidence
        const confidencePercent = Math.round(data.confidence * 100) + '%';
        confidenceValue.textContent = confidencePercent;
        confidenceBar.style.width = confidencePercent;

        // Explanation
        explanationText.textContent = data.explanation;

        // Reveal Section
        resultsSection.classList.remove('hidden');
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function handleFeedbackClick(type) {
        if (type === 'correct') {
            submitFeedback(currentPrediction);
        } else {
            correctionArea.classList.remove('hidden');
        }
    }

    async function submitCorrection() {
        const correctedCategory = correctionSelect.value;
        await submitFeedback(correctedCategory);
        correctionArea.classList.add('hidden');
    }

    async function submitFeedback(correctedCategory) {
        const text = emailInput.value.trim();

        try {
            const response = await fetch('/feedback', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email_text: text,
                    predicted_category: currentPrediction,
                    corrected_category: correctedCategory
                })
            });

            if (response.ok) {
                showToast('Thanks for your feedback! 🚀');
            }
        } catch (error) {
            console.error('Feedback Error:', error);
        }
    }

    function setLoading(isLoading) {
        if (isLoading) {
            classifyBtn.disabled = true;
            classifyBtn.textContent = 'Analyzing...';
            emailInput.disabled = true;
        } else {
            classifyBtn.disabled = false;
            classifyBtn.textContent = 'Analyze Email';
            emailInput.disabled = false;
        }
    }

    function clearUI() {
        emailInput.value = '';
        resultsSection.classList.add('hidden');
        correctionArea.classList.add('hidden');
        currentPrediction = null;
        emailInput.focus();
    }

    function showToast(message) {
        toast.textContent = message;
        toast.classList.remove('hidden');
        toast.style.opacity = '1';

        setTimeout(() => {
            toast.style.opacity = '0';
            setTimeout(() => toast.classList.add('hidden'), 300);
        }, 3000);
    }
});
