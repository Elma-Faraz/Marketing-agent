from crewai_tools import DallETool
import os
from dotenv import load_dotenv

"""Load environment variables and set up API keys."""
load_dotenv()

os.environ["AZURE_API_KEY"] = os.getenv("AZURE_API_KEY")
os.environ["AZURE_API_BASE"] = os.getenv("AZURE_ENDPOINT")
os.environ["AZURE_MODEL_NAME"] = "dall-e-3"
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_API_VERSION")


# Define the DALL-E tool

def create_dalle_tool():
    """
    Create a DALL-E tool for image generation.
    """
    return DallETool(model="azure/dall-e-3",
                     api_key=os.getenv("AZURE_API_KEY"),
                     size="1024x1024",
                     quality="standard",
                     n=1)