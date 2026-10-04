<!-- ═══════════════════════ HEADER ═══════════════════════ -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:2b2f38,100:6b7280&height=290&section=header&text=AI-Powered%20Collections%20Strategy&fontSize=46&fontColor=ffffff&fontAlignY=36&animation=fadeIn&desc=Geldium%20Finance%20%E2%80%A2%20Tata%20iQ%20GenAI-Powered%20Data%20Analytics%20Job%20Simulation&descSize=17&descAlignY=60" width="100%" alt="AI-Powered Collections Strategy"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=900&color=3B82F6&center=true&vCenter=true&width=860&height=50&lines=%F0%9F%A4%96+Agentic+AI+for+debt+collection;%F0%9F%93%89+From+reactive+recovery+to+proactive+risk+mitigation;%E2%9A%96%EF%B8%8F+Fair%2C+explainable+and+regulation-aware;%F0%9F%8F%A6+Built+for+Geldium+Finance" alt="Typing animation"/>

<br/>

<!-- Animated workflow (file: assets/agentic-flow.svg) -->
<img src="./assets/agentic-flow.svg" width="92%" alt="Animated workflow: data pipeline, decision engine, action layer, learning loop"/>

<br/><br/>

<img src="https://img.shields.io/badge/Machine%20Learning-4B5563?style=for-the-badge&labelColor=111827" alt="Machine Learning"/>
<img src="https://img.shields.io/badge/Agentic%20AI-9CA3AF?style=for-the-badge&labelColor=111827" alt="Agentic AI"/>
<img src="https://img.shields.io/badge/Explainable%20AI-SHAP-2563EB?style=for-the-badge&labelColor=111827" alt="Explainable AI SHAP"/>
<img src="https://img.shields.io/badge/Responsible%20AI-Fair%20Lending-4B5563?style=for-the-badge&labelColor=111827" alt="Responsible AI"/>

<br/><br/>

<!-- ═══════════════════════ NAVIGATION ═══════════════════════ -->
<a href="#summary"><img src="https://img.shields.io/badge/Summary-111827?style=for-the-badge" alt="Summary"/></a>
<a href="#deliverables"><img src="https://img.shields.io/badge/Deliverables-4B5563?style=for-the-badge" alt="Deliverables"/></a>
<a href="#architecture"><img src="https://img.shields.io/badge/Architecture-2563EB?style=for-the-badge" alt="Architecture"/></a>
<a href="#guardrails"><img src="https://img.shields.io/badge/Guardrails-111827?style=for-the-badge" alt="Guardrails"/></a>
<a href="#impact"><img src="https://img.shields.io/badge/Impact-4B5563?style=for-the-badge" alt="Impact"/></a>
<a href="#run"><img src="https://img.shields.io/badge/How%20To%20Run-2563EB?style=for-the-badge" alt="How to run"/></a>

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ SUMMARY ═══════════════════════ -->
<a id="summary"></a>

## 📌 Executive Summary

### AI-Powered Autonomous Debt-Management & Collections Strategy

This repository contains an end-to-end **Machine Learning and Agentic AI** solution developed for **Geldium Finance** to modernize debt collection and delinquency risk management.

By shifting from **reactive debt recovery** to **proactive risk mitigation**, the system dynamically identifies at-risk credit cardholders, predicts delinquency probability, and deploys personalized, responsible interventions, while following global financial regulatory frameworks (**ECOA, FCRA, GDPR, FCA**).

<div align="center">

| 🔎 **Identify** | 📊 **Predict** | 🎯 **Intervene** | ⚖️ **Stay Compliant** |
|:---:|:---:|:---:|:---:|
| At-risk credit cardholders | Delinquency probability | Personalized, responsible actions | ECOA • FCRA • GDPR • FCA |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ DELIVERABLES ═══════════════════════ -->
<a id="deliverables"></a>

## 🛠️ Key Project Deliverables

<table>
<tr>
<td width="50%" valign="top">

