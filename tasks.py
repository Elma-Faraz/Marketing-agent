from crewai import Task
from agents import create_post_writer_agent, create_image_generator_agent, create_validator_agent, create_prompt_agent, edited_content_validator_agent, content_regenerator_agent

#Task for generate post
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
            4. Identify the required content type(LinkedIn Post, Blog Post, Email etc) based on the provided guidelines and instructions, if not mentioned in the **Additional Instructions** or it is "Other".
            5. Ignore the instructions in input related to image generation or image creation, if such instructions are provided. 
            6. Adjust tone, structure and length accordingly while maintaining clarity and engagement.
            7. Strictly follow the provided input in the given preference order.
            8. Maintain coherence, proper flow, and a professional or engaging tone as required.
            9. Incorporate product details, key messages, and branding elements as specified. Also provide a title for the post.
            10. Use language that aligns with the brand's voice and the target audience.
            11. Structure content for clarity and engagement.
            12. Format according to platform-specific best practices.
            13. Ensure proper grammar, spelling and readability.
            14. Provide a final version that is publication ready without requiring major edits.
            15. The title, headings, subheadings and paragraphs should be distinguishable and well structured. It should strictly distinguish the heading, subheadings, etc in the below format:
                Indicate Title with %%
                Indicate Heading1 with *
                Indicate Subheadings with **
            (It should just indicate heading levels with the asterisks)
            16. Write headings and its contents separately.
            
            '''
        ),
        expected_output="A well structured , grammatically perfect, and platform optimized content piece ensuring clarity, coherence, brand consistency and readiness for immediate publication.",
        agent=post_writer_agent,
        async_execution=False,
        output_file='new-blog-post.md'  # Example of output customization
    )
  
#Task for conflict report between user guidelines and configurations
def create_validator_task(guidelines, additional_instructions):
    """
    Creates a guideline validator task dynamically based on the provided guidelines and product specifications.
    """
    validator_agent = create_validator_agent(guidelines, additional_instructions)
    return Task(
        description=(
            f'''
            Compare the provided guidelines: {guidelines} and instructions: {additional_instructions} to identify any conflicting or overlapping information regarding post length, tone, target audience, and other key parameters. 
            Provide the conflicts in bullets and highlight the conflicting elements.
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
 
#Task for prompt for image generation   
def create_prompt_task(content,combined_instructions):
    """
    Create a task for generating prompts for the LinkedIn posts.
    """
    prompt_writer_task = create_prompt_agent()
    return Task(
        description=f"""
        1. Generate a high-quality, detailed but short prompt for an image generation model(DALL-E) based on the provided content: {content} and the user instructions: {combined_instructions}.
        2. In user instructions search only for image generation instructions in **Guidelines** and **Instructions**.
        3. The prompt should be between 50-100 words, ensuring clarity, conciseness, and specificity to align with the instructions. 
        4. Inform the image generation model not to include any text in the image.
        5. The generated prompt must accurately reflect the provided content and the branding guidelines while maintaining coherence and completeness.
        6. Carefully analyze image generation instructions in the branding guidelines and include any relevant details in the generated prompt.
        7. The prompt must strictly adhere to OPENAI DALL-E's safety standards, avoiding any content that promotes bias, misinformation, or inappropriate themes and requests that include text generation within the image.
        8. The prompt should include precise description of objects, actions, lighting, mood, perspective, and artistic style to produce high quality images.
        9. The prompt should be well-structured and free from ambiguity to ensure optimal output from the image generation model.
        10. The prompt should be written in a way that is easy to understand and can be easily followed by the Image Generation Model.
        """,
        expected_output="A short, clear and structured prompt that contains the necessary information for the Image Generation Agent to create relevant and high quality image",
        agent=prompt_writer_task,
        async_execution=False
    )
  
#Task for image generation  
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
   
#Task edited content conflict report based on user guidelines and configurations
def edited_content_validator_task(edited_content, generated_content):
    """
    Create a task for validating the edited post.
    """
    validator_agent = edited_content_validator_agent()
    return Task(
        description=f"""
            1. Inputs:
                Original Content - The initial version of the content before any user edits. : {generated_content}
                Edited Content - The modified version of the content after user edits.: {edited_content}
            2. Original content will be formated as:
                Indicates Title with %%
                Indicates Heading1 with *
                Indicates Subheadings with **
                Paragraphs will be separated with new line.
            3. Accept both the original and edited content in a structured format (title, headings, subheadings, paragraphs).
            4. Traverse each field (e.g., title, each heading, each paragraph under a heading) and compare the edited version to the original.
            5. For each section:
                Detect new text (sentences, phrases, or even entirely new sections) that exist in the edited content but not in the original.
            6. Focus only on added content, ignoring deletions and rewordings unless they introduce new ideas or data.
            7. Maintain the structural context of the additions:
                For example: “Under heading 'Benefits of AI', the following sentence was added: ‘It also enhances decision-making by providing predictive insights.’”
            8. If new headings or subheadings are introduced, treat their entire content as new.
            9. If a paragraph is extended with additional sentences, extract only the new sentences.
            10. Avoid duplication and ensure clarity in how and where content was added.
        """,
        expected_output=f"""
        1. Each entry contains:
            The section heading (where the paragraph appears).
            The full paragraph where new content has been added (even if it's mixed with old).
        2. If a completely new section is introduced, it’s marked as "New Heading" or "New Subheading" for clarity.
        3.The output is focused on full paragraphs, preserving their structure and making it easier for the Regeneration Agent to refine them with context
        """,
        agent=validator_agent,
        async_execution=False
    )

#Task for regenerate edited content  
def regenerate_content_task(edited_content, input):
    """
    Create a task for regenerating the content.
    """
    regenerator_agent = content_regenerator_agent()
    return Task(
        description=f"""
            1. Regenerate the content based on the user-edited content: {edited_content} and the user input.
            2. User input is provided below:
                {input}
            3. User input includes **User Guidelines**, **User Instructions** and **Configurations**.
            4. Verify if edited content with input provided. If any conflicts are present then change them according to the input based on the below priorities.
            5. Priority should be given in the following order: Configurations > User Instructions > User Guidelines. if configurations are not provided, then follow User Instructions > User Guidelines.  
            6. Correct the grammar and spelling errors, and ensure the content is coherent and well-structured.
            7. Ensure that the regenerated content aligns with the provided user guidelines covering tone, format, structure, language, and style rules, etc.
            8. The regenerated content should be publication-ready without requiring major edits.
            9. Do not change the provided edited content structure, tone, or style just regenerate the content.
            10. The title, headings, subheading can be available in edited content, do not change them.
            11. The headings, subheadings will be indicated in following format:
                Indicate Title with %%
                Indicate Heading1 with *
                Indicate Subheadings with **
        """,
        expected_output="A well-structured, grammatically correct, and platform-optimized content piece ensuring clarity, coherence, brand consistency, and readiness for immediate publication.",
        agent=regenerator_agent,
        async_execution=False
    )

