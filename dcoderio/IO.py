import os.path
import json
import sys
IO_FILE_PATH = '/usr/src/io.json'

def setOutput(key,value):
    data = None
    blockId  = os.environ.get("BLOCK_ID")
    if(os.path.isfile(IO_FILE_PATH)):
        f = open(IO_FILE_PATH, "r",encoding='utf-8')
        data = json.loads(f.read())
        f.close()
        if "steps" not in data:
            data["steps"] = {}
        if blockId not in data['steps']:
            data['steps'][blockId] = {}
        if "outputs" not in data['steps'][blockId]:
            data['steps'][blockId]['outputs'] = {}
        
        data['steps'][blockId]['outputs'][key] = value

    else:
        data = {
            "steps": {
                blockId:{
                    'outputs':{
                        key:value
                    }
                }
            }
        }
    data = json.dumps(data)
    f = open(IO_FILE_PATH, "w",encoding='utf-8')
    f.write(data)
    f.close()


def getInput(key):
    data = None
    blockId  = os.environ.get("BLOCK_ID")
    
    if(os.path.isfile(IO_FILE_PATH)):
        f = open(IO_FILE_PATH, "r",encoding='utf-8')
        data = json.loads(f.read())
        f.close()
        if "steps" not in data:
            return ''
        if blockId not in data['steps']:
            return ''
        if "inputs" not in data['steps'][blockId]:
            return ''
        
        if "inputs" in data['steps'][blockId] and key in data['steps'][blockId]['inputs']:
            return data['steps'][blockId]['inputs'][key] 
        else:
            return ''

    else:
        return ''

def getAuthToken(key):
    data = None
    blockId  = os.environ.get("BLOCK_ID")
    
    if(os.path.isfile(IO_FILE_PATH)):
        f = open(IO_FILE_PATH, "r",encoding='utf-8')
        data = json.loads(f.read())
        f.close()
        if "steps" not in data:
            raise Exception("Your account is not authenticated or linked.")
        if blockId not in data['steps']:
            raise Exception("Your account is not authenticated or linked.")
        if "auths" not in data['steps'][blockId]:
            raise Exception("Your account is not authenticated or linked.")
        
        if key in data['steps'][blockId]['auths'] and 'ACCESS_TOKEN' in data['steps'][blockId]['auths'][key]:
            return data['steps'][blockId]['auths'][key]['ACCESS_TOKEN']
        else:
            raise Exception("Your account is not authenticated or linked.")

    else:
        raise Exception("Your account is not authenticated or linked.")

def getSecret(key):
    if key.upper() in os.environ:
        return os.environ.get(key.upper())
    else:
        raise Exception("Secret doesn\'t exist.")

def setFailed(message):
    print(message)
    sys.exit(1)

def logFile():
    f = open(IO_FILE_PATH, "r",encoding='utf-8')
    print(f.read())
    f.close()
