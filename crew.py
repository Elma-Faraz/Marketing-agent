import streamlit as st
from crewai import Crew, Process
from agents import blog_writer
from tasks import blog_write_task
from docx import Document  # To read Word files

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_writer],
    tasks=[blog_write_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=False,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large",  # mixedbread-ai/mxbai-embed-large-v1 · Hugging Face
            "base_url": "http://localhost:11434",
        }
    },
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Streamlit UI
st.title("🚀 Marketing Agent")
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextArea textarea {
        font-family: "Courier New", monospace;
        font-size: 14px;
    }
    .stButton > button {
        border: 2px solid black; /* Add a black border */
        border-radius: 5px;      /* Optional: Add rounded corners */
        padding: 10px 20px;      /* Optional: Add padding for better spacing */
        font-size: 16px;         /* Optional: Adjust font size */
        font-weight: bold;       /* Optional: Make the text bold */
        cursor: pointer;         /* Optional: Add a pointer cursor on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("### Provide details for generating content:")

# File uploader for font formatting conditions
st.markdown("#### Upload Font Formatting Guidelines:")
font_conditions_file = st.file_uploader("Upload a Word file:", type=["docx"])

# Textbox for product specifications and blog instructions
st.markdown("#### User Instructions:")
product_specs = st.text_area(
    "Enter your instructions here:",
    placeholder="Highlight the features of products and write instructions for the post and generating image.",
    height=150,
)

# Button to generate results
if st.button("Generate Results"):
    st.markdown("### Generating Results... Please wait ⏳")
    
    # Read content from uploaded Word file
    font_conditions = ""
    if font_conditions_file is not None:
        doc = Document(font_conditions_file)
        font_conditions = "\n".join([para.text for para in doc.paragraphs])
    
    # Start the task execution process
    inputs = {
        'font_conditions': font_conditions,
        'product_specs': product_specs
    }
    result = crew.kickoff(inputs=inputs)

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

    # Display the blog post
    st.markdown("### 📝 Generated Post:")
    st.text_area("Final Output:", value=blog_post, height=300)

    # Display an image
    st.markdown("### 🖼️ Generated Image:")
    image_path = "images/images.jpeg"  # Replace with the path to your image
    st.image(image_path, caption="Generated Image", use_container_width=True)