from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools.semanticSearch import semanticSearchTool
from tools.normalQueryTools import search_by_experience_tool,search_by_name_tool
import os

load_dotenv()

# Declaring the Gemini Key
GEMINI_API_KEY = os.getenv("geminiAPIKEY")


# Initialize Gemini LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",  # free tier model
#     temperature=0.7,
#     google_api_key=GEMINI_API_KEY
# ) # DON'T TRY THIS - TOO SLOW

# Declaring the llm
llm = ChatOpenAI( # SET UP your OpenAI API KEY in the env with OPENAI_API_KEY="YOUR API KEY"
    temperature=0,
    model="gpt-4o-mini",
    verbose=True
)

# Define the HR Agent (no tools yet, just chat)
hr_agent = initialize_agent(
    tools=[semanticSearchTool,search_by_name_tool,search_by_experience_tool],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    agent_kwargs = {
    "system_message": """
        You are an HR Assistant.
        - Answer only HR-related queries.
        - Decide which tool to use based on the query:
            - For simple queries like searching by name or years of experience, call the appropriate basic tool.
            - For complex queries involving multiple skills, projects, or domain-specific requirements, use the semantic search tool.
        - Format the final response as a professional, conversational HR recommendation.
        - For each top candidate, provide: - Full name in bold - Years of relevant experience - Specific projects they worked on that are relevant - Key skills (technical or domain-specific) - Availability status - Notable achievements or publications if available - Present the information as a natural, professional message suitable for an HR recommendation. - Keep the response concise but informative. Example format: "Based on your requirements for [role/skills/project], I found [X] excellent candidate(s): **[Candidate Name]** . She/He has [Y] years of [skill/domain] experience and specifically worked on '[Project Name]' where [brief contribution]. Her/His skills include [skills list]. [Availability]. [Notable achievements].""
        """
    }
)
