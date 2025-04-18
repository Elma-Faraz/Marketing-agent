from crewai import Agent, Task, Crew, LLM

font_conditions = '''
    Coforge Brand Prompt Guide for Content Generation
LinkedIn Post Prompt Template

Write a LinkedIn post of 300-400 words for Coforge readers on the topic: "{insert topic here}".
Follow this structure:
- Hook (20–30 words): Start with a question or attention-grabbing statement.
- Introduction (50–100 words): Contextualize the topic within the industry/domain.
- Industry Trends: Provide 3–5 bullet points.
- Coforge's Point of View: 100–150 words of insights or unique perspectives.
- CTA (Call to Action): 25–50 words encouraging engagement.

Tone: professional, concise, and informative. Use SEO-rich keywords and include technical details if relevant.

SEO Blog Prompt Template

Write an SEO-friendly blog post of around 800-1000 words on the topic: "{insert topic here}". Focus on the latest advancements and their impact on the "{domain}" industry.

Structure:
- Introduction: Define topic and its relevance.
- Trends: Explore AI, ML, IoT, Blockchain, etc.
- Use Cases: Provide real-world examples, include Coforge solutions.
- Customer Experience: Highlight improvements due to technology.
- Disruptors: Mention startups and innovation.
- Challenges & Opportunities: Discuss key hurdles and benefits.
- Future Outlook: Predict future trends and technologies.
- CTA: Encourage readers to engage or contact Coforge.

Tone: Professional, informative, and aligned with Coforge’s brand. Use SEO-rich keywords and technical details.

Brand Voice Notes

- Objective: Set clear goals for the content.
- Target Audience: Coforge readers and professionals in relevant domains.
- Tone: Informative, confident, professional.
- Examples: Include case studies or statistics for credibility.
- Technicality: Adapt based on audience — beginner, intermediate, or advanced.
- SEO: Use relevant keywords to enhance visibility.
- Review: Proofread and ensure alignment with Coforge standards.


'''
product_specs = '''
Product Nme:
Instagram Caption Generator
Overview:
Instagram Caption Generator is an AI-powered tool that automates Instagram caption creation for product marketing. It intelligently crafts engaging and professional posts based on predefined guidelines and product details, ensuring consistency and high-quality content.
Key Features:
AI-Driven Content Generation – Automatically creates engaging Instagram captions based on provided guidelines and product specifications.
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
🚀 Ready to elevate your LinkedIn content? Automate your posts with LinkedIn Post Generator and create engaging, high-quality content effortlessly!
'''
 
# Prompt Generator Agent
prompt_generator = Agent(
    role="Prompt Generator",
    goal="Transform raw guidelines and product specifications into a structured and clear prompt.",
    backstory="A detail-oriented AI assistant that ensures the prompt is precise and well-structured.",
    llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
    verbose=True,
    memory = f"""
    Here are the necessary detaials for generating a structured prompt:
    
    **Guidelines**: {font_conditions}
    **Product Specifications(!Important)**: {product_specs}
    
    Ensure that the output strictly follows both the guidelines and product specifications. Do not introduce unrelated products.
    
    """
)
 
# Writer Agent
writer_agent = Agent(
    role="Writer",
    goal="Generate an engaging LinkedIn post based on the structured prompt provided.",
    backstory="A creative marketing expert skilled at crafting professional LinkedIn posts.",
    llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
    verbose=True
)
 
# Proofreader Agent
proofreader_agent = Agent(
    role="Proofreader",
    goal="Review the LinkedIn post to ensure adherence to guidelines and product relevance.",
    backstory="A strict editor ensuring quality, accuracy, and compliance with given specifications.",
    llm=LLM(model="ollama/llama3.2", base_url="http://localhost:11434"),
    verbose=True
)
 
# Define tasks
prompt_task = Task(
    description=f"Clear a structured prompt that follows the provided guidelines: {font_conditions} and focuses strictly on the specified product and its features:{product_specs}. The output must not reference any other products.",
    expected_output="A well structured prompt containing tone and style, product details, post length, mandatory keywords/hashtags, and strict instructions to focus only on the given product.",
    agent=prompt_generator
)
 
write_task = Task(
    description="Generate an engaging LinkedIn post following the structured prompt provided.",
    expected_output="A professional and engaging LinkedIn post of 300-400 words, focusing strictly on the provided product and specifications.",
    agent=writer_agent
)
 
proofread_task = Task(
    description="Proofread the LinkedIn post to ensure it adheres to the product specifications and guidelines strictly.",
    expected_output="A validation report stating whether the post adheres to the product specifications and guidelines strictly. Suggests and implements necessary changes if required.",
    agent=proofreader_agent
)
 
# Create Crew
crew = Crew(
    agents=[prompt_generator, writer_agent, proofreader_agent],
    tasks=[prompt_task, write_task, proofread_task],
    embedder=None,
)



# inputs = {
#     "font_conditions": font_conditions,
#     "product_specifications": product_specs
# }
# Execute the process
crew.kickoff()














# # Define tasks
# prompt_task = Task(
#     description="Clear a structured prompt that follows the provided guidelines and focuses strictly on the specified product and its features. The output must not reference any other products.",
#     expected_output='''
#         "A well-structured prompt containing",
#         "- Tone and style- e.g., professional but engaging with a compelling call to action.",
#         "- Product details- e.g., key features, benefits, and use cases.",
#         "- Post Length- e.g., concise and engaging within LinkedIn character limits.",
#         "- Mandatory Keywords/Hashtags- If applicable.",
#         "- Strict Instructions to focus only on the given product."
#         ''',
#     agent=prompt_generator
# )
 
# write_task = Task(
#     description="Generate an engaging LinkedIn post following the structured prompt provided.",
#     expected_output='''
#         "A concise LinkedIn post",
#         "Engaging, product-focused, audience-relevant content and well structured.",
#         "Includes features, benefits, and a compelling call to action.",
#         "Uses clear and professional language with relevant hashtags (if specified)."
#         ''',
#     agent=writer_agent
# )
 
# proofread_task = Task(
#     description="Proofread the LinkedIn post to ensure it adheres to the product specifications and guidelines strictly.",
#     expected_output='''
#         "A validated LinkedIn post that:",
#         "- Strictly focuses on the given product and its features.",
#         "- Uses correct tone and structure.",
#         "- Has no irrelevant information or deviations from the guidelines.",
#         "- Is free of grammatical errors and typos.",
#         "A report highlighting any discrepancies or suggestions for improvement."
#         ''',
#     agent=proofreader_agent
# )