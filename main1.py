import streamlit as st
from utils import final_output, format_document, process_uploaded_file, generate_instruction_report
from io import BytesIO

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

# Streamlit UI
st.title("🚀 Marketing Agent")

# State to track whether the output is being generated
if "output_generated" not in st.session_state:
    st.session_state.output_generated = False

# Ensure the generated post and other outputs are stored in session state
if "generated_post" not in st.session_state:
    st.session_state.generated_post = None
if "generated_image" not in st.session_state:
    st.session_state.generated_image = None

# Initial layout: Single column for inputs
if not st.session_state.output_generated:
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
        help="You can manually enter instructions or upload a Word file.",
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
        help="Specify the desired length for the LinkedIn post.",
    )

    # Tone input
    tone = st.selectbox(
        "Select the tone of the blog:",
        options=["Professional", "Formal", "Informal", "Persuasive", "Neutral"],
        help="Choose the tone for the blog post.",
    )

    # Target Audience input
    target_audience = st.text_input(
        "Enter the target audience:",
        placeholder="e.g., Marketing Professionals, Tech Enthusiasts, etc.",
        help="Specify the target audience for the blog post.",
    )
    
    # Technicality input
    techicality = st.selectbox(
        "Select the level of technicality:",
        options=["Basic", "Intermediate", "Advanced"],
        help="Choose the level of technicality for the blog post.",
    )
    
    #content type
    content_type = st.selectbox(
        "Select the content type:",
        options=["LinkedIn Post", "Blog Post", "Email","Other"],
        help="Choose the content type for the blog post.",
    )

    # Button to generate results
    generate_button = st.button("Generate Results")

    # Store configurations
    configurations = {
        "length": length,
        "tone": tone,
        "target_audience": target_audience,
        "technicality": techicality,
        "content_type": content_type
    }

    # Handle the "Generate Results" button click
    if generate_button:
        # Ensure product_specs has a default value
        if not product_specs:
            product_specs = "No instructions provided, maybe present in the guidelines."

        # Read content from uploaded Word file
        font_conditions = ""
        if font_conditions_file is not None:
            font_conditions = process_uploaded_file(font_conditions_file)

        # Generate instruction report
        report = generate_instruction_report(font_conditions, configurations)

        # Store the report in session state
        st.session_state.report = report
        st.session_state.font_conditions = font_conditions
        st.session_state.product_specs_input = product_specs
        st.session_state.configurations = configurations
        st.session_state.output_generated = True

# After clicking "Generate Results": Two-column layout
if st.session_state.output_generated:
    col1, col2 = st.columns([1, 1])  # Divide the screen into two equal halves

    # Inputs in the left column
    with col1:
        st.markdown("### Inputs:")
        st.markdown("#### User Instructions:")
        st.text_area(
            "Instructions:",
            value=st.session_state.product_specs_input,
            height=150,
            disabled=True,
        )
        st.markdown("#### Additional Inputs:")
        st.text(f"Length: {st.session_state.configurations['length']}")
        st.text(f"Tone: {st.session_state.configurations['tone']}")
        st.text(f"Target Audience: {st.session_state.configurations['target_audience']}")

    # Outputs in the right column
    with col2:
        st.markdown("### Results:")

        # Display the validation report
        with st.expander("Instructions Conflicts:"):
            st.text_area(
                "Validation Report:",
                value=st.session_state.report,
                height=300,
                disabled=True,
            )

        # Add buttons for user to choose between "Guidelines" or "Instructions"
        st.markdown("### Resolve Conflicts:")
        col1, col2 = st.columns(2)
        with col1:
            choose_guidelines = st.button("Choose Guidelines")
        with col2:
            choose_instructions = st.button("Choose Instructions")

        # Proceed based on the user's choice
        if choose_guidelines or choose_instructions:
            # Generate the post after the user makes a choice
            st.markdown("### Generating Post... Please wait ⏳")

            # Call the final_output function to generate the post
            generated_output = final_output(
                st.session_state.font_conditions,
                st.session_state.product_specs_input,
                st.session_state.configurations,
                "generated_post",
            )
            st.session_state.generated_post = generated_output["Generated Post"]
            st.session_state.generated_image = generated_output["Image"]

        # Display the generated post if it exists in session state
        if st.session_state.generated_post:
            st.markdown("### Generated Post:")
            st.text_area(
                "Final Output:",
                value=st.session_state.generated_post,
                height=300,
                key="generated_output",
                help="This is the generated output.",
            )

            # Add a download button for the Word file
            if st.button("Download"):
                styling_guide_path = "input_guide/styling_guide.docx"
                output_file_path = "output_files/generated_post.docx"
                format_document(
                    styling_guide_path,
                    st.session_state.generated_post,
                    output_file_path,
                )

                with open(output_file_path, "rb") as f:
                    word_file = BytesIO(f.read())

                st.download_button(
                    label="Download Word File",
                    data=word_file,
                    file_name="Generated_Post.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

        # Display the generated image if it exists in session state
        if st.session_state.generated_image:
            st.markdown("### Generated Image:")
            st.image(
                st.session_state.generated_image,
                caption="Generated Image",
                use_container_width=True,
            )

