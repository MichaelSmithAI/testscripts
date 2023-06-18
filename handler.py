import runpod
from model import GPT2PPLV2

detector = GPT2PPLV2()

## load your model(s) into vram here

def handler(event):
    print(event)
    text = event['input']['prompt']
    
    result = detector(text, 100, "v1.1")
    
    return result

runpod.serverless.start({
    "handler": handler
})