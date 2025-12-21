const Synapse = require('./src/core/Synapse');

console.log("--- INITIALISATION DU DIAGNOSTIC SYNAPSE ---");

// 1. Création du lien neuronal
// ID: LINK-01, Source: Cortex, Target: Logic, Poids initial: 1.0
const mySynapse = new Synapse("LINK-01", "Cortex", "Logic", 1.0);
console.log(`[STATUS] Synapse créée. Poids initial: ${mySynapse.weight}`);

// 2. Test de tir simple (Signal brut)
const inputSignal = 100;
console.log(`\n[ACTION] Tir du signal: ${inputSignal}`);
let output = mySynapse.fire(inputSignal);
console.log(`[RESULT] Sortie: ${output} (Attendu: 100)`);

// 3. Modulation Neuroplastique (On injecte du Phi)
console.log("\n[ACTION] Ajustement du poids (+0.618 - Approche de Phi)");
mySynapse.adjustWeight(0.618); 
console.log(`[STATUS] Nouveau poids: ${mySynapse.weight}`);

// 4. Test de tir modulé
console.log(`[ACTION] Tir du signal: ${inputSignal}`);
output = mySynapse.fire(inputSignal);
console.log(`[RESULT] Sortie: ${output} (Doit être amplifié)`);

// 5. Vérification de l'historique (Mémoire)
console.log("\n[MEMORY] Inspection de l'historique du signal:");
console.log(mySynapse.signalHistory);

console.log("\n--- DIAGNOSTIC TERMINÉ ---");
