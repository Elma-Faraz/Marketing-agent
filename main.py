import streamlit as st
from crewai import Crew, Process
from agents import create_post_writer_agent, create_image_generator_agent, create_validator_agent,create_prompt_agent
from tasks import create_blog_write_task, create_validator_task,create_prompt_task
from utils import create_image, crew_result, generate_instruction_report
from docx import Document  # To read Word files

# Inject custom CSS to make the layout full screen
st.markdown(
    """
    <style>
    .main {
        padding: 0px;
        max-width: 100%;
    }
    .block-container {
        padding: 1rem 0.5rem;
    }
    .custom-textarea textarea {
        width: 100% !important; /* Set the width to 100% of the container */
        height: 150px !important; /* Set the height to 150px */
    }
    .custom-output-textarea textarea {
        width: 100% !important; /* Set the width to 100% of the container */
        height: 300px !important; /* Set the height to 300px */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def process_uploaded_file(file):
    if file is not None:
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def writer_crew_result(agents,tasks):
    crew = Crew(
            agents=agents,
            tasks=tasks,
        )
    result = crew.kickoff()
    
    # Extract the blog post from the result object
    blog_post = None
    if result.json_dict and 'blog_post' in result.json_dict:
        blog_post = result.json_dict['blog_post']
    elif result.raw:
        blog_post = result.raw
    elif result.tasks_output:
        for task_output in result.tasks_output:
            if hasattr(task_output, 'output') and 'blog_post' in task_output.output:
                blog_post = task_output.output['blog_post']
                break
    if not blog_post:
        blog_post = "No blog post generated."
    return blog_post

def validator_crew_result(agents,tasks):
    '''Function to validate the guidelines and instructions'''
    crew = Crew(
            agents=agents,
            tasks=tasks,
        )
    result = crew.kickoff()
    # Extract the blog post from the result object
    report = None
    if result.json_dict and 'blog_post' in result.json_dict:
        report = result.json_dict['blog_post']
    elif result.raw:
        report = result.raw
    elif result.tasks_output:
        for task_output in result.tasks_output:
            if hasattr(task_output, 'output') and 'blog_post' in task_output.output:
                report = task_output.output['blog_post']
                break
    if not report:
        report = "No blog post generated."
    return report

def additional_instructions(configurations: dict):
    additional_instructions = f"""
    Write the post with length: {configurations["length"]}
    The tone of the post should be: {configurations["tone"]}
    The target audience of the post should be: {configurations["target_audience"]}
    """
    return additional_instructions

def combined_inputs(guidelines, instructions, additional_instructions):
    combined_input = f"""
    1. **Guidelines** : {guidelines}
    2. **Instructions** : {instructions}
    3. **Additional Instructions** : {additional_instructions}
    """
    return combined_input

# Streamlit UI
st.title("🚀 Marketing Agent")

# State to track whether the output is being generated
if "output_generated" not in st.session_state:
    st.session_state.output_generated = False

# Conditional layout based on whether output is generated
if not st.session_state.output_generated:
    # Centered layout for inputs
    col1 = st.container()
    with col1:
        st.markdown("### Provide details for generating content:")
        
        # File uploader for font formatting conditions
        st.markdown("#### Upload Guidelines:")
        font_conditions_file = st.file_uploader("Upload a Word file:", type=["docx"])
        
        # Textbox for product specifications and blog instructions
        st.markdown("#### User Instructions:")
        product_specs = st.text_area(
            "Enter your instructions here:",
            placeholder="Highlight the features of products and write instructions for the post and generating image.",
            height=150,
            key="product_specs",  # Add a unique key if needed
            label_visibility="visible",
            help="You can manually enter instructions or upload a Word file."
        )
        
        # Button to upload instructions from a Word file
        st.markdown("#### Upload Additional Instructions:")
        instructions_file = st.file_uploader("Upload a Word file for instructions:", type=["docx"])
        
        # If a file is uploaded, read its content and populate the textbox
        if instructions_file is not None:
            uploaded_instructions = process_uploaded_file(instructions_file)
            product_specs = st.text_area(
                "Uploaded Instructions:",
                value=uploaded_instructions,
                height=150,
            )
        
        # Add additional user inputs for blog customization
        st.markdown("#### Additional Inputs for Blog Customization:")

        # Length input
        length = st.text_input(
            "Enter the desired length for the post:",
            placeholder="200-300 words",
            help="Specify the desired length for the linkedin post."
        )

        # Tone input
        tone = st.selectbox(
            "Select the tone of the blog:",
            options=["Professional", "Formal", "Informal", "Persuasive", "Neutral"],
            help="Choose the tone for the blog post."
        )

        # Target Audience input
        target_audience = st.text_input(
            "Enter the target audience:",
            placeholder="e.g., Marketing Professionals, Tech Enthusiasts, etc.",
            help="Specify the target audience for the blog post."
        )
        
        configurations = {
            "length": length,
            "tone": tone,
            "target_audience": target_audience
        }

        # Combine all inputs into a single string to pass to the blog writer crew
        additional_inputs = additional_instructions(configurations)

        # Button to generate results
        generate_button = st.button("Generate Results")
else:
    # Full-screen two-column layout
    col1, space, col2 = st.columns([1, 0.2, 1])  # Divide the screen into two equal halves

    # Inputs in the left column
    with col1:
        st.markdown("### Provide details for generating content:")
        
        # File uploader for font formatting conditions
        st.markdown("#### Upload Guidelines:")
        font_conditions_file = st.file_uploader("Upload a Word file:", type=["docx"])
        
        # Textbox for product specifications and blog instructions
        st.markdown("#### User Instructions:")
        product_specs = st.text_area(
            "Enter your instructions here:",
            placeholder="Highlight the features of products and write instructions for the post and generating image.",
            height=150,
            key="product_specs",  # Add a unique key if needed
            label_visibility="visible",
            help="You can manually enter instructions or upload a Word file."
        )
        
        # Button to upload instructions from a Word file
        st.markdown("#### Upload Additional Instructions:")
        instructions_file = st.file_uploader("Upload a Word file for instructions:", type=["docx"])
        
        # If a file is uploaded, read its content and populate the textbox
        if instructions_file is not None:
            uploaded_instructions = process_uploaded_file(instructions_file)
            product_specs = st.text_area(
                "Uploaded Instructions:",
                value=uploaded_instructions,
                height=150,
            )
        
        # Add additional user inputs for blog customization
        st.markdown("#### Additional Inputs for Blog Customization:")

        # Length input
        length = st.text_input(
            "Enter the desired length for the post:",
            placeholder="200-300 words",
            help="Specify the desired length for the linkedin post."
        )

        # Tone input
        tone = st.selectbox(
            "Select the tone of the blog:",
            options=["Professional","Formal", "Informal", "Persuasive", "Neutral"],
            help="Choose the tone for the blog post."
        )

        # Target Audience input
        target_audience = st.text_input(
            "Enter the target audience:",
            placeholder="e.g., Marketing Professionals, Tech Enthusiasts, etc.",
            help="Specify the target audience for the blog post."
        )

        # Combine all inputs into a single string to pass to the blog writer crew
        configurations = {
            "length": length,
            "tone": tone,
            "target_audience": target_audience
        }

        # Combine all inputs into a single string to pass to the blog writer crew
        additional_inputs = additional_instructions(configurations)

        # Button to generate results
        generate_button = st.button("Generate Results")

    # Output in the right column
    with col2:
        st.markdown("### Generating Results... Please wait ⏳")
        
        # Read content from uploaded Word file
        font_conditions = ""
        if font_conditions_file is not None:
            font_conditions = process_uploaded_file(font_conditions_file)

        # Ensure product_specs has a default value
        if not product_specs:
            product_specs = "No instructions provided maybe present in the guidelines."
        
        #creating combined inputs   
        combined_input = combined_inputs(font_conditions, product_specs, additional_inputs)

        
        #Executing validator task
        report = generate_instruction_report(font_conditions, configurations)
        
        # Executing blog writing task
        post_writer_agent = create_post_writer_agent(combined_input)
        blog_write_task = create_blog_write_task(combined_input)
        
        agents = [post_writer_agent]
        tasks = [blog_write_task]
        result = writer_crew_result(agents,tasks)
        
        # Display the validation report
        with st.expander("Instructions Conflicts:"):
            st.text_area(
                "Validation Report:",
                value=report,
                height=300,
                key="validation_report",  # Add a unique key if needed
                label_visibility="visible",
                help="This is the validation report.",
            )

        # Display the blog post with the custom CSS class
        st.markdown("### Generated Post:")
        st.text_area(
            "Final Output:",
            value=result,
            height=300,
            key="generated_output",  # Add a unique key if needed
            help="This is the generated output.",
            label_visibility="visible",
        )
        
        prompt_agent = create_prompt_agent()
        prompt_task = create_prompt_task(result, font_conditions)
        prompt = crew_result([prompt_agent], [prompt_task])
        
        # Display an image
        st.markdown("### Generated Image:")
        image_path = create_image(prompt)  # Replace with the path to your image
        st.image(image_path, caption="Generated Image", use_container_width=True)
        
        

# Update the state when the button is clicked
if generate_button:
    st.session_state.output_generated = True