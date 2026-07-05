# Data Science: Complete Roadmap, Resources & Career Guide

*Built for a BSCS student with existing EDA/pandas experience (Titanic, Google Play Store, Pakistani census, Ames Housing, career-recommendation dataset) and NAVTTC ML training.*

---

## What "Data Science" Actually Covers

Unlike CV or multimodal AI, data science is less about one deep technical stack and more about a full pipeline plus judgment:

```
Business/Research Question
    → Data Collection & Cleaning
        → Exploratory Data Analysis (EDA)
            → Statistical Analysis / Modeling
                → Communication (visualization, storytelling)
                    → Deployment / Decision Impact
```

You already have real reps on EDA (multiple full workflows completed) and modeling basics (KNN/DT/RF). This roadmap fills in statistics rigor, SQL/data engineering basics, and the storytelling/deployment side — which is usually where self-taught people are weakest and where hiring managers actually filter.

---

## PHASE 0 — Statistics Foundation (the actual differentiator)

This is the single biggest gap between "someone who ran `.describe()` and made a heatmap" and an actual data scientist. Don't skip this phase — it's where interviews and real analysis quality come from.

| Topic | Why it matters | Resource |
|---|---|---|
| Descriptive statistics | You've done this in EDA already — formalize it | Khan Academy Statistics (free) |
| Probability distributions | Understanding your data's shape, choosing right tests | *Think Stats* (free book, Python-based — fits your workflow) |
| Hypothesis testing (t-test, chi-square, ANOVA) | "Is this difference real or noise?" — core DS skill | StatQuest (YouTube, Josh Starmer — genuinely excellent, free) |
| Confidence intervals & p-values | Communicating uncertainty correctly | Same StatQuest series |
| A/B testing | The #1 practical statistics application in industry DS roles | *Trustworthy Online Controlled Experiments* (Kohavi et al.) — the standard reference |
| Correlation vs. causation, confounders | Avoiding the most common analytical mistake | Any intro causal inference primer — e.g., *Causal Inference: The Mixtape* (free online, Scott Cunningham) |
| Bayesian thinking (basics) | Increasingly expected, especially for experimentation roles | *Think Bayes* (free book) |

**Milestone:** Re-analyze one of your existing datasets (e.g., Ames Housing or Pakistani census) but this time formally test a hypothesis — e.g., "is there a statistically significant price difference between X and Y neighborhoods?" — with a proper test and confidence interval, not just a visual comparison.

---

## PHASE 1 — SQL & Data Engineering Basics (3–4 weeks)

Almost every real DS job starts with "can you actually get the data" — this is non-negotiable and often skipped by self-taught learners.

- **Course:** *SQL for Data Science* (free on Coursera, UC Davis) or Mode Analytics' free SQL tutorial (widely used, practical)
- **Practice:** **LeetCode SQL** or **StrataScratch** — practice actual interview-style SQL questions
- **Topics:**
  - Joins (all types), window functions, CTEs, subqueries
  - Aggregations, GROUP BY logic
  - Query optimization basics (indexes, why some queries are slow)
