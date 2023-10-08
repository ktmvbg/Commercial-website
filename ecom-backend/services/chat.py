from sqlalchemy.orm import Session, joinedload
from models import *
from dtos.chat import CreateChatMessage
import openai

from langchain.llms import OpenAI, OpenAIChat
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from langchain.prompts.prompt import PromptTemplate

FINE_TUNED_MODEL = "davinci:ft-personal-2023-08-14-17-48-17"
CONTEXT_FINE_TUNED_MODEL = "davinci:ft-personal-2023-09-20-14-24-58"
RESPONSE_FINE_TUNED_MODEL = "davinci:ft-personal-2023-09-20-14-54-18"

OPENAPI_API_KEY = ""
SQL_CONNECTION_STRING = "postgresql://postgres:123456@localhost/ecom"


def create_chat_message(session: Session, user_id: int, chat_message: CreateChatMessage) -> Chat:
    chat = Chat(user_id=user_id, content=chat_message.message)
    session.add(chat)
    session.commit()
    session.refresh(chat)
    return chat


def response_message(session: Session, chat_id: int) -> Chat:
    chat = session.query(Chat).filter(Chat.id == chat_id).first()

    get_context_completion = openai.Completion.create(
        model=CONTEXT_FINE_TUNED_MODEL,
        prompt=chat.content,
        max_tokens=256,
        n=1,
        temperature=0.0,
        stop="###"
    )

    prompt = get_context_completion.choices[0].text + \
        "###" + "Customer:" + chat.content + "\n" + "Agent:"

    response = openai.Completion.create(
        model=RESPONSE_FINE_TUNED_MODEL,
        prompt=prompt,
        max_tokens=256,
        n=1,
        temperature=0.0,
        stop="\n"
    )
    chat.prompt = prompt
    chat.response = response.choices[0].text
    session.commit()
    session.refresh(chat)
    return chat


def langchain_response_message(session: Session, chat_id: int) -> Chat:
    chat = session.query(Chat).filter(Chat.id == chat_id).first()

    get_context_completion = openai.Completion.create(
        model=CONTEXT_FINE_TUNED_MODEL,
        prompt=chat.content,
        max_tokens=30,
        n=1,
        temperature=0.0,
        stop="###"
    )

    if ("Specific information: Pricing" in get_context_completion.choices[0].text):
        print("Specific information: Pricing")
        # _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the query result and return the answer.
        # Use the following format:

        # Question: "Question here"
        # SQLQuery: "SQL Query to run"
        # SQLResult: "Result of the SQLQuery"
        # Answer: "Final answer here"

        # Only use the following tables:

        # {table_info}

        # Use LIKE operator to match strings. Unit price is VND. Return product name and price.

        # Question: {input}"""

        _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the query result and return the answer.

        Only use the following tables:

        {table_info}

        Use LIKE operator to match strings. Unit price is VND. Return product name and price.
        
        Question: {input}"""
        PROMPT = PromptTemplate(
            input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE
        )

        db = SQLDatabase.from_uri(SQL_CONNECTION_STRING)
        llm = OpenAI(temperature=0, verbose=True,
                     openai_api_key=OPENAPI_API_KEY)
        db_chain = SQLDatabaseChain.from_llm(
            llm, db, verbose=True, use_query_checker=True, prompt=PROMPT)
        chat.response = db_chain.run(chat.content)
        session.commit()
        session.refresh(chat)
        return chat
    else:
        prompt = get_context_completion.choices[0].text + \
            "###" + "Customer:" + chat.content + "\n" + "Agent:"

        response = openai.Completion.create(
            model=RESPONSE_FINE_TUNED_MODEL,
            prompt=prompt,
            max_tokens=30,
            n=1,
            temperature=0.0,
            stop="\n"
        )
        chat.prompt = prompt
        chat.response = response.choices[0].text
        session.commit()
        session.refresh(chat)
        return chat


def gpt35_response_message(session, chat_id) -> Chat:
    chat = session.query(Chat).filter(Chat.id == chat_id).first()

    FIRST_PROMPT = open("1.txt", "r").read()

    SECOND_PROMPT = open("2.txt", "r").read()

    first_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": FIRST_PROMPT
            },
            {
                "role": "user",
                "content": chat.content
            }
        ],
    )

    first_response = first_response.choices[0].message.content
    if (first_response == "No" or first_response == "No."):
        prompt = open("3.txt", "r").read()
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": chat.content
                }
            ]
        )
        second_response = second_response.choices[0].message.content
        # chat.prompt = prompt
        chat.response = second_response
        session.commit()
        session.refresh(chat)
        return chat

    first_response = [x.lower() for x in first_response]
    first_response = ''.join(first_response)
    if ("yes" in first_response):
        shop_info = open("7.txt", "r").read()
        prompt = shop_info
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": chat.content
                }
            ]
        )
        second_response = second_response.choices[0].message.content
        # chat.prompt = prompt
        chat.response = second_response
        session.commit()
        session.refresh(chat)
        return chat

    file = None

    products = ["spotify premium upgrade",
                "netflix shared slot", "youtube premium upgrade"]
    if products[0] in first_response:
        file = open("5.txt", "r")
    elif products[1] in first_response:
        file = open("4.txt", "r")
    elif products[2] in first_response:
        file = open("6.txt", "r")
    else:
        file = open("3.txt", "r")
    prompt = SECOND_PROMPT.replace("{Summary}", first_response).replace(
        "{Specific infos}", file.read())
    second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": chat.content
            }
        ]
    )
    second_response = second_response.choices[0].message.content
    # chat.prompt = prompt
    chat.response = second_response
    session.commit()
    session.refresh(chat)
    return chat
