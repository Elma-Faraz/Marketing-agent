from crewai_tools import DallETool

# Define the DALL-E tool
dalle_tool = DallETool(model="dall-e-3",
                       size="1024x1024",
                       quality="standard",
                       n=1)