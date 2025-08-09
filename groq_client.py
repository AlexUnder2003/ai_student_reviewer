import json
import os
from groq import Groq
from dotenv import load_dotenv
from schemas import QuizReview

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
system_prompt = "Оцени ответы кандидата на вопросы собеседования объективно, если ответ частично верный — ставь true, дай краткий комментарий с разъяснением, как мог бы выглядеть полный правильный ответ. В total запиши общую оценку по тесту в процентах, но это должно просто целое число без знака %. В поле text ты вносишь то что ответил user."


def review_test(answers):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": answers},
    ]

    response = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "test_review",
                "schema": QuizReview.model_json_schema(),
            },
        },
    )

    review = QuizReview.model_validate(
        json.loads(response.choices[0].message.content)
    )

    return review.model_dump()
