from crewai import Task
from agents import blog_writer

# Writing task with language model configuration
blog_write_task = Task(
  description=(
    "This task involves generating a well-structured and engaging blog post "
    "based on the provided product specifications and formatting conditions. "
    "The blog post should highlight the key features of the product and adhere "
    "to the specified font formatting guidelines."
  ),
  expected_output=(
    "A complete blog post in Markdown format, including headings, subheadings, "
    "and formatted text (e.g., bold, italic) as per the provided font formatting "
    "conditions. The content should be clear, concise, and tailored to the target audience."
  ),
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)
