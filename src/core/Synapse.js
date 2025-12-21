/**
 * Synapse.js (V2.1.6 Refactor)
 * Composant de liaison pour le système nerveux SynapseΩ.
 * Aligné sur les constantes : PHI (Structure) et PI (Temps).
 */

const PHI = 1.61803398875;
const PI  = 3.14159265359;

class Synapse {
    constructor(id, sourceNode, targetNode, weight = 1.0) {
        this.id = id;
        this.source = sourceNode;
        this.target = targetNode;
        this.weight = weight;
        this.active = true;
        this.signalHistory = [];
    }

    /**
     * Générateur de temps fractal (Pi-Time approximation)
     * Convertit le temps linéaire en cycles de Pi pour l'indexation.
     */
    getPiTime() {
        const now = Date.now();
        // Formule simplifiée de l'ancrage temporel V2
        return (now / 1000) * PI; 
    }

    /**
     * Transmet un signal.
     * @param {any} signal - Idéalement un FC-496 Atom ou un Number
     */
    fire(signal) {
        if (!this.active) return null;

        let processedSignal = signal;
        
        // Modulation Quantique V2
        if (typeof signal === 'number') {
            // L'amplification respecte la signature harmonique
            processedSignal = signal * this.weight;
        }

        const transmission = {
            // CORRECTION V2 : Utilisation du Pi-Time
            timestamp: this.getPiTime(), 
            original_epoch: Date.now(), // On garde la ref pour le debug humain seulement
            input: signal,
            output: processedSignal,
            synapseId: this.id,
            coherence: PHI // Marqueur de cohérence théorique
        };

        this.signalHistory.push(transmission);
        
        // Gestion mémoire "Rolling Wave"
        if (this.signalHistory.length > 50) this.signalHistory.shift();

        return processedSignal;
    }

    adjustWeight(delta) {
        this.weight += delta;
        // La borne PHI * 2 est parfaite, on la garde.
        this.weight = Math.max(0, Math.min(this.weight, PHI * 2)); 
    }
    
    // ... disable/enable inchangés
}

module.exports = Synapse;
