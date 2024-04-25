import uvicorn

import web

if __name__ == "__main__":
    uvicorn.run(web.api, port=8000)
