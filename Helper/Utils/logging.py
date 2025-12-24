"""File which stores the NexusLogging Class"""
from typing import Optional
import json

import webview

from Helper.NexusColors.color import NexusColor
from Helper.NexusColors.gradient import GradientPrinter



class NexusLogging:
    """A class for Logging"""

    LC = f"{NexusColor.NEXUS}[{NexusColor.LIGHTBLACK}NEXUS{NexusColor.NEXUS}]"

            
    @staticmethod
    def print_status(token: str, message: str, color: str, prefix: Optional[str] = None, length: Optional[int] = 45) -> None:
        try:
            window = webview.windows[0]
            js_code = f'addLog("{token[:length]} {NexusColor.RESET} -> {color}{message}", "succses");'
            window.evaluate_js(js_code)
        except Exception as e:
            print(f"[JS Log Fallback] {message} (info) | Error: {e}")
        GradientPrinter.gradient_print(
            input_text=token[:length],
            end_text=f"{NexusColor.RESET} -> {color}{message}",
            start_color="#ff08b5",
            end_color="#8308ff",
            prefix=prefix
        )

    @staticmethod
    def print_error(
            token: str, message: str, response: str
        ) -> None:
        """
        Prints error details in case of a failed operation.

        Args:
            token (str): The token associated with the failed operation.
            message (str): The error message to display.
            response (requests.Response): The server response containing error details.
        """
        try:
            window = webview.windows[0]
            log_message = f"{token[:45]} {NexusColor.RESET} -> {NexusColor.RED}{message}: {response.text} ({response.status_code})"
            js_code = f'addLog({json.dumps(log_message)}, "succses");'
            window.evaluate_js(js_code)
        except Exception as e:
            print(f"[JS Log Fallback] {message} (info) | Error: {e}")
                    
        GradientPrinter.gradient_print(
            input_text=token[:45],
            end_text=f"{NexusColor.RESET} -> {NexusColor.RED}{message}: {response.text} ({response.status_code})",
            start_color="#ff08b5",
            end_color="#8308ff",
            correct=False,
        )
   