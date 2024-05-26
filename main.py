import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.header("Object Detection with YOLO")
with st.sidebar:
    model = st.selectbox(
        "Select Model",
        ("Yolov9c.pt", "Yolov8m.pt"),
        index=None,
        placeholder="Choose a Model")
    if model == "Yolov9c.pt":
        model = "yolov9c.pt"
        yolo = YOLO(model=model)
        st.write(model + " has been selected")
    elif model == "Yolov8m.pt":
        model = "yolov8m.pt"
        yolo = YOLO(model=model)
        st.write(model + " has been selected")
    else:
        model = "yolov9c.pt"
        yolo = YOLO(model=model)

    st.markdown("##")

    options = st.multiselect(
    'Select objects you want to detect',
    ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck',  'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 
     'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
    )
    opt = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck',  'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 
     'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
    liste = []
    if options:
        st.write('You selected:', options)
        for i in options:   
            liste.append(opt.index(i))    

st.markdown("YOLO (You Only Look Once) is a popular object detection model known for its speed and accuracy. It was first introduced by Joseph Redmon et al. in 2016 and has since undergone several iterations, the latest being YOLO v9")
st.markdown("##")
st.markdown("The YOLO-World Model introduces an advanced, real-time Ultralytics YOLOv9-based approach for Open-Vocabulary Detection tasks. This innovation enables the detection of any object within an image based on descriptive texts")
st.subheader("Demo on Yolo")
st.divider()
st.markdown("**Demo 1**")
col1, col2 = st.columns(2)
with col1:
    st.write("input image")
    im1 = "dog.jpg"
    st.image(im1)

with col2:
    st.write("output image")
    st.image("dog2.jpg")

st.markdown("##")

st.markdown("Demo 2")
col3, col4 = st.columns(2)
with col3:
    st.write("input image")
    im2 = "cat.jpg"
    st.image(im2)
with col4:
    st.write("output image")
    st.image("cat2.jpg")

st.divider()
st.markdown("<h3>Detect Objects using yolo</h3>", unsafe_allow_html=True)
st.markdown("##")
image = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
if image is not None:
    image = Image.open(image)
    col5 , col6 = st.columns(2)
    with col5:
        st.markdown("Input image")
        st.image(image)
        if liste:
            ans = yolo.predict(image, classes = liste)
        else:
            ans = yolo.predict(image)
    
    with col6:
        st.markdown("Output Image")
        st.image(Image.fromarray(ans[0].plot()[:,:,::-1]))
        
 

        
    
