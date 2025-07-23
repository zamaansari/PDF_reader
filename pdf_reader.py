import pyttsx3
import PyPDF2

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 300)  # You can adjust speed

# Path to the PDF file
pdf_path = "sample.pdf"  # 🔁 Change this to your PDF file name

try:
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)
        print(f"Total Pages: {total_pages}")

        # Ask which page to read
        page_number = int(input(f"Enter page number to read (1-{total_pages}): "))
        if 1 <= page_number <= total_pages:
            page = reader.pages[page_number - 1]
            text = page.extract_text()

            print("\n📖 Reading Page Content:\n")
            print(text)

            engine.say(text)
            engine.runAndWait()
        else:
            print("❌ Invalid page number.")
except FileNotFoundError:
    print("❌ PDF file not found. Make sure the path is correct.")
except Exception as e:
    print(f"⚠️ Error: {e}")
