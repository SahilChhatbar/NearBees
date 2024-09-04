from flask import Flask, request, send_file, jsonify, redirect
from io import BytesIO
import os
import cv2 as cv
from ultralytics import YOLO

app = Flask(__name__)

def detect_and_annotate(image_path):
    if not os.path.exists(image_path):  
        print(f"Image '{image_path}' not found.")
        return

    image = cv.imread(image_path)
    model = YOLO("/home/caliexa/Project/nearbees-v2/nearbees/best.pt")
    class_names = ["Rose", "SunFlower"]

    results = model(image)

    rose_detected = False
    sunflower_detected = False
    for box, cls_idx in zip(results[0].boxes.xyxy, results[0].boxes.cls):
        x1, y1, x2, y2 = box[:4].tolist()
        class_name = class_names[int(cls_idx)]

        if class_name == "Rose":
            rose_detected = True
        elif class_name == "SunFlower":
            sunflower_detected = True

        cv.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv.putText(
            image,
            class_name,
            (int(x1), int(y1) - 10),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 0),
            2,
        )

    annotated_image_path = "static/annotated_image.jpg"  # Save to static directory
    cv.imwrite(annotated_image_path, image)

    return annotated_image_path, rose_detected, sunflower_detected


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file_path = 'uploaded_image.jpg'
        file.save(file_path)
        annotated_image_path, rose_detected, sunflower_detected = detect_and_annotate(file_path)

        if rose_detected:
            return redirect("/rose")  # Redirect to /rose if Rose is detected
        elif sunflower_detected:
            return redirect("/sun")  # Redirect if SunFlower is detected
        
        return send_file(annotated_image_path, mimetype='image/jpeg')




@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>s
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./nearbees.css">
    <title>Upload Image</title>
</head>
<body>
<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #171717;
}
.header {
    background-color: hsl(50, 100%, 50%);
    font-size: 25px;
    color: #171717;
    padding: 20px;
    text-align: center;
}
.container {
    display: flex;
    align-items: stretch;
    height: 100vh;
}
.content {
    flex: 1; /* Take remaining space */
    padding: 20px;
}
pre {font-family: 'Times New Roman', Times, serif;
    /* Other styles */
    font-size: 20px;
    color: #333;
    background-color: hsl(50, 100%, 50%);
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-left: auto;
    margin-right: auto;
}
/* left menu bar*/
#menu {
    position: fixed;
    top: 0;
    left: -250px;
    width: 250px;
    height: 100%;
    background: #333;
    transition: all 0.3s ease;
  }
  #menu.active {
    left: 0;
  }
  #menu ul {
    padding: 0;
    margin: 0;
    list-style: none;
  }
  #menu ul li {
    padding: 15px;
    border-bottom: 1px solid #555;
  }
  #menu ul li a {
    color: #fff;
    text-decoration: none;
  }
  #menu ul li:hover {
    background: #555;
  }
  #menu-btn {
    position: fixed;
    left: 20px;
    top: 20px;
    cursor: pointer;
    z-index: 2;
  }
/* left menu bar ended*/
/* inline block code */
.inline {
  display: inline-block;
  vertical-align: top;
  /* Optionally, you can add other styles here */
}
/* image box in the flesh */
.box {
  width: 450px;
  height: 300px; /* Adjust the box height as needed */
  position: relative;
  overflow: hidden;
  border: 1px solid #ccc;
}

.image {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  transition: opacity 0.5s ease;
}

.thumbnails {
  margin-top: 10px; /* Adjust spacing between box and thumbnails */
  text-align: center;
  border: #ccc;
}

.thumbnail {
  width: 50px; /* Adjust thumbnail size as needed */
  height: auto;
  margin: 0 5px; /* Adjust spacing between thumbnails */
  cursor: pointer;
  transition: opacity 0.3s ease;
  border: #fff;
  border-width: 1px;
}

.thumbnail:hover {
  opacity: 0.7; /* Reduce opacity on hover */
}

/* get started code */
.cssbuttons-io-button {
  background: hsl(50, 100%, 50%);
  color: white;
  font-family: inherit;
  padding: 0.35em;
  padding-left: 1.2em;
  font-size: 17px;
  font-weight: 500;
  border-radius: 0.9em;
  border: none;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  box-shadow: inset 0 0 1.6em -0.6em #fffb00;
  overflow: hidden;
  position: relative;
  height: 2.8em;
  padding-right: 3.3em;
  cursor: pointer;
}

.cssbuttons-io-button .icon {
  background: white;
  margin-left: 1em;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 2.2em;
  width: 2.2em;
  border-radius: 0.7em;
  box-shadow: 0.1em 0.1em 0.6em 0.2em #fffb00;
  right: 0.3em;
  transition: all 0.3s;
}

.cssbuttons-io-button:hover .icon {
  width: calc(100% - 0.6em);
}

.cssbuttons-io-button .icon svg {
  width: 1.1em;
  transition: transform 0.3s;
  color: #ecf406;
}

.cssbuttons-io-button:hover .icon svg {
  transform: translateX(0.1em);
}

.cssbuttons-io-button:active .icon {
  transform: scale(0.95);
}
/* code ended here for the get started */
/* center allignment */
.center {
  display: flex;
  justify-content: center; /* Horizontally center the button */
  align-items: center; /* Vertically center the button *//* Set container height to full viewport height */
}
/* =================================================================================================== */
.form {
  background-color: #fff;
  box-shadow: 0 10px 60px rgb(218, 229, 255);
  border: 1px solid rgb(159, 159, 160);
  border-radius: 20px;
  padding: 2rem .7rem .7rem .7rem;
  text-align: center;
  font-size: 1.125rem;
  max-width: 320px;
}

