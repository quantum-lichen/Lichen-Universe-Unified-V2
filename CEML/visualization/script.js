// LMEC_CEML/script.js

// Constantes
const PHI = 1.618;
const RADIUS = 45;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;

// DOM Elements
const coherenceInput = document.getElementById('coherence');
const entropyInput = document.getElementById('entropy');
const valC = document.getElementById('val-c');
const valH = document.getElementById('val-h');
const scoreRing = document.getElementById('score-ring');
const finalScoreEl = document.getElementById('final-score');
const decisionEl = document.getElementById('decision-text');
const fractalBg = document.getElementById('fractal-bg');

// Initialisation du Cercle SVG
scoreRing.style.strokeDasharray = `${CIRCUMFERENCE} ${CIRCUMFERENCE}`;
scoreRing.style.strokeDashoffset = CIRCUMFERENCE;

// Fonction de calcul CEML
function updateCEML() {
    const C = parseFloat(coherenceInput.value);
    const H = parseFloat(entropyInput.value);

    valC.textContent = C.toFixed(2);
    valH.textContent = H.toFixed(2);

    // ÉQUATION MAÎTRESSE : J = C / (H + epsilon)
    let score = C / (H + 0.001);
    
    finalScoreEl.textContent = score.toFixed(2);

    // Visualisation
    const maxVisualScore = 5.0;
    let percent = Math.min(score / maxVisualScore, 1.0);
    const offset = CIRCUMFERENCE - (percent * CIRCUMFERENCE);
    scoreRing.style.strokeDashoffset = offset;

    // Logique de Décision
    if (score >= PHI) {
        // RÉSONANCE
        decisionEl.textContent = "RÉSONANCE";
        decisionEl.style.color = "var(--success)";
        scoreRing.style.stroke = "var(--success)";
        pulseFractal(true);
    } else if (C > 0.8 && H < 0.1) {
        // HALLUCINATION POTENTIELLE
        decisionEl.textContent = "HALLUCINATION ?";
        decisionEl.style.color = "var(--neon-blue)";
        scoreRing.style.stroke = "var(--neon-blue)";
        pulseFractal(false);
    } else {
        // DISSONANCE (Rejet)
        decisionEl.textContent = "DISSONANCE";
        decisionEl.style.color = "var(--danger)";
        scoreRing.style.stroke = "var(--danger)";
        pulseFractal(false);
    }
}

function initFractal() {
    for(let i=0; i<80; i++) {
        let div = document.createElement('div');
        div.style.position = 'absolute';
        div.style.width = '3px';
        div.style.height = '3px';
        div.style.background = 'rgba(212, 175, 55, 0.4)';
        div.style.borderRadius = '50%';
        
        // Maths Spirale d'Or
        let angle = i * 137.5 * (Math.PI / 180); 
        let r = 6 * Math.sqrt(i); 
        
        let x = 50 + r * Math.cos(angle); 
        let y = 50 + r * Math.sin(angle); 
        
        div.style.left = x + '%';
        div.style.top = y + '%';
        div.className = 'fractal-dot';
        
        fractalBg.appendChild(div);
    }
}

function pulseFractal(isResonant) {
    const dots = document.querySelectorAll('.fractal-dot');
    dots.forEach(dot => {
        if(isResonant) {
            dot.style.transform = "scale(1.5)";
            dot.style.boxShadow = "0 0 8px var(--gold)";
            dot.style.opacity = "1";
        } else {
            dot.style.transform = "scale(1)";
            dot.style.boxShadow = "none";
            dot.style.opacity = "0.4";
        }
    });
}

coherenceInput.addEventListener('input', updateCEML);
entropyInput.addEventListener('input', updateCEML);

initFractal();
setTimeout(updateCEML, 50);
