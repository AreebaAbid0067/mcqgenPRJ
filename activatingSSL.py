import httpx


import openai
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

openai.api_key = 'sk-None-FlKmLtEd2n3HDvRibx2LT3BlbkFJIp1KgsdXRSAB6a5YuVWR'
openai.Engine("davinci").search({
  "documents": ["White House", "hospital", "school"],
  "query": "the president"
}, headers={"Authorization": f"Bearer {openai.api_key}"}, verify=ssl_context)


client = httpx.Client(verify=False)

