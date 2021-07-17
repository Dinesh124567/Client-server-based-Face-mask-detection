import shutil
import requests
import cv2
# send request to host
def get_scanned_from_api(ip_byte_file, url= "http://localhost:8000/facemask_detect"):

    """
    input : image byte data
    output :scanned cv2 image data
    """

    
    r = requests.post(url,
                files ={
                        "input_file" :
                            ip_byte_file
                        }
                    )


    
    r.raw.decode_content = True
    label = r.headers["mask-status"]

    print(label)
    """print(r.raw)
    with open("abc.jpg" , "wb") as f:
        for c in r:
            f.write(c)
    print("saved successfully")"""

    # get face mask detected data

    
    
    with open("masked.jpg", "wb") as f:
        f.write(r.content)
    
    result = cv2.imread("masked.jpg")
    
    r.close()

    """cv2.imshow("img" , result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
    return result

#data = get_scanned_from_api(open("camera.jpg", "rb"))



# save file data to file

