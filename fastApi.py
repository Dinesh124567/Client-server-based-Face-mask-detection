import shutil
import cv2

from fastapi import FastAPI  
from fastapi.responses import FileResponse,HTMLResponse
import uvicorn
from fastapi import FastAPI, File, UploadFile

import detect_mask_image
import detect_mask_mp4

def execute_video(input_file, output_file):
    """
    input : video path 
    output : saves scanned video 
    """
    result = detect_mask_mp4.mask_video(input_file, output_file)

def execute_image (input_file, output_file):
    """
    input : image 
    output : saves scanned image
    """
    result, label = detect_mask_image.mask_image(input_file)
    cv2.imwrite(output_file , result)

    return result, label

work_place= "work place/"
app=FastAPI()

@app.post('/facemask_detect')
def get_output(input_file: UploadFile = File(...)):
    """
    input types supported : photos - jpeg, png, jpg
                            video  - mp4
    """ 
    label = "none"
    input_wp=work_place+"inputs/"
    output_wp=work_place+"outputs/"

    print("type of file :", type(input_file))
    print("name of file :",input_file.filename)

    #uploading the file to host
    with open(input_wp+input_file.filename, "wb+") as b:
        shutil.copyfileobj(input_file.file, b)

    inp_file=input_wp+input_file.filename
    out_file=output_wp+input_file.filename+".jpg"

    if input_file.filename[-4:] == ".mp4":
        out_file = output_wp+input_file.filename+".avi"
        execute_video(inp_file , out_file)
       
    else:
        result, label = execute_image(inp_file,out_file)

    
    response = FileResponse(out_file , media_type='application/octet-stream',filename="output.jpg" if input_file.filename[-4:] != ".mp4" else "output.avi")
    response.headers["mask-status"] = label
    return response

@app.get("/")
async def main():
    content = """
        <body>
        <form action="/facemask_detect" enctype="multipart/form-data" method="post">
        <input name="input_file" type="file" multiple>
        <input type="submit">
        </form>


        </body>
    """
    return HTMLResponse(content=content)


from fastapi import FastAPI, Request

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    uvicorn.run(app, port=8000)