- **Bonus (given your dev background):** Learn how data actually gets into a warehouse — basic ETL/ELT concepts, what tools like Airflow do conceptually (you don't need to master this, just know it exists and why)

**Milestone:** Recreate one of your pandas-based EDA workflows entirely in SQL against a database (load one of your existing CSVs into SQLite/Postgres and do the same analysis via queries).

---

## PHASE 2 — Deepen EDA & Feature Engineering (you're already strong here — sharpen it)

You've done full EDA cycles already. Push toward the parts that separate junior from senior analysis.

- **Book:** *Feature Engineering for Machine Learning* (Alice Zheng & Amanda Casari, O'Reilly) — practical, not just theory
- **Course:** Kaggle's free **"Feature Engineering"** micro-course (short, hands-on)
- **Topics to add on top of your existing EDA skill:**
  - Handling class imbalance (SMOTE, class weighting) — you'll hit this constantly in real datasets
  - Outlier treatment strategies beyond just IQR/Z-score (robust scaling, domain-informed capping)
  - Feature selection (mutual information, recursive feature elimination) vs. just throwing everything into a model
  - Time-series-specific EDA (seasonality, trend decomposition, autocorrelation) — a common gap if you've only worked with tabular snapshot data so far

**Milestone:** Take one of your past EDA projects and add a full feature engineering pass — document *why* each feature was created, not just that it was created (this "why" is what interviewers actually probe).

---

## PHASE 3 — Statistical Modeling & Machine Learning for DS (2–3 months)

You have KNN/DT/RF. Now build the breadth and the *judgment* about when to use what — this matters more in DS than knowing every algorithm.

- **Course:** Andrew Ng's *Machine Learning Specialization* (if not done) — still the best on-ramp
- **Book:** *An Introduction to Statistical Learning* (ISLR, free PDF, James/Witten/Hastie/Tibshirani) — the standard DS reference, has R and Python versions
- **Course:** *Applied Data Science with Python Specialization* (University of Michigan, Coursera)
- **Topics:**
  - Linear/logistic regression — done *properly* (assumptions, diagnostics, interpretation of coefficients), not just as a black box
  - Regularization: Ridge, Lasso, Elastic Net
  - Ensemble methods beyond Random Forest: Gradient Boosting (XGBoost, LightGBM — these dominate real-world tabular DS work)
  - Model evaluation beyond accuracy: precision/recall/F1, ROC-AUC, calibration — and *which metric fits which business problem*
  - Cross-validation done correctly (especially with time-series or grouped data, where naive k-fold leaks information)
  - Clustering (K-means, hierarchical) and dimensionality reduction (PCA) for unsupervised work

**Milestone:** Take a Kaggle tabular competition (not a toy dataset — an actual live/past competition), and get a model into a respectable percentile using XGBoost/LightGBM with proper cross-validation.

---

## PHASE 4 — Communication & Business Impact (ongoing, but start now)

This is the most underrated phase and the one that actually determines whether you get hired/promoted. Technical skill gets you in the door; communication determines your ceiling.

- **Book:** *Storytelling with Data* (Cole Nussbaumer Knaflic) — short, practical, widely referenced in the industry
- **Book:** *The Truthful Art* (Alberto Cairo) — deeper dive on visualization done honestly
- **Practice:** Take every EDA project you've already done and rewrite the summary as if presenting to a non-technical manager — one page, no jargon, clear recommendation
- **Tooling:** Learn to build a simple dashboard (Streamlit or Plotly Dash — Python-based, fits your stack) rather than only static notebooks

**Milestone:** Turn one of your existing EDA projects (e.g., career-recommendation dataset) into a short Streamlit dashboard with a clear narrative, not just charts.

---

## PHASE 5 — Deployment & Production Awareness (1–2 months)

Most self-taught data scientists never ship anything — this is a real differentiator, and it plays directly to your existing full-stack strength.

- **Topics:**
  - Model serialization (pickle, joblib, ONNX basics)
  - Serving a model via a simple API (FastAPI — you already have teammates using this on your career-advisor project, good overlap)
  - Basic MLOps awareness: what experiment tracking (MLflow/wandb), model versioning, and monitoring for drift actually mean — you don't need to master a full MLOps stack, just understand why it exists
  - Cloud basics: at least one of AWS/GCP/Azure at a beginner level (S3-equivalent storage, a managed notebook environment, a basic deployment target)

**Milestone:** Take a trained model from one of your projects and wrap it in a small FastAPI service with a `/predict` endpoint, deployed somewhere simple (Render, Railway, or similar free-tier host).

---

## Capstone Options (pick one)

1. **End-to-end Pakistani-context project** — e.g., using the Pakistani census data you've already worked with, build a full pipeline: SQL-backed data storage → statistical analysis with real hypothesis tests → a predictive model → a Streamlit dashboard telling a clear story (e.g., regional disparities, some socioeconomic trend). This is genuinely differentiated since most portfolio projects use generic Western datasets (Titanic, housing prices).
2. **A/B testing simulation project** — simulate an experiment (e.g., on synthetic e-commerce data), and do a full proper analysis: power calculation, statistical test, confidence intervals, and a clear go/no-go recommendation. This directly targets the #1 skill industry DS interviews probe.
3. **Time-series forecasting project** — pick a domain (sales, weather, currency — PKR/USD is topical) and build a proper forecasting model (ARIMA/Prophet/or a gradient-boosted approach with lag features), with honest backtesting.
4. **Career-advisor project, formalized** — you already have this in progress as an ML lead. Push it to include proper statistical validation of your model choices (not just "Random Forest got highest accuracy") and a deployed, story-driven dashboard — this could double as your DS portfolio piece with minimal extra scope.

---

## Career Options

| Role | What it involves | Fits you if... |
|---|---|---|
| **Data Analyst** | SQL, dashboards, reporting, lighter statistics | Good entry point if you want to start working sooner while building deeper skills |
| **Data Scientist** | Full pipeline: stats, modeling, communication | The core target of this roadmap |
| **Machine Learning Engineer** | Production ML systems, less business-analysis, more engineering | Strong fit given your full-stack + ML background — significant overlap with your other roadmaps |
| **Business/Product Analyst** | Less technical modeling, more metrics + business judgment | If you enjoy the storytelling/impact side more than deep modeling |
| **Data Engineer** | Building the pipelines that feed everything above | If you find yourself enjoying Phase 1 (SQL/ETL) more than modeling |
| **Quantitative/Research Analyst** | Heavier statistics/finance-specific modeling | If you want to specialize toward finance later |

### Companies/ecosystem to know
- **Every industry now hires DS roles** — this is the most universally applicable of your three roadmaps (CV/AV, multimodal AI, and this one). Fintech, e-commerce, telecom, healthcare, logistics all hire heavily.
- **Pakistan-specific context:** Local tech companies (Bykea, Airlift-successors, fintechs like NayaPay/SadaPay, telecoms like Jazz/Telenor) all run internal data teams — this is one of the roadmaps where **local jobs genuinely exist**, unlike AV which is geographically concentrated abroad.
- **Remote/freelance angle:** Data analysis, dashboarding, and lighter ML work are extremely common on Upwork/Fiverr-style platforms and also through direct freelance/contract work with startups — a realistic near-term income path given your dev background lets you deliver the full "analysis + dashboard + deployed app" package, not just a notebook.
- **Global remote roles:** DS/analyst roles are among the more remote-friendly tech roles globally, more so than AV-specific or even much research-heavy multimodal AI work.

---

## Future Potential

- Data science as "run stats and build a model" is being partially automated/compressed by AutoML and LLM-assisted analysis — but the roles that combine **domain judgment, correct statistical reasoning, and clear communication** remain very durable, because those are exactly the parts that are hardest to automate.
- **The bar has risen** — "I can use pandas and sklearn" is now a baseline expectation, not a differentiator. Statistics rigor (Phase 0) and business communication (Phase 4) are where you'll actually stand out, especially early in your career.
- **Analytics engineering** (a newer hybrid of data engineering + analytics, centered on tools like dbt) is a fast-growing niche worth knowing exists, especially if Phase 1 (SQL) turns out to be something you enjoy.
- **LLM-assisted data work** (using LLMs to help write analysis code, generate SQL, summarize findings) is becoming standard tooling — worth being comfortable with, but doesn't replace the underlying judgment this roadmap builds.
- Of your three roadmaps (self-driving/AV, multimodal AI, and this one), **data science is the most immediately employable and geographically flexible** — it's a reasonable "day job" specialization to run in parallel with a longer-term AV or multimodal AI specialization if you want to keep options open while building toward the more competitive, geographically concentrated fields.

---

## Do's and Don'ts

### Do
- **Prioritize statistics over collecting more ML algorithms.** You already know KNN/DT/RF/XGBoost is learnable in weeks — proper hypothesis testing and knowing when correlation isn't causation is what actually separates skill levels in this field.
- **Learn SQL properly and prove it** — it's asked in nearly every DS interview and used far more day-to-day than people expect coming from a pure ML background.
- **Use local/regional datasets and context where you can** (Pakistani census, PKR-related time series, regional e-commerce) — it makes your portfolio distinctive instead of "another Titanic notebook," and it's genuinely useful if you're targeting local companies.
- **Practice explaining findings to a non-technical audience** — this is a trainable skill, not an innate talent, and it's the one most self-taught data scientists never practice.
- **Ship at least one deployed, interactive artifact** (a Streamlit dashboard, a small API) — this plays directly to your full-stack strength and instantly differentiates you from candidates who only have static notebooks.
- **Learn to say "I don't have enough data/confidence to conclude that"** — knowing the limits of an analysis is a mark of seniority, not weakness, and interviewers specifically probe for this.

### Don't
- **Don't chase every new tool/library** — the fundamentals (SQL, stats, pandas, one solid modeling library) matter far more than breadth of tool exposure. A DS interview rarely tests "do you know tool X"; it tests reasoning.
- **Don't present a model's accuracy without context** — "95% accuracy" on an imbalanced dataset (95% majority class) is meaningless; always sanity-check against a baseline and pick metrics that match the actual business question.
- **Don't skip the "so what" in your analysis** — a chart or a p-value alone isn't a data science project; every project needs a clear recommendation or conclusion at the end.
- **Don't confuse correlation with causation in your write-ups** — this is the single most common credibility-killer in junior DS work, and it's an easy trap when you're excited about a finding.
- **Don't ignore data quality issues** — you already handle nulls/outliers well from your EDA experience, but extend that instinct to questioning *how* the data was collected and what biases that introduces, not just cleaning what's visibly messy.
- **Don't treat this as separate from your CV/multimodal work** — a huge amount of real-world data science now involves unstructured data (images, text) alongside tabular data. Your CV and NLP-adjacent skills from the other two roadmaps are a genuine advantage here, not a separate track.

---

## Suggested Order of Attack (given your current standing)

1. **Now–Month 1:** Statistics foundation (Phase 0) — this is your highest-leverage gap given how strong your EDA/pandas skills already are.
2. **Month 1–2:** SQL (Phase 1) — short, high-ROI, commonly tested in interviews, currently a gap based on your project history.
3. **Month 2–3:** Feature engineering sharpening (Phase 2) — fast, since you already have the base EDA skill.
4. **Month 2–4 (parallel):** Modeling breadth — XGBoost/LightGBM, proper cross-validation, metric selection (Phase 3).
5. **Month 3–5:** Communication practice (Phase 4) — start this early and keep doing it throughout, it compounds.
6. **Month 4–6:** Deployment (Phase 5) + capstone — likely your Pakistani-context project or the formalized career-advisor project, since both are already close to in-flight.

---

*Data science moves slower than AV/multimodal AI in terms of "new model every few months" — most of what's in this roadmap will stay relevant for years. Revisit every 4–6 months mainly to update tooling (new library versions, maybe a new gradient-boosting library) rather than core concepts.*
