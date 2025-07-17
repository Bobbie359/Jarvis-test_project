# commands.py
import os
import webbrowser
import pyautogui

def execute_command(text):
    text = text.lower()
    if text.startswith("write ") or text.startswith("fill "):
        to_type = text.replace("write ", "").replace("fill ", "").strip()
        pyautogui.write(to_type)
        return f"Filling: {to_type}"
    if text.startswith("search youtube") or text.startswith("youtube search"):
        query = text.replace("search youtube", "").replace("youtube search", "").strip()
        if query:
            import urllib.parse
            url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
            webbrowser.open(url)
            return f"Searching YouTube: {query}"
        else:
            return "Tell me what to search on YouTube."
    if text.startswith("search google") or text.startswith("google search"):
        query = text.replace("search google", "").replace("google search", "").strip()
        if query:
            import urllib.parse
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            webbrowser.open(url)
            return f"Searching Google: {query}"
        else:
            return "Tell me what to search on Google."
    if "youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "browser" in text or "chrome" in text or "safari" in text:
        webbrowser.open("https://www.google.com")
        return "Opening browser."
    elif "discord" in text:
        os.system("open -a Discord")
        return "Opening Discord."
    elif "email" in text or "mail" in text:
        os.system("open -a Mail")
        return "Opening mail app."
    elif "google" in text or "search" in text:
        query = text.replace("google", "").replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google: {query}"
    elif text.startswith("open google") or text.startswith("open google") or text.startswith("start google") or text.startswith("start google"):
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    if any(phrase in text for phrase in ["what time is it", "tell me the time", "the time", "what is the time", "the time is"]):
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return f"It is {now}."
    elif "stop" in text or "turn off" in text:
        return "Turning off. Have a nice day!"
    elif any(phrase in text for phrase in ["what is the date", "tell me the date", "date", "what day is today", "today's date"]):
        from datetime import datetime
        now = datetime.now()
        date_str = now.strftime("%d.%m.%Y")
        weekday = now.strftime("%A")
        # List of holidays (example)
        holidays = {
            "01.01": "New Year's Day",
            "03.03": "National Holiday of Bulgaria",
            "01.05": "Labor Day",
            "06.05": "St. George's Day",
            "24.05": "Day of Bulgarian Education and Culture",
            "06.09": "Unification Day",
            "22.09": "Independence Day",
            "01.11": "Day of National Enlighteners",
            "24.12": "Christmas Eve",
            "25.12": "Christmas",
            "26.12": "Christmas"
        }
        key = now.strftime("%d.%m")
        if key in holidays:
            return f"Today is {date_str}, {weekday}. Holiday: {holidays[key]}!"
        else:
            return f"Today is {date_str}, {weekday}. No official holiday."
    else:
        return None
