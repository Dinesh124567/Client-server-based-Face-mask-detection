import cv2
import detect_mask_image

def frames_vedio(cv2_vedio):
    """
    input - cv2 vedio object
    output - frames list

    """
    result = []
    success = 1
    while success:

        # vidObj object calls read
        # function extract frames
        success, image = cv2_vedio.read()
  
        # append the frames with frame-count
        result.append(image)
    
    return result


def mask_video(path, output_file):
    """
    input : path of video
    output :returns scanned vedio cv2 object
    """
    vidObj = cv2.VideoCapture(path)
    fps = vidObj.get(cv2.CAP_PROP_FPS)
    print("fps of input vedio is :", fps)
    frames = frames_vedio(vidObj)
    result = []
    for frame in frames:
        try :
            resframe = detect_mask_image.mask_image_2(frame)
            result.append(resframe)
        except : 
            pass
    h , w, l = result[0].shape
    size = (w, h)


    out = cv2.VideoWriter(output_file,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(result)):
        # writing to a image array
        out.write(result[i])
    out.release()

    final_vd = cv2.VideoCapture(output_file)
    return final_vd

