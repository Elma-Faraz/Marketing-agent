# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

# AZURE_TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
# AZURE_TRANSLATOR_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
# AZURE_REGION = os.getenv("AZURE_REGION")
# API_VERSION = '3.0'
 
# # Detect the language of input text
# def detect_language(text: str) -> str:
#     url = f"{AZURE_TRANSLATOR_ENDPOINT}/detect"
#     params = {'api-version': API_VERSION}
#     headers = {
#         'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
#         'Ocp-Apim-Subscription-Region': AZURE_REGION,
#         'Content-Type': 'application/json'
#     }
#     body = [{'text': text}]
#     response = requests.post(url, params=params, headers=headers, json=body, timeout=10, verify=False)
#     response.raise_for_status()
#     return response.json()[0]['language']
 
# # Translate text
# def translate_text(text: str, to_lang: str, from_lang: str = None) -> str:
#     url = f"{AZURE_TRANSLATOR_ENDPOINT}/translate"
#     params = {
#         'api-version': API_VERSION,
#         'to': to_lang
#     }
#     if from_lang:
#         params['from'] = from_lang
 
#     headers = {
#         'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
#         'Ocp-Apim-Subscription-Region': AZURE_REGION,
#         'Content-Type': 'application/json'
#     }
#     body = [{'text': text}]
#     response = requests.post(url, params=params, headers=headers, json=body, verify=False)
#     response.raise_for_status()
#     return response.json()[0]['translations'][0]['text']
 
# # Main method: Your full desired flow
# def full_translate_flow(input_text: str, output_lang_name: str) -> str:
#     output_lang = get_lang_code(output_lang_name)
 
#     detected_lang = detect_language(input_text)
 
#     # Step 1: Translate to English if needed
#     if detected_lang != "en":
#         english_text = translate_text(input_text, to_lang="en", from_lang=detected_lang)
#         print("*****english text: ",english_text)
#     else:
#         english_text = input_text
 
#     # Step 2: Translate English to target language if needed
#     if output_lang != "en":
#         final_translation = translate_text(english_text, to_lang=output_lang, from_lang="en")
#     else:
#         final_translation = english_text
 
#     return final_translation
 
# # Language name to ISO code mapping
# LANGUAGE_NAME_TO_CODE = {
#     "english": "en",
#     "hindi": "hi",
#     "french": "fr",
#     "german": "de",
#     "spanish": "es",
#     "chinese": "zh-Hans",
#     "japanese": "ja",
#     "russian": "ru",
#     "italian": "it",
#     "arabic": "ar",
#     "portuguese": "pt",
#     "korean": "ko",
#     "bengali": "bn",
#     "tamil": "ta",
#     "telugu": "te",
#     "marathi": "mr",
#     # Add more as needed
# }
 
# def get_lang_code(language_name: str) -> str:
#     code = LANGUAGE_NAME_TO_CODE.get(language_name.strip().lower())
#     if not code:
#         raise ValueError(f"Unsupported or unknown language: {language_name}")
#     return code

# text = """
# * Emocionante lanzamiento: Conoce a TARA: tu asistente con IA

# **Introducción
# En el dinámico panorama corporativo actual, un soporte fluido de RR. HH. y TI es vital para la productividad y la satisfacción de los empleados. En Coforge, nos enorgullece presentar TARA, nuestro innovador chatbot con IA, diseñado específicamente para optimizar los procesos de RR. HH. y TI para nuestros valiosos empleados.

# **Capacidades clave
# TARA cuenta con sólidas funcionalidades que revolucionan el soporte diario:
# • Proporciona información rápida y precisa sobre las políticas de RR. HH.
# • Asiste con solicitudes de permisos, verificación de asistencia y consultas relacionadas con RR. HH.
# • Ofrece soporte para preguntas relacionadas con TI y facilita la gestión de solicitudes de servicio e incidentes.
# • Disponible 24/7 para garantizar que recibas asistencia instantánea y confiable cuando la necesites.

# Gracias a la tecnología de IA de vanguardia, TARA empodera a los empleados al reducir los tiempos de espera, mejorar la eficiencia y optimizar la experiencia operativa general dentro de la organización. Nuestro compromiso con la innovación se refleja en la capacidad de TARA para integrarse fácilmente con los sistemas actuales, lo que garantiza que cuente con las herramientas necesarias para el éxito en el trabajo.

# **Llamada a la acción
# Explore TARA hoy mismo y experimente el futuro del soporte en el lugar de trabajo. Comparta sus experiencias en los comentarios y cuéntenos cómo TARA ha transformado sus interacciones diarias.

# #IA #TecnologíaRRHH #Chatbot #ExperienciaEmpleado
# """

