from server_endpoints import *

def main():
    uvicorn.run(app, host="localhost", port=8002)

if __name__ == "__main__":
    main()