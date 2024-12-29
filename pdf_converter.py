import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_images(pdf_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            pdf_name = os.path.splitext(filename)[0]  # Get the filename without the extension

            try:
                images = convert_from_path(pdf_path)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue
            
            for i, image in enumerate(images):
                image_name = f"{pdf_name} - {i+1}.png"
                image_path = os.path.join(output_folder, image_name)
                image.save(image_path, 'PNG')
                print(f"Successfully converted {pdf_name}, page {i+1}")
            
            print(f"Processed {filename} - {len(images)} page(s)")

if __name__ == "__main__":
    pdf_input_folder = "input" 
    image_output_folder = "output" 
    
    pdf_to_images(pdf_input_folder, image_output_folder)
    print("Finished converting pdfs to images")