import webview

def send_log_to_js(message, type="info"):
        try:
            window = webview.windows[0]
            js_code = f'addLog("{message}", "{type}");'
            window.evaluate_js(js_code)
        except Exception as e:
            print(f"[JS Log Fallback] {message} ({type}) | Error: {e}")
