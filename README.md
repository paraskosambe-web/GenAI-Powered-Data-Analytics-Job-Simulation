# AI-Powered Autonomous Debt-Management & Collections Strategy

## 📌 Executive Summary
This repository contains an end-to-end Machine Learning and Agentic AI solution developed for **Geldium Finance** to modernize debt collection and delinquency risk management. 

By shifting from reactive debt recovery to proactive risk mitigation, the system dynamically identifies at-risk credit cardholders, predicts delinquency probability, and deploys personalized, responsible interventions while adhering to global financial regulatory frameworks (ECOA, FCRA, GDPR, FCA).

---

## 🛠️ Key Project Deliverables

- **`Business_Summary_Report_Geldium.docx`**: Executive briefing document containing portfolio predictive insights, SMART recommendation frameworks, and ethical AI strategies.
- **`AI_Powered_Collections_Strategy_Geldium.pptx`**: High-level C-suite presentation deck covering system architecture, agentic AI workflows, guardrails, and quantitative business impact.
- **`Delinquency_prediction_dataset.xlsx`**: Portfolio credit card dataset utilized for behavioral feature engineering and risk segmentation.
- **`Task 2_ModelPlan_Template.docx`**: Technical model evaluation plan and feature mapping template.

---

## 🏗️ System Architecture & Workflow

The autonomous collections system operates across four integrated layers:

1. **Data Pipeline (Real-Time Ingestion):**
   - Monitors credit utilization velocity (>60% risk threshold), payment friction logs (trailing 6 months), and account balance dynamics.
2. **Decision Engine (Hybrid Predictive Model):**
   - Evaluates machine learning delinquency risk scores alongside business rules and SHAP explainability reason codes to assign accounts into **Low**, **Medium**, or **High** risk tiers.
3. **Action Layer (Targeted Interventions):**
   - **Low Risk:** Automated monthly statement delivery & self-service digital links.
   - **Medium Risk:** Multi-channel SMS/WhatsApp alerts, temporary interest freezes, and proactive repayment plans.
   - **High Risk:** Direct phone outreach by dedicated collections agents and early hardship restructuring.
4. **Learning Loop (Closed-Loop Optimization):**
   - Continuously tracks 30/60/90-day repayment velocity and engagement rates to refine probability thresholds and lower cost-to-collect.

---

## 🛡️ Responsible AI & Regulatory Guardrails

- **Fairness & Bias Audit:** Continuous Adverse Impact Ratio (AIR) monitoring across age and regional tiers to enforce the regulatory **80% rule** (0.80 ≤ AIR ≤ 1.25).
- **Explainability (XAI):** Extraction of top 3 plain-language SHAP reason codes per account score to meet Fair Lending and Adverse Action notice mandates.
- **Regulatory Compliance:** Built-in alignment with **ECOA** (non-discrimination), **FCRA** (data accuracy), **GDPR** (right to explanation & auditability), and **FCA Consumer Duty** (fair treatment of vulnerable customers).

---

## 📈 Target Business Impact

| Metric / KPI | Projected Outcome | Key Driver |
| :--- | :--- | :--- |
| **30+ Day Delinquency Rate** | **15% Reduction** | Proactive hardship intervention before write-off escalation |
| **Hardship Plan Opt-In** | **25% Opt-In Rate** | Personalized SMS/Email outreach offering flexible terms |
| **Operational Costs** | **40% Reduction** | Automation of digital reminders for Low/Medium-Risk cohorts |
| **Capital Recovery** | **18% Increase** | Reallocation of manual agent capacity to severe default cases |

---

## 🚀 How to Run & Generate Reports

## 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AI-Debt-Management-Collections.git](https://github.com/paraskosambe-web/GenAI-Powered-Data-Analytics-Job-Simulation.git)
cd AI-Debt-Management-Collections
```

## 2. Install Dependencies
```bash
pip install -r requirements.txt
3. Generate Documents via Python
To programmatically generate or update the Word report and PowerPoint presentation:
```


## python generate_docs.py
```bash
👤 Author & Governance
Author: Paras Kosambe — AI Transformation Consultant (Tata iQ)
```
Organization: Tata iQ / Geldium Finance
