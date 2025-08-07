# Incident Response Automation Simulator

A Python-based automation suite to simulate production-like failures—such as HTTP 500 errors, CPU spikes, app crashes, and memory exhaustion. Integrated with GitHub Actions to trigger simulations via manual workflow dispatch.

---

## 🧩 Project Features

- ✅ Simulates 4 types of incidents:
  - `http500`: Internal server error
  - `cpu`: High CPU usage
  - `crash`: App crash simulation
  - `memory`: Memory exhaustion
- 🔧 CLI-based Python script to control error type
- ⚙️ GitHub Actions workflow with manual input selector
- 📡 Optional webhook alert step (can be extended to SNS, Slack, etc.)

---

## 📁 Folder Structure

incident-response-simulator/
│
├── scripts/
│ └── simulate_error.py
│
├── .github/
│ └── workflows/
│ └── simulate_incident.yml
│
├── requirements.txt
└── README.md

## Running Locally 

clone repo 

cd to working directory 

## command line instructions 
pip install -r requirements.text

simulation python scripts/simulate_error.py http500
python scripts/simulate_error.py cpu
python scripts/simulate_error.py crash
python scripts/simulate_error.py memory
