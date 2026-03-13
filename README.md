# 📊 Egypt Data Job Market Analysis

> An interactive dashboard analyzing **2,533 job listings from Wuzzuf** to map the landscape of data roles in Egypt — built with Python, Pandas, Plotly & Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://marwanessa2006-egypt-job-market-analysis.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2-blue?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.22-blue?logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit&logoColor=white)

---

## 🔍 Overview

This project explores **what it really takes to land a data job in Egypt** by analyzing job postings scraped from Wuzzuf — Egypt's largest job platform.

The analysis answers 10 key questions:

| # | Question |
|---|----------|
| 1 | What technical skills are most in demand? |
| 2 | How much experience do employers require? |
| 3 | What work models are available (remote / hybrid / on-site)? |
| 4 | Which cities have the most data jobs? |
| 5 | What are the top job titles? |
| 6 | How does experience compare to the general market? |
| 7 | What percentage of roles are entry-level? |
| 8 | Which companies are hiring the most? |
| 9 | How does the data job market compare to all other jobs? |
| 10 | How hireable is a junior data professional in Egypt? |

---

## 📸 Dashboard Preview

### Tab 1 — Data Jobs Overview

<img width="1200" height="900" alt="wuzzuf_dashboard_tab1" src="https://github.com/user-attachments/assets/e278acc6-2336-47c7-bfd6-ad5b0808064c" />


### Tab 2 — Data vs General Market
<img width="1200" height="900" alt="wuzzuf_dashboard_tab2" src="https://github.com/user-attachments/assets/99a1d4a7-202c-4844-82d5-46b1e5200010" />

---

## 🔑 Key Findings

- 🎯 **209 data roles** found out of 2,533 total listings — just **8.3%** of the market
- 🥇 **Business Analysis** (27.3%) and **SQL** (18.7%) are the top demanded skills
- 🏙️ **Cairo** dominates with **73.7%** of all data job postings
- 🚪 Only **1.9%** of data roles are entry-level — **3× harder to break into** than average
- 🏠 Remote data jobs are rare — just **1.0%** vs 3.9% across all jobs
- 📅 Most roles require **3–5 years** of experience

---

## 🗂️ Project Structure

```
egypt-job-market-analysis/
│
├── app.py                  # Streamlit dashboard
├── data_jobs_clean.csv     # Cleaned dataset (209 data roles)
├── skills_analysis.csv     # Skills frequency table
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
└── assets/
    ├── linkedin_tab1.png   # Dashboard preview — Tab 1
    └── linkedin_tab2.png   # Dashboard preview — Tab 2
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core language |
| **Pandas** | Data cleaning & EDA |
| **Plotly** | Interactive charts |
| **Streamlit** | Web dashboard |

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/MarwanEssa2006/egypt-job-market-analysis.git
cd egypt-job-market-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📦 Requirements

```
streamlit==1.35.0
pandas==2.2.2
plotly==5.22.0
```

---

## 📊 Dataset

- **Source:** [Wuzzuf Jobs Dataset — Kaggle](https://www.kaggle.com/)
- **License:** Apache 2.0
- **Size:** 2,533 job listings
- **Data jobs extracted:** 209 rows after keyword filtering

**Keywords used to filter data roles:**
`data analyst`, `data engineer`, `data scientist`, `business intelligence`,
`bi analyst`, `reporting analyst`, `database`, `analytics`

**Excluded:**
`financial analyst`, `financial planning`, `finance analyst`

---

## 💡 Dashboard Features

- **Interactive filters** — city, work model, experience level, job type
- **Real-time KPI cards** — update with filters applied
- **6 chart types** — horizontal bar, donut, treemap, histogram, grouped bar, vertical bar
- **2 tabs** — Data Jobs Overview + Data vs General Market
- **Fully responsive** — works on mobile and desktop
- **Wuzzuf blue theme** with glassmorphism design

---

## 👤 Author

**Marwan Hassan Essa**
- 📧 marwanessa402@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/marwanessa-fullstack)
- 🐙 [GitHub](https://github.com/MarwanEssa2006)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

> *Built as part of a personal data analytics portfolio project — March 2026*
