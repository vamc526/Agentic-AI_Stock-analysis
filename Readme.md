# **Stock Analysis AI Agent 🤖📈**
An AI-powered agent system that analyzes stock performance by integrating real-time news sentiment and financial data

## Project Overview

This AI agent system combines web intelligence and financial analysis to provide comprehensive stock insights:

🕵️ Web Search Agent scours news sources for market sentiment

💹 Financial Agent analyzes stock fundamentals and recommendations

🤖 Powered by Groq's ultra-fast LLM (Llama-3.2-90b) for real-time analysis

## Business Goal: 
Transform complex financial data into actionable insights by combining analyst recommendations with market news analysis.

### Key Features
Multi-Agent Architecture

Web Search Agent (DuckDuckGo integration)

Financial Analysis Agent (Yahoo Finance integration)

Real-Time Data Synthesis

Stock prices & fundamentals

Analyst recommendations

Latest company news

Intelligent Presentation

Automatic table formatting

Source verification

Markdown reports

#### Quick Start
Installation
bash
Copy
# Clone repository
git clone https://github.com/yourusername/stock-analysis-ai.git
cd stock-analysis-ai

## Install dependencies
```
pip install -r requirements.txt
```

# Set up environment
cp .env.example .env
Configuration
Get Groq API Key

Update .env:

env
Copy
GROQ_API_KEY=your_api_key_here
Usage
python
Copy
# Run analysis for any stock
```
python main.py --stock NVDA
```
Example Request:

python
Copy
mutli_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA", 
    stream=True
)

Agent Architecture
1. Web Search Agent 🌐
Tools: DuckDuckGo Search API

Functions:

News aggregation

Market sentiment analysis

Source validation

2. Financial Analysis Agent 💹
Tools: Yahoo Finance API (yfinance)

Functions:

Real-time stock prices

Analyst recommendations

Fundamental analysis

Historical performance

Multi-Agent Collaboration
Web Agent gathers market news

Financial Agent analyzes quantitative data

Groq LLM synthesizes insights

Unified report generation

Sample Output
markdown
Copy
## NVIDIA Corporation (NVDA) Analysis

### Financial Overview
| Metric          | Value       |
|-----------------|-------------|
| Current Price   | $132.45     |
| 52-Week High    | $140.76     |
| P/E Ratio       | 78.34       |

### Analyst Recommendations
| Firm          | Rating | Price Target |
|---------------|--------|--------------|
| Morgan Stanley| Buy    | $160         |
| Goldman Sachs | Hold   | $135         |

### Recent News
1. "NVIDIA announces breakthrough in AI chips" (Source: TechCrunch)
2. "Partnership with AWS expands cloud AI offerings" (Source: Reuters)
Dependencies
Package	Use Case
phidata	Agent framework
fastapi	Web interface
yfinance	Financial data
duckduckgo-search	News aggregation
groq	LLM processing
python-dotenv	Environment management
License

MIT License - Free for academic and commercial use with proper attribution.


