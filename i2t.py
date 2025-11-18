import os
os.sys.path.append(".")
import base64
from volcenginesdkarkruntime import Ark
# ! 或者从文件读取API Key
with open("./data/your_apikey.txt", "r") as f:
    os.environ["ARK_API_KEY"] = f.read().strip()
# print(f"YOUR API Key: {os.environ['ARK_API_KEY']}")

def query_with_image(query: str, image_path: str):
    # 读取图像文件
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    data_url = f"data:image/png;base64,{b64}"

    client = Ark(
        base_url="https://ark.cn-beijing.volces.com/api/v3",
        api_key=os.environ.get("ARK_API_KEY"))

    try:
        response = client.chat.completions.create(
            model="doubao-seed-1-6-vision-250815",  # 模型ID
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url
                            },
                        },
                        {"type": "text", "text": query},
                    ],
                }
            ],)
    except Exception as e:
        print(f"YOUR API Key: {os.environ['ARK_API_KEY']}")
        print(e)
        return None

    return response.choices[0]