### 📄 `Business_Summary_Report_Geldium.docx`
Executive briefing document with portfolio predictive insights, **SMART recommendation frameworks** and ethical AI strategies.

</td>
<td width="50%" valign="top">

### 📽️ `AI_Powered_Collections_Strategy_Geldium.pptx`
High-level C-suite presentation covering system architecture, agentic AI workflows, guardrails and **quantitative business impact**.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 `Delinquency_prediction_dataset.xlsx`
Portfolio credit card dataset used for **behavioral feature engineering** and risk segmentation.

</td>
<td width="50%" valign="top">

### 🧾 `Task 2_ModelPlan_Template.docx`
Technical **model evaluation plan** and feature mapping template.

</td>
</tr>
</table>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ ARCHITECTURE ═══════════════════════ -->
<a id="architecture"></a>

## 🏗️ System Architecture & Workflow

The autonomous collections system works across **four integrated layers**.

```mermaid
flowchart LR
    A["📥 1. Data Pipeline<br/>Real-time ingestion"] --> B["🧠 2. Decision Engine<br/>Hybrid predictive model"]
    B --> C["🎯 3. Action Layer<br/>Targeted interventions"]
    C --> D["🔁 4. Learning Loop<br/>Closed-loop optimization"]
    D -. "refines thresholds" .-> B
    style A fill:#111827,stroke:#4b5563,color:#fff
    style B fill:#1f2937,stroke:#2563eb,stroke-width:2px,color:#fff
    style C fill:#4b5563,stroke:#9ca3af,color:#fff
    style D fill:#d1d5db,stroke:#6b7280,color:#111827
```

<table>
<tr>
<td width="50%" valign="top">

### 📥 1. Data Pipeline
**Real-time ingestion** that monitors:
- Credit utilization velocity (**>60% risk threshold**)
- Payment friction logs (trailing 6 months)
- Account balance dynamics

</td>
<td width="50%" valign="top">

### 🧠 2. Decision Engine
**Hybrid predictive model** that combines:
- Machine learning delinquency risk scores
- Business rules
- **SHAP** explainability reason codes

Accounts are assigned to **Low**, **Medium** or **High** risk tiers.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎯 3. Action Layer
**Targeted interventions** by risk tier (see below).

</td>
<td width="50%" valign="top">

### 🔁 4. Learning Loop
**Closed-loop optimization** that tracks **30/60/90-day** repayment velocity and engagement rates to refine probability thresholds and lower cost-to-collect.

</td>
</tr>
</table>

### 🎚️ Risk tiers and interventions

```mermaid
flowchart LR
    S["📊 Delinquency<br/>risk score"] --> L["🟢 Low risk"]
    S --> M["🟡 Medium risk"]
    S --> H["🔴 High risk"]
    L --> L1["📧 Automated monthly statements<br/>+ self-service digital links"]
    M --> M1["💬 Multi-channel SMS / WhatsApp alerts<br/>+ temporary interest freezes<br/>+ proactive repayment plans"]
    H --> H1["📞 Direct phone outreach by<br/>dedicated collections agents<br/>+ early hardship restructuring"]
    style S fill:#111827,stroke:#2563eb,stroke-width:2px,color:#fff
    style L fill:#d1d5db,stroke:#6b7280,color:#111827
    style M fill:#9ca3af,stroke:#4b5563,color:#111827
    style H fill:#1f2937,stroke:#2563eb,color:#fff
    style L1 fill:#f3f4f6,stroke:#9ca3af,color:#111827
    style M1 fill:#e5e7eb,stroke:#6b7280,color:#111827
    style H1 fill:#374151,stroke:#9ca3af,color:#fff
```

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ GUARDRAILS ═══════════════════════ -->
<a id="guardrails"></a>

## 🛡️ Responsible AI & Regulatory Guardrails

<table>
<tr>
<td width="33%" valign="top">

