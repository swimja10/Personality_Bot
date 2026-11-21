from collections.abc import Callable

from config import WORKING_DIR
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.write_file import schema_write_file, write_file

available_functions: list = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
]

function_map: dict[str, Callable[..., str]] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
}


def call_function(tool_use, verbose: bool = False) -> dict:
    function_name = tool_use.name
    function_args = dict(tool_use.input)
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")

    if function_name not in function_map:
        return {
            "type": "tool_result",
            "tool_use_id": tool_use.id,
            "content": f"Error: Unknown function: {function_name}",
            "is_error": True,
        }

    function_args["working_directory"] = WORKING_DIR
    result = function_map[function_name](**function_args)

    return {
        "type": "tool_result",
        "tool_use_id": tool_use.id,
        "content": result or "(empty file)",
    }
