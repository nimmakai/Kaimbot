sitecode ="test"# "ff"
templates = "stub unreferenced uncategorized update reflist"

editsummary = {
    "add": [],
    "remove": []
}

def getsummary():
    summary = ""
    summary += "Added " + ", ".join(f"[[{ns}:{tem}|]]" for tem, ns in editsummary["add"]) if editsummary["add"] else ""
    if summary and editsummary["remove"]: summary += "; "
    summary += "Removed " + ", ".join(f"[[{ns}:{tem}|]]" for tem, ns in editsummary["remove"]) if editsummary["remove"] else ""
    return summary

def put_summary(tem,ns,action):
    if tem not in editsummary[action]: editsummary[action].append((tem,ns))

def clear_summary():
    global editsummary
    editsummary = {key: [] for key in editsummary}



