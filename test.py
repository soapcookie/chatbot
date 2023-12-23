import openai
import time

# OpenAI API 키를 설정합니다.

openai.api_key = "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"

def get_gpt_response(prompt):
    time.sleep(1)  # 요청 사이에 1초 대기합니다.
    response = openai.Completion.create(
        model="text-davinci-003",  # GPT-3의 최신 버전인 Davinci 모델을 사용합니다.
        prompt=prompt,
        max_tokens=100  # 필요에 따라 최대 토큰 수를 조정합니다.
    )
    return response.choices[0].text.strip()

# 테스트 프롬프트
test_prompt = "What are the latest developments in renewable energy?"
print(get_gpt_response(test_prompt))



