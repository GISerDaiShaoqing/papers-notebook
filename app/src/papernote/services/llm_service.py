from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class LLMRequestError(RuntimeError):
    """Raised when an OpenAI-compatible chat endpoint cannot answer."""


@dataclass(frozen=True, slots=True)
class LLMPreferences:
    base_url: str
    model: str
    api_key: str = ""


def _chat_endpoint(base_url: str) -> str:
    url = base_url.strip().rstrip("/")
    if not url:
        raise LLMRequestError("请先配置 API 地址。")
    if url.endswith("/chat/completions"):
        return url
    if url.endswith("/v1"):
        return f"{url}/chat/completions"
    return f"{url}/v1/chat/completions"


def complete_chat(
    preferences: LLMPreferences,
    messages: list[dict[str, str]],
    timeout: float = 180.0,
) -> str:
    if not preferences.model.strip():
        raise LLMRequestError("请先配置模型名称。")

    payload = json.dumps(
        {
            "model": preferences.model.strip(),
            "messages": messages,
            "temperature": 0.2,
            "stream": False,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if preferences.api_key:
        headers["Authorization"] = f"Bearer {preferences.api_key}"
    request = Request(_chat_endpoint(preferences.base_url), data=payload, headers=headers)

    try:
        with urlopen(request, timeout=timeout) as response:
            result = json.load(response)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1200]
        raise LLMRequestError(f"模型服务返回 HTTP {exc.code}: {detail}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise LLMRequestError(f"无法连接模型服务：{exc}") from exc
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise LLMRequestError(f"模型服务返回了无法读取的响应：{exc}") from exc

    choices = result.get("choices") or []
    if not choices:
        raise LLMRequestError("模型服务的响应中没有 choices。")
    content = (choices[0].get("message") or {}).get("content", "")
    if isinstance(content, list):
        content = "".join(
            str(part.get("text", "")) if isinstance(part, dict) else str(part)
            for part in content
        )
    text = str(content).strip()
    if not text:
        raise LLMRequestError("模型服务返回了空内容。")
    return text
