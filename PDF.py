from PIL import Image
from reportlab.pdfgen import canvas
import os
import glob

def images_to_pdf(image_paths, output_pdf):
    """
    Converts a list of images to a PDF where each page matches the image size.
    """
    c = None  

    for i, img_path in enumerate(image_paths):
        if not os.path.exists(img_path):
            print(f"Warning: {img_path} not found. Skipping.")
            continue

        try:
            with Image.open(img_path) as img:
                img_width, img_height = img.size

               
                width_pt = img_width * 0.75
                height_pt = img_height * 0.75

              
                if i == 0:
                    c = canvas.Canvas(output_pdf, pagesize=(width_pt, height_pt))
                else:
                    c.setPageSize((width_pt, height_pt))
                    c.showPage()

              
                c.drawImage(img_path, 0, 0, width=width_pt, height=height_pt)

        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    if c:
        c.save()
        print(f"PDF saved as {output_pdf}")
    else:
        print("No valid images were processed.")

# Example usage
if __name__ == "__main__":
    folder_path = r"C:\Users\SltyIcCrm\FolderToConvert"
            #change name based on user folder names

    extensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.tiff"]

    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(folder_path, ext)))

    if not image_paths:
        print("No images found in the folder.")
    else:
        output = r"C:/Users/SltyIcmCrm/FolderToAddPDF/my_images.pdf"
        #change name based on user folder names
        images_to_pdf(image_paths, output)


