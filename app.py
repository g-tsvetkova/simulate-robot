from fastapi import FastAPI, Response
from starlette.responses import StreamingResponse
import shutil

app = FastAPI()


@app.get("/video")
def stream_video():
    video_path = "robot-arm.mp4" 
    
    def generate():
        with open(video_path, "rb") as video_file:
            while True:
                video_chunk = video_file.read(1024)
                if not video_chunk:
                    break
                yield video_chunk
    
    return StreamingResponse(generate(), media_type="video/mp4")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)
