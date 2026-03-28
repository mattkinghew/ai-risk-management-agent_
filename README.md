# AI Risk Management Agent 🤖📈

A robust quantitative engine integrated with GenAI to translate complex financial risks into actionable, plain-language insights for the silver economy and retail investors.

## 🎯 Business Context (商業背景)

* **Situation:** Traditional financial risk metrics (like 95% Value at Risk and Expected Shortfall) are mathematically complex and unintuitive for average retail investors, especially retirees managing their pensions. 
* **Task:** Build a reliable bridge between hardcore quantitative models and human-centric financial advice, ensuring the underlying calculation engine is immune to data-type crashes from unstructured external inputs.
* **Action:** Engineered a bulletproof Python quantitative engine (stripping Pandas dataframes into pure NumPy arrays to prevent `unhashable type` errors) and integrated it with an LLM via Prompt Engineering.
* **Result:** Achieved a 0% crash rate in handling dynamic portfolio weights and successfully translated extreme tail-loss matrices into empathetic, jargon-free wealth management advice tailored for the silver economy.

[Image of AI risk management system architecture]

## 🏗 Architecture & Tech Stack (技術架構)

* **Quant Engine:** Python 3, `NumPy` (Bulletproof Matrix Multiplication, Flattening), `Pandas` (Data ingestion).
* **AI Layer:** `OpenAI API` / `Google Gemini API` (Semantic translation & Prompt Engineering).
* **Architecture:** API-ready / Microservice design pattern.
* **Environment:** `venv` (Isolated environment), `python-dotenv` (Credential management).

## 💡 Core Features (核心功能)

* **Bulletproof Quant Engine (防彈量化引擎):** Resolves common Autograder and external API crashes by forcefully decoupling indexing from data. Converts all incoming unstructured weights (Dicts, Series, multi-dimensional arrays) into flattened 1D pure numerical arrays before performing Cholesky decomposition and dot products.
* **Dynamic Risk Calculation (動態風險精算):** Automates the calculation of Minimum Variance Portfolios, Historical VaR (95%), and Expected Shortfall (CVaR) using Monte Carlo simulation principles.
* **LLM Insight Translation (AI 語意轉換):** Contextualizes statistical maximum losses into digestible narratives