# output_lang = "Italian"

# translated_text = full_translate_flow(text, output_lang)
# print(translated_text)

from utils import final_output
guidelines = """
Guía de propuestas de marca de Coforge para la generación de contenido
Plantilla de propuesta para publicación en LinkedIn

Redacta una publicación en LinkedIn de 400 a 500 palabras para los lectores de Coforge sobre el tema: "{insertar tema aquí}".
Sigue esta estructura:
- Gancho (20-30 palabras): Comienza con una pregunta o una afirmación que capte la atención.
- Introducción (50-100 palabras): Contextualiza el tema dentro del sector/dominio.
- Tendencias del sector: Incluye de 3 a 5 viñetas.
- Perspectiva de Coforge: De 100 a 150 palabras con ideas o perspectivas únicas.
- Llamada a la acción (CTA): De 25 a 50 palabras que fomenten la interacción.

Tono: Conciso e informativo. Usa palabras clave optimizadas para SEO e incluye detalles técnicos si es relevante.

Plantilla de propuesta para blog SEO

Redacta una publicación de blog optimizada para SEO de unas 800 a 1000 palabras sobre el tema: "{insertar tema aquí}". Centrarse en los últimos avances y su impacto en la industria "{domain}".

Estructura:
- Introducción: Definir el tema y su relevancia.
- Tendencias: Explorar IA, ML, IoT, Blockchain, etc.
- Casos de uso: Proporcionar ejemplos reales, incluyendo las soluciones de Coforge.
- Experiencia del cliente: Destacar las mejoras gracias a la tecnología.
- Disruptivos: Mencionar startups e innovación.
- Desafíos y oportunidades: Analizar los principales obstáculos y beneficios.
- Perspectivas de futuro: Predecir tendencias y tecnologías futuras.
- Llamada a la acción: Animar a los lectores a interactuar o contactar con Coforge.

Tono: Profesional, informativo y alineado con la marca Coforge. Utilizar palabras clave optimizadas para SEO y detalles técnicos.

Notas de voz de la marca

- Objetivo: Establecer objetivos claros para el contenido.
- Público objetivo: Lectores de Coforge y profesionales de sectores relevantes.
- Tono: Informativo, seguro y profesional.
- Ejemplos: Incluir casos prácticos o estadísticas para mayor credibilidad. - Tecnicidad: Adaptación según el público: principiante, intermedio o avanzado.
- SEO: Utiliza palabras clave relevantes para mejorar la visibilidad. - Revisión: Revisar y asegurar la conformidad con los estándares de Coforge

Guía de Estilo
Título
• Fuente: Century
• Tamaño: 16
• Negrita: Sí
• Alineación: Centrado
• Color: Azul
Encabezado 1
• Fuente: Calibri
• Tamaño: 14
• Negrita: Sí
• Alineación: Izquierda
• Color: Negro
Encabezado 2
• Fuente: Calibri
• Tamaño: 12
• Cursiva: Sí
• Alineación: Izquierda
• Color: Negro
Párrafo
• Fuente: Calibri
• Tamaño: 12
• Alineación: Izquierda
• Espaciado posterior: 6
• Color: Negro
Viñeta
• Fuente: Calibri
• Tamaño: 12
• Alineación: Izquierda
• Color: Negro
Hipervínculo
• Fuente: Calibri
• Color: Azul
• Subrayado: Sí
"""

instructions = """
Genera el contenido que presenta TARA, el chatbot de Coforge con IA, diseñado para ayudar a los empleados con consultas relacionadas con RR. HH. y TI. La publicación debe destacar las principales funciones de TARA, incluyendo:
• Proporcionar información sobre políticas de RR. HH.
• Ayudar a los empleados a solicitar permisos y verificar la asistencia
• Responder preguntas relacionadas con RR. HH.
• Asistencia con consultas relacionadas con TI
• Facilitar la gestión de solicitudes de servicio de TI e incidentes
• Estar disponible 24/7 para soporte inmediato
El tono debe ser profesional pero atractivo, destacando cómo TARA mejora la experiencia del empleado al hacer que el soporte de RR. HH. y TI sea fluido y eficiente. La publicación debe animar a los empleados a explorar TARA y compartir sus experiencias en los comentarios. Mantén la extensión entre 150 y 300 palabras e incluye hashtags relevantes del sector como #IA #TecnologíaRR.HH. #Chatbot #ExperienciaDeEmpleado.
"""

configurations = {
    "length": "short",
    "tone": "casual",
    "target_audience": "general",
    "content_type": "blog"
}

filename = "test.docx"
output_language = "italian"


result = final_output(guidelines, instructions, configurations, filename, output_language)
print(result["Generated Post"])
