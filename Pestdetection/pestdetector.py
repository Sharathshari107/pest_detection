from ultralytics import YOLO
import random
def process(impath):
    # Load a model
    model = YOLO('best.pt')  # pretrained YOLOv8n model
    # Run batched inference on a list of images
    results = model(str(impath))  # return a list of Results objects
    #print("results==",results)
    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        #print("boxes==",boxes)
        masks = result.masks  # Masks object for segmentation masks outputs
        #print("masks==",masks)
        keypoints = result.keypoints  # Keypoints object for pose outputs
        #print("keypoints==",keypoints)
        probs = result.probs  # Probs object for classification outputs
        #print("probs==",probs)
        clist= result[0].boxes.cls
        cls = set()
        for cno in clist:
            cls.add(model.names[int(cno)])
        #print("cls==",cls)
        
        result.show()  # display to screen
        result.save(filename=impath)  # save to disk
        return cls
# classpred=process("./a.jpg")
# final_res=list(classpred)[0]
# print("predicted class==",final_res)
    