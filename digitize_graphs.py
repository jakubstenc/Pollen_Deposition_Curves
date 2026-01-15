
import cv2
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import pytesseract

# Directories
INPUT_DIR = "Data_images"
OUTPUT_DIR = "data/extracted"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def analyze_axis_labels(img):
    """
    Uses OCR to find text labels at the bottom (X-axis) and left (Y-axis).
    Returns x_label, y_label.
    """
    height, width, _ = img.shape
    
    # Preprocess for text detection (grayscale, Otsu threshold)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Use pytesseract to get bounding boxes and text
    custom_config = r'--oem 3 --psm 11' # PSM 11: Sparse text
    data = pytesseract.image_to_data(gray, config=custom_config, output_type=pytesseract.Output.DICT)
    
    x_texts = []
    y_texts = []
    
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        text = data['text'][i].strip()
        if not text:
            continue
            
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        
        # Determine position
        # Bottom 15% -> X axis candidate
        if y > 0.85 * height:
            x_texts.append(text)
        
        # Left 15% -> Y axis candidate
        # Note: Y axis text might be rotated (tesseract might fail on 90deg text without rotation)
        # For now, we look for horizontal text on the left.
        if x < 0.15 * width:
            y_texts.append(text)

    # Join identified text chunks to form labels
    x_label = " ".join(x_texts) if x_texts else "X_Axis"
    y_label = " ".join(y_texts) if y_texts else "Y_Axis"
    
    # Cleanup typical OCR noise if needed
    
    return x_label, y_label

def process_image(image_path):
    print(f"Processing {image_path}...")
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load {image_path}")
        return

    # OCR for Labels
    x_label, y_label = analyze_axis_labels(img)
    print(f"  Detected X-Label: {x_label}")
    print(f"  Detected Y-Label: {y_label}")

    # Image processing for shapes
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Thresholding
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    points = []
    
    # Visualization image
    qc_img = img.copy()
    height, width, _ = img.shape
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 10: # Minimum area
            continue
            
        perimeter = cv2.arcLength(cnt, True)
        if perimeter == 0:
            continue
            
        # Shape descriptors
        circularity = 4 * np.pi * (area / (perimeter * perimeter))
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h
        
        # 1. Detect Points (High circularity, roughly 1:1 aspect ratio)
        if 0.6 < circularity < 1.2 and 0.5 < aspect_ratio < 2.0 and area < 500:
            # Centroid
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = x + w//2, y + h//2

            norm_x = cX / width
            # Standard graph Y (0 at bottom)
            norm_y_graph = 1 - (cY / height)
            
            points.append({
                "pixel_x": cX,
                "pixel_y": cY,
                "normalized_x": norm_x,
                "normalized_y": norm_y_graph
            })
            
            # Draw GREEN circle for Points
            cv2.circle(qc_img, (cX, cY), 5, (0, 255, 0), 2)
            
        # 2. Detect Error Bars (Low circularity, very thin)
        # Vertical bars: height >> width
        elif aspect_ratio < 0.2 and h > 10:
             # Draw RED line for Error Bars
            cv2.rectangle(qc_img, (x, y), (x+w, y+h), (0, 0, 255), 1)
            
        # 3. Detect Axis Lines/Ticks (Horizontal or Vertical long lines)
        # (Simplified visualization, usually we filter these out from data)
        
    # Check if we found any points
    if not points:
        print(f"Warning: No points found in {image_path}")
    else:
        print(f"Found {len(points)} points.")

    # Prepare data for saving
    bib_id = os.path.basename(image_path).rsplit('.', 1)[0]
    
    df = pd.DataFrame(points)
    
    if not df.empty:
        df['bib_id'] = bib_id
        df['x_label'] = x_label
        df['y_label'] = y_label
        
        # Reorder columns
        df = df[['bib_id', 'x_label', 'y_label', 'pixel_x', 'pixel_y', 'normalized_x', 'normalized_y']]
        
        # Save CSV
        csv_filename = os.path.join(OUTPUT_DIR, f"{bib_id}.csv")
        df.to_csv(csv_filename, index=False)
        print(f"Saved extracted data to {csv_filename}")
        
        # Save QC Image
        qc_filename = os.path.join(OUTPUT_DIR, f"{bib_id}_QC.png")
        cv2.imwrite(qc_filename, qc_img)
        print(f"Saved QC image to {qc_filename}")

def main():
    extensions = ['*.jpg', '*.png', '*.jpeg', '*.JPG', '*.PNG']
    image_files = []
    
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(INPUT_DIR, '**', ext), recursive=True))
    
    if not image_files:
        print(f"No images found in {INPUT_DIR}")
        return

    for img_path in image_files:
        process_image(img_path)

if __name__ == "__main__":
    main()
