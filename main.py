import argparse
import sys

import anthropic

from call_function import available_functions, call_function
from config import MAX_ITERS, MODEL
from soul import soul


def main() -> None:
    parser = argparse.ArgumentParser(description="Personality Bot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = anthropic.Anthropic()
    messages: list = []
    print("Personality Bot (type 'exit' to quit)")

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": user_input})
        reply = run_turn(client, messages, args.verbose)
        if reply is None:
            break
        print(f"\nKate: {reply}")


def generate_content(
    client: anthropic.Anthropic, messages: list, verbose: bool
) -> str | None:
    message = client.messages.create(
        model=MODEL,
        max_tokens=10000,
        system=soul,
        messages=messages,
        tools=available_functions,
    )
    messages.append({"role": "assistant", "content": message.content})

    if message.stop_reason != "tool_use":
        return "".join(b.text for b in message.content if b.type == "text")

    tool_results = []
    for block in message.content:
        if block.type != "tool_use":
            continue
        result = call_function(block, verbose)
        if verbose:
            print(f"-> {result['content']}")
        tool_results.append(result)

    messages.append({"role": "user", "content": tool_results})
    return None


def run_turn(client: anthropic.Anthropic, messages: list, verbose: bool) -> str | None:
    for _ in range(MAX_ITERS):
        try:
            reply = generate_content(client, messages, verbose)
        except Exception as e:
            print(f"Error in generate_content: {e}")
            return None
        if reply is not None:
            return reply
    print(f"Maximum iterations ({MAX_ITERS}) reached")
    return None


if __name__ == "__main__":
    main()