### ⚖️ Fairness & Bias Audit
Continuous **Adverse Impact Ratio (AIR)** monitoring across age and regional tiers to enforce the regulatory **80% rule**.

```text
0.80 ≤ AIR ≤ 1.25
```

</td>
<td width="33%" valign="top">

### 🔍 Explainability (XAI)
Extraction of the **top 3 plain-language SHAP reason codes** per account score, to meet Fair Lending and Adverse Action notice mandates.

</td>
<td width="34%" valign="top">

### 📜 Regulatory Compliance
Built-in alignment with the frameworks below.

</td>
</tr>
</table>

<div align="center">

| Framework | Focus |
|:---:|:---|
| <img src="https://img.shields.io/badge/ECOA-111827?style=for-the-badge" alt="ECOA"/> | Non-discrimination |
| <img src="https://img.shields.io/badge/FCRA-4B5563?style=for-the-badge" alt="FCRA"/> | Data accuracy |
| <img src="https://img.shields.io/badge/GDPR-2563EB?style=for-the-badge" alt="GDPR"/> | Right to explanation and auditability |
| <img src="https://img.shields.io/badge/FCA%20Consumer%20Duty-9CA3AF?style=for-the-badge&labelColor=111827" alt="FCA Consumer Duty"/> | Fair treatment of vulnerable customers |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ IMPACT ═══════════════════════ -->
<a id="impact"></a>

## 📈 Target Business Impact

<div align="center">

| 📉 **30+ Day Delinquency Rate** | 🤝 **Hardship Plan Opt-In** | 💸 **Operational Costs** | 💰 **Capital Recovery** |
|:---:|:---:|:---:|:---:|
| <h2>15%</h2>Reduction | <h2>25%</h2>Opt-In Rate | <h2>40%</h2>Reduction | <h2>18%</h2>Increase |

</div>

| Metric / KPI | Projected Outcome | Key Driver |
|:---|:---|:---|
| **30+ Day Delinquency Rate** | **15% Reduction** | Proactive hardship intervention before write-off escalation |
| **Hardship Plan Opt-In** | **25% Opt-In Rate** | Personalized SMS/Email outreach offering flexible terms |
| **Operational Costs** | **40% Reduction** | Automation of digital reminders for Low/Medium-Risk cohorts |
| **Capital Recovery** | **18% Increase** | Reallocation of manual agent capacity to severe default cases |

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ HOW TO RUN ═══════════════════════ -->
<a id="run"></a>

## 🚀 How to Run & Generate Reports

**1️⃣ Clone the repository**

```bash
git clone https://github.com/paraskosambe-web/GenAI-Powered-Data-Analytics-Job-Simulation.git
cd GenAI-Powered-Data-Analytics-Job-Simulation
```

**2️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**3️⃣ Generate documents via Python**

To programmatically generate or update the Word report and PowerPoint presentation:

```bash
python generate_docs.py
```

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:6b7280,100:d1d5db&height=3" width="100%" alt="divider"/>

<!-- ═══════════════════════ AUTHOR ═══════════════════════ -->
## 👤 Author & Governance

<div align="center">

<table>
<tr>
<td align="center" width="50%"><b>Author</b><br/>Paras Kosambe<br/><sub>AI Transformation Consultant (Tata iQ)</sub></td>
<td align="center" width="50%"><b>Organization</b><br/>Tata iQ / Geldium Finance</td>
</tr>
</table>

<br/>

<a href="https://github.com/paraskosambe-web"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
<a href="https://www.linkedin.com/in/paras-kosambe"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:paraskosambe@gmail.com"><img src="https://img.shields.io/badge/Email-4B5563?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=17&duration=3500&pause=1200&color=3B82F6&center=true&vCenter=true&width=700&lines=Proactive+risk+mitigation%2C+not+reactive+recovery.;Responsible+AI+for+fair+and+explainable+collections." alt="Footer typing"/>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:2b2f38,100:6b7280&height=120&section=footer" width="100%" alt="footer wave"/>
