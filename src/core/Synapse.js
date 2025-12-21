/**
 * Synapse.js
 * Composant de liaison pour le système nerveux du projet.
 * Gère la transmission des signaux, la pondération (Weight) et la synchronisation.
 */

const PHI = 1.61803398875; // La signature du patron ^_-

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
     * Transmet un signal du noeud source au noeud cible.
     * Applique une modulation basée sur le poids et potentiellement Phi.
     * @param {any} signal - La donnée ou l'impulsion à transmettre
     */
    fire(signal) {
        if (!this.active) return null;

        // Si le signal est numérique, on applique une modulation quantique/fractale simple
        let processedSignal = signal;
        if (typeof signal === 'number') {
            processedSignal = signal * this.weight;
        }

        const transmission = {
            timestamp: Date.now(),
            input: signal,
            output: processedSignal,
            synapseId: this.id
        };

        this.signalHistory.push(transmission);
        
        // Logique de 'nettoyage' pour ne pas saturer la mémoire (Keep it clean)
        if (this.signalHistory.length > 50) this.signalHistory.shift();

        return processedSignal;
    }

    /**
     * Ajuste le poids de la synapse (Neuroplasticité simulée)
     * @param {number} delta - Le changement de poids
     */
    adjustWeight(delta) {
        this.weight += delta;
        // On s'assure que le poids reste dans des bornes logiques
        this.weight = Math.max(0, Math.min(this.weight, PHI * 2)); 
    }

    disable() {
        this.active = false;
    }

    enable() {
        this.active = true;
    }
}

module.exports = Synapse;
