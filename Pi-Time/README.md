# π-Time : Mathematical Index
**Version:** 1.1
**Scope:** Temporal Conversion and Validation.

---


## 1. The Fundamental Frequency ($f_{\pi}$)
The beat frequency of the Lichen Kernel.


### 📐 LaTeX


$$
f_{\pi} = \frac{1}{\pi} \text{ Hz} \approx 0.3183 \text{ Hz}
$$



### 💻 Python
```python
import math
FREQ_PI = 1.0 / math.pi
```

2. The Timestamp Vector ($T_{\pi}$)
The structured representation of an instant.

📐 LaTeX



$$T_{\pi} = \{ C, S, P, D \}$$



Where:



$C = \lfloor t / \pi \r



floor$ (Cycle)$D = \text{BBP}(P)$ (Digit at Position P)



3. Bailey–Borwein–Plouffe (BBP) Formula

Used to calculate the $n$-th digit of $\pi$ without computing the preceding ones (hexadecimal basis, adapted for validation).


📐 LaTeX



$$\pi = \sum_{k=0}^{\infty} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right)$$



---

### 4. `Pi-Time/poc/pi_clock.js` 💻
*(Adapté de ton code TypeScript vers un JS exécutable direct)*

```javascript
/**
 * π-TIME CORE PROTOTYPE
 * Version: 1.1
 * Run with: node pi_clock.js
 */

const MATH_PI = Math.PI;

// --- 1. CORE UTILITIES ---

function computePiDigit(position) {
    // MOCK: In production, this uses the BBP algorithm.
    // Here we simulate a digit for the PoC based on the math.PI sequence
    const piString = "14159265358979323846264338327950288419716939937510";
    if (position < piString.length) {
        return parseInt(piString[position]);
    }
    return (position % 10); // Fallback for infinite simulation
}

function getSystemPiTime() {
    const now = Date.now(); // ms since 1970
    const seconds = now / 1000;
    
    // Calculate Pi-Cycles (Example: 1 Cycle = PI seconds)
    const rawCycles = seconds / MATH_PI;
    
    const cycle = Math.floor(rawCycles);
    const sub = Math.floor((rawCycles - cycle) * 1000);
    const position = Math.floor(seconds * 100000) % 1000000; // Fake high-res index
    const digit = computePiDigit(position % 50); // Mock lookup

    return {
        cycle: cycle,
        sub: sub,
        position: position,
        digit: digit,
        formatted: `π${cycle}.${sub.toString().padStart(3, '0')}.${position}.${digit}`
    };
}

// --- 2. PARSER & VALIDATOR ---

function parsePiTime(piString) {
    // Regex: π[CYCLE].[SUB].[POSITION].[DIGIT]
    const regex = /^π(\d+)\.(\d+)\.(\d+)\.(\d)$/;
    const match = piString.match(regex);

    if (!match) return null;

    return {
        cycle: parseInt(match[1], 10),
        sub: parseInt(match[2], 10),
        position: parseInt(match[3], 10),
        digit: parseInt(match[4], 10)
    };
}

function verifyTimestamp(piString) {
    console.log(`🔍 Verifying: ${piString}`);
    const piObj = parsePiTime(piString);
    
    if (!piObj) {
        console.error("❌ Invalid Format");
        return false;
    }

    // CHECK: Does the digit match the position? (Proof of Time)
    const expectedDigit = computePiDigit(piObj.position % 50);
    
    if (piObj.digit === expectedDigit) {
        console.log("✅ INTEGRITY CONFIRMED: Digit matches Position.");
        return true;
    } else {
        console.warn(`🚨 TEMPORAL DISSONANCE! Expected ${expectedDigit}, got ${piObj.digit}`);
        return false;
    }
}

// --- 3. DEMO RUNNER ---

function main() {
    console.log("⏱️  STARTING π-CLOCK...");
    
    // Generate current time
    const now = getSystemPiTime();
    console.log(`Current Time: ${now.formatted}`);
    
    // Verify it
    verifyTimestamp(now.formatted);

    // Simulate a Fake/Corrupted timestamp
    console.log("\n--- Simulating Attack ---");
    const fakeTime = `π${now.cycle}.${now.sub}.${now.position}.${(now.digit + 1) % 10}`;
    verifyTimestamp(fakeTime);
}

main();


