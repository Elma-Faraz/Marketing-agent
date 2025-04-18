from crewai import Task
from agents import create_post_writer_agent, create_image_generator_agent, create_validator_agent, create_prompt_agent, create_edited_validator_agent

def create_blog_write_task(input):
    """
    Creates a blog writing task dynamically based on the provided guidelines and product specifications.
    """
    post_writer_agent = create_post_writer_agent(input)
    return Task(
        description=(
            f'''
            Generate an engaging and professional LinkedIn/Blog/Email etc post based on ONLY the provided guidelines and instructions. The input consists of: 
            {input}
            
            1. Review **Guidelines**, **Instructions** and **Additional Instructions** provided in input.
            2. Give preference in the following order: Additional Instructions > Instructions > Guidelines.
            3. In **Additional Instructions**, content-type is mentioned. Generate the post for the provided content-type only. for example, if the content-type is LinkedIn post, generate a LinkedIn post only.
            3. If Additional Instructions are not provided or are None, use Guidelines > Instructions.
            4. Identify the required content type(LinkedIn Post, Blog Post, Email etc) based on the provided guidelines and instructions, if not mentioned in the input or it is "Other".
            5. Adjust tone, structure and length accordingly while maintaining clarity and engagement.
            6. Strictly follow the provided input in the given preference order.
            7. Maintain coherence, proper flow, and a professional or engaging tone as required.
            8. Incorporate product details, key messages, and branding elements as specified. Also provide a title for the post.
            9. Use language that aligns with the brand's voice and the target audience.
            10. Structure content for clarity and engagement.
            11. Format according to platform-specific best practices.
            12. Ensure proper grammar, spelling and readability.
            13. Provide a final version that is publication ready without requiring major edits.
            14. The title, headings, subheadings and paragraphs should be distinguishable and well structured. It should distinguish the heading, subheadings, etc in the below format:
                Indicate Heading1 with *
                Indicate Subheadings with **
            (It should just indicate heading levels with the asterisks)
            15. Write headings and its contents separately.
            
            '''
        ),
        expected_output="A well structured , grammatically perfect, and platform optimized content piece ensuring clarity, coherence, brand consistency and readiness for immediate publication.",
        agent=post_writer_agent,
        async_execution=False,
        output_file='new-blog-post.md'  # Example of output customization
    )
    
def create_validator_task(guidelines, additional_instructions):
    """
    Creates a guideline validator task dynamically based on the provided guidelines and product specifications.
    """
    validator_agent = create_validator_agent(guidelines, additional_instructions)
    return Task(
        description=(
            f'''
            Compare the provided guidelines: {guidelines} and instructions: {additional_instructions} to identify any conflicting or overlapping information regarding post length, tone, target audience, and other key parameters. 
            Present conflicts as nested JSON in the following format:
                Key for outer JSON: "parmeter_name"
                Key for inner JSON: "guideline" and "instruction"
                Value for inner JSON: "provide value of parameter present in guidelines" and "provide value of parameter present in instructions"
            Provide report only for the parameters for which conflicts are found.
            If no discrepancies are found, just state "No discrepancies found".
            Keep the report concise and to the point.
            Just inform the user about the discrepancies between the guidelines and instructions.
            '''
        ),
        expected_output="Identify and list any discrepancy between guidelines and instructions. Present the discrepancies as bullet points, highlighting the conflicting elements. List all the descrepancies and keep the response clear and professional.",
        agent=validator_agent,
        async_execution=False,
        output_file='guideline-validation-report.md'  # Example of output customization
    )
    
def create_prompt_task(content,combined_instructions):
    """
    Create a task for generating prompts for the LinkedIn posts.
    """
    prompt_writer_task = create_prompt_agent()
    return Task(
        description=f"""
        1. Generate a high-quality, detailed but short prompt for an image generation model(DALL-E) based on the provided content: {content} and the branding guidelines: {combined_instructions}.
        2. The prompt should be between 50-100 words, ensuring clarity, conciseness, and specificity to align with the instructions. 
        3. The generated prompt must accurately reflect the provided content and the branding guidelines while maintaining coherence and completeness.
        4. Carefully analyze image generation instructions in the branding guidelines and include any relevant details in the generated prompt.
        5. The prompt must strictly adhere to OPENAI DALL-E's safety standards, avoiding any content that promotes bias, misinformation, or inappropriate themes and requests that include text generation within the image.
        6. The prompt should include precise description of objects, actions, lighting, mood, perspective, and artistic style to produce high quality images.
        7. The prompt should be well-structured and free from ambiguity to ensure optimal output from the image generation model.
        8. The prompt should be written in a way that is easy to understand and can be easily followed by the Image Generation Model.
        """,
        expected_output="A short, clear and structured prompt that contains the necessary information for the Image Generation Agent to create relevant and high quality image",
        agent=prompt_writer_task,
        async_execution=False
    )
    
def create_image_generator_task():
    """
    Create a task for generating high-quality images for the LinkedIn posts.
    """
    image_generator_agent = create_image_generator_agent()
    return Task(
        description="Generate high-quality image for the Linkedin posts.",
        expected_output="High-quality images that complement the LinkedIn posts.",
        agent=image_generator_agent,
        async_execution=False
    )
    
def create_edited_post_validator_task(edited_content, content, user_guidelines):
    """
    Create a task for validating the edited post.
    """
    validator_agent = create_edited_validator_agent()
    return Task(
        description=f"""
            1. Validate the edited post: {edited_content} against the original content: {content} and the user guidelines: {user_guidelines}.
            2. Check if edited content deviates from the original generated content.
            3. If the edited content deviates, verify the deviated content with the user guidelines.
            4. If any discrepancies are found, notify the user.
            5. Ensure that the validation process is thorough and comprehensive, covering all aspects of the content.
            6. Provide the report in bullet points format, highlighting the discrepancies and providing a short explanation for each.
            7. Keep the report concise and to the point.
        """,
        expected_output="A report that highlights any discrepancies between the edited content and the original content, along with a short explanation for each discrepancy.",
        agent=validator_agent,
        async_execution=False
    )

