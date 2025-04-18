# from docx import Document
# from docx.shared import Inches
# from copy import deepcopy
# from docx.enum.text import WD_ALIGN_PARAGRAPH 
 
# def insert_image_in_doc(doc_path, image_path, image_width_inch=5):
#     # Load the original document
#     doc = Document(doc_path)
 
#     # Make a backup copy of the original body elements    
#     original_elements = [deepcopy(el) for el in doc._element.body]    
    
#     # Remove all elements from the document body    
#     for child in list(doc._element.body):    
#         doc._element.body.remove(child)    
    
#     # Create a new paragraph and center it  
#     paragraph = doc.add_paragraph()  
#     paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER  

#     # Add the image into a new run in this centered paragraph  
#     run = paragraph.add_run()  
#     run.add_picture(image_path, width=Inches(image_width_inch))  
    
#     # Optional: Add a blank paragraph for additional spacing if desired  
#     doc.add_paragraph('')  
        
#     # Re-insert the original content below    
#     for el in original_elements:    
#         doc._element.body.append(el)    
        
#     # Save the modified document    
#     doc.save(doc_path)    

# image_path = "images/image_1.png"
# doc_path = "output_files/generated_post.docx"    
# print("inserting image")

# insert_image_in_doc(doc_path, image_path)
# print(f"Image inserted at {doc_path}")

from utils import image_integration, process_uploaded_file

guidelines_path = "input_guide/Updated_Brand_Prompt_Guide.docx"
guidelines = """"
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

user_instructions = """"
"Generate the content introducing TARA, Coforge’s AI-powered chatbot designed to assist employees with HR and IT-related queries. The post should highlight the key capabilities of TARA, including:
•	Providing information on HR policies
•	Helping employees apply for leaves and check attendance
•	Answering HR-related questions
•	Assisting with IT-related queries
•	Facilitating IT service request and incident management
•	Being available 24/7 for instant support
The tone should be professional yet engaging, emphasizing how TARA enhances the employee experience by making HR and IT support seamless and efficient. The post should encourage employees to explore TARA and share their experiences in the comments. Keep the length between 150-300 words and include relevant industry hashtags like #AI #HRTech #Chatbot #EmployeeExperience."*
"""
content = """"
* Exciting Launch: Meet TARA – Your AI-Powered Assistant

**Introduction  
In today’s fast-paced corporate landscape, seamless HR and IT support is vital for employee productivity and satisfaction. At Coforge, we’re proud to introduce TARA, our innovative AI-powered chatbot designed specifically to streamline HR and IT processes for our valued employees.

**Key Capabilities  
TARA is equipped with robust functionalities that revolutionize day-to-day support:  
• Provides quick and accurate information on HR policies  
• Assists with leave applications, attendance verification, and HR-related queries  
• Offers support for IT-related questions and facilitates service request and incident management  
• Available 24/7 to ensure you receive instant, reliable assistance whenever needed

Harnessing cutting-edge AI technology, TARA empowers employees by reducing wait times, enhancing efficiency, and improving overall operational experience within the organization. Our commitment to innovation is reflected in TARA’s ability to integrate effortlessly with current systems, ensuring that you have the tools necessary to succeed at work.

**Call to Action  
Explore TARA today and experience the future of workplace support. Share your experiences in the comments and let us know how TARA has transformed your daily interactions. 

#AI #HRTech #Chatbot #EmployeeExperience
"""
generated_image_name = "image_generated.jpg"
image_path = "images/image_generated.jpg"
output_path = "output_files/generated_post.docx"

print("integrating image")

image_integration(output_path, True, image_path, generated_image_name, content, guidelines, user_instructions)

print(f"Image integrated at {output_path}")
