from dotenv import load_dotenv

load_dotenv()

from griptape.drivers import OpenAiChatPromptDriver
from griptape.structures import Agent

agent = Agent(
    prompt_driver=OpenAiChatPromptDriver(
        model="gpt-3.5-turbo"
    )
)

agent.run(
    "based on https://www.griptape.ai/, tell me what Griptape is"
)
