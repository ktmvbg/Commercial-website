from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from langchain.prompts.prompt import PromptTemplate

_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:

{table_info}

Use LIKE operator to match strings. Unit price is VND.
If question is about product information, return product name, unit price, and description.

Question: {input}"""
PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
)

OPENAPI_API_KEY = ""
SQL_CONNECTION_STRING = "postgresql://postgres:123456@localhost/ecom"

db = SQLDatabase.from_uri(SQL_CONNECTION_STRING)
llm = OpenAI(temperature=0, verbose=True, openai_api_key=OPENAPI_API_KEY)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, use_query_checker=True, prompt=PROMPT)
db_chain.run("Thông tin sản phẩm spotify 1 năm")