import docx
import os
import shutil  # Import shutil for deleting folders
from PIL import Image
from io import BytesIO
from utils import format_document, insert_image_in_doc, regenerate_content

def extract_and_resize_images(docx_path, output_folder, size=(300, 300)):
    read_images_folder = os.path.join(output_folder, "read_images")
    os.makedirs(read_images_folder, exist_ok=True)
    doc = docx.Document(docx_path)
    image_count = 0

    for rel in doc.part._rels:
        rel = doc.part._rels[rel]
        if "image" in rel.target_ref:
            image_count += 1
            img_data = rel.target_part.blob
            img_ext = rel.target_part.content_type.split('/')[-1]

            # Open the image with PIL
            img = Image.open(BytesIO(img_data))

            # Resize the image
            resized_img = img.resize(size)

            # Save the resized image in the read_images folder
            img_name = f"image_{image_count}.{img_ext}"
            img_path = os.path.join(read_images_folder, img_name)
            resized_img.save(img_path)

    return read_images_folder


def delete_read_images_folder(folder_path):
    """
    Deletes the specified folder and all its contents.

    :param folder_path: Path to the folder to delete.
    """
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
    else:
        print(f"Folder '{folder_path}' does not exist.")
        
def finalize_document(docx_path, styling_guide, content):
    """
    Finalizes the document by applying the styling guide and formatting the text.  
    """
    # Load the document
    doc = docx.Document(docx_path)
    
    #read images from document
    read_images_folder_path = extract_and_resize_images(docx_path, "images", size=(1024, 1024))
    
    format_document(styling_guide,content, docx_path)
    
    #iterate through the read images folder path to access all images
    for image_name in os.listdir(read_images_folder_path):
        image_path = os.path.join(read_images_folder_path, image_name)
        # Add the image to the document
        insert_image_in_doc(docx_path, image_path)
        
    # delete the images folder
    delete_read_images_folder(read_images_folder_path)
    # Save the modified document
    doc.save(docx_path)
    print(f"Document saved with applied styles and images: {docx_path}")
    


# Example usage

user_guidelines = """
Coforge Brand Prompt Guide for Content Generation
LinkedIn Post Prompt Template

Write a LinkedIn post of 400-500 words for Coforge readers on the topic: "{insert topic here}".
Follow this structure:
- Hook (20–30 words): Start with a question or attention-grabbing statement.
- Introduction (50–100 words): Contextualize the topic within the industry/domain.
- Industry Trends: Provide 3–5 bullet points.
- Coforge's Point of View: 100–150 words of insights or unique perspectives.
- CTA (Call to Action): 25–50 words encouraging engagement.

Tone:  concise, and informative. Use SEO-rich keywords and include technical details if relevant.

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
- Review: Proofread and ensure alignment with Coforge standards



Styling Guide
Title
•	Font: Century
•	Size: 16
•	Bold: Yes
•	Alignment: Center
•	Color: Blue
Heading 1
•	Font: Calibri
•	Size: 14
•	Bold: Yes
•	Alignment: Left
•	Color: Black
Heading 2
•	Font: Calibri
•	Size: 12
•	Italic: Yes
•	Alignment: Left
•	Color: Black
Paragraph
•	Font: Calibri
•	Size: 12
•	Alignment: Left
•	Spacing After: 6
•	Color: Black
Bullet
•	Font: Calibri
•	Size: 12
•	Alignment: Left
•	Color: Black
Hyperlink
•	Font: Calibri
•	Color: Blue
•	Underline: Yes
"""
text = """
%% TARA: Your 24/7 HR & IT Companion by Coforge

* Hook  
Have you ever wished for instant HR or IT assistance at your fingertips? Meet TARA – the revolutionary AI-powered chatbot transforming your employee support experience.

* Introduction  
In today’s fast-paced work environment, timely support is essential for seamless operations. Coforge introduces TARA, an AI-driven solution designed to streamline your HR and IT needs. From providing detailed HR policy information to facilitating IT service requests, TARA ensures that you receive immediate and accurate support. This innovative tool not only simplifies processes such as leave applications and attendance verification but also empowers you to resolve queries efficiently, making your workday smoother and more productive.

* Key Features  
- Provides comprehensive information on HR policies  
- Assists with leave applications and attendance verification  
- Answers a wide range of HR-related questions  
- Supports IT inquiries and manages service requests and incidents  
- Available 24/7 for continuous, round-the-clock support

* Coforge Perspective  
At Coforge, we are committed to enhancing employee experiences through innovation. TARA embodies our vision by integrating advanced AI technologies into everyday workplace interactions. This intelligent chatbot is designed not only to improve operational efficiency in HR and IT but also to elevate your overall satisfaction. By ensuring that critical support is available whenever you need it, TARA transforms traditional assistance into a dynamic, user-friendly service. We are proud to lead this transformation, reinforcing our dedication to modern, employee-centric solutions that drive efficiency and foster a positive work environment.

* Call to Action  
Experience the efficiency of TARA today and see how it makes HR and IT support more engaging! Share your feedback or experiences in the comments, and let’s explore the future of workplace assistance together. #IA #TecnologíaRR.HH. #Chatbot #ExperienciaDeEmpleado
"""

user_inst = """
"Generate the content introducing TARA, Coforge’s AI-powered chatbot designed to assist employees with HR and IT-related queries. The post should highlight the key capabilities of TARA, including:
•	Providing information on HR policies
•	Helping employees apply for leaves and check attendance
•	Answering HR-related questions
•	Assisting with IT-related queries
•	Facilitating IT service request and incident management
•	Being available 24/7 for instant support
The tone should be professional yet engaging, emphasizing how TARA enhances the employee experience by making HR and IT support seamless and efficient. The post should encourage employees to explore TARA and share their experiences in the comments. Keep the length between 150-300 words and include relevant industry hashtags like #AI #HRTech #Chatbot #EmployeeExperience."*
"""
configs = {
        "length": "200 words",
        "tone": "Professional",
        "target_audience": "Tech Professionals",
        "technicality": "Intermediate",
        "content_type": "LinkedIn Post"
    }

output_path = "output_files/generated_post.docx"

# Finalize the document with the styling guide and content
#finalize_document(output_path, styling_guide, text)

edited_content = regenerate_content(text, user_guidelines, user_inst, configs, output_path)
print(edited_content)