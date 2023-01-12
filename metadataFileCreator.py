import json, os


i = 1
for image in os.listdir("images/"):
    data = {
  "attributes": [
    {
      "display_type": "number",
      "trait_type": "generation",
      "value": 1
    }
  ],
  "description": "Psychadelic Rug",
  "external_url": "https://twitter.com/neuralnfts",
  "image": "ipfs://bafybeidbxifxz2zlghtzlgpxdirxndpvjxujaeqmrsykhlf62acufjzfoe/images/"+str(i)+".jpg",
  "name": "Psychadelic Rug #"+str(i)
}
    with open("metadata/"+str(i), "w") as f:
        json.dump(data, f)
