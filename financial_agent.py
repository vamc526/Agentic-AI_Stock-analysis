from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools


import os 
from dotenv import load_dotenv
load_dotenv()




#Agent one websearch agent 

web_search_agent = Agent(
    name = 'web search Agent',
    role= "Search the web for the information",
    model = Groq(id = "llama-3.2-90b-vision-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls = True,
    markdown= True,

)



#Financial Agent 
finance_agent = Agent(
    name = 'Finance AI Agent',
    model = Groq(id = "llama-3.2-90b-vision-preview"), 
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                           company_news= True) ], 
    instructions = ['Use tables to display data'],
    show_tools_calls = True,
    markdown = True,
)

multi_ai_agent = Agent(
    model = Groq(id = "llama-3.2-90b-vision-preview"),
    team = [web_search_agent, finance_agent],
    instructions = ["Always include sources","Use tables to display data"],
    show_too_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream = True)