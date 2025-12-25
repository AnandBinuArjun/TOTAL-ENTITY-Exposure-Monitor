# TOTAL ENTITY Exposure Monitor

### *Identity Risk Intelligence System*

---

[![Developer](https://img.shields.io/badge/Developer-ANAND%20BINU%20ARJUN-6366f1?style=for-the-badge&logo=code)](http://anandbinuarjun.live/)
[![Status](https://img.shields.io/badge/Status-PRODUCTION%20READY-success?style=for-the-badge)](http://anandbinuarjun.live/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> **"Don't just ask 'Was I breached?' Ask 'What will destroy me first?'"**

TOTAL ENTITY is a next-generation **Identity Risk Intelligence System (IRIS)**. unlike traditional breach checkers that simply list leaked passwords, TOTAL ENTITY builds a dynamic **Identity Graph** of your digital footprint, calculates the **Blast Radius** of a compromised credential, and strictly prioritizes remediation actions based on **Risk-Return ROI**.

---

## 🧠 System Architecture

```mermaid
graph TD
    user((User Identity)) -->|Email/Phone| api[FastAPI Backend]
    
    subgraph "Core Intelligence Engine"
        api --> privacy[Privacy Layer\nk-Anonymity Hashing]
        privacy --> ingestion[Ingestion Engine\nHIBP API + Leaks]
        ingestion --> graph[Identity Graph\nBlast Radius Map]
        graph --> risk[Risk Math Core\nL x I x (1-M)]
        risk --> actions[Action Prioritization\nROI Calculation]
    end
    
    actions --> db[(PostgreSQL\nRisk Store)]
    
    subgraph "Client Omni-Channel"
        db --> web[React Web Cockpit]
        db --> android[Android Shield]
        db --> ios[iOS Recovery]
    end
```

---

## 🚀 Key Features

### 1. **Exposure Intelligence Engine**

Not just a database lookup. CORTEX analyzes the **context** of a breach:

* **Data Classes**: Distinguishes between a harmless "Name" leak and a critical "Password Hash" leak.
* **Recency Decay**: Older breaches strictly carry less weight ($0.9^{years}$).
* **Verification**: Integrates live with **Have I Been Pwned Enterprise API**.

### 2. **Identity Blast Radius**

Visualizes the "domino effect" of a compromise.

* Maps **Recovery Authority** (e.g., Email controls Bank).
* Maps **SSO Chains** (e.g., Facebook controls Tinder).
* Calculates **Node Criticality** to find your single point of failure.

### 3. **Deterministic Risk Scoring**

A transparent, auditable math model:
$$ Risk = (Likelihood \times Impact) \times (1 - Mitigation) $$

* **Likelihood**: Probability of account takeover.
* **Impact**: Financial or reputational damage potential.
* **Mitigation**: Reduction from 2FA (SMS vs. YubiKey).

### 4. **ROI-Based Action Plan**

Stops "Security Fatigue" by ranking fixes.

* Calculates `ROI = Risk Reduction / User Effort`.
* Tells you to **"Use a YubiKey on Email"** (High ROI) before **"Change old forum password"** (Low ROI).

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python, FastAPI | High-performance async API |
| **Ingestion** | HTTPX, HIBP API | Real-time breach verify |
| **Database** | PostgreSQL, Redis | Structured storage & Caching |
| **Frontend** | React, Vite | Responsive Web Cockpit |
| **Mobile** | Kotlin (Android), SwiftUI (iOS) | Native client experiences |
| **Design** | CSS Modules, Framer Motion | Premium "Dark Mode" Aesthetic |

---

## 📸 Interface Preview

### **Web Cockpit**

*The command center for your digital identity.*
> *(Placeholder: Imagine a sleek, dark-mode dashboard showing a central risk score gauge at '72/100', a list of 'Critical' breaches, and a force-directed graph showing an email node connected to banking nodes.)*

### **Mobile Shield**

*On-the-go protection and alerts.*
> *(Placeholder: A mobile screen showing a large clean 'Secure' shield icon and a 'Scan' button.)*

---

## ⚡ Quick Start

### 1. Backend API

```bash
# Clone and Enter
git clone https://github.com/AnandBinuArjun/TOTAL-ENTITY-Exposure-Monitor.git
cd backend

# Install Dependencies
pip install -r requirements.txt

# Configure Real-World Data (Optional)
# Create a .env file and add your HIBP Key:
# HIBP_API_KEY=your_key_here

# Launch Engine
uvicorn main:app --reload
```

### 2. Web Frontend

```bash
cd frontend
npm install
npm run dev
```

*Access at `http://localhost:5173`*

### 3. Mobile Apps

* **Android**: Open `mobile_android` in **Android Studio**.
* **iOS**: Open `mobile_ios` in **Xcode**.

---

## 👨‍💻 Developer

**Developed by [ANAND BINU ARJUN](http://anandbinuarjun.live/)**

* **Portfolio**: [http://anandbinuarjun.live/](http://anandbinuarjun.live/)
* **GitHub**: [https://github.com/AnandBinuArjun](https://github.com/AnandBinuArjun)
* **Role**: Lead Architect & Full Stack Engineer
* **Focus**: Advanced Agentic Coding & Systems Architecture

> *"Security is not a product, it's a process. TOTAL ENTITY makes that process visible."* - Anand Binu Arjun

---
*© 2025 TOTAL ENTITY Systems. All Rights Reserved.*
