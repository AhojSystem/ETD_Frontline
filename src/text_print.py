def text_print(win, y, x, max_height, max_width, text: str, color=None):
    assert text.count("\n") <= max_height - 1, f"text {text[:10]}...{text[-10:]} is too long"
    assert len(text) <= max_width * max_height, f"text {text[:10]}...{text[-10:]} is too long"
    if color is not None:
        win.addstr(y, x, text, color)
    else:
        win.addstr(y, x, text)
