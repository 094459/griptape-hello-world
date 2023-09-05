from dotenv import load_dotenv

load_dotenv()

import boto3
from griptape.drivers import AmazonSageMakerPromptDriver
from griptape.drivers import SageMakerFalconPromptModelDriver

from griptape.structures import Agent

agent = Agent(
    prompt_driver=AmazonSageMakerPromptDriver(
        model="huggingface-pytorch-sagemaker-endpoint",
        session=boto3.Session(region_name="eu-west-1"),
        prompt_model_driver_type=SageMakerFalconPromptModelDriver,
    )
)

agent.run(
    "based on https://www.griptape.ai/, tell me what Griptape is"
)
