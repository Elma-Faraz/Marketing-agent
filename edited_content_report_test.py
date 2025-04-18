from utils import generate_edited_content_report

original_content = """
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

edited_content = """
%% Introducing TARA - Empowering Seamless HR & IT Support

*Hook  
Start your workday with ease – imagine having a 24/7 digital assistant ready to resolve your HR and IT queries instantly!
Tara is an intelligent HR and IT service bot designed to assist employees with a wide range of workplace tasks. Whether you need to ask a quick query, get information about company policies, or apply for leave, Tara is always ready to help. Acting as a virtual assistant, Tara streamlines common HR and IT requests, making processes faster and more efficient. From checking leave balances to troubleshooting basic IT issues, Tara ensures employees get support anytime, improving productivity and enhancing the overall employee experience.

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

result = generate_edited_content_report(edited_content, original_content)
print(result)