.form-title {
  color: #000000;
  font-size: 1.8rem;
  font-weight: 500;
}

.form-paragraph {
  margin-top: 10px;
  font-size: 0.9375rem;
  color: rgb(105, 105, 105);
}

.drop-container {
  background-color: #fff;
  position: relative;
  display: flex;
  gap: 10px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px;
  margin-top: 2.1875rem;
  border-radius: 10px;
  border: 2px dashed rgb(171, 202, 255);
  color: #444;
  cursor: pointer;
  transition: background .2s ease-in-out, border .2s ease-in-out;
}

.drop-container:hover {
  background: rgba(0, 140, 255, 0.164);
  border-color: rgba(17, 17, 17, 0.616);
}

.drop-container:hover .drop-title {
  color: #222;
}

.drop-title {
  color: #444;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  transition: color .2s ease-in-out;
}

#file-input {
  width: 350px;
  max-width: 100%;
  color: #444;
  padding: 2px;
  background: #fff;
  border-radius: 10px;
  border: 1px solid rgba(8, 8, 8, 0.288);
}

#file-input::file-selector-button {
  margin-right: 20px;
  border: none;
  background: #084cdf;
  padding: 10px 20px;
  border-radius: 10px;
  color: #fff;
  cursor: pointer;
  transition: background .2s ease-in-out;
}

#file-input::file-selector-button:hover {
  background: #0d45a5;
}
/* file upload button  */


</style>
    <div class="header">
        <h1>NearBees</h1>
        <p>Let's reconnect with nature, Flower recognition system</p>
    </div>
    <div class="content" class="inline">
        <div class="center">
            <form method=post enctype=multipart/form-data action="/upload">
                <span class="form-title">Upload your file</span>
                <p class="form-paragraph">File should be an image</p>
                <label for="file-input" class="drop-container">
                    <span class="drop-title">Drop files here</span>
                    or
                    <input type="file" accept="image/*" required id="file-input" name="file">
                </label>
                <!-- <input type="submit">Upload</input> -->
                <input type=submit value=Upload> 
            </form>
        </div>
        <div id="menu" style="text-align: center;">
            <ul>
                <li><a href="homepage.html">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="upload.html">Explore</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
        <div id="menu-btn">&#9776;</div>
    </div>
    <!-- <script src="nearbees.js"></script> -->
</body>
</html>
    '''

from flask import render_template

@app.route('/rose')
def rose():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #000000;
            color:#f5f5f5;
        }
        .container {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            padding: 20px;
        }
        .image {
            width: 50%;
            padding: 10px;
        }
        .description {
            width: 50%;
            padding: 10px;
            color:#f5f5f5;
        }
        .image img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            padding-top: 2px;
        }
        .description h1 {
            font-size: 2rem;
            color: #f5f5f5;
        }
        .description p {
            font-size: 1.125rem;
            color:#f5f5f5;
            line-height: 1.6;
        }
        .header {
            background-color: hsl(50, 100%, 50%);
            font-size: 25px;
            color: #171717;
            padding: 10px 20px;
            text-align: center;
            border-radius: 10px;
            z-index: 2;
            position: relative;
            height: 150px;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><img src="/static/NearBees.png" style="width: 100px; height:100px;"></h1>
    </div>
    <div class="container">
        <div class="image">
            <img src="/static/annotated_image.jpg" alt="Description of the image">
        </div>
        <div class="description">
            <h1>Rose</h1>
            <p>The rose (Rosa spp.) is a popular flowering plant known for its stunning blooms and delightful fragrance. To grow roses successfully, start by selecting a sunny location with well-drained soil. Plant roses in spring or fall, ensuring they receive at least 6 hours of sunlight daily. Space plants adequately to allow for air circulation and avoid fungal diseases. Water roses regularly but avoid overhead watering to prevent mildew. Apply a balanced fertilizer and prune dead or diseased branches to promote healthy growth and flowering.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/sun')
def sun():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #000000;
            color:#f5f5f5;
        }
        .container {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            padding: 20px;
        }
        .image {
            width: 50%;
            padding: 10px;
        }
        .description {
            width: 50%;
            padding: 10px;
            color:#f5f5f5;
        }
        .image img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            padding-top: 2px;
        }
        .description h1 {
            font-size: 2rem;
            color: #f5f5f5;
        }
        .description p {
            font-size: 1.125rem;
            color:#f5f5f5;
            line-height: 1.6;
        }
        .header {
            background-color: hsl(50, 100%, 50%);
            font-size: 25px;
            color: #171717;
            padding: 10px 20px;
            text-align: center;
            border-radius: 10px;
            z-index: 2;
            position: relative;
            height: 150px;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><img src="/static/NearBees.png" style="width: 100px; height:100px;"></h1>
    </div>
    <div class="container">
        <div class="image">
            <img src="/static/annotated_image.jpg" alt="Description of the image">
        </div>
        <div class="description">
            <h1>Sunflower</h1>
            <p>The sunflower (Helianthus annuus) is a vibrant and cheerful flowering plant renowned for its large, sun-like blooms and impressive height. To cultivate sunflowers effectively, choose a sunny location with well-drained soil. Plant seeds directly in the garden after the last frost, spacing them about 6-12 inches apart to accommodate their growth. Sunflowers thrive with at least 6-8 hours of sunlight daily and require regular watering, especially during dry spells. Ensure the soil remains consistently moist but not waterlogged. Sunflowers benefit from a balanced fertilizer applied during the growing season. To support tall varieties, consider staking the plants to prevent them from bending or breaking. Remove any diseased or damaged leaves to maintain plant health and encourage vigorous blooming.</p>
        </div>
    </div>
</body>
</html>
"""


if __name__ == '__main__':
    app.run(port=8000)
