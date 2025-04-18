from agents import edited_content_validator_agent, content_regenerator_agent
from tasks import edited_content_validator_task, regenerate_content_task
from utils import crew_result, additional_instructions, combined_inputs, process_uploaded_file
def generate_edited_content_report(edited_content, user_guidelines, configurations:dict=None): 
    try:
        # Executing Edited Content Validation task
        validator_agent = edited_content_validator_agent()
        validator_task = edited_content_validator_task(edited_content, user_guidelines)
        if configurations is not None:
            configurations_instructions = additional_instructions(configurations)
            validator_task = edited_content_validator_task(edited_content, configurations_instructions )
        edited_content_report = crew_result([validator_agent], [validator_task])
        
        return edited_content_report
    except Exception as e:
        print(f"Error during generate_edited_content_report: {e}")
        return "No report generated."
    
def regenerate_content(edited_content, user_guidelines,user_instructions, configurations:dict):
    try:
        configurations_instructions = additional_instructions(configurations)
        
        combined_instructions = combined_inputs(user_guidelines, user_instructions, configurations_instructions)
        # Executing Edited Content Validation task
        regenerator_agent = content_regenerator_agent()
        regenrator_task = regenerate_content_task(edited_content, combined_instructions)
        edited_content_report = crew_result([regenerator_agent], [regenrator_task])
        
        return edited_content_report
    except Exception as e:
        print(f"Error during write_edited_content: {e}")
        return "No content generated."
    
user_guuidelines_path  = "input_guide/Updated_Brand_Prompt_Guide.docx"
user_guidelines = process_uploaded_file(user_guuidelines_path)
user_instructions = """
Product Name:
LinkedPost AI
Overview:
LinkedPost AI is an AI-powered tool that automates LinkedIn post creation for product marketing. It intelligently crafts engaging and professional posts based on predefined guidelines and product details, ensuring consistency and high-quality content.
Key Features:
AI-Driven Content Generation – Automatically creates engaging LinkedIn posts based on provided guidelines and product specifications.
Customizable Writing Style – Ensures posts align with specific tone, structure, and formatting requirements.
Seamless Product Integration – Highlights key product features and benefits in a compelling way.
Optimized for Engagement – Generates posts designed to capture attention and drive interactions on LinkedIn.
Hashtag & CTA Support – Adds relevant hashtags and calls to action for better reach and engagement.
Target Audience:
Marketing professionals
Product managers
Content creators
Social media strategists
Business owners & startups
Call to Action:
🚀 Ready to elevate your LinkedIn content? Automate your posts with LinkedPost AI and create engaging, high-quality content effortlessly!
"""

configurations = {
            "length": "200",
            "tone": "Formal",
            "target_audience": "Marketing professionals",
            "technicality":"Intermediate",
            "content_type":"LinkedIn Post",
        }

edited_content = """
* Exciting Launch: Meet TARA – Your AI-Powered Assistant

**Introduction  
In today’s fast-paced corporate landscape, seamless HR and IT support is vital for employee productivity and satisfaction. At Coforge, we’re proud to introduce TARA, our innovative AI-powered chatbot designed specifically to streamline HR and IT processes for our valued employees.

**Key Capabilities  
TARA is equipped with robust functionalities that revolutionize day-to-day support:  
• Provides quick and accurate information on HR policies  
• Assists with leave applications, attendance verification, and HR-related queries  
• Offers support for IT-related questions and facilitates service request and incident management  
• Available 24/7 to ensure you receive instant, reliable assistance whenever needed

I want to add a few more lines to this content:
    Integrates seamlessly with existing systems to enhance user experience

Harnessing cutting-edge AI technology, TARA empowers employees by reducing wait times, enhancing efficiency, and improving overall operational experience within the organization. Our commitment to innovation is reflected in TARA’s ability to integrate effortlessly with current systems, ensuring that you have the tools necessary to succeed at work.

**Call to Action  
Explore TARA today and experience the future of workplace support. Share your experiences in the comments and let us know how TARA has transformed your daily interactions. 

#AI #HRTech #Chatbot #EmployeeExperience
"""
generate_report = generate_edited_content_report(edited_content, user_guidelines, configurations=None)
print("Generated report",generate_report)
generate_regenerated_content = regenerate_content(edited_content, user_guidelines, user_instructions, configurations)
print("Regenerated Content",generate_regenerated_content)