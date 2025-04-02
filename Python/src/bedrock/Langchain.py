from langchain_aws import BedrockLLM

llm = BedrockLLM(model_id="anthropic.claude-v2:1")

response = llm.invoke("랭체인으로 LLM 활용하기 참 쉽죠?")

print(response)