import argparse
import anthropic
import sys
from soul import soul


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = anthropic.Anthropic()

    messages = [{"role": "user", "content": args.user_prompt}]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    try:
        reply = generate_content(client, messages)
    except Exception as e:
        print(f"Error in generate_content: {e}")
        sys.exit(1)

    print(reply)


def generate_content(client: anthropic.Anthropic, messages: list) -> str:
    message = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=10000,
        system=soul,
        messages=messages,
    )

    return "".join(block.text for block in message.content if block.type == "text")


if __name__ == "__main__":
    main()
