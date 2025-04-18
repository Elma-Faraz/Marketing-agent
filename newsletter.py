from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os
 
# Setup
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('newsletter_template.html')

content = """
%% Introducing TARA - Empowering Seamless HR & IT Support

*Hook  
Start your workday with ease – imagine having a 24/7 digital assistant ready to resolve your HR and IT queries instantly!

**Introduction  
At Coforge, we are passionate about merging innovation with exceptional employee experience. Today, we introduce TARA, our advanced AI-powered chatbot tailored to support tech professionals. TARA is designed to bridge the gap between intricate process requirements and real-time support, making HR and IT interactions smoother than ever.

**Key Capabilities  
• Provides comprehensive HR policy information  
• Assists with leave applications and attendance checks  
• Quickly answers HR-related questions  
• Facilitates IT service requests and incident management  
• Ensures round-the-clock availability for immediate assistance

**Coforge’s Point of View  
TARA represents the forefront of digital transformation in employee support. Harnessing cutting-edge AI, TARA reduces bottlenecks and streamlines routine tasks, empowering professionals to focus on strategic initiatives. Our commitment to leveraging technology means that TARA not only simplifies processes but also fosters a proactive work environment. By integrating advanced technical solutions with our HR and IT systems, Coforge continuously enhances productivity and employee satisfaction.

*Call to Action  
Experience the future of support with TARA! Share your thoughts and experiences with our innovative chatbot in the comments below. #AI #HRTech #Chatbot #EmployeeExperience
"""

# Function to parse dynamic content into newsletter_data
def parse_content_to_newsletter_data(content):
    lines = content.strip().split("\n")
    newsletter_data = {
        "title": "",
        "header_image": "https://example.com/banner.png",  # Replace with a valid image URL or local path
        "sections": [],
        "footer_text": "Thank you for being part of our community! Stay tuned for more updates."
    }
    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith("%%"):  # Title
            newsletter_data["title"] = line.lstrip("%%").strip()
        elif line.startswith("*"):  # Heading
            if current_section:
                newsletter_data["sections"].append(current_section)
            current_section = {"heading": line.lstrip("*").strip(), "image": "", "text": ""}
        elif line.startswith("**"):  # Subheading
            if current_section:
                newsletter_data["sections"].append(current_section)
            current_section = {"heading": line.lstrip("**").strip(), "image": "", "text": ""}
        elif current_section:  # Section content
            current_section["text"] += (line + "\n")

    if current_section:
        newsletter_data["sections"].append(current_section)

    return newsletter_data

# Parse the dynamic content
newsletter_data = parse_content_to_newsletter_data(content)

# Render HTML
html_out = template.render(data=newsletter_data)

# Save to PDF
HTML(string=html_out).write_pdf("newsletter_dynamic.pdf")
print("Newsletter created successfully!")