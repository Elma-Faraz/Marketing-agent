from crewai import Agent, LLM
from langchain.llms import Ollama
from tools import create_dalle_tool
import os
from dotenv import load_dotenv

"""Load environment variables and set up API keys."""
load_dotenv()
os.environ["AZURE_API_KEY"] = os.getenv("AZURE_API_KEY")
os.environ["AZURE_API_BASE"] = os.getenv("AZURE_ENDPOINT")
os.environ["AZURE_MODEL_NAME"] = os.getenv("DEPLOYMENT_NAME")
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_API_VERSION")

# Agent to generate content
def create_post_writer_agent(input):
    """Create a LinkedIn Post Writer Agent."""
    return Agent(
        role="Writer",
        goal="Generate an engaging Content based on the structured prompt provided.",
        backstory="A creative marketing expert skilled at crafting professional Content.",
        llm="azure/o3-mini",
        verbose=True,
        memory=f"""
        Here are the necessary details for generating an engaging LinkedIn post:

        {input}
        
        Ensure that the output strictly follows both the guidelines and product specifications. Do not introduce unrelated products.
        """
    )

#Agent to generate conflict report between user guidelines and configuration
def create_validator_agent(guidelines,product_specs):
    """Create a Comparison Agent."""
    return Agent(
        role = "Guideline Validator Expert",
        goal="Compare the provided guidelines and instructions to identify any conflicting or overlapping information regarding post length, tone, target audience, and other key parameters.",
        backstory="You ensure that the instructions align with the established guidelines. If differences are found, you notify the user.",
        llm="azure/o3-mini",
        verbose=True,
    )

#Agent to generate prompt for image generation    
def create_prompt_agent():
    """Create a Prompt Agent."""
    return Agent(
        role="Prompt Generator",
        goal="Designed to process the provided content and the branding guidelines to generate a detailed and structured prompt. This prompt will be consumed for the Image Generator agent to create a relevant and high quality image.",
        backstory="The agent processes provided content to identify the key themes and tone, while also incorporating companies branding guidelines, such as colors, design preference and logo usage.",
        llm="azure/o3-mini",
        verbose=True,
    )

#Agent to generate image
def create_image_generator_agent():
    """Create an Image Generator Agent."""
    dalle_tool = create_dalle_tool()
    return Agent(
        role='Image Generator',
        goal='Generate high-quality images for the LinkedIn posts.',
        verbose=True,
        memory=False,
        backstory=(
            "The Image Generator agent is equipped with state-of-the-art tools and techniques to create visually appealing "
            "and engaging images for the blog posts. With a keen eye for design and aesthetics, the agent leverages advanced "
            "image generation models to produce high-quality visuals that complement the written content. Whether it's product "
            "mockups, infographics, or illustrations, the agent can generate a wide range of images to enhance the overall appeal "
            "of the blog posts. By combining creativity with technical expertise, the Image Generator agent ensures that every image "
            "is tailored to the specific requirements of the task, helping to create a visually cohesive and impactful blog post."
        ),
        llm = "azure/o3-mini",
        tools=[dalle_tool],
        allow_delegation=False
    )
 #Agent to generate coflict report in edited content from user guidelines and configurations   
def edited_content_validator_agent():
    """Create an Edited Validator Agent."""
    return Agent(
        role = "Content Difference Detector",
        goal="To analyze the original and edited versions of content and identify the new content that has been added during the editing process.",
        backstory="In content generation workflows, especially those involving human-in-the-loop systems or collaborative editing, it's important to track what modifications are made to the original output. This agent was developed to help content teams, reviewers, or automation systems identify exactly what new text has been added to a piece of content after it has been edited. By focusing on additions, the agent helps in tracking enhancements, detecting inserted instructions, and ensuring compliance with tone, length, or guidelines.",
        llm="azure/o3-mini",
        verbose=True,
    )

#Agent to regenerate edited content.
def content_regenerator_agent():
    """Create a Regenerator Agent."""
    return Agent(
        role="Regenerator",
        goal="Generate a new content based on the user-edited content and the provided user guidelines.",
        backstory="You are an expert in content generation and editing. Your primary responsibility is to create high-quality content that align with the provided user guidelines. You will analyze the user-edited content and ensure it meets all specified requirements.",
        llm="azure/o3-mini",
        verbose=True,
    )