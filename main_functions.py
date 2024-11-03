import os
from PyQt6.QtWidgets import QFileDialog
from PIL import Image, ImageDraw, ImageFont


def add_functions(ui, MainWindow):
    ui.img_choose.clicked.connect(lambda: choose_img(ui, MainWindow))
    ui.path_choose.clicked.connect(lambda: choose_file(ui, MainWindow))
    ui.textEdit.textChanged.connect(lambda: text_watermark(ui))

    ui.create_btn.clicked.connect(lambda: create_image(ui))


def create_image(ui):
    try:
        # Check for text watermark creation
        if hasattr(ui, 'file_path') and hasattr(ui, 'text_watermark') and ui.text_watermark:
            print(f'Creating watermark from text on image: {ui.file_path}')
            image = Image.open(ui.file_path).convert("RGBA")
            watermarked = image.copy()

            # Create a transparent layer for drawing
            txt = Image.new('RGBA', watermarked.size, (255, 255, 255, 0))

            # Specify font (use a TTF font file for better results)
            # Replace with a path to a TTF file if needed
            font = ImageFont.truetype("arial.ttf", 36)
            draw = ImageDraw.Draw(txt)

            # Watermark text settings
            text = ui.text_watermark
            # Get the bounding box of the text to determine width and height
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            spacing_x = text_width + 20  # Horizontal spacing
            spacing_y = text_height + 20  # Vertical spacing

            # Draw the watermark repeatedly across the image
            for y in range(0, watermarked.size[1], spacing_y):
                for x in range(0, watermarked.size[0], spacing_x):
                    draw.text((x, y), text, font=font, fill=(
                        255, 255, 255, 100))  # Semi-transparent white

            # Combine original image with the text layer
            watermarked = Image.alpha_composite(watermarked, txt)

            # Display and save the output
            watermarked.show()
            watermarked.save("output_image_with_repeating_watermark.png")
            print("Watermarked image created successfully.")

        # Check for image watermark creation
        elif hasattr(ui, 'file_path') and hasattr(ui, 'img_path'):
            print(f'Creating watermark from image on image: {ui.file_path}')
            print(f'Using watermark image: {ui.img_path}')
            # Implement image watermark logic if needed
            # Open the base image and the watermark image
            base_image = Image.open(ui.file_path).convert("RGBA")
            watermark_image = Image.open(ui.img_path).convert("RGBA")

            # Resize the watermark if necessary (e.g., to 30% of the base image width)
            scale_factor = 0.3
            new_width = int(base_image.width * scale_factor)
            new_height = int(
                new_width * (watermark_image.height / watermark_image.width))
            watermark_image = watermark_image.resize(
                (new_width, new_height), Image.LANCZOS)

            # Create a transparent layer to hold the watermark
            watermark_layer = Image.new(
                "RGBA", base_image.size, (255, 255, 255, 0))

            # Position the watermark (bottom right corner with padding)
            padding = 10
            position = (base_image.width - watermark_image.width - padding,
                        base_image.height - watermark_image.height - padding)

            # Paste the watermark onto the transparent layer
            watermark_layer.paste(watermark_image, position, watermark_image)

            # Composite the base image and the watermark layer
            watermarked_image = Image.alpha_composite(
                base_image, watermark_layer)
            watermarked_image.show()
            watermarked_image.save("output_image_with_image_watermark.png")
            print("Watermarked image created successfully.")
        else:
            print("Please select both an image and a watermark (text or image) first.")
    except Exception as e:
        print(f"Error creating watermark: {e}")

def choose_file(ui, MainWindow):
    file_path, _ = QFileDialog.getOpenFileName(
        MainWindow, 'Open File', '', 'Images (*.png *.jpg *.jpeg *.bmp *.gif)'
    )
    if file_path:
      ui.file_path = file_path
      filename = os.path.basename(file_path)
      print(f'Selected file: {file_path}')
      ui.path_choose.setText(filename)


def choose_img(ui, MainWindow):
    img_path, _ = QFileDialog.getOpenFileName(
        MainWindow, 'Select Image', '', 'Images (*.png *.jpg *.jpeg *.bmp *.gif)'
    )
    if img_path:
      ui.img_path = img_path
      # Extract the filename from the full path
      filename = os.path.basename(img_path)
      print(f'Selected image: {filename}')
      ui.img_choose.setText(filename)


def text_watermark(ui):
    ui.text_watermark = ui.textEdit.toPlainText()  # Store input text as an attribute
    #print(f'Watermark text: {ui.text_watermark}')
