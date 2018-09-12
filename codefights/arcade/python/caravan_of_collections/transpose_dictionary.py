def transposeDictionary(scriptByExtension):
    return sorted([[scriptByExtension[k], k] for k in scriptByExtension.keys()])




scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}

print(transposeDictionary(scriptByExtension))