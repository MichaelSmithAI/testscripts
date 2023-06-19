import runpod
import os
from model import GPT2PPLV2

detector = GPT2PPLV2()

chunkSize = int(os.environ.get('CHUNK_SIZE', 100))

## load your model(s) into vram here

def handler(event):
    print(event)
    text = event['input']['prompt']
    
    result = detector(text, chunkSize, "v1.1")
    
    return result

runpod.serverless.start({
    "handler": handler
